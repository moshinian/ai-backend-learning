# LEARNING BACKLOG

## 1. 定位

`LEARNING_BACKLOG.md` 是柔性学习任务池。

它负责回答：

> 现在具体要推进哪些学习任务？

它不负责写长篇知识笔记。正式知识沉淀应写入 `backend/`、`fundamentals/`、`projects/`、`interview/`、`mistakes/` 等对应位置。

---

## 2. 任务来源

Backlog 任务可以来自：

1. `LEARNING_ROADMAP.md`
2. 真实面试暴露
3. 项目表达短板
4. 临时技术问题
5. 个人主动学习
6. 长期基础补课
7. 旧冲刺计划迁移

规则：

1. 来自 Roadmap 的任务必须填写 `RoadmapRef`。
2. 有长期价值但 Roadmap 缺节点时，先补 Roadmap 能力节点，再加入 Backlog。
3. 临时问题可以只进入 Backlog。
4. 临时问题反复出现或被确认有长期能力价值时，需要回补 Roadmap。

---

## 3. 优先级和状态

优先级：

1. P0：当前最想学、最有动力、最应该优先推进的知识
2. P1：面试、项目表达、实际问题暴露出的短板
3. P2：长期重要但不紧急的基础知识

状态：

1. TODO：待学习
2. DOING：正在学习
3. REVIEW：已学完一轮，等待复盘或表达验证
4. DONE：已完成当前验收标准
5. BLOCKED：暂时卡住或等待外部信息

任务暂停时必须更新：

1. 状态
2. 当前断点
3. 下一步动作
4. 关联文件

任务完成时必须更新：

1. 状态
2. 验收结果
3. 关联沉淀文件
4. 是否需要回补 `LEARNING_ROADMAP.md` 或 `mistakes/`

---

## 4. 任务条目格式

每个任务至少包含：

1. ID
2. 优先级
3. 来源
4. RoadmapRef
5. 状态
6. 主题
7. 学习目标
8. 验收标准
9. 当前断点
10. 关联文件
11. 下一步动作

---

## 5. 当前任务池

### BL-014 金蝶 AI 应用开发高级工程师面试准备

- ID：BL-014
- 优先级：P0
- 来源：真实面试准备 + 目标岗位要求
- RoadmapRef：RM-03 Java / Spring / 并发能力；RM-04 Redis / MQ / 分布式能力；RM-05 项目深挖与工程表达；RM-06 AI Backend / RAG / Agent 能力；RM-08 面试复盘与查漏补缺
- 状态：DONE
- 主题：围绕金蝶软件中国 AI 应用开发高级工程师岗位，压缩 Java 后端、ERP 对接、Harness、Skill / MCP / API 工程化、Agent 和服务治理表达
- 学习目标：在 2026-07-13 19:00 面试前，把个人优势定位为“Java 后端工程化 + RAG / Agent 工具生态接入”，能把结算系统、RAG + Agent 系统、LangGraph / MCP / 工具调用学习、Redis / MQ / Spring / 微服务经验迁移到金蝶的 ERP 外部生态、Harness 工具研发、Skill / MCP / API 标准化和服务治理场景。
- 验收标准：能完成 60 秒自我介绍；能解释 Harness / Skill / MCP / API 在企业 AI 应用中的工程定位；能回答如何把 ERP、第三方 API 或 MCP Server 接入 Agent 工具体系；能说明工具调用的权限、幂等、超时、审计、灰度和高风险 human-in-the-loop；能处理“AI 项目是否正式上线”的边界追问；能把 Redis、Kafka / MQ、Docker、SpringCloud、MyBatis、MySQL / SQL Server、CI/CD 等关键词落到可靠服务治理，而不是堆栈罗列。
- 当前断点：2026-07-13 已完成金蝶软件中国 AI 应用开发高级工程师面试准备和真实面试归档。准备阶段完成新版简历口径、Harness / Skill / MCP / API、ERP Tool 接入、安全治理、持续交付、Agent 诊断流程、工具失败处理、重复入账、RAG 评测、Hybrid / Rerank、语义切分和表格 chunk 的口述准备。真实面试实际重心仍落在 RAG 项目深挖，暴露文档解析、chunk、Rerank、私有语料排序失效、模型部署和前沿算法跟踪短板，已回流到 `BL-013`。
- 关联文件：`interview/mock-records/2026-07-13-kingdee-ai-application-senior-engineer-prep.md`、`sessions/2026-07-13-kingdee-ai-application-interview-prep.md`、`interview/real-records/2026-07-13-kingdee-ai-application-senior-engineer.md`、`interview/rag-project-story.md`、`interview/ai-application-questions.md`、`backend/redis/distributed-lock.md`、`backend/java/thread-pool.md`、`mistakes/interview/rag-rerank-algorithm-depth.md`
- 下一步动作：任务已完成；后续学习入口转入 `BL-013`。

### BL-013 RAG 检索、重排与文档结构化解析补课

- ID：BL-013
- 优先级：P0
- 来源：真实面试暴露
- RoadmapRef：RM-06 AI Backend / RAG / Agent 能力；RM-08 面试复盘与查漏补缺
- 状态：DOING
- 主题：补齐 RAG 从工程链路进入算法追问时的关键短板
- 学习目标：理解混合检索、结果融合、Rerank、私有语料排序失效、结构化文档解析、语义切分、PDF / OCR 和 RAG 评测的机制边界，能把工程实现和算法原理连接起来。
- 验收标准：能讲清关键词检索、向量检索、RRF / 加权融合和 Rerank 的区别；能解释 cross-encoder rerank 的基本机制及其和 embedding 双塔召回的差异；能回答“最相关片段被排在最后怎么办”；能说明 Word 标题层级、表格、图片、PDF / OCR 对文档解析和切分的影响；能用 Recall@K、MRR、NDCG、faithfulness、引用准确性组织 RAG 评测。
- 当前断点：2026-07-13 金蝶真实面试再次暴露 RAG 文档解析、chunk、Rerank 和私有语料排序失效短板。当前项目实际落地仍应表述为固定窗口 + overlap + 自然边界兜底；成熟优化方向应表述为结构优先、长度兜底、语义增强、评测闭环。语义切分理解为句子 / 段落基础单元或相邻单元组 embedding 相似度下降处作为候选切点，再加 min_tokens / max_tokens / overlap 和结构保护。表格 chunk 不能按普通文本切，应先抽取表格结构，再按明细表、宽表、交叉表、KV 表、多页表分别处理，并保留 table summary、row-level KV、structured JSON 和原始 HTML / Markdown 等多种表示。下一轮要把这些内容从面试准备口径沉淀为正式知识笔记和可复述答案。
- 关联文件：`interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`、`sessions/2026-07-07-huashengtong-ai-application-interview-review.md`、`interview/real-records/2026-07-13-kingdee-ai-application-senior-engineer.md`、`sessions/2026-07-13-kingdee-ai-application-interview-prep.md`、`mistakes/interview/rag-rerank-algorithm-depth.md`、`interview/mock-records/2026-07-07-huashengtong-ai-application-engineer-prep.md`、`interview/mock-records/2026-07-13-kingdee-ai-application-senior-engineer-prep.md`、`interview/ai-application-questions.md`、`interview/rag-project-story.md`
- 下一步动作：优先把语义切分和表格 chunk 单独沉淀到正式 RAG 项目笔记或 `interview/ai-application-questions.md`；随后继续整理 Rerank 机制：bi-encoder 召回 vs cross-encoder 重排、训练数据、hard negative、私有语料微调、业务规则特征、评测集和反馈闭环。

### BL-012 华盛通大模型应用工程师面试专项准备

- ID：BL-012
- 优先级：P0
- 来源：真实面试准备 + 目标岗位要求
- RoadmapRef：RM-06 AI Backend / RAG / Agent 能力；RM-08 面试复盘与查漏补缺
- 状态：DONE
- 主题：围绕华盛通 SZ-大模型应用工程师 JD，压缩 RAG、LangChain / Dify、后端工程和推理加速边界表达
- 学习目标：在真实面试前，把个人简历中的 RAG 项目表达、后端工程迁移能力、金融场景可信 RAG 风险控制、LangChain / Dify / LangGraph 边界、CUDA / TensorRT 短板防守整理成可口述答案。
- 验收标准：能完成 60 秒自我介绍；能讲清企业知识库 RAG 的离线索引链路和在线问答链路；能回答 Chunk、Embedding、向量检索、召回排查、pgvector、权限隔离、幻觉控制、索引任务失败、版本冲突、金融场景风险；能诚实说明 RAG 未生产上线、Agent / LangGraph / Dify / CUDA 不是简历主经验；能把优势落到 Java 后端 + RAG 应用工程化。
- 当前断点：2026-07-07 已完成面试前准备和 20:00 华盛通真实面试验证。准备内容覆盖开场介绍、RAG 项目主线、RAG 排查链路、金融可信 RAG、LangChain / Dify 定位、Redis / MQ / Spring / FastAPI 后端支撑、CUDA / TensorRT 防守表达。面试后已归档真实复盘，新增 `BL-013` 处理 Rerank、检索融合和文档结构化解析短板。
- 关联文件：`interview/mock-records/2026-07-07-huashengtong-ai-application-engineer-prep.md`、`sessions/2026-07-07-huashengtong-ai-application-interview-prep.md`、`interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`、`sessions/2026-07-07-huashengtong-ai-application-interview-review.md`、`interview/rag-project-story.md`、`interview/ai-application-questions.md`、`interview/redis-questions.md`、`backend/redis/distributed-lock.md`
- 下一步动作：任务已完成；后续学习入口转入 `BL-013`。

### BL-011 LangChain / LangGraph 机制梳理

- ID：BL-011
- 优先级：P0
- 来源：个人主动学习 + 目标岗位要求
- RoadmapRef：RM-06 AI Backend / RAG / Agent 能力
- 状态：DOING
- 主题：LangChain / LangGraph 的核心机制、边界和工程使用方式
- 学习目标：系统梳理 LangChain 与 LangGraph 分别解决什么问题，掌握 LangChain 的 Core components、Middleware、Runtime、Frontend、Advanced usage 目录层级，以及 LangGraph 的 Capabilities、Production、Frontend、Graph API / Functional API 等目录层级；能把这些内容压缩成工程可用的框架地图，而不是只记零散 API。
- 验收标准：能说明 LangChain、LangGraph、LangSmith 的职责边界；能按官方目录画出 LangChain / LangGraph 的学习地图；能解释 `create_agent`、Middleware、Runtime context、Graph API、Functional API、checkpoint、store、interrupt、streaming、subgraph、time travel 的作用和边界；能结合个人 RAG / Agent 项目说明什么时候用框架、什么时候保留业务状态在 Java 后端。
- 当前断点：2026-07-07 已完成第一轮机制梳理和实验验证，但随后对照官方文档发现学习范围偏向 `create_agent`、StateGraph、checkpoint、interrupt 等 runtime 片段，仍缺 LangChain 官方目录中的 Core components / Middleware / Frontend / Advanced usage 全貌，以及 LangGraph 官方目录中的 Capabilities / Production / Frontend / LangGraph APIs 全貌。因此 `BL-011` 从 REVIEW 拉回 DOING，先补“官方目录地图级理解”，再进入口述验收。已验证 interrupt / resume、node 重放与幂等、调用方循环处理 interrupt、业务状态冲突校验、`stream_mode="updates"` / `stream_mode="values"`、`InMemorySaver` 下 `thread_id` 和 checkpoint 存储介质边界；已通过真实 `create_agent()` demo 验证标准模型工具调用 loop，并通过混合 mock demo 验证高风险副作用工具应放在 StateGraph / Java 后端受控执行节点。
- 关联文件：`LEARNING_ROADMAP.md`、`interview/ai-application-questions.md`、`sessions/2026-07-05-langchain-langgraph-agent-runtime.md`、`sessions/2026-07-05-langgraph-runtime-demo.md`、`sessions/2026-07-06-create-agent-stategraph-boundary.md`、`sessions/2026-07-07-langchain-langgraph-learning-summary.md`、`sessions/2026-07-07-langchain-langgraph-official-doc-map-gap.md`、`labs/langgraph-runtime-demo/README.md`、`labs/langgraph-runtime-demo/approval_flow_demo.py`、`labs/langgraph-runtime-demo/streaming_demo.py`、`labs/langgraph-runtime-demo/checkpoint_demo.py`、`labs/langgraph-runtime-demo/create_agent_demo.py`、`labs/langgraph-runtime-demo/hybrid_agent_graph_demo.py`、LangChain 官方文档：`https://docs.langchain.com/oss/python/langchain/overview`、LangGraph 官方文档：`https://docs.langchain.com/oss/python/langgraph/overview`
- 下一步动作：补官方目录地图：先整理 LangChain 的 Core components、Middleware、Runtime、Frontend、Advanced usage 分层，再整理 LangGraph 的 Capabilities、Graph API / Functional API、Production、Frontend 分层；补完后再进行 2 到 3 分钟口述验证，要求同时讲清“模型负责建议、runtime 负责流程、Java DB 负责事实和权限”的项目边界。

### BL-001 Redis 数据结构与对象存储边界

- ID：BL-001
- 优先级：P0
- 来源：真实面试暴露 + 旧冲刺计划迁移
- RoadmapRef：RM-04 Redis / MQ / 分布式能力
- 状态：TODO
- 主题：Redis 常见数据结构、Hash 与序列化 String 的对象存储边界
- 学习目标：能讲清 Redis 对外数据类型的典型场景，并能解释对象用 Hash 或 String 存储的取舍。
- 验收标准：能用 1 分钟回答 Redis 常见数据结构；能比较 Hash 与序列化 String；能解释为什么分布式锁通常使用 String。
- 当前断点：2026-06-30 真实面试暴露 Redis 数据结构回答偏底层实现，未先回答对外数据类型。
- 关联文件：`interview/real-records/2026-06-30-ai-agent-rag-backend.md`、`interview/redis-questions.md`
- 下一步动作：先复盘 String、Hash、List、Set、ZSet、Stream 的工程场景，再整理 Hash 与 String 存对象的面试回答。

### BL-002 Redis 分布式锁粒度表达

- ID：BL-002
- 优先级：P0
- 来源：真实面试暴露 + 旧冲刺计划迁移
- RoadmapRef：RM-04 Redis / MQ / 分布式能力
- 状态：REVIEW
- 主题：业务抢占锁、框架级任务锁、数据库状态机处理权的边界
- 学习目标：能先区分锁的目标，再回答锁应该覆盖短临界区还是整个任务周期。
- 验收标准：能用 1 分钟讲清 Redis 分布式锁实现；能解释为什么不能只依赖 Redis 锁保证任务只处理一次；能结合数据库 `process_token` 和状态机回答长任务场景。
- 当前断点：Redis 分布式锁第一轮已学习，但面试中锁粒度表达出现摇摆。
- 关联文件：`backend/redis/distributed-lock.md`、`interview/redis-questions.md`、`mistakes/distributed/redis-lock.md`
- 下一步动作：重写“锁整个任务还是只锁临界区”的面试回答，并用结算任务场景复述。

### BL-003 MQ 可靠性主线

- ID：BL-003
- 优先级：P1
- 来源：旧冲刺计划迁移
- RoadmapRef：RM-04 Redis / MQ / 分布式能力
- 状态：TODO
- 主题：消息不丢、重复消费、幂等消费、顺序消息、消息积压
- 学习目标：建立 MQ 可靠性问题的完整主线，并能落到项目状态流转和补偿场景。
- 验收标准：能解释 MQ 为什么出现；能回答消息不丢和重复消费；能结合幂等键、状态机和补偿讲项目实践。
- 当前断点：MQ 主线尚未系统学习。
- 关联文件：`LEARNING_ROADMAP.md`
- 下一步动作：从“MQ 解决什么工程问题”开始，建立生产者、Broker、消费者和业务幂等的链路。

### BL-004 Java 并发锁体系

- ID：BL-004
- 优先级：P1
- 来源：旧冲刺计划迁移
- RoadmapRef：RM-03 Java / Spring / 并发能力
- 状态：TODO
- 主题：`synchronized`、`volatile`、CAS、AQS
- 学习目标：补齐 Java 并发锁体系，并和线程池、任务执行、分布式锁边界连接起来。
- 验收标准：能区分互斥、可见性、原子性和同步队列；能回答至少 2 个并发追问；能说明单 JVM 锁和分布式锁边界。
- 当前断点：线程池主线已完成第一轮，但 Java 锁、CAS、AQS 尚未展开。
- 关联文件：`backend/java/thread-pool.md`、`interview/java-concurrency-questions.md`、`mistakes/concurrency/thread-pool.md`
- 下一步动作：先从 `synchronized` 解决什么问题开始，再进入 `volatile`、CAS、AQS。

### BL-005 Spring 核心机制

- ID：BL-005
- 优先级：P1
- 来源：旧冲刺计划迁移
- RoadmapRef：RM-03 Java / Spring / 并发能力
- 状态：TODO
- 主题：IOC、AOP、Bean 生命周期、`@Transactional` 失效场景
- 学习目标：建立 Spring 核心机制和 Web 请求链路的连接。
- 验收标准：能讲清 IOC 和 AOP 解决的问题；能说明 Bean 生命周期关键阶段；能回答 `@Transactional` 常见失效场景。
- 当前断点：Spring MVC 请求链路已有基础，Spring 核心机制尚未系统学习。
- 关联文件：`fundamentals/network/http-tcp-request-flow.md`、`interview/computer-fundamentals-questions.md`
- 下一步动作：先从 IOC 为什么出现开始，再补 AOP 和事务代理边界。

### BL-006 结算系统项目表达

- ID：BL-006
- 优先级：P1
- 来源：项目表达短板 + 旧冲刺计划迁移
- RoadmapRef：RM-05 项目深挖与工程表达
- 状态：DOING
- 主题：结算系统 2 分钟和 10 分钟项目表达
- 学习目标：把业务功能表达升级为工程能力表达。
- 验收标准：能用 2 分钟讲清系统定位、核心链路、异步状态、幂等恢复、规模瓶颈；能用 10 分钟展开一致性或幂等设计。
- 当前断点：项目素材充分，但系统架构、数据流和性能瓶颈容易混在一起。
- 关联文件：`interview/real-records/2026-06-10-llm-application-engineer.md`、`interview/real-records/2026-06-30-ai-agent-rag-backend.md`
- 下一步动作：按“系统定位 -> 业务场景 -> 上下游与核心数据流 -> 状态管理 -> 失败恢复 -> 规模与瓶颈”重写 2 分钟回答。

### BL-007 RAG / Agent 项目事实边界表达

- ID：BL-007
- 优先级：P1
- 来源：真实面试暴露
- RoadmapRef：RM-06 AI Backend / RAG / Agent 能力
- 状态：TODO
- 主题：未生产上线的 RAG / Agent 项目如何表达工程价值
- 学习目标：明确区分已实现能力、个人实践、生产化设计和未落地边界。
- 验收标准：能回答“没有生产上线为什么仍能证明能力”；能区分固定 Pipeline、Workflow 和 Agent；能避免把设计方案包装成生产经验。
- 当前断点：2026-06-30 真实面试中，项目真实性和 Agent 概念被持续追问。
- 关联文件：`interview/rag-project-story.md`、`interview/ai-application-questions.md`、`interview/real-records/2026-06-30-ai-agent-rag-backend.md`
- 下一步动作：整理“事实 -> 架构 -> 职责 -> 难点 -> 边界 -> 下一步验证”的项目回答。

### BL-008 MySQL 追问复盘

- ID：BL-008
- 优先级：P2
- 来源：旧冲刺计划迁移
- RoadmapRef：RM-02 数据库核心能力
- 状态：REVIEW
- 主题：死锁、锁分类、慢 SQL 和事务日志边界
- 学习目标：把已学 MySQL 主线转成稳定追问能力。
- 验收标准：能回答死锁产生与排查；能区分共享锁、排他锁、乐观锁、悲观锁、Redis 锁和数据库锁；能用执行计划反推访问路径。
- 当前断点：事务、MVCC、索引和锁已完成第一轮，但追问稳定性仍需复盘。
- 关联文件：`backend/mysql/transaction.md`、`backend/mysql/lock-and-batch-processing.md`、`interview/mysql-questions.md`、`mistakes/database/transaction.md`
- 下一步动作：用 3 到 5 个追问验证死锁、锁分类和慢 SQL 访问路径。

### BL-009 算法保底

- ID：BL-009
- 优先级：P2
- 来源：旧冲刺计划迁移
- RoadmapRef：RM-07 算法与问题求解能力
- 状态：TODO
- 主题：滑动窗口、二分、DP 代表题复述
- 学习目标：建立算法面试保底表达能力。
- 验收标准：完成至少 3 道代表题的思路复述；能讲清状态、选择、边界、复杂度；能独立写出基础 Java 实现。
- 当前断点：DP 已完成多轮学习，滑动窗口和二分尚未开始。
- 关联文件：`fundamentals/algorithm/dp-basic.md`、`mistakes/algorithm/dp.md`
- 下一步动作：先短时复述 DP 代表题，再选择滑动窗口或二分开始第一轮。

### BL-010 综合模拟面试与错题清单

- ID：BL-010
- 优先级：P2
- 来源：旧冲刺计划迁移
- RoadmapRef：RM-08 面试复盘与查漏补缺
- 状态：TODO
- 主题：综合模拟面试、评分、错题和表达问题清单
- 学习目标：通过模拟面试检验后端基础、项目表达和算法表达。
- 验收标准：完成至少一轮综合模拟面试；形成高频错题和表达问题清单；将反复错误回补到 `mistakes/` 或 Backlog。
- 当前断点：已有真实面试复盘，但尚未完成正式综合模拟面试。
- 关联文件：`interview/real-records/`、`mistakes/`
- 下一步动作：在 Redis 和项目表达补齐后，安排一轮 Java 后端综合模拟面试。
