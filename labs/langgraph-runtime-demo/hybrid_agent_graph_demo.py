from __future__ import annotations

from pprint import pprint
from typing import Any, Literal, TypedDict

try:
    from langgraph.checkpoint.memory import InMemorySaver
except ImportError:
    from langgraph.checkpoint.memory import MemorySaver as InMemorySaver

from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt


class RefundState(TypedDict, total=False):
    order_id: str
    order_status: str
    refund_recommendation: dict[str, Any]
    action_id: str
    approval_result: Literal["approved", "rejected"]
    refund_executed: bool
    audit_log: list[str]


JAVA_DB: dict[str, dict[str, Any]] = {
    "orders": {
        "order-1001": {
            "status": "DELIVERY_FAILED",
            "amount": 12800,
            "currency": "CNY",
        },
        "order-1002": {
            "status": "PAID",
            "amount": 9900,
            "currency": "CNY",
        },
    },
    "actions": {},
    "refunds": {},
}


def append_log(state: RefundState, message: str) -> list[str]:
    return [*state.get("audit_log", []), message]


def query_order_tool(order_id: str) -> dict[str, Any]:
    return JAVA_DB["orders"][order_id]


def mock_agent_recommendation(order_id: str) -> dict[str, Any]:
    order = query_order_tool(order_id)
    if order["status"] == "DELIVERY_FAILED":
        return {
            "needs_refund": True,
            "reason": "Delivery failed after payment.",
            "amount": order["amount"],
            "currency": order["currency"],
        }
    return {
        "needs_refund": False,
        "reason": f"Order status is {order['status']}; no refund recommendation.",
    }


def recommend_refund_node(state: RefundState) -> RefundState:
    order_id = state["order_id"]
    order = query_order_tool(order_id)
    recommendation = mock_agent_recommendation(order_id)

    return {
        "order_status": order["status"],
        "refund_recommendation": recommendation,
        "refund_executed": False,
        "audit_log": append_log(
            state,
            "mock_agent_recommendation: queried order and produced "
            f"recommendation={recommendation['needs_refund']}",
        ),
    }


def route_after_recommendation(state: RefundState) -> Literal["approval", "done"]:
    if state["refund_recommendation"]["needs_refund"]:
        return "approval"
    return "done"


def ensure_refund_action(state: RefundState) -> str:
    order_id = state["order_id"]
    action_id = state.get("action_id", f"refund-action-{order_id}")
    actions = JAVA_DB["actions"]

    if action_id not in actions:
        actions[action_id] = {
            "order_id": order_id,
            "status": "WAITING_CONFIRMATION",
            "amount": state["refund_recommendation"]["amount"],
            "create_count": 1,
        }
        return action_id, "created WAITING_CONFIRMATION refund action"

    actions[action_id]["create_count"] += 1
    return action_id, "refund action already exists, skipped duplicate create"


def approval_node(state: RefundState) -> RefundState:
    action_id, idempotency_message = ensure_refund_action(state)
    action = JAVA_DB["actions"][action_id]

    payload = {
        "action_id": action_id,
        "order_id": state["order_id"],
        "amount": action["amount"],
        "risk_level": "HIGH",
        "question": "Approve controlled refund execution?",
        "recommendation": state["refund_recommendation"],
        "idempotency_message": idempotency_message,
    }

    decision = interrupt(payload)
    normalized = normalize_decision(decision)

    if action["status"] != "WAITING_CONFIRMATION":
        raise RuntimeError(
            f"Refuse to apply refund decision for {action_id}: "
            f"Java DB status is {action['status']}"
        )

    action["status"] = "APPROVED" if normalized == "approved" else "REJECTED"

    return {
        "action_id": action_id,
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


def route_after_approval(state: RefundState) -> Literal["execute_refund", "cancel"]:
    if state.get("approval_result") == "approved":
        return "execute_refund"
    return "cancel"


def controlled_refund_tool(action_id: str) -> dict[str, Any]:
    action = JAVA_DB["actions"][action_id]
    refund_id = f"refund-{action['order_id']}"
    if refund_id not in JAVA_DB["refunds"]:
        JAVA_DB["refunds"][refund_id] = {
            "action_id": action_id,
            "order_id": action["order_id"],
            "amount": action["amount"],
            "status": "REFUNDED",
        }
    return JAVA_DB["refunds"][refund_id]


def execute_refund_node(state: RefundState) -> RefundState:
    action_id = state["action_id"]
    action = JAVA_DB["actions"][action_id]

    if action["status"] != "APPROVED":
        raise RuntimeError(
            f"Refuse to execute refund for {action_id}: "
            f"Java DB status is {action['status']}"
        )

    refund = controlled_refund_tool(action_id)
    action["status"] = "EXECUTED"

    return {
        "refund_executed": True,
        "audit_log": append_log(
            state,
            f"execute_refund_node: controlled refund_tool executed {refund['status']}",
        ),
    }


def cancel_node(state: RefundState) -> RefundState:
    action_id = state["action_id"]
    JAVA_DB["actions"][action_id]["status"] = "CANCELLED"

    return {
        "refund_executed": False,
        "audit_log": append_log(state, "cancel_node: refund recommendation rejected"),
    }


def done_node(state: RefundState) -> RefundState:
    return {
        "refund_executed": False,
        "audit_log": append_log(state, "done_node: no refund action required"),
    }


def build_graph():
    builder = StateGraph(RefundState)
    builder.add_node("recommend_refund", recommend_refund_node)
    builder.add_node("approval", approval_node)
    builder.add_node("execute_refund", execute_refund_node)
    builder.add_node("cancel", cancel_node)
    builder.add_node("done", done_node)

    builder.add_edge(START, "recommend_refund")
    builder.add_conditional_edges(
        "recommend_refund",
        route_after_recommendation,
        {
            "approval": "approval",
            "done": "done",
        },
    )
    builder.add_conditional_edges(
        "approval",
        route_after_approval,
        {
            "execute_refund": "execute_refund",
            "cancel": "cancel",
        },
    )
    builder.add_edge("execute_refund", END)
    builder.add_edge("cancel", END)
    builder.add_edge("done", END)

    return builder.compile(checkpointer=InMemorySaver())


def print_section(title: str, value: Any) -> None:
    print(f"\n== {title} ==")
    pprint(value, sort_dicts=False)


def get_interrupt_payloads(result: dict[str, Any]) -> list[Any]:
    return [item.value for item in result.get("__interrupt__", [])]


def drive_graph_until_done(
    graph: Any,
    first_input: RefundState,
    config: dict[str, Any],
    scripted_decisions: list[dict[str, str]],
) -> RefundState:
    next_input: RefundState | Command = first_input
    step = 1

    while True:
        result = graph.invoke(next_input, config=config)
        print_section(f"invoke step {step} result", result)

        interrupt_payloads = get_interrupt_payloads(result)
        if not interrupt_payloads:
            return result

        print_section("interrupt payloads for controlled approval", interrupt_payloads)
        print_section("java db while waiting for approval", JAVA_DB)

        if not scripted_decisions:
            raise RuntimeError("Graph interrupted, but no scripted decision remains")

        human_decision = scripted_decisions.pop(0)
        print_section("simulated human decision", human_decision)
        next_input = Command(resume=human_decision)
        step += 1


def run_refund_approved_path() -> None:
    graph = build_graph()
    config = {"configurable": {"thread_id": "hybrid-refund-approved"}}

    final_result = drive_graph_until_done(
        graph=graph,
        first_input={"order_id": "order-1001"},
        config=config,
        scripted_decisions=[{"decision": "approved"}],
    )
    print_section("refund approved final result", final_result)
    print_section("java db after refund approved path", JAVA_DB)


def run_refund_rejected_path() -> None:
    graph = build_graph()
    config = {"configurable": {"thread_id": "hybrid-refund-rejected"}}

    final_result = drive_graph_until_done(
        graph=graph,
        first_input={"order_id": "order-1001", "action_id": "refund-action-rejected"},
        config=config,
        scripted_decisions=[{"decision": "rejected"}],
    )
    print_section("refund rejected final result", final_result)
    print_section("java db after refund rejected path", JAVA_DB)


def run_no_refund_path() -> None:
    graph = build_graph()
    config = {"configurable": {"thread_id": "hybrid-no-refund"}}

    final_result = drive_graph_until_done(
        graph=graph,
        first_input={"order_id": "order-1002"},
        config=config,
        scripted_decisions=[],
    )
    print_section("no refund final result", final_result)
    print_section("java db after no refund path", JAVA_DB)


if __name__ == "__main__":
    run_refund_approved_path()
    run_refund_rejected_path()
    run_no_refund_path()
