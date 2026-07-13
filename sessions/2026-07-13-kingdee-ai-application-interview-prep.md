# 2026-07-13 金蝶 AI 应用开发面试准备

## 日期

2026-07-13

## 主题

金蝶软件中国 AI 应用开发高级工程师面试前准备；同时补齐 RAG 文档切分、语义切分和表格 chunk 的面试表达。

## 本次做了什么

1. 根据金蝶 JD 新增 `BL-014`，把今晚面试定位为“AI 应用开发 + ERP / 外部系统生态接入 + Harness / Skill / MCP / API 工程化 + 服务治理”。
2. 按新版简历重新校准口径：荣耀经历是企业后端生产经验；RAG + Agent 系统是围绕企业知识库和结算文档问答场景建设的 AI 应用工程项目。
3. 完成一轮核心口述演练：60 秒自我介绍、为什么适合金蝶、Harness / Skill / MCP / API 关系、ERP Tool 接入、Agent 工具安全治理、统一服务治理、Skill / MCP / API 持续交付。
4. 完成一轮防守题演练：AI 项目是否正式上线、工具调用失败 / 超时 / 重复执行、SpringCloud / Kafka / Redis / MyBatis / Docker / SQL Server 经验边界、ERP 入账如何防重复、Agent 诊断订单未入账流程、Agent 选错工具或传错参数怎么办、MCP 和普通 API / function calling 的关系。
5. 补齐 RAG 追问表达：RAG 评测、Hybrid Retrieval / Fusion / Rerank 区别、正确文档召回但排序靠后的短中长期方案。
6. 深挖 Chunk 短板：确认当前项目实际落地是固定窗口 + overlap + 自然边界兜底；语义切分、结构化切分和表格 chunk 属于需要继续沉淀的优化方向。

## 关键结论

1. 金蝶岗位的核心表达不是“我会 RAG”，而是“我能把 LLM / Agent 能力安全、稳定、可审计地接入 ERP 和第三方系统生态”。
2. 自我介绍要避免主动自降为“个人 demo”。如果面试官不问是否正式上线，不主动展开；如果明确问，要诚实说明不是公司正式生产上线项目，并立即强调完整工程链路和可迁移能力。
3. Harness 可以表达为承载 Agent / LLM 应用运行、上下文、工具调用、状态、人工确认、权限和观测的工程层。
4. Skill 不能简单说成 Prompt 应用。更稳的说法是：面向业务场景封装的可调用能力单元，包含工具说明、参数 Schema、业务语义、权限、错误处理、返回格式和治理策略。
5. ERP Tool 接入应按“风险分级 -> 工具契约 -> Adapter -> Runtime 治理 -> 高风险人工确认 -> 审计回放”表达。
6. ERP 入账防重复要讲清：业务唯一键、条件更新抢占、推送状态、入账状态、下游幂等、超时查状态 / 对账；同步推送成功不等于最终入账成功。
7. RAG chunk 面试要诚实守边界：当前实现是固定窗口 + overlap + 自然边界；成熟优化方向是结构优先、长度兜底、语义增强、评测闭环。
8. 语义切分的工程表达：句子 / 段落作为基础单元或相邻单元组，计算 embedding 相似度，语义距离明显变化处作为候选切点，再加 min_tokens、max_tokens、overlap 和结构保护。
9. 表格 chunk 的工程表达：先抽取表格结构，再按表格类型处理。普通明细表适合 row-level KV；宽表按列族拆；交叉表把行头 + 列头 + 单元格值转成事实；多页表要继承表头；同时保留 table summary、row-level KV、structured JSON、原始 HTML / Markdown 多种表示。

## 下次入口

面试前最后复习顺序：

1. 60 秒自我介绍：Java 后端生产经验 + RAG / Agent 工程项目 + 金蝶岗位匹配。
2. 岗位适配：ERP / 外部 API / MCP / Skill 接入 Harness，核心是权限、幂等、审计、服务治理。
3. ERP Tool 接入：查询类和写操作分风险，写操作 human-in-the-loop，超时按未知结果处理。
4. AI 项目边界：不主动自降；被问正式上线时诚实说明边界，并强调完整工程系统而非 demo。
5. RAG chunk：固定窗口已落地；语义切分和表格 chunk 是成熟优化方向，不能包装成已完整落地。
6. 面试后立即新增 `interview/real-records/2026-07-13-kingdee-ai-application-senior-engineer.md`，记录真实追问、现场回答、暴露短板和后续任务。

## 关联文件

1. `LEARNING_BACKLOG.md`
2. `START_HERE.md`
3. `LEARNING_JOURNAL.md`
4. `interview/mock-records/2026-07-13-kingdee-ai-application-senior-engineer-prep.md`
5. `interview/rag-project-story.md`
6. `interview/ai-application-questions.md`
7. `mistakes/interview/rag-rerank-algorithm-depth.md`
8. `interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`
