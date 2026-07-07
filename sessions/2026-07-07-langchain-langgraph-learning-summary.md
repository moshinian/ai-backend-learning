# 2026-07-07 LangChain / LangGraph 学习归纳

## 日期

2026-07-07

## 主题

归纳 `BL-011 LangChain / LangGraph 机制梳理` 已完成内容，并将当前进度推进到表达验证阶段。

## 本次做了什么

1. 重新按文档权威顺序读取 `AGENTS.md`、`LEARNING_ROADMAP.md`、`LEARNING_JOURNAL.md`、`LEARNING_BACKLOG.md`、`START_HERE.md`。
2. 梳理 LangChain、`create_agent`、LangGraph、StateGraph 的职责边界。
3. 归纳 `StateGraph -> interrupt -> Command(resume)`、streaming、checkpoint / `thread_id`、`create_agent()` 工具调用 loop 的实验结论。
4. 将 `create_agent` 与 StateGraph 的关系整理成面试表达。
5. 将 `BL-011` 推进到 `REVIEW`，下一步进入口述验证和项目表达压缩。

## 关键结论

1. LangChain 更偏 LLM 应用组件层，负责模型、Prompt、messages、工具、Agent Harness、结构化输出和检索组件。
2. `create_agent()` 是 LangChain 提供的上层 Agent Harness，会把模型、工具、messages 和常见 tool loop 组装成一个基于 LangGraph runtime 的 agent graph。
3. LangGraph 更偏状态化编排运行时，负责 State、Node、Edge、checkpoint、interrupt、streaming、resume 和 human-in-the-loop。
4. 手写 StateGraph 适合强业务流程控制、审批、恢复、状态机和高风险副作用边界。
5. Agent loop 不是一次模型调用，而是“模型提出工具调用意图 -> runtime 执行工具 -> ToolMessage 回填 -> 模型继续推理”的循环。
6. `AIMessage.tool_calls[*].name` 用来匹配注册工具，`args` 用来传参，`id` 用来和后续 `ToolMessage.tool_call_id` 建立结果归属。
7. LangGraph checkpoint 只保存运行时现场；Java DB / 后端数据库保存业务事实、审批结果、权限和副作用执行状态。
8. 高风险动作不能只靠 prompt 约束。模型可以生成建议，真正执行必须进入受控流程，审批通过并校验 Java DB 状态后再调用工具。
9. LangChain 和 LangGraph 可以配合，但不要让两者争夺流程主导权。强业务流程由 LangGraph / 后端状态机主导，LangChain 作为某些 node 内的局部 LLM 能力。
10. 外层 LangGraph State 不应等同于 LangChain messages。两者通过 node 内的输入投影和输出映射连接，避免业务状态和 LLM 对话状态混叠。

## 下次入口

继续 `BL-011` 的 REVIEW 阶段：

1. 进行口述验证：用 2 到 3 分钟讲清 LangChain / `create_agent` / LangGraph / StateGraph 的边界。
2. 将个人 RAG / Agent 项目表达压缩成事实边界清楚的回答。
3. 如果表达稳定，再把 `BL-011` 标记为 DONE；否则继续补 `interview/ai-application-questions.md` 或 `mistakes/`。

## 关联文件

1. `LEARNING_BACKLOG.md`
2. `START_HERE.md`
3. `interview/ai-application-questions.md`
4. `sessions/2026-07-05-langchain-langgraph-agent-runtime.md`
5. `sessions/2026-07-05-langgraph-runtime-demo.md`
6. `sessions/2026-07-06-create-agent-stategraph-boundary.md`
7. `labs/langgraph-runtime-demo/README.md`
