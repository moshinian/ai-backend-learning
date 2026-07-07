# START HERE

## 1. 用法

新会话优先读取本文件，用于快速恢复当前学习上下文。

本文件只记录恢复入口，不写长篇知识内容。

---

## 2. 当前候选最高优先级

当前候选任务：

- `BL-013`：RAG 检索、重排与文档结构化解析补课

说明：

- 2026-07-07 晚 20:00 已完成华盛通 SZ-大模型应用工程师面试，面试官主要围绕 RAG 项目、文档解析、切片、混合检索、Rerank、并发、版本更新和 AI 应用认知展开追问。
- 面试结论：RAG 工程化、后端落地、Java / Python 分工、权限审计、版本切换和并发限流表达较稳；短板集中在 Rerank / NLP 算法机制、私有语料排序失效破局、结构化文档解析深度、模型部署和前沿算法关注。
- `BL-012` 面试专项准备已完成，当前最高优先级切换为 `BL-013`。
- `BL-011` LangChain / LangGraph 机制梳理仍是长期 P0，但应在 `BL-013` 第一轮补课后恢复。

---

## 3. 当前断点

当前断点：

1. 华盛通面试整体不是失败局。面试官认可工程化应用方向，但明确指出不懂算法会限制 RAG 项目深入落地。
2. 需要保留的优势表达：RAG 两条链路、Java / Python 分工、权限和审计、文档版本、向量灰度切换、并发瓶颈拆分和限流。
3. 需要立即补的短板：Rerank 的底层机制不能再泛化成“编码器-解码器”；要讲清 bi-encoder 召回、cross-encoder 重排、pairwise 打分、训练数据和 hard negative。
4. 文档解析不能只停留在固定窗口：需要补 Word 标题层级、段落、表格、图片、PDF / OCR、结构化切分和语义切分。
5. 对“私有数据强、开源 rerank 效果差、最相关片段排最后”要形成可执行方案：规则特征、业务字段加权、人工标注、hard negative、微调 reranker、评测集闭环。
6. 当前不急着继续泛学 LangGraph，先把 `BL-013` 中 RAG 检索 / 重排 / 文档解析补稳。

---

## 4. 最近学习位置

最近一次归档：

1. `interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`
2. `sessions/2026-07-07-huashengtong-ai-application-interview-review.md`
3. `mistakes/interview/rag-rerank-algorithm-depth.md`
4. `interview/mock-records/2026-07-07-huashengtong-ai-application-engineer-prep.md`
5. `sessions/2026-07-07-huashengtong-ai-application-interview-prep.md`
6. `sessions/2026-07-07-langchain-langgraph-official-doc-map-gap.md`
7. `sessions/2026-07-07-langchain-langgraph-learning-summary.md`
8. `interview/ai-application-questions.md`
9. `interview/rag-project-story.md`

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
2. 读取 `interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`
3. 读取 `mistakes/interview/rag-rerank-algorithm-depth.md`
4. 开始 `BL-013` 第一轮：Rerank / Fusion / 私有语料排序失效破局
5. 第一轮完成后再补文档结构化解析和 RAG 评测指标

---

## 6. 优先读取文件

1. `LEARNING_BACKLOG.md`
2. `interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`
3. `sessions/2026-07-07-huashengtong-ai-application-interview-review.md`
4. `mistakes/interview/rag-rerank-algorithm-depth.md`
5. `interview/mock-records/2026-07-07-huashengtong-ai-application-engineer-prep.md`
6. `interview/rag-project-story.md`
7. `interview/ai-application-questions.md`
8. `sessions/2026-07-07-langchain-langgraph-official-doc-map-gap.md`
9. `LEARNING_ROADMAP.md`

需要判断长期能力方向时，再读取：

1. `LEARNING_ROADMAP.md`

需要确认文档规则时，再读取：

1. `AGENTS.md`
