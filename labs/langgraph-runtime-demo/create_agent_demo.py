from __future__ import annotations

from pprint import pprint
from typing import Any

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.language_models.fake_chat_models import FakeMessagesListChatModel
from langchain_core.messages import AIMessage


ORDERS = {
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
}


class ToolCallingFakeModel(FakeMessagesListChatModel):
    def bind_tools(self, tools: list[Any], *, tool_choice: Any = None, **kwargs: Any):
        return self


@tool
def query_order(order_id: str) -> str:
    """Query order status by order id."""
    order = ORDERS[order_id]
    return (
        f"order_id={order_id}, status={order['status']}, "
        f"amount={order['amount']}, currency={order['currency']}"
    )


def build_agent():
    model = ToolCallingFakeModel(
        responses=[
            AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "query_order",
                        "args": {"order_id": "order-1001"},
                        "id": "call-query-order-1",
                    }
                ],
            ),
            AIMessage(
                content=(
                    "order-1001 is DELIVERY_FAILED. "
                    "Recommendation: create a refund review request, "
                    "but do not execute refund directly."
                )
            ),
        ]
    )

    return create_agent(
        model=model,
        tools=[query_order],
        system_prompt=(
            "You can query order status and produce recommendations. "
            "Do not execute refunds. Refund execution must be handled by a "
            "controlled StateGraph or Java backend workflow."
        ),
    )


def print_message_flow(messages: list[Any]) -> None:
    for index, message in enumerate(messages, start=1):
        print(f"\n== message {index}: {type(message).__name__} ==")
        details = {
            "content": getattr(message, "content", None),
            "tool_calls": getattr(message, "tool_calls", None),
            "tool_call_id": getattr(message, "tool_call_id", None),
            "name": getattr(message, "name", None),
        }
        pprint(details, sort_dicts=False)


def run_create_agent_demo() -> None:
    agent = build_agent()
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Check order-1001 and recommend what to do.",
                }
            ]
        }
    )

    print_message_flow(result["messages"])


if __name__ == "__main__":
    run_create_agent_demo()
