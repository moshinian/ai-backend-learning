# START HERE

## 1. 用法

新会话优先读取本文件，用于快速恢复当前学习上下文。

本文件只记录恢复入口，不写长篇知识内容。

---

## 2. 当前候选最高优先级

当前候选任务：

- `BL-011`：LangChain / LangGraph 机制梳理

说明：

- 这是用户在 2026-07-03 主动提出的当前最想学、最有动力学习内容。
- 该任务已回补到 `LEARNING_ROADMAP.md` 的 `RM-06 AI Backend / RAG / Agent 能力`，并加入 `LEARNING_BACKLOG.md`。
- 2026-07-05 已完成 LangChain / LangGraph 第一轮机制理解，当前继续推进代码实操和运行时验证。
- Redis 数据结构和锁粒度仍是面试暴露短板，保留在任务池中，但当前候选学习入口仍为 LangChain / LangGraph。

---

## 3. 当前断点

已完成第一轮理解：

1. LangChain 和 LangGraph 分别解决什么问题
2. LangChain 的模型、消息、工具、Agent Harness 和 Middleware 如何组成一次 Agent 调用
3. LangGraph 的 Graph、State、Node、Edge、Checkpoint、Interrupt、Streaming 分别承担什么职责
4. 在个人 RAG / Agent 项目中，哪些状态可以交给 LangGraph Runtime，哪些业务状态仍应由 Java 后端负责

当前断点：

1. 已理解 Agent loop 是“决策 -> 工具执行 -> observation -> 再决策”，不是一次模型调用。
2. 已理解 `messages` 是结构化对话状态，`AIMessage.tool_calls` 与 `ToolMessage.tool_call_id` 需要建立工具调用结果归属。
3. 已理解模型只生成工具调用意图，工具执行、权限、安全、审计和业务状态必须由 runtime / 后端代码控制。
4. 已理解 checkpoint 保存 LangGraph runtime 现场，Java DB 保存审批、权限、副作用和业务事实；恢复时 checkpoint 决定“从哪里恢复”，Java DB 决定“是否允许继续”。
5. 下一步需要把概念落到最小代码：`StateGraph -> node -> conditional edge -> interrupt -> Command(resume)`，并验证 interrupt 前副作用幂等。

---

## 4. 最近学习位置

最近一次归档：

1. `sessions/2026-07-05-langchain-langgraph-agent-runtime.md`
2. `interview/ai-application-questions.md`
3. `interview/real-records/2026-06-30-ai-agent-rag-backend.md`
4. `sessions/2026-06-30-ai-agent-rag-backend-interview.md`

相关主题已有沉淀：

1. `interview/rag-project-story.md`
2. `interview/ai-application-questions.md`
3. `interview/real-records/2026-06-30-ai-agent-rag-backend.md`
4. `backend/redis/distributed-lock.md`
5. `interview/redis-questions.md`
6. `mistakes/distributed/redis-lock.md`

---

## 5. 下一步动作

建议下一步：

1. 读取 `LEARNING_BACKLOG.md`
2. 读取 `sessions/2026-07-05-langchain-langgraph-agent-runtime.md`
3. 继续 `BL-011`，从最小可运行 LangGraph 代码开始：`StateGraph -> node -> conditional edge -> interrupt -> Command(resume)`
4. 重点验证：interrupt 恢复时 node 重放、interrupt 前副作用幂等、Java DB 与 checkpoint 状态冲突时以后端业务事实为准
5. 若用户改选任务，以 `LEARNING_BACKLOG.md` 中的任务池为准

---

## 6. 优先读取文件

1. `LEARNING_BACKLOG.md`
2. `LEARNING_ROADMAP.md`
3. `sessions/2026-07-05-langchain-langgraph-agent-runtime.md`
4. `interview/ai-application-questions.md`
5. LangGraph 官方文档：`https://docs.langchain.com/oss/python/langgraph/overview`
6. LangChain 官方文档：`https://docs.langchain.com/oss/python/langchain/overview`
7. `interview/real-records/2026-06-30-ai-agent-rag-backend.md`

需要判断长期能力方向时，再读取：

1. `LEARNING_ROADMAP.md`

需要确认文档规则时，再读取：

1. `AGENTS.md`
