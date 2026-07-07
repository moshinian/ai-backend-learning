# 2026-07-06 create_agent 与 StateGraph 边界验证

## 日期

2026-07-06

## 主题

通过混合架构 mock demo 验证：标准 Agent 建议生成可以交给 `create_agent` 类上层 harness，但高风险副作用工具必须进入 StateGraph / Java 后端受控流程。

## 本次做了什么

1. 讨论 `create_agent` 与手写 `StateGraph` 的职责边界。
2. 明确 `create_agent` 更适合标准模型工具调用 loop，`StateGraph` 更适合强业务流程控制。
3. 新增 `labs/langgraph-runtime-demo/hybrid_agent_graph_demo.py`。
4. 将原来的 `mock_create_agent_recommendation()` 改名为 `mock_agent_recommendation()`，避免误以为该 demo 已真实调用 `create_agent()`。
5. 新增 `labs/langgraph-runtime-demo/create_agent_demo.py`，真实调用 `langchain.agents.create_agent()`。
6. 用 fake chat model 模拟模型先输出 tool call，再基于 `ToolMessage` 输出最终建议。
7. 用 `mock_agent_recommendation()` 模拟 Agent 查询订单并生成退款建议。
8. 用 StateGraph 控制退款审批、`interrupt()`、`Command(resume=...)` 和受控退款执行。
9. 跑通真实 `create_agent` 工具调用 loop，以及退款建议后审批通过、审批拒绝、无需退款三条路径。

## 关键结论

1. `create_agent` 可以理解为上层 Agent Harness，用来组织模型、工具、messages 和常见 Agent loop。
2. `StateGraph` 提供更强流程控制能力，适合显式建模审批、恢复、状态机和高风险动作边界。
3. “StateGraph 能力更强”不等于所有标准工具调用场景都应该手写 StateGraph。
4. 对订单查询和退款建议，Agent 可以负责查询、分析和生成建议。
5. 对真正退款执行，不能把 `refund_tool` 直接交给模型自主调用。
6. 高风险副作用工具应只放在受控执行节点里，审批通过并经过 Java DB 状态校验后才调用。
7. 成熟边界是：模型负责建议，LangGraph runtime 负责流程，Java DB 负责业务事实和权限，工具执行必须受控。
8. 真实 `create_agent()` 会把模型、工具、messages 和 tool loop 组装成一个 agent graph。
9. 在标准工具调用 loop 中，模型输出 `AIMessage.tool_calls`，runtime 根据 tool call 执行工具并产生 `ToolMessage`，然后模型继续生成最终回答。
10. 本次真实 demo 使用 fake chat model，不依赖外部 LLM API；它验证的是 `create_agent()` 的执行结构，不验证真实模型推理能力。

## 下次入口

继续 `BL-011`：

1. 进入面试表达整理：如何回答 LangChain、LangGraph、`create_agent`、StateGraph 的职责边界。
2. 继续保持事实边界：当前 RAG / Agent 项目未生产上线，不包装成生产经验。

## 关联文件

1. `LEARNING_BACKLOG.md`
2. `START_HERE.md`
3. `labs/langgraph-runtime-demo/create_agent_demo.py`
4. `labs/langgraph-runtime-demo/hybrid_agent_graph_demo.py`
5. `labs/langgraph-runtime-demo/README.md`
6. `sessions/2026-07-05-langgraph-runtime-demo.md`
