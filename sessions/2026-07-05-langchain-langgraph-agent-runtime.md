# 2026-07-05 LangChain / LangGraph Agent Runtime 机制梳理

## 日期

2026-07-05

## 主题

LangChain / LangGraph 的职责边界、Agent loop、messages / tool call、LangGraph checkpoint / interrupt / human-in-the-loop，以及 Java 后端与 LangGraph Runtime 的状态边界。

## 本次做了什么

1. 将 `BL-011 LangChain / LangGraph 机制梳理` 从学习计划推进到第一轮机制理解。
2. 梳理 LangChain 与 LangGraph 的职责边界。
3. 练习 Agent loop、messages、`AIMessage`、`ToolMessage`、`tool_call_id` 的表达。
4. 梳理模型只生成工具调用意图，工具执行由 runtime / 业务代码完成的安全边界。
5. 梳理 LangGraph 的 Graph、State、Node、Edge、checkpoint、interrupt、human-in-the-loop。
6. 用高风险删除动作讨论 Java 后端、LangGraph checkpoint、人工确认、后端审批状态和工具执行副作用的边界。

## 关键结论

1. LangChain 更偏上层 Agent 组装：模型调用、消息结构、Prompt、工具绑定、Agent loop、middleware 和结构化输出。
2. LangGraph 更偏底层 Agent 编排运行时：Graph、State、Node、Edge、checkpoint、interrupt、streaming 和 human-in-the-loop。
3. Agent 不是一次模型调用，而是“决策 -> 工具执行 -> observation -> 再决策”的循环。
4. `messages` 是结构化对话状态，优于普通 prompt string 承载多轮对话和工具调用过程。
5. `AIMessage` 是模型输出，可能包含 `tool_calls`；`ToolMessage` 是工具执行结果，需要通过 `tool_call_id` 归属到某次工具调用。
6. 模型只生成工具调用意图；工具执行、权限、安全、审计、错误处理和业务状态更新必须由 runtime / 后端代码控制。
7. `State` 可以包含 `messages`，但不等于 `messages`；State 还可以包含运行时字段、审批结果、错误、重试次数等控制信息。
8. checkpoint 保存 LangGraph runtime 执行现场；Java 后端数据库保存业务事实、审批结果、权限和副作用执行状态。
9. 恢复时 checkpoint 决定“从哪里恢复”，Java DB 决定“是否允许继续”。
10. `interrupt()` 会暂停并向 graph 调用方暴露 payload；服务化架构下通常由 Python Runtime 接住并返回给 Java 后端。
11. `interrupt` 所在 node 恢复时会从头重放，因此 interrupt 前副作用必须幂等，或移动到 interrupt 后的独立 node。
12. 高风险动作应采用：模型推荐动作 -> LangGraph interrupt -> Java 后端落库 WAITING_CONFIRMATION -> 用户确认 / 拒绝 -> 后端保存审批结果和校验权限 -> resume -> execute 或 cancel。

## 当前掌握情况

已基本掌握：

1. LangChain / LangGraph 的职责边界。
2. Agent loop 与普通一次性 LLM 调用的区别。
3. messages、`AIMessage`、`ToolMessage` 和 `tool_call_id` 的作用。
4. 工具调用的执行边界：模型负责意图，runtime / 后端负责执行。
5. checkpoint、interrupt、human-in-the-loop 的核心工程意义。
6. Java DB 与 LangGraph checkpoint 的状态权威边界。

仍不稳定：

1. 还没有亲手跑通最小 `StateGraph` 代码。
2. `create_agent`、Graph API、checkpoint config、thread / run、streaming 还没进入实操。
3. reducer / state update 的细节还没有系统练习。
4. interrupt + `Command(resume=...)` 的代码形态只做了伪代码理解，还需要真实例子验证。

## 下次入口

从最小可运行代码开始，不再继续只讲概念：

1. 定义 `AgentState`：`messages`、`tool_call_id`、`action_id`、`approval_result`。
2. 写 `approval_node`：幂等创建待确认 action，然后 `interrupt(payload)`。
3. 写 conditional edge：确认则进入 `execute_tool_node`，拒绝则进入 `cancel_node`。
4. 写 `execute_tool_node`：再次查询 Java DB 确认 action 已 APPROVED，再执行工具并返回 `ToolMessage`。
5. 用 `Command(resume={...})` 模拟用户确认 / 拒绝。

## 关联文件

1. `LEARNING_BACKLOG.md`
2. `START_HERE.md`
3. `LEARNING_JOURNAL.md`
4. `interview/ai-application-questions.md`
5. `interview/real-records/2026-06-30-ai-agent-rag-backend.md`
