# RAG Rerank 与算法深度表达不足

## 错误表现

1. 面试官追问 Rerank 模型内部机制时，回答泛化为语料训练、编码器-解码器和向量转换，没有讲到 Rerank 的核心交互机制。
2. 面对“私有数据强、开源 reranker 效果差、最相关片段排在末尾”的极端场景，未能给出有效破局方案。
3. 文档切片和解析能讲工程策略，但对 Word 标题层级、PDF / OCR、表格、图片、多模态解析和结构化切分的前置方案不够清晰。
4. 前沿算法关注回答停留在推文浅层了解，未体现对 RAG / LLM 应用算法的持续跟踪机制。
5. 面对“语义切分”和“表格怎么 chunk”时，容易只说固定窗口、overlap 或让大模型辅助切分，没有先说明当前实现边界，也没有讲出结构抽取、候选切点、表格类型、row-level KV、多级索引和评测闭环。

## 根因

1. 当前优势集中在 RAG 后端工程链路，算法机制学习没有跟上项目关键词。
2. 对 Rerank 的理解停留在“排序更准”这一作用层，没有建立 bi-encoder 召回和 cross-encoder 重排的边界。
3. 对私有语料适配缺少训练数据、hard negative、业务规则特征、微调和评测闭环的完整框架。
4. 文档解析被当成普通文本解析，没有把 Word / PDF / OCR / 表格 / 图片作为 RAG 数据质量的上游关键问题。
5. 对 chunk 的理解初始偏“文本长度控制”，缺少“结构优先、长度兜底、语义增强、评测闭环”的工程分层；对表格缺少“先还原结构，再按表格类型 chunk”的检索工程视角。

## 正确理解

1. RAG 第一阶段召回常用 bi-encoder，把 query 和 chunk 分别编码成向量，适合快速召回。
2. Rerank 常用 cross-encoder，把 query 和候选 chunk 作为一对输入模型，让模型直接输出相关性分数；它更慢，但能捕捉更细粒度的 token 交互。
3. 私有语料场景中，通用 reranker 失效时，需要建立 query、正例 chunk、hard negative 和业务特征，做私有评测集和必要的微调。
4. 排序失效不能只排除模型因素，要从候选集是否包含正确证据、融合策略、Rerank 模型、业务特征、版本字段和评测数据逐层定位。
5. 文档解析和切片是 RAG 效果上游。标题层级、段落、表格、图片、PDF / OCR 和语义边界会直接影响 chunk 质量、召回质量和引用准确性。
6. 语义切分不是让大模型随意切，而是把句子 / 段落作为基础单元或相邻单元组，计算 embedding 相似度，语义距离明显变化的位置作为候选切分点，再结合 min_tokens、max_tokens、overlap 和文档结构约束。
7. 表格 chunk 的核心不是把表格转成普通文本后固定窗口切，而是先抽取表格结构，再按普通明细表、宽表、交叉表、Key-Value 表、多页表分别处理；检索侧应保留 table summary、row-level KV、structured JSON 和原始 HTML / Markdown 等多种表示。

## 复盘触发条件

1. 面试官追问 Rerank、Fusion、BM25、向量召回、cross-encoder、hard negative、私有语料微调。
2. 面试官问“最相关片段明明召回了，但排在最后怎么办”。
3. 面试官追问 Word / PDF 文档解析、标题层级、表格、图片或 OCR。
4. 面试官问是否关注前沿 RAG / LLM 应用算法。
5. 面试官追问固定窗口之外如何语义切分，或问 PDF / Word / CSV 中个性化表格如何 chunk。

## 关联主题

1. `BL-013 RAG 检索、重排与文档结构化解析补课`
2. `interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`
3. `interview/real-records/2026-07-13-kingdee-ai-application-senior-engineer.md`
4. `interview/ai-application-questions.md`
5. `interview/rag-project-story.md`
