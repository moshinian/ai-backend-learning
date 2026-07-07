# LangGraph Runtime Demo

## 实验目标

本实验用于验证 `BL-011 LangChain / LangGraph 机制梳理` 中的最小 runtime 链路：

1. `StateGraph` 如何定义状态和节点
2. `interrupt()` 如何暂停执行并向调用方暴露审批 payload
3. `Command(resume=...)` 如何恢复执行
4. conditional edge 如何根据审批结果分流
5. interrupt 所在 node 恢复时为何需要处理副作用幂等
6. 调用方如何循环处理一次或多次 `__interrupt__`
7. resume 输入和后端业务状态机冲突时，为什么以后端业务事实为准
8. `stream_mode="updates"` 和 `stream_mode="values"` 的输出差异
9. `create_agent` 类上层 harness 与手写 `StateGraph` 的职责边界
10. 真实 `create_agent()` 如何执行标准模型工具调用 loop

## 运行方式

建议使用临时虚拟环境运行，避免污染仓库：

```bash
python3 -m venv /tmp/langgraph-learning-venv
/tmp/langgraph-learning-venv/bin/pip install -r labs/langgraph-runtime-demo/requirements.txt
/tmp/langgraph-learning-venv/bin/python labs/langgraph-runtime-demo/approval_flow_demo.py
/tmp/langgraph-learning-venv/bin/python labs/langgraph-runtime-demo/streaming_demo.py
/tmp/langgraph-learning-venv/bin/python labs/langgraph-runtime-demo/checkpoint_demo.py
/tmp/langgraph-learning-venv/bin/python labs/langgraph-runtime-demo/create_agent_demo.py
/tmp/langgraph-learning-venv/bin/python labs/langgraph-runtime-demo/hybrid_agent_graph_demo.py
```

## 关键验证点

1. 第一次执行会在审批节点触发 `interrupt()`。
2. 恢复执行时，`approval_node` 会从节点开头重新运行。
3. `approval_node` 中 interrupt 前的模拟落库动作必须通过 `action_id` 幂等。
4. `Command(resume=...)` 的值会成为 `interrupt()` 的返回值。
5. 工具执行前再次读取模拟 Java DB，确认业务状态允许执行。
6. 调用方不能把一次 `invoke()` 的结果直接当成最终结果，必须先检查是否包含 `__interrupt__`。
7. 如果 resume 后再次返回 `__interrupt__`，调用方应继续交给外部确认并再次 resume，直到没有 interrupt 才算本轮图执行完成。
8. `approval_node` 收到 resume 后不能无条件覆盖 Java DB 状态；只有 `WAITING_CONFIRMATION` 可以流转为 `APPROVED` 或 `REJECTED`。
9. 如果等待确认期间 action 已被外部改为 `CANCELLED`，即使 resume 输入是 `approved`，也必须拒绝继续执行。
10. `stream_mode="updates"` 输出每个节点的增量更新，例如 `propose_action`、`approval`、`execute_tool` 和 `__interrupt__`。
11. `stream_mode="values"` 输出每一步后的完整 state，更适合观察状态如何逐步累积。
12. `thread_id` 是 checkpoint 的查找 key，不是 checkpoint 本身。
13. `InMemorySaver` 只保存当前 Python 进程内的 checkpoint；新建 graph / checkpointer 后，即使用同一个 `thread_id`，也不能恢复原来的暂停现场。
14. 标准模型工具调用 loop 可以由 `create_agent` 类上层 harness 负责。
15. 高风险副作用工具不应直接交给通用 Agent loop，应放在 StateGraph / Java 后端受控执行节点里。
16. 订单退款场景中，Agent 可以生成退款建议，真正 `refund_tool` 必须在审批通过并通过 Java DB 校验后执行。
17. `create_agent()` 接收模型、工具和 system prompt，返回一个基于 LangGraph 的 agent graph。
18. 标准工具调用 loop 中，模型先输出 `AIMessage.tool_calls`，runtime 执行工具并生成 `ToolMessage`，随后模型再基于工具结果生成最终 `AIMessage`。

## 边界说明

本目录只保存可运行学习实验代码。

它不替代：

1. 正式项目深挖：`projects/`
2. 后端技术主笔记：`backend/`
3. 面试表达沉淀：`interview/`
4. 当前任务调度：`LEARNING_BACKLOG.md`
5. 新会话恢复入口：`START_HERE.md`

## 关联任务或主题

1. `BL-011 LangChain / LangGraph 机制梳理`
2. `RM-06 AI Backend / RAG / Agent 能力`
3. `sessions/2026-07-05-langchain-langgraph-agent-runtime.md`
4. `sessions/2026-07-06-create-agent-stategraph-boundary.md`
