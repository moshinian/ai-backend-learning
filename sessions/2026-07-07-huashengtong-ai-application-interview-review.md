# 2026-07-07 华盛通大模型应用工程师真实面试复盘

## 日期

2026-07-07

## 主题

归档华盛通 SZ-大模型应用工程师真实技术面试，提炼表现较好的部分、暴露短板和下一步学习入口。

## 本次做了什么

1. 阅读用户提供的腾讯会议元宝总结。
2. 将面试过程整理为真实面试复盘：`interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`。
3. 将核心错误模式整理为：`mistakes/interview/rag-rerank-algorithm-depth.md`。
4. 将 `BL-012` 标记为 DONE，并新增 `BL-013 RAG 检索、重排与文档结构化解析补课`。
5. 更新 `START_HERE.md` 和 `LEARNING_JOURNAL.md`，把恢复入口切到面试后暴露的最高优先级短板。

## 关键结论

1. 这次面试不是失败局。RAG 工程化、后端落地、Java / Python 分工、权限审计、版本切换和并发限流表达较稳。
2. 面试官真正暴露出的短板是 Rerank / NLP 算法机制、私有语料排序失效、结构化文档解析、模型部署和前沿算法关注。
3. 岗位偏工程化应用，但并不是纯业务开发；算法理解会决定 RAG 项目能否深入。
4. 短期学习不应继续泛学 LangGraph，而应优先补 RAG 检索、重排、结构化解析和评测。
5. 后续表达要从“我不擅长算法”升级为“我当前工程长板明确，下一步补 Rerank / Fusion / 文档解析 / 评测闭环”。

## 下次入口

继续 `BL-013`：

1. 先补 Rerank：bi-encoder vs cross-encoder、query-document pair、hard negative、私有语料微调。
2. 再补混合检索融合：BM25 / 关键词、向量召回、RRF、归一化加权、Rerank。
3. 再补文档解析和切片：Word 标题层级、表格、PDF / OCR、结构化切分、语义切分。
4. 最后补 RAG 评测：Recall@K、MRR、NDCG、faithfulness、引用准确性。

## 关联文件

1. `LEARNING_BACKLOG.md`
2. `START_HERE.md`
3. `interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`
4. `mistakes/interview/rag-rerank-algorithm-depth.md`
5. `interview/mock-records/2026-07-07-huashengtong-ai-application-engineer-prep.md`
6. `sessions/2026-07-07-huashengtong-ai-application-interview-prep.md`
