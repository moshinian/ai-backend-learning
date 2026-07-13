# START HERE

## 1. 用法

新会话优先读取本文件，用于快速恢复当前学习上下文。

本文件只记录恢复入口，不写长篇知识内容。

---

## 2. 当前候选最高优先级

当前候选任务：

- `BL-014`：金蝶 AI 应用开发高级工程师面试准备

说明：

- 2026-07-13 19:00 有金蝶软件中国 AI 应用开发高级工程师面试。
- 岗位重点是 Harness 面向外部系统的工具研发、ERP 对接、第三方 MCP / API 生态接入、Skill / MCP / API 工程化、统一服务治理、持续交付、安全和标准化。
- 本次准备应把既有 Java 后端、结算系统、RAG 项目、LangChain / LangGraph 学习重新组织成“企业 AI 应用工具生态接入 + 后端可靠性治理”的表达。
- 2026-07-13 已完成一轮面试前口述准备，当前处于等待今晚面试验证阶段。
- `BL-013` RAG 检索、重排与文档结构化解析仍是重要短板，但今晚前优先服务 `BL-014`。
- `BL-011` LangChain / LangGraph 机制梳理仍是长期 P0，本次只抽取 Agent 工具调用、checkpoint、interrupt、human-in-the-loop 和业务状态边界用于面试。

---

## 3. 当前断点

当前断点：

1. 当前面试不是纯 AI 算法岗，也不是传统 Java 业务岗，而是“AI 应用开发 + 企业外部系统生态接入 + 服务治理”岗位。
2. 需要优先突出的优势：Java 后端工程经验、结算系统状态机 / 幂等 / 异常修复、RAG + Agent 项目工程链路、权限审计、任务状态、失败重试、LangGraph / MCP 工具调用边界理解。
3. 需要主动补齐的岗位语言：Harness 是承载 Agent / LLM 调用外部能力的工程层；Skill / MCP / API 是工具能力标准化和生态接入方式；ERP 对接关注权限、租户、字段映射、幂等、审计、超时、重试和补偿。
4. AI 项目边界口径：不主动自降为“个人 demo”；如果被明确问是否公司正式生产上线，回答不是正式生产上线项目，但它不是只调 Prompt / API 的 demo，而是覆盖 RAG、Agent Runtime、工具调用、人工确认、任务恢复和后端治理的工程系统。
5. 如果被追问 SQL Server、Hive、Spark、大数据经验，应诚实说明主经验在 MySQL / PostgreSQL / 后端系统，理解数据接入和批处理思路，但不包装为深度生产经验。
6. RAG chunk 新断点：当前项目实际落地固定窗口 + overlap + 自然边界兜底；结构化切分、语义切分、表格 chunk 是已补一轮认知但仍需后续正式沉淀和实践验证的短板。
7. 面试后需要新增真实面试复盘，并根据暴露问题更新 `LEARNING_BACKLOG.md` 和必要的 `mistakes/`。

---

## 4. 最近学习位置

最近一次归档：

1. `interview/mock-records/2026-07-13-kingdee-ai-application-senior-engineer-prep.md`
2. `sessions/2026-07-13-kingdee-ai-application-interview-prep.md`
3. `interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`
4. `sessions/2026-07-07-huashengtong-ai-application-interview-review.md`
5. `mistakes/interview/rag-rerank-algorithm-depth.md`
6. `interview/mock-records/2026-07-07-huashengtong-ai-application-engineer-prep.md`
7. `sessions/2026-07-07-langchain-langgraph-official-doc-map-gap.md`
8. `sessions/2026-07-07-langchain-langgraph-learning-summary.md`
9. `interview/ai-application-questions.md`
10. `interview/rag-project-story.md`

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
2. 读取 `interview/mock-records/2026-07-13-kingdee-ai-application-senior-engineer-prep.md`
3. 面试前重点复习 60 秒自我介绍、岗位适配、ERP Tool 接入、安全治理、AI 项目上线边界、RAG 语义 / 表格 chunk 六组回答
4. 如时间不足，优先背 `sessions/2026-07-13-kingdee-ai-application-interview-prep.md` 的“下次入口”
5. 面试后新增 `interview/real-records/2026-07-13-kingdee-ai-application-senior-engineer.md` 复盘，并决定 `BL-014` 是否 DONE，以及是否恢复 `BL-013` 或继续补 `BL-011`

---

## 6. 优先读取文件

1. `LEARNING_BACKLOG.md`
2. `interview/mock-records/2026-07-13-kingdee-ai-application-senior-engineer-prep.md`
3. `sessions/2026-07-13-kingdee-ai-application-interview-prep.md`
4. `interview/ai-application-questions.md`
5. `interview/rag-project-story.md`
6. `backend/redis/distributed-lock.md`
7. `backend/java/thread-pool.md`
8. `interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`
9. `mistakes/interview/rag-rerank-algorithm-depth.md`
10. `LEARNING_ROADMAP.md`

需要判断长期能力方向时，再读取：

1. `LEARNING_ROADMAP.md`

需要确认文档规则时，再读取：

1. `AGENTS.md`
