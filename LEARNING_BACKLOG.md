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

### BL-015 平安系 Java 后端面试准备

- ID：BL-015
- 优先级：P0
- 来源：真实面试准备 + HR 明确建议 + 求职主线调整
- RoadmapRef：RM-02 数据库核心能力；RM-03 Java / Spring / 并发能力；RM-04 Redis / MQ / 分布式能力；RM-05 项目深挖与工程表达；RM-06 AI Backend / RAG / Agent 能力；RM-08 面试复盘与查漏补缺
- 状态：REVIEW
- 主题：围绕 2026-07-21 平安系 Java 后端面试，准备项目表达、Java / Spring / MySQL 高频题、生产排障和 AI 工程补充问题
- 学习目标：以 Java 后端为主身份完成本次面试准备；能用真实项目证据回答设计模式、生产问题、SQL 优化、线程与任务可靠性问题，并能以补充能力回答 Nebula、RAG 文件切分和 AI Coding。
- 验收标准：完成 60 秒自我介绍和两个代表项目的 2 分钟版本；每个项目至少准备一个真实难点、一个设计选择、一个故障或风险处理和一个复盘改进；能回答 HashMap / ConcurrentHashMap / Hashtable、依赖注入、Bean 创建时机与作用域、`@Transactional` 失效、SQL 优化和生产事故排查；能诚实说明 Nebula 使用边界；能回答 RAG 文件切分和 AI Coding 的实际使用；完成至少一轮按真实追问方式进行的模拟面试。
- 当前断点：2026-07-21 已完成 HR 三组建议的第一轮覆盖，并完成一次 60 秒自我介绍口述纠偏，评分 8/10。已能围绕真实项目回答策略模式、N+1 批处理优化、事务事故和生产排障；已完成 Spring DI、Bean 生命周期与作用域、事务代理边界、Java Map 对比、ConcurrentHashMap 的 CAS / 桶级同步、SQL 优化、RAG 文件切分和 AI Coding 的机制梳理。JVM、RocketMQ、缓存和通用 SQL 题只完成快速覆盖。两个项目的正式 2 分钟口述和完整综合模拟尚未完成。2026-07-23 已确认平安产险面试完成且未通过；尚未还原真实面试问题、现场回答和暴露短板，暂不判定未通过的具体原因。用户已明确暂停本次面试复盘，先推进 `BL-006` 与 Java 后端简历。
- 关联文件：`interview/mock-records/2026-07-21-pingan-java-backend-prep.md`、`projects/settlement-system/transaction-flow-and-reconciliation.md`、`sessions/2026-07-21-java-resume-project-evidence-and-pingan-breakpoint.md`、`sessions/2026-07-21-pingan-java-interview-prep-closeout.md`、`resume/java-backend-resume.md`、`backend/spring/ioc-bean-and-transaction-proxy.md`、`backend/java/map-and-concurrent-hash-map.md`、`backend/java/thread-pool.md`、`backend/mysql/sql-performance-analysis.md`、`backend/mysql/transaction.md`、`backend/mysql/lock-and-batch-processing.md`、`interview/mysql-questions.md`、`backend/redis/distributed-lock.md`、`interview/redis-questions.md`、`interview/rag-project-story.md`、`interview/ai-application-questions.md`
- 下一步动作：完成当前 Java 后端简历完善后，再按独立公司和场次还原平安产险面试的真实问题、现场回答、追问反应和主观感受；再基于证据分析未通过原因，归档真实面试记录，将可执行短板回流到 Backlog 或 `mistakes/`，并判断 `BL-015` 是否可以 DONE。

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
- 下一步动作：任务已完成；面试暴露问题当时已回流到 `BL-013`，当前全局恢复入口以 `START_HERE.md` 为准。

### BL-013 RAG 检索、重排与文档结构化解析补课

- ID：BL-013
- 优先级：P1
- 来源：真实面试暴露
- RoadmapRef：RM-06 AI Backend / RAG / Agent 能力；RM-08 面试复盘与查漏补缺
- 状态：REVIEW
- 主题：补齐 RAG 从工程链路进入算法追问时的关键短板
- 学习目标：理解混合检索、结果融合、Rerank、私有语料排序失效、结构化文档解析、语义切分、PDF / OCR 和 RAG 评测的机制边界，能把工程实现和算法原理连接起来。
- 验收标准：能讲清关键词检索、向量检索、RRF / 加权融合和 Rerank 的区别；能解释 cross-encoder rerank 的基本机制及其和 embedding 双塔召回的差异；能回答“最相关片段被排在最后怎么办”；能说明 Word 标题层级、表格、图片、PDF / OCR 对文档解析和切分的影响；能用 Recall@K、MRR、NDCG、faithfulness、引用准确性组织 RAG 评测。
- 当前断点：2026-07-21 已在 `BL-015` 中完成 RAG 文件切分答案梳理：常见方式包括长度、递归、结构、语义和父子多粒度切分；当前项目事实仍是固定窗口 + overlap + 自然边界兜底，其他方式属于优化方向。尚未进行独立口述追问验证。求职和学习主线仍是 Java 后端，本任务保持 AI 补充能力 REVIEW。
- 关联文件：`interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`、`sessions/2026-07-07-huashengtong-ai-application-interview-review.md`、`interview/real-records/2026-07-13-kingdee-ai-application-senior-engineer.md`、`sessions/2026-07-13-kingdee-ai-application-interview-prep.md`、`mistakes/interview/rag-rerank-algorithm-depth.md`、`interview/mock-records/2026-07-07-huashengtong-ai-application-engineer-prep.md`、`interview/mock-records/2026-07-13-kingdee-ai-application-senior-engineer-prep.md`、`interview/ai-application-questions.md`、`interview/rag-project-story.md`
- 下一步动作：只有后续目标岗位明确要求检索算法深度时，再做文件切分口述追问，并恢复语义切分、表格 chunk 和 Rerank 专项建设。

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
- 下一步动作：任务已完成；面试暴露问题当时已回流到 `BL-013`，当前全局恢复入口以 `START_HERE.md` 为准。

### BL-011 LangChain / LangGraph 机制梳理

- ID：BL-011
- 优先级：P2
- 来源：个人主动学习 + 目标岗位要求
- RoadmapRef：RM-06 AI Backend / RAG / Agent 能力
- 状态：TODO
- 主题：LangChain / LangGraph 的核心机制、边界和工程使用方式
- 学习目标：系统梳理 LangChain 与 LangGraph 分别解决什么问题，掌握 LangChain 的 Core components、Middleware、Runtime、Frontend、Advanced usage 目录层级，以及 LangGraph 的 Capabilities、Production、Frontend、Graph API / Functional API 等目录层级；能把这些内容压缩成工程可用的框架地图，而不是只记零散 API。
- 验收标准：能说明 LangChain、LangGraph、LangSmith 的职责边界；能按官方目录画出 LangChain / LangGraph 的学习地图；能解释 `create_agent`、Middleware、Runtime context、Graph API、Functional API、checkpoint、store、interrupt、streaming、subgraph、time travel 的作用和边界；能结合个人 RAG / Agent 项目说明什么时候用框架、什么时候保留业务状态在 Java 后端。
- 当前断点：2026-07-07 已完成第一轮机制梳理和实验验证，已验证 interrupt / resume、node 重放与幂等、调用方循环处理 interrupt、业务状态冲突校验、streaming、checkpoint 存储边界、标准模型工具调用 loop 和高风险副作用受控执行边界。尚缺 LangChain / LangGraph 官方目录地图级全貌。2026-07-18 因求职和学习主线切回 Java 后端，本任务降为 P2 TODO，保留现有实验与断点，不继续扩张框架目录。
- 关联文件：`LEARNING_ROADMAP.md`、`interview/ai-application-questions.md`、`sessions/2026-07-05-langchain-langgraph-agent-runtime.md`、`sessions/2026-07-05-langgraph-runtime-demo.md`、`sessions/2026-07-06-create-agent-stategraph-boundary.md`、`sessions/2026-07-07-langchain-langgraph-learning-summary.md`、`sessions/2026-07-07-langchain-langgraph-official-doc-map-gap.md`、`labs/langgraph-runtime-demo/README.md`、`labs/langgraph-runtime-demo/approval_flow_demo.py`、`labs/langgraph-runtime-demo/streaming_demo.py`、`labs/langgraph-runtime-demo/checkpoint_demo.py`、`labs/langgraph-runtime-demo/create_agent_demo.py`、`labs/langgraph-runtime-demo/hybrid_agent_graph_demo.py`、LangChain 官方文档：`https://docs.langchain.com/oss/python/langchain/overview`、LangGraph 官方文档：`https://docs.langchain.com/oss/python/langgraph/overview`
- 下一步动作：仅在目标岗位明确要求 LangChain / LangGraph，或 Java 主线稳定后，再恢复官方目录地图和 2 到 3 分钟口述验证。

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
- 优先级：P0
- 来源：旧冲刺计划迁移
- RoadmapRef：RM-03 Java / Spring / 并发能力
- 状态：TODO
- 主题：`synchronized`、`volatile`、CAS、AQS
- 学习目标：补齐 Java 并发锁体系，并和线程池、任务执行、分布式锁边界连接起来。
- 验收标准：能区分互斥、可见性、原子性和同步队列；能回答至少 2 个并发追问；能说明单 JVM 锁和分布式锁边界。
- 当前断点：线程池主线已完成第一轮；2026-07-21 通过 ConcurrentHashMap 补了 CAS 空桶插入、桶级 `synchronized`、可见性、协作扩容和复合操作原子性的入口，但尚未系统学习 `synchronized`、`volatile`、CAS 通用问题和 AQS。
- 关联文件：`backend/java/thread-pool.md`、`backend/java/map-and-concurrent-hash-map.md`、`interview/java-concurrency-questions.md`、`mistakes/concurrency/thread-pool.md`
- 下一步动作：先从 `synchronized` 解决什么问题开始，再进入 `volatile`、CAS、AQS。

### BL-005 Spring 核心机制

- ID：BL-005
- 优先级：P0
- 来源：旧冲刺计划迁移
- RoadmapRef：RM-03 Java / Spring / 并发能力
- 状态：REVIEW
- 主题：IOC、AOP、Bean 生命周期、`@Transactional` 失效场景
- 学习目标：建立 Spring 核心机制和 Web 请求链路的连接。
- 验收标准：能讲清 IOC 和 AOP 解决的问题；能说明 Bean 生命周期关键阶段；能回答 `@Transactional` 常见失效场景。
- 当前断点：2026-07-21 已完成 IOC / DI、Bean 创建时机、生命周期、作用域、prototype 销毁、AOP 代理与 `@Transactional` 失效的第一轮梳理，并能用对账辅账事务事故解释同类自调用和独立 Service 修复。当前仍缺独立口述验证，以及循环依赖、BeanPostProcessor 细节和更完整的 AOP 调用链。
- 关联文件：`backend/spring/ioc-bean-and-transaction-proxy.md`、`interview/mock-records/2026-07-21-pingan-java-backend-prep.md`、`projects/settlement-system/transaction-flow-and-reconciliation.md`、`fundamentals/network/http-tcp-request-flow.md`、`interview/computer-fundamentals-questions.md`
- 下一步动作：面试事件收口后，用 3 至 5 个追问验证 IOC、Bean 生命周期、代理、自调用和回滚规则；再决定是否进入循环依赖与 AOP 深挖。

### BL-006 结算系统项目表达与双版本简历完善

- ID：BL-006
- 优先级：P0
- 来源：项目表达短板 + 旧冲刺计划迁移
- RoadmapRef：RM-05 项目深挖与工程表达
- 状态：DOING
- 主题：结算系统 2 分钟和 10 分钟项目表达，以及 Java 后端 / AI 应用双版本简历完善
- 学习目标：把业务功能表达升级为工程能力表达，并形成事实一致、重点不同、可以按目标岗位继续定制的两份投递基准稿。
- 验收标准：Java 和 AI 两份简历的工作时间、项目事实与量化数据保持一致，分别突出 Java 生产工程能力和 RAG / Agent 应用能力；能用 2 分钟讲清结算系统定位、核心链路、异步状态、幂等恢复和规模瓶颈；能用 10 分钟展开一致性或幂等设计。
- 当前断点：2026-07-21 已将主职责统一为“交易流水处理与核销业务域”，并还原 FFP 文件集成、流水处理、订单匹配、辅账、ERP、待对账池和核销链路。已确认十组项目证据：三年不少于 50 次上游流水纠错、N+1 改造后达到 100 万笔 8 分钟以内、对账辅账事故涉及数千笔辅账及百万级关联明细、主动发现 ERP 发票/收据凭证 ID 命名空间碰撞并以“凭证 ID + 接口名”组合业务键修复、设计未对账池批量终止与恢复能力并实现受控状态流转和逐笔审计、通过动态 MySQL 分区查询范围将对账池生成任务由接近 40 分钟缩短至约 8 分钟并修复部分命中漏数据问题、通过分页与总数解耦和联合索引修复将亿级流水表尾页查询从超过 120 秒降至 3 秒以内、通过抢占式调度、Redis 锁、批次事务和明细级 Checkpoint 实现对账池任务中断续跑、独立设计结算单电子盖章模块并实现批量异步申请、跨系统回调关联、幂等状态更新、超时恢复和文件版本切换且上线运行 3 个月未发生生产故障或数据错误、通过 Heap Dump 定位 `ReconcileData` 及关联对象占用或保留内存超过 10GB且被 MyBatis 缓存长期持有，关闭对应查询缓存后经低内存对照测试与生产三个月运行均未再发生 OOM。2026-07-24 已完成 Java 后端和 AI 应用两份可投递基准稿及终稿审校：Java 版从十组证据中筛选六组最适合简历的生产案例，按职责、性能、可靠性、OOM 排障、主动防错和独立交付组织；AI 版突出 RAG 全链路、Java / Python 边界和受控 Agent，同时保留四年 Java 生产经验作为工程可信度。两份简历已删除期望薪资，避免过早锚定；MCP 明确为协议理解，MQ 只保留实际使用口径，不包装为中间件建设经验；公司时间、项目时间、规模与量化结果已校验一致。当前基准稿可以用于投递，获得具体 JD 后再调整关键词与案例顺序。结算系统 2 分钟和 10 分钟口述版本尚未完成。
- 关联文件：`projects/settlement-system/transaction-flow-and-reconciliation.md`、`projects/settlement-system/settlement-document-stamping.md`、`sessions/2026-07-24-java-ai-resume-and-project-evidence.md`、`sessions/2026-07-21-java-resume-project-evidence-and-pingan-breakpoint.md`、`sessions/2026-07-21-pingan-java-interview-prep-closeout.md`、`interview/mock-records/2026-07-21-pingan-java-backend-prep.md`、`backend/mysql/sql-performance-analysis.md`、`backend/spring/ioc-bean-and-transaction-proxy.md`、`resume/java-backend-resume.md`、`resume/ai-application-resume.md`、`interview/real-records/2026-06-10-llm-application-engineer.md`、`interview/real-records/2026-06-30-ai-agent-rag-backend.md`
- 下一步动作：由用户通读 Java 后端和 AI 应用两份基准稿，确认专业技能中的每个关键词都能接受追问；收到具体 JD 后分别调整关键词、个人优势和项目证据顺序。投递文件在仓库外补充真实联系方式并导出 PDF / Word。随后按“系统定位 -> 核心链路 -> 一致性 -> 失败恢复 -> 性能 -> 复盘”完成结算系统 2 分钟和 10 分钟口述版本。Map 构建、配置缓存和场景 ID 优先级语义仍作为待确认事实，不写入简历。

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
- 当前断点：事务、MVCC、索引和锁已完成第一轮；2026-07-21 又通过真实 N+1 案例梳理了“单条 SQL 耗时、调用次数、扫描范围、锁等待和整体访问模型”的 SQL 优化主线，并快速复盘 Join、Group By、Distinct、Union 和重复属性查询。死锁与执行计划追问稳定性仍需验证。
- 关联文件：`backend/mysql/transaction.md`、`backend/mysql/lock-and-batch-processing.md`、`backend/mysql/sql-performance-analysis.md`、`interview/mysql-questions.md`、`interview/mock-records/2026-07-21-pingan-java-backend-prep.md`、`mistakes/database/transaction.md`
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
- 当前断点：2026-07-21 开始平安产险模拟面试，仅完成一题 60 秒自我介绍并获得 8/10 评价；主要问题是职责范围偏大、AI 技术名词过密和结尾岗位匹配偏弱。尚未完成项目介绍和正式综合模拟。
- 关联文件：`interview/real-records/`、`mistakes/`
- 下一步动作：在 Redis 和项目表达补齐后，安排一轮 Java 后端综合模拟面试。
