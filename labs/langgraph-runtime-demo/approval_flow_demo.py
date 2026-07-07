from __future__ import annotations

from pprint import pprint
from typing import Any, Literal, TypedDict

try:
    from langgraph.checkpoint.memory import InMemorySaver
except ImportError:  # Older LangGraph versions used MemorySaver.
    from langgraph.checkpoint.memory import MemorySaver as InMemorySaver

from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt


class AgentState(TypedDict, total=False):
    action_id: str
    action_name: str
    approval_result: Literal["approved", "rejected"]
    executed: bool
    audit_log: list[str]


JAVA_DB: dict[str, dict[str, Any]] = {"actions": {}}


def append_log(state: AgentState, message: str) -> list[str]:
    return [*state.get("audit_log", []), message]


def propose_action_node(state: AgentState) -> AgentState:
    action_id = state.get("action_id", "action-delete-doc-001")
    action_name = state.get("action_name", "delete_document")

    return {
        "action_id": action_id,
        "action_name": action_name,
        "executed": False,
        "audit_log": append_log(
            state,
            f"propose_action_node: proposed {action_name} with action_id={action_id}",
        ),
    }


def ensure_waiting_action(state: AgentState) -> str:
    action_id = state["action_id"]
    action_name = state["action_name"]
    actions = JAVA_DB["actions"]

    if action_id not in actions:
        actions[action_id] = {
            "action_name": action_name,
            "status": "WAITING_CONFIRMATION",
            "create_count": 1,
        }
        return "created WAITING_CONFIRMATION action"

    actions[action_id]["create_count"] += 1
    return "action already exists, skipped duplicate create"


def approval_node(state: AgentState) -> AgentState:
    idempotency_message = ensure_waiting_action(state)

    payload = {
        "action_id": state["action_id"],
        "action_name": state["action_name"],
        "risk_level": "HIGH",
        "question": "Approve this high-risk tool action?",
        "idempotency_message": idempotency_message,
    }

    decision = interrupt(payload)
    normalized = normalize_decision(decision)

    action = JAVA_DB["actions"][state["action_id"]]
    if action["status"] != "WAITING_CONFIRMATION":
        raise RuntimeError(
            "Refuse to apply human decision for "
            f"{state['action_id']}: Java DB status is {action['status']}"
        )

    action["status"] = "APPROVED" if normalized == "approved" else "REJECTED"

    return {
        "approval_result": normalized,
        "audit_log": append_log(
            state,
            f"approval_node: resumed with {normalized}; {idempotency_message}",
        ),
    }


def normalize_decision(decision: Any) -> Literal["approved", "rejected"]:
    if isinstance(decision, dict):
        decision = decision.get("decision")
    if decision in (True, "approved", "approve", "yes"):
        return "approved"
    return "rejected"


def route_after_approval(state: AgentState) -> Literal["execute_tool", "cancel"]:
    if state.get("approval_result") == "approved":
        return "execute_tool"
    return "cancel"


def execute_tool_node(state: AgentState) -> AgentState:
    action_id = state["action_id"]
    action = JAVA_DB["actions"][action_id]

    if action["status"] != "APPROVED":
        raise RuntimeError(
            f"Refuse to execute {action_id}: Java DB status is {action['status']}"
        )

    action["status"] = "EXECUTED"

    return {
        "executed": True,
        "audit_log": append_log(
            state,
            "execute_tool_node: Java DB approved, tool side effect executed",
        ),
    }


def cancel_node(state: AgentState) -> AgentState:
    action_id = state["action_id"]
    JAVA_DB["actions"][action_id]["status"] = "CANCELLED"

    return {
        "executed": False,
        "audit_log": append_log(state, "cancel_node: action cancelled"),
    }


def build_graph():
    builder = StateGraph(AgentState)
    builder.add_node("propose_action", propose_action_node)
    builder.add_node("approval", approval_node)
    builder.add_node("execute_tool", execute_tool_node)
    builder.add_node("cancel", cancel_node)

    builder.add_edge(START, "propose_action")
    builder.add_edge("propose_action", "approval")
    builder.add_conditional_edges(
        "approval",
        route_after_approval,
        {
            "execute_tool": "execute_tool",
            "cancel": "cancel",
        },
    )
    builder.add_edge("execute_tool", END)
    builder.add_edge("cancel", END)

    return builder.compile(checkpointer=InMemorySaver())


def print_section(title: str, value: Any) -> None:
    print(f"\n== {title} ==")
    pprint(value, sort_dicts=False)


def get_interrupt_payloads(result: dict[str, Any]) -> list[Any]:
    return [item.value for item in result.get("__interrupt__", [])]


def drive_graph_until_done(
    graph: Any,
    first_input: AgentState,
    config: dict[str, Any],
    scripted_decisions: list[dict[str, str]],
) -> AgentState:
    next_input: AgentState | Command = first_input
    step = 1

    while True:
        result = graph.invoke(next_input, config=config)
        print_section(f"invoke step {step} result", result)

        interrupt_payloads = get_interrupt_payloads(result)
        if not interrupt_payloads:
            return result

        print_section("interrupt payloads for human confirmation", interrupt_payloads)
        print_section("java db while waiting for confirmation", JAVA_DB)

        if not scripted_decisions:
            raise RuntimeError("Graph interrupted, but no scripted human decision remains")

        human_decision = scripted_decisions.pop(0)
        print_section("simulated human decision", human_decision)

        next_input = Command(resume=human_decision)
        step += 1


def run_approved_path() -> None:
    graph = build_graph()
    config = {"configurable": {"thread_id": "approval-demo-approved"}}

    final_result = drive_graph_until_done(
        graph=graph,
        first_input={
            "action_id": "action-delete-doc-001",
            "action_name": "delete_document",
        },
        config=config,
        scripted_decisions=[{"decision": "approved"}],
    )
    print_section("approved path final result", final_result)
    print_section("java db after approved path", JAVA_DB)


def run_rejected_path() -> None:
    graph = build_graph()
    config = {"configurable": {"thread_id": "approval-demo-rejected"}}

    final_result = drive_graph_until_done(
        graph=graph,
        first_input={"action_id": "action-drop-index-002", "action_name": "drop_index"},
        config=config,
        scripted_decisions=[{"decision": "rejected"}],
    )
    print_section("rejected path final result", final_result)
    print_section("java db after rejected path", JAVA_DB)


def run_cancelled_before_resume_path() -> None:
    graph = build_graph()
    config = {"configurable": {"thread_id": "approval-demo-cancelled-before-resume"}}

    first_result = graph.invoke(
        {
            "action_id": "action-cancelled-before-resume-003",
            "action_name": "delete_index",
        },
        config=config,
    )
    print_section("cancelled-before-resume first invoke result", first_result)
    print_section("java db before external cancellation", JAVA_DB)

    action = JAVA_DB["actions"]["action-cancelled-before-resume-003"]
    action["status"] = "CANCELLED"
    print_section("java db after external cancellation", JAVA_DB)

    try:
        graph.invoke(Command(resume={"decision": "approved"}), config=config)
    except RuntimeError as exc:
        print_section("resume rejected by Java DB business state", str(exc))

    print_section("java db after rejected resume attempt", JAVA_DB)


if __name__ == "__main__":
    run_approved_path()
    run_rejected_path()
    run_cancelled_before_resume_path()
