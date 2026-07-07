from __future__ import annotations

from pprint import pprint
from typing import Any

from langgraph.types import Command

from approval_flow_demo import JAVA_DB, build_graph


def print_section(title: str, value: Any) -> None:
    print(f"\n== {title} ==")
    pprint(value, sort_dicts=False)


def run_same_graph_resume_path() -> None:
    graph = build_graph()
    config = {"configurable": {"thread_id": "checkpoint-demo-same-graph"}}

    first_result = graph.invoke(
        {
            "action_id": "checkpoint-same-graph-001",
            "action_name": "delete_document",
        },
        config=config,
    )
    print_section("same graph first invoke", first_result)
    print_section("java db after same graph interrupt", JAVA_DB)

    resumed_result = graph.invoke(
        Command(resume={"decision": "approved"}),
        config=config,
    )
    print_section("same graph resume result", resumed_result)
    print_section("java db after same graph resume", JAVA_DB)


def run_new_graph_same_thread_id_path() -> None:
    config = {"configurable": {"thread_id": "checkpoint-demo-new-graph"}}

    first_graph = build_graph()
    first_result = first_graph.invoke(
        {
            "action_id": "checkpoint-new-graph-001",
            "action_name": "delete_document",
        },
        config=config,
    )
    print_section("new graph first invoke", first_result)
    print_section("java db after new graph interrupt", JAVA_DB)

    second_graph = build_graph()
    resumed_result = second_graph.invoke(
        Command(resume={"decision": "approved"}),
        config=config,
    )
    print_section("new graph resume result", resumed_result)
    print_section("java db after new graph resume attempt", JAVA_DB)


if __name__ == "__main__":
    run_same_graph_resume_path()
    run_new_graph_same_thread_id_path()
