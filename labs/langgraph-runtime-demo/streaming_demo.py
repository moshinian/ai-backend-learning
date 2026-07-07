from __future__ import annotations

from pprint import pprint
from typing import Any

from langgraph.types import Command

from approval_flow_demo import JAVA_DB, build_graph


def print_section(title: str, value: Any) -> None:
    print(f"\n== {title} ==")
    pprint(value, sort_dicts=False)


def stream_and_print(graph: Any, input_value: Any, config: dict[str, Any], mode: str) -> None:
    print(f"\n## stream_mode={mode}")
    for index, chunk in enumerate(
        graph.stream(input_value, config=config, stream_mode=mode),
        start=1,
    ):
        print_section(f"chunk {index}", chunk)


def run_streaming_path(mode: str) -> None:
    graph = build_graph()
    action_id = f"streaming-demo-{mode}-001"
    config = {"configurable": {"thread_id": f"streaming-demo-{mode}"}}

    first_input = {
        "action_id": action_id,
        "action_name": "delete_document",
    }

    print_section("first stream input", first_input)
    stream_and_print(graph, first_input, config, mode)
    print_section("java db after first stream", JAVA_DB)

    resume_input = Command(resume={"decision": "approved"})
    print_section("resume stream input", {"decision": "approved"})
    stream_and_print(graph, resume_input, config, mode)
    print_section("java db after resume stream", JAVA_DB)


if __name__ == "__main__":
    run_streaming_path("updates")
    run_streaming_path("values")
