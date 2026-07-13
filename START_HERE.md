# START HERE

## 1. 用法

新会话优先读取本文件，用于快速恢复当前学习上下文。

本文件只记录恢复入口，不写长篇知识内容。

---

## 2. 当前候选最高优先级

当前候选任务：

- `BL-013`：RAG 检索、重排与文档结构化解析补课

说明：

- 2026-07-13 已完成金蝶软件中国 AI 应用开发高级工程师面试准备和真实面试归档。
- 金蝶面试虽然 JD 重点是 Harness、ERP 对接、Skill / MCP / API 工程化和服务治理，但实际追问仍集中在 RAG 项目深挖。
- 真实暴露问题和华盛通面试高度重合：文档解析、chunk、Hybrid Retrieval、Rerank、私有语料排序失效、模型部署边界和前沿算法跟踪。
- 当前最高收益不是继续背岗位适配，而是把 RAG 文档结构化解析、语义 / 表格 chunk、Rerank 和评测闭环补成稳定能力。
- `BL-011` LangChain / LangGraph 机制梳理仍是长期 P0，本次只抽取 Agent 工具调用、checkpoint、interrupt、human-in-the-loop 和业务状态边界用于面试。

---

## 3. 当前断点

当前断点：

1. `BL-014` 金蝶面试准备已完成，真实复盘已归档到 `interview/real-records/2026-07-13-kingdee-ai-application-senior-engineer.md`。
2. 两场真实面试连续证明：RAG 工程链路能讲通，但一旦进入文档解析、chunk、Rerank、私有语料排序失效和评测，回答会从工程经验滑向概念描述。
3. 当前项目实际落地边界仍应诚实表述为固定窗口 + overlap + 自然边界兜底；成熟优化方向应表述为结构优先、长度兜底、语义增强、评测闭环。
4. 语义切分要讲到基础单元、相邻单元组 embedding、cosine similarity、候选切点、min_tokens / max_tokens / overlap 和结构保护。
5. 表格 chunk 要讲“先抽取结构，再按表格类型处理”，保留 table summary、row-level KV、structured JSON 和原始 HTML / Markdown 等多种表示。
6. Rerank 要补到 bi-encoder 召回 vs cross-encoder 重排、query-document pair 打分、训练数据、hard negative、私有语料微调、业务规则特征和反馈闭环。
7. 面试表达中需要避免“丢弃旧量”这类金融 / 结算高风险措辞，先判断数据是否允许丢弃。

---

## 4. 最近学习位置

最近一次归档：

1. `interview/real-records/2026-07-13-kingdee-ai-application-senior-engineer.md`
2. `interview/mock-records/2026-07-13-kingdee-ai-application-senior-engineer-prep.md`
3. `sessions/2026-07-13-kingdee-ai-application-interview-prep.md`
4. `interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`
5. `sessions/2026-07-07-huashengtong-ai-application-interview-review.md`
6. `mistakes/interview/rag-rerank-algorithm-depth.md`
7. `interview/mock-records/2026-07-07-huashengtong-ai-application-engineer-prep.md`
8. `sessions/2026-07-07-langchain-langgraph-official-doc-map-gap.md`
9. `sessions/2026-07-07-langchain-langgraph-learning-summary.md`
10. `interview/ai-application-questions.md`
11. `interview/rag-project-story.md`

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
2. 读取 `interview/real-records/2026-07-13-kingdee-ai-application-senior-engineer.md`
3. 读取 `mistakes/interview/rag-rerank-algorithm-depth.md`
4. 优先把语义切分和表格 chunk 单独沉淀到正式 RAG 项目笔记或 `interview/ai-application-questions.md`
5. 随后继续整理 Rerank 机制：bi-encoder 召回 vs cross-encoder 重排、训练数据、hard negative、私有语料微调、业务规则特征、评测集和反馈闭环

---

## 6. 优先读取文件

1. `LEARNING_BACKLOG.md`
2. `interview/real-records/2026-07-13-kingdee-ai-application-senior-engineer.md`
3. `mistakes/interview/rag-rerank-algorithm-depth.md`
4. `interview/ai-application-questions.md`
5. `interview/rag-project-story.md`
6. `interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`
7. `interview/mock-records/2026-07-13-kingdee-ai-application-senior-engineer-prep.md`
8. `sessions/2026-07-13-kingdee-ai-application-interview-prep.md`
9. `backend/redis/distributed-lock.md`
10. `backend/java/thread-pool.md`
11. `LEARNING_ROADMAP.md`

需要判断长期能力方向时，再读取：

1. `LEARNING_ROADMAP.md`

需要确认文档规则时，再读取：

1. `AGENTS.md`
