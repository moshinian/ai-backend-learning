# 2026-07-05 LangGraph Runtime 最小代码实验

## 日期

2026-07-05

## 主题

用最小可运行代码验证 LangGraph `StateGraph`、`interrupt()`、`Command(resume=...)`、conditional edge、checkpoint 和副作用幂等。

## 本次做了什么

1. 新增 `labs/` 目录职责规则，用于保存可运行学习实验代码。
2. 新增 `labs/langgraph-runtime-demo/`。
3. 编写 `approval_flow_demo.py`，模拟高风险工具动作审批流。
4. 使用 `/tmp/langgraph-learning-venv` 安装并运行 `langgraph 1.2.7`。
5. 跑通 approved 和 rejected 两条路径。
6. 补充 `drive_graph_until_done()`，模拟 Python Runtime / Java 后端调用方循环处理 `__interrupt__`。
7. 补充外部取消后再 resume 的冲突路径，验证后端业务状态机优先于 resume 输入。
8. 新增 `streaming_demo.py`，观察 `stream_mode="updates"` 和 `stream_mode="values"` 的输出差异。
9. 新增 `checkpoint_demo.py`，验证同一个 `thread_id` 在同一个 checkpointer 与新 checkpointer 下的恢复差异。

## 关键结论

1. 第一次 `graph.invoke(...)` 在 `approval_node` 内触发 `interrupt()` 后暂停，并在结果中返回 `__interrupt__`。
2. `Command(resume=...)` 的 payload 会成为 `interrupt()` 的返回值。
3. 恢复执行时，LangGraph 会从触发 `interrupt()` 的 node 开头重新执行，而不是只从 `interrupt()` 下一行继续。
4. `approval_node` 中 interrupt 前的模拟落库逻辑在 resume 后再次执行，`create_count` 从 1 变成 2。
5. 通过 `action_id` 做幂等键，可以避免重复创建业务动作。
6. 工具执行前再次查询模拟 Java DB，体现业务事实由后端状态决定，而不是只相信 LangGraph checkpoint。
7. rejected 路径不会进入工具执行节点，而是进入 `cancel_node`。
8. 调用方不能把一次 `invoke()` 的返回值天然当成最终结果；需要先检查 `__interrupt__`，有 interrupt 就把 payload 交给外部确认，并用同一个 `thread_id` resume。
9. 如果 resume 后再次返回 `__interrupt__`，调用方应继续循环处理，直到返回值中没有 `__interrupt__`。
10. `approval_node` 收到 resume 后不能无条件把业务状态覆盖成 `APPROVED`；必须先确认 Java DB 中 action 仍是 `WAITING_CONFIRMATION`。
11. 如果等待确认期间 action 已经被外部取消，即使 resume 输入是 `approved`，也应该拒绝继续执行，并保持业务状态为 `CANCELLED`。
12. `stream_mode="updates"` 更适合观察“哪个节点产生了什么增量更新”，interrupt 也会作为 `__interrupt__` chunk 出现。
13. `stream_mode="values"` 更适合观察“每一步后的完整 state”，能看到 state 从输入、节点更新、interrupt 到最终执行结果的累积过程。
14. 同一个 graph / `InMemorySaver` 中，使用同一个 `thread_id` 可以从 interrupt 恢复。
15. 新建 graph / checkpointer 后，即使用同一个 `thread_id`，也不能恢复旧的 interrupt 现场；`thread_id` 只是查询 key，checkpoint 是否存在取决于存储介质。

## 下次入口

继续 `BL-011`，下一步从以下方向推进：

1. 再进入 `create_agent` 和 LangChain 上层 Agent Harness。
2. 如有需要，再补持久化 checkpointer 或 `stream_events()` 对比事件级输出。

## 关联文件

1. `LEARNING_BACKLOG.md`
2. `START_HERE.md`
3. `labs/langgraph-runtime-demo/README.md`
4. `labs/langgraph-runtime-demo/approval_flow_demo.py`
5. `labs/langgraph-runtime-demo/streaming_demo.py`
6. `labs/langgraph-runtime-demo/checkpoint_demo.py`
7. `sessions/2026-07-05-langchain-langgraph-agent-runtime.md`
