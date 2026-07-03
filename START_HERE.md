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
- Redis 数据结构和锁粒度仍是面试暴露短板，保留在任务池中，但当前候选学习入口切换为 LangChain / LangGraph。

---

## 3. 当前断点

需要先补齐：

1. LangChain 和 LangGraph 分别解决什么问题
2. LangChain 的模型、消息、工具、Agent Harness 和 Middleware 如何组成一次 Agent 调用
3. LangGraph 的 Graph、State、Node、Edge、Checkpoint、Interrupt、Streaming 分别承担什么职责
4. 在个人 RAG / Agent 项目中，哪些状态可以交给 LangGraph Runtime，哪些业务状态仍应由 Java 后端负责

---

## 4. 最近学习位置

最近一次归档：

1. `interview/real-records/2026-06-30-ai-agent-rag-backend.md`
2. `sessions/2026-06-30-ai-agent-rag-backend-interview.md`

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
2. 从 `BL-011` 开始学习 LangChain / LangGraph 的职责边界和最小 Agent 调用链路
3. 若用户改选任务，以 `LEARNING_BACKLOG.md` 中的任务池为准

---

## 6. 优先读取文件

1. `LEARNING_BACKLOG.md`
2. `LEARNING_ROADMAP.md`
3. LangGraph 官方文档：`https://docs.langchain.com/oss/python/langgraph/overview`
4. LangChain 官方文档：`https://docs.langchain.com/oss/python/langchain/overview`
5. `interview/real-records/2026-06-30-ai-agent-rag-backend.md`

需要判断长期能力方向时，再读取：

1. `LEARNING_ROADMAP.md`

需要确认文档规则时，再读取：

1. `AGENTS.md`
