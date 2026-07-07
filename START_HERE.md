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
- 2026-07-07 已完成 LangChain / LangGraph 第一轮机制理解和实验验证，但随后对照官方文档发现还缺 LangChain 的 Core components / Middleware / Frontend / Advanced usage 全貌，以及 LangGraph 的 Capabilities / Production / Frontend / LangGraph APIs 全貌。因此 `BL-011` 已从 REVIEW 拉回 DOING，下一步先补官方目录地图级理解，再做口述验收。
- Redis 数据结构和锁粒度仍是面试暴露短板，保留在任务池中，但当前候选学习入口仍为 LangChain / LangGraph。

---

## 3. 当前断点

已完成第一轮理解：

1. LangChain 和 LangGraph 分别解决什么问题
2. LangChain 的模型、消息、工具、Agent Harness 和 Middleware 如何组成一次 Agent 调用
3. LangGraph 的 Graph、State、Node、Edge、Checkpoint、Interrupt、Streaming 分别承担什么职责
4. 在个人 RAG / Agent 项目中，哪些状态可以交给 LangGraph Runtime，哪些业务状态仍应由 Java 后端负责

仍需补全的官方目录地图：

1. LangChain：Core components、Middleware、Runtime、Frontend、Advanced usage 分别解决什么问题
2. LangGraph：Capabilities、Production、Frontend、Graph API / Functional API 分别解决什么问题
3. Checkpointer / Store、Graph API / Functional API、LangChain frontend / LangGraph frontend 的边界
4. 这些能力如何回到个人 RAG / Agent 项目的工程表达，而不是停留在框架功能清单

当前断点：

1. 已理解 Agent loop 是“决策 -> 工具执行 -> observation -> 再决策”，不是一次模型调用。
2. 已理解 `messages` 是结构化对话状态，`AIMessage.tool_calls` 与 `ToolMessage.tool_call_id` 需要建立工具调用结果归属。
3. 已理解模型只生成工具调用意图，工具执行、权限、安全、审计和业务状态必须由 runtime / 后端代码控制。
4. 已理解 checkpoint 保存 LangGraph runtime 现场，Java DB 保存审批、权限、副作用和业务事实；恢复时 checkpoint 决定“从哪里恢复”，Java DB 决定“是否允许继续”。
5. 已跑通最小代码：`StateGraph -> node -> conditional edge -> interrupt -> Command(resume)`。
6. 已验证 resume 会重放触发 interrupt 的 node，interrupt 前副作用需要用 `action_id` 幂等。
7. 已验证调用方需要循环处理 `__interrupt__`，直到没有 interrupt 才算图执行完成。
8. 已验证 `approval_node` 不能无条件覆盖 Java DB 业务状态，等待确认期间被取消的 action 不能被 resume approved 重新批准。
9. 已验证 `stream_mode="updates"` 观察节点增量，`stream_mode="values"` 观察每一步完整 state。
10. 已验证 `thread_id` 只是 checkpoint 查找 key，`InMemorySaver` 只能恢复当前 Python 进程内仍存在的 checkpoint。
11. 已验证真实 `create_agent()` 会执行标准模型工具调用 loop：`AIMessage.tool_calls -> ToolMessage -> final AIMessage`。
12. 已验证标准查询 / 建议生成可以由 `create_agent` 类上层 harness 负责，高风险副作用工具应放在 StateGraph / Java 后端受控执行节点。
13. 已归纳面试表达入口：LangChain、`create_agent`、LangGraph、StateGraph 的职责边界，以及个人 RAG / Agent 项目中如何保留 Java 后端业务状态权威。
14. 当前不直接进入 DONE 验收，先补官方目录地图，避免只掌握 runtime 片段而漏掉框架全貌。

---

## 4. 最近学习位置

最近一次归档：

1. `sessions/2026-07-05-langchain-langgraph-agent-runtime.md`
2. `sessions/2026-07-05-langgraph-runtime-demo.md`
3. `sessions/2026-07-06-create-agent-stategraph-boundary.md`
4. `sessions/2026-07-07-langchain-langgraph-learning-summary.md`
5. `sessions/2026-07-07-langchain-langgraph-official-doc-map-gap.md`
6. `interview/ai-application-questions.md`
7. `labs/langgraph-runtime-demo/README.md`
8. `labs/langgraph-runtime-demo/create_agent_demo.py`
9. `labs/langgraph-runtime-demo/hybrid_agent_graph_demo.py`
10. `interview/real-records/2026-06-30-ai-agent-rag-backend.md`
11. `sessions/2026-06-30-ai-agent-rag-backend-interview.md`

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
3. 继续 `BL-011` 的 DOING：先补 LangChain / LangGraph 官方目录地图
4. 补完后再用 2 到 3 分钟口述 LangChain / `create_agent` / Middleware / Runtime / LangGraph / Graph API / Functional API / StateGraph 的职责边界
5. 继续保持边界：模型负责建议，LangGraph runtime 负责流程，Java DB 负责业务事实和权限
6. 若用户改选任务，以 `LEARNING_BACKLOG.md` 中的任务池为准

---

## 6. 优先读取文件

1. `LEARNING_BACKLOG.md`
2. `LEARNING_ROADMAP.md`
3. `sessions/2026-07-05-langchain-langgraph-agent-runtime.md`
4. `sessions/2026-07-05-langgraph-runtime-demo.md`
5. `sessions/2026-07-06-create-agent-stategraph-boundary.md`
6. `sessions/2026-07-07-langchain-langgraph-learning-summary.md`
7. `sessions/2026-07-07-langchain-langgraph-official-doc-map-gap.md`
8. `interview/ai-application-questions.md`
9. `labs/langgraph-runtime-demo/README.md`
10. `labs/langgraph-runtime-demo/approval_flow_demo.py`
11. `labs/langgraph-runtime-demo/streaming_demo.py`
12. `labs/langgraph-runtime-demo/checkpoint_demo.py`
13. `labs/langgraph-runtime-demo/create_agent_demo.py`
14. `labs/langgraph-runtime-demo/hybrid_agent_graph_demo.py`
15. LangChain 官方文档：`https://docs.langchain.com/oss/python/langchain/overview`
16. LangGraph 官方文档：`https://docs.langchain.com/oss/python/langgraph/overview`
17. `interview/real-records/2026-06-30-ai-agent-rag-backend.md`

需要判断长期能力方向时，再读取：

1. `LEARNING_ROADMAP.md`

需要确认文档规则时，再读取：

1. `AGENTS.md`
