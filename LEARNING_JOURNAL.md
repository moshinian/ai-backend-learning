# LEARNING JOURNAL

## 作用

这个文件只负责四类信息：

1. 长期学习画像
2. 阶段性反思和重要变化
3. 长期典型误区模式
4. 已沉淀主题与历史会话索引

它不是当前状态权威文件。

当前恢复学习进度时，只需要优先读取：

1. `START_HERE.md`

任务优先级、状态、验收标准、当前断点和下一步动作以 `LEARNING_BACKLOG.md` 为准。

具体知识笔记和错误纠偏不在本文件展开，只保留索引。

---

## 长期学习画像

- 背景：
  - 有 Java 后端开发经验
  - 做过云服务结算系统
  - 也在做 RAG 知识问答系统
- 当前目标：
  - 以 Java 后端作为求职和长期能力建设主航道，从“会做业务开发”升级为“能讲清机制、能设计系统、能稳定应对 Java 后端面试”
  - 保留 RAG / Agent 应用工程能力作为差异化补充，重点体现模型能力接入业务系统时的后端工程价值，不再把算法型 AI 应用岗位作为主要竞争方向
- 学习偏好：
  - 优先理解本质
  - 优先建立知识结构
  - 优先结合项目和面试表达
  - 不希望直接灌输标准答案

---

## 重要变化

### 2026-07-18 求职与学习主线切回 Java 后端

- 连续的实际求职和 HR 沟通反馈表明，部分 AI 应用岗位更倾向于具备算法、模型训练、检索排序或推理部署背景的候选人。
- 当前更有证据支撑的优势仍是 Java 后端、结算业务、状态流转、幂等、批处理、数据库、缓存和失败恢复。
- 后续职业定位调整为“Java 后端主线 + AI 应用工程补充”：优先竞争 Java 后端、平台后端及偏工程接入的 AI 平台后端岗位。
- 已有 RAG / Agent 学习不作废，但后续只在岗位明确需要或能强化后端差异化时继续投入，不再无边界扩张算法和框架知识面。
- 具体任务优先级和当前断点以 `LEARNING_BACKLOG.md`、`START_HERE.md` 为准。

### 2026-07-21 Java 主线从方向判断进入证据化表达

- 平安产险面试准备把“切回 Java 后端”从求职方向判断推进到实际学习和表达：结算系统不再按功能清单介绍，而是围绕交易流水与核销业务域、真实故障、性能结果和设计边界组织。
- 已确认当前最有竞争力的证据不是技术名词数量，而是三类可追问事实：上游纠错的冲销补偿、N+1 批处理优化、事务边界事故定位与修复。
- Java 基础开始和真实项目互相验证：Spring 代理解释事务事故，SQL 访问模型解释 N+1 性能问题，CAS / 桶级同步解释并发容器，状态抢占与业务幂等解释定时任务唯一性。
- 当前能力仍不均衡：Spring、事务、SQL 和项目证据已完成第一轮结构化；JVM、RocketMQ、Redis 数据结构、`synchronized` / `volatile` / AQS 仍偏面试速答，后续不能把“看过答案”误认为“稳定掌握”。
- 面试表达形成新的校验顺序：先限定本人职责，再讲问题和证据，然后解释机制、结果与复盘；不确定的框架细节、生产效果和他人负责模块明确保留边界。

### 2026-07-24 项目证据形成双版本简历基准

- 结算系统经历从三组代表案例扩展为覆盖性能、可靠性、跨系统状态、主动防错和 JVM 排障的十组可追问证据，并分别归档到交易核销与电子盖章项目文档。
- Java 后端与 AI 应用两份简历不再按技术栈多少区分，而是共享同一组工作事实、按岗位选择不同证据：Java 版突出生产工程能力，AI 版突出 RAG / Agent 链路及 Java / Python 协作边界。
- 简历事实校验形成稳定原则：量化结果必须带真实条件和生产验证；无法确认的 MyBatis 缓存层级、Mapper 结构和待落地优化不写成确定事实；MQ 保持实际使用口径，MCP 只表述为协议理解。
- 两份简历已成为可继续按 JD 定制的投递基准稿；具体任务断点仍以 `BL-006` 和 `START_HERE.md` 为准。

---

## 长期典型误区模式

本节只记录长期反复出现的认知模式。具体错误表现、根因和纠正内容，以 `mistakes/`、`backend/`、`fundamentals/`、`interview/` 和 `sessions/` 中的主题文件为准。

### 1. 容易把框架链路当成完整链路

典型表现：

- HTTP 请求只讲到 Controller、Service、DAO，容易漏掉 DNS、TCP、端口、容器、线程和内核协议栈。
- 三次握手、可靠传输、连接复用等边界容易混在一起。

主要索引：

1. `fundamentals/network/http-tcp-request-flow.md`
2. `mistakes/network/request-flow.md`
3. `interview/computer-fundamentals-questions.md`

### 2. 容易把机制名词背熟，但边界说不稳

典型表现：

- MySQL 事务、隔离级别、MVCC、undo log、redo log、binlog 的职责边界容易混淆。
- 快照读、当前读、行锁、间隙锁、Next-Key Lock 容易被统一说成“锁机制”。
- 慢 SQL、索引失效和执行计划容易只背结论，缺少访问路径分析。
- 容易把 SQL 性能问题等同于单条慢 SQL，忽略 N+1、累计调用次数和数据库往返。
- 容易只看到 `@Transactional` 注解，忽略真实代理调用链、异常规则、线程和数据源边界。
- 容易把 JDBC 回滚异常直接解释成事务未开启或数据库部分提交，缺少对原始异常和最终数据状态的核对。

主要索引：

1. `backend/mysql/transaction.md`
2. `backend/mysql/lock-and-batch-processing.md`
3. `mistakes/database/transaction.md`
4. `interview/mysql-questions.md`

### 3. 容易把任务状态、处理权和业务幂等混在一起

典型表现：

- 初始容易只用 `status` 判断任务是否还能推进，忽略 `process_token`、租约、心跳、重试和补偿。
- 外部 ERP 调用超时时，容易把“不知道结果”误判成“失败”。
- Redis 锁、数据库状态机和业务幂等键的职责容易混答。

主要索引：

1. `backend/mysql/lock-and-batch-processing.md`
2. `backend/redis/distributed-lock.md`
3. `mistakes/distributed/redis-lock.md`
4. `interview/redis-questions.md`

### 4. Java 并发容易把执行模型和可靠性问题混在一起

典型表现：

- 线程池提交顺序、队列风险、拒绝策略、`submit/execute` 异常处理、中断语义需要反复稳定。
- 容易把线程数、队列容量、数据库连接池、下游容量和任务可靠性放在一个层次里讲。
- 容易把“线程安全容器”理解为整段业务逻辑自动原子化，忽略单次原子操作与多步复合操作的区别。
- ConcurrentHashMap 容易停留在“分段锁”旧口径，需要区分 Java 7 Segment 和 Java 8 以后 CAS、桶级同步、协作扩容的实现主线。

主要索引：

1. `backend/java/thread-pool.md`
2. `mistakes/concurrency/thread-pool.md`
3. `interview/java-concurrency-questions.md`

### 5. 算法题容易先套分类，后定义状态

典型表现：

- DP 中容易先想公式或背包分类，而不是先定义子问题、状态含义、答案位置和转移依赖。
- 前缀长度、字符下标、`dp[0]` 初始化、一维压缩中的旧值和新值需要持续用语义校验。

主要索引：

1. `fundamentals/algorithm/dp-basic.md`
2. `mistakes/algorithm/dp.md`

### 6. 项目表达容易堆功能，缺少问题分层

典型表现：

- 结算系统容易把业务场景、系统架构、数据流、性能瓶颈和技术栈混在一起。
- RAG 项目容易罗列文档解析、向量化、模型调用等功能，而不是按业务问题、架构、职责、难点和指标组织。

主要索引：

1. `interview/rag-project-story.md`
2. `interview/ai-application-questions.md`
3. `interview/real-records/2026-06-10-llm-application-engineer.md`
4. `interview/real-records/2026-06-30-ai-agent-rag-backend.md`

### 7. AI Backend 表达容易混淆已实现、设计方案和生产经验

典型表现：

- RAG / Agent 项目没有生产上线时，需要主动说明事实边界，不能虚构生产效果，也不能只说“没上线”。
- 固定 RAG Pipeline、Workflow、Agent、模型选型、工具调用和人工确认容易混答。
- 检索、融合、Rerank、Prompt 和生成层优化需要分层表达。
- LangChain / LangGraph 学习中，容易把框架 runtime 状态、checkpoint、后端业务状态、审批事实和工具执行副作用混成一层，需要持续区分“执行现场”和“业务事实”。
- 学习 LangChain / LangGraph 时，容易只抓住已跑通的 `create_agent`、StateGraph、checkpoint、interrupt 片段，忽略官方文档中的 Core components、Middleware、Runtime、Frontend、Capabilities、Production、Graph API / Functional API 等目录级全貌。
- RAG 工程链路能讲通后，容易在 Rerank、私有语料排序失效、文档结构化解析和前沿算法追问处变成泛化回答，需要把工程链路和检索 / NLP 算法机制接起来。
- RAG 文档切分容易停留在固定窗口 + overlap，面对语义切分、Word / PDF / OCR / 表格等复杂文档结构时，需要主动区分“已落地实现”和“成熟优化方案”，并把结构抽取、语义边界、表格结构和评测闭环讲清。

主要索引：

1. `interview/rag-project-story.md`
2. `interview/ai-application-questions.md`
3. `interview/real-records/2026-06-30-ai-agent-rag-backend.md`
4. `sessions/2026-06-30-ai-agent-rag-backend-interview.md`
5. `sessions/2026-07-05-langchain-langgraph-agent-runtime.md`
6. `sessions/2026-07-05-langgraph-runtime-demo.md`
7. `labs/langgraph-runtime-demo/README.md`
8. `sessions/2026-07-06-create-agent-stategraph-boundary.md`
9. `sessions/2026-07-07-langchain-langgraph-learning-summary.md`
10. `sessions/2026-07-07-langchain-langgraph-official-doc-map-gap.md`
11. `interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`
12. `mistakes/interview/rag-rerank-algorithm-depth.md`
13. `sessions/2026-07-13-kingdee-ai-application-interview-prep.md`
14. `interview/real-records/2026-07-13-kingdee-ai-application-senior-engineer.md`

### 8. 学习管理容易把路线、任务、断点和归档混在一起

典型表现：

- 长期能力地图、当前任务池、会话恢复入口和历史归档容易互相写重复内容。
- 后续维护时要坚持：Roadmap 管能力，Backlog 管任务，Start Here 管当前恢复，Journal 管长期画像和索引，sessions 管单次归档。

主要索引：

1. `AGENTS.md`
2. `LEARNING_ROADMAP.md`
3. `LEARNING_BACKLOG.md`
4. `START_HERE.md`

---

## 已沉淀主题索引

### 网络请求链路

1. `fundamentals/network/http-tcp-request-flow.md`
2. `interview/computer-fundamentals-questions.md`
3. `mistakes/network/request-flow.md`

### 学习计划和文档口径

1. `AGENTS.md`
2. `LEARNING_ROADMAP.md`
3. `LEARNING_BACKLOG.md`
4. `START_HERE.md`

### MySQL 事务

1. `backend/mysql/transaction.md`
2. `interview/mysql-questions.md`
3. `mistakes/database/transaction.md`

### MySQL 锁、批处理和索引访问路径

1. `backend/mysql/lock-and-batch-processing.md`
2. `backend/mysql/sql-performance-analysis.md`
3. `interview/mysql-questions.md`
4. `sessions/2026-06-01-mysql-lock-index-batch-processing.md`
5. `sessions/2026-06-02-mysql-index-explain-lock-path.md`

### 动态规划入门

1. `fundamentals/algorithm/dp-basic.md`
2. `mistakes/algorithm/dp.md`
3. `sessions/2026-06-03-dp-basic.md`
4. `sessions/2026-06-04-dp-knapsack.md`
5. `sessions/2026-06-05-dp-lcs-edit-distance.md`
6. `sessions/2026-06-09-dp-space-optimization-and-review.md`

### RAG 与 AI 应用面试

1. `interview/rag-project-story.md`
2. `interview/ai-application-questions.md`
3. `sessions/2026-06-10-llm-application-interview-preparation.md`
4. `sessions/2026-06-11-llm-application-interview-review.md`
5. `interview/real-records/2026-06-10-llm-application-engineer.md`
6. `sessions/2026-06-15-rag-engineering-governance.md`
7. `interview/real-records/2026-06-30-ai-agent-rag-backend.md`
8. `sessions/2026-06-30-ai-agent-rag-backend-interview.md`
9. `sessions/2026-07-05-langchain-langgraph-agent-runtime.md`
10. `sessions/2026-07-05-langgraph-runtime-demo.md`
11. `labs/langgraph-runtime-demo/README.md`
12. `sessions/2026-07-06-create-agent-stategraph-boundary.md`
13. `sessions/2026-07-07-langchain-langgraph-learning-summary.md`
14. `sessions/2026-07-07-langchain-langgraph-official-doc-map-gap.md`
15. `interview/mock-records/2026-07-07-huashengtong-ai-application-engineer-prep.md`
16. `sessions/2026-07-07-huashengtong-ai-application-interview-prep.md`
17. `interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`
18. `sessions/2026-07-07-huashengtong-ai-application-interview-review.md`
19. `mistakes/interview/rag-rerank-algorithm-depth.md`
20. `interview/mock-records/2026-07-13-kingdee-ai-application-senior-engineer-prep.md`
21. `sessions/2026-07-13-kingdee-ai-application-interview-prep.md`
22. `interview/real-records/2026-07-13-kingdee-ai-application-senior-engineer.md`

### Java 线程池与后台任务

1. `backend/java/thread-pool.md`
2. `interview/java-concurrency-questions.md`
3. `mistakes/concurrency/thread-pool.md`
4. `sessions/2026-06-12-thread-pool-task-execution.md`
5. `sessions/2026-06-14-thread-pool-lifecycle-monitoring.md`

### Spring IOC、Bean 与事务代理

1. `backend/spring/ioc-bean-and-transaction-proxy.md`
2. `interview/mock-records/2026-07-21-pingan-java-backend-prep.md`
3. `projects/settlement-system/transaction-flow-and-reconciliation.md`

### Java Map 与并发容器

1. `backend/java/map-and-concurrent-hash-map.md`
2. `interview/mock-records/2026-07-21-pingan-java-backend-prep.md`

### 结算系统项目深挖与 Java 求职表达

1. `projects/settlement-system/transaction-flow-and-reconciliation.md`
2. `projects/settlement-system/settlement-document-stamping.md`
3. `sessions/2026-07-24-java-ai-resume-and-project-evidence.md`
4. `sessions/2026-07-21-java-resume-project-evidence-and-pingan-breakpoint.md`
5. `sessions/2026-07-21-pingan-java-interview-prep-closeout.md`
6. `interview/mock-records/2026-07-21-pingan-java-backend-prep.md`
7. `backend/spring/ioc-bean-and-transaction-proxy.md`
8. `backend/java/map-and-concurrent-hash-map.md`
9. `backend/mysql/sql-performance-analysis.md`
10. `resume/java-backend-resume.md`
11. `resume/ai-application-resume.md`

### Redis / 分布式锁

1. `backend/redis/distributed-lock.md`
2. `interview/redis-questions.md`
3. `mistakes/distributed/redis-lock.md`
4. `sessions/2026-06-16-redis-distributed-lock.md`
5. `interview/real-records/2026-06-30-ai-agent-rag-backend.md`
6. `sessions/2026-06-30-ai-agent-rag-backend-interview.md`

---

## 历史会话索引

1. `sessions/2026-05-28-http-tcp-request-flow.md`
2. `sessions/2026-05-29-learning-plan-and-doc-consolidation.md`
3. `sessions/2026-05-29-mysql-transaction-first-pass.md`
4. `sessions/2026-06-01-mysql-lock-index-batch-processing.md`
5. `sessions/2026-06-02-mysql-index-explain-lock-path.md`
6. `sessions/2026-06-03-dp-basic.md`
7. `sessions/2026-06-04-dp-knapsack.md`
8. `sessions/2026-06-05-dp-lcs-edit-distance.md`
9. `sessions/2026-06-09-dp-space-optimization-and-review.md`
10. `sessions/2026-06-10-llm-application-interview-preparation.md`
11. `sessions/2026-06-11-llm-application-interview-review.md`
12. `sessions/2026-06-12-thread-pool-task-execution.md`
13. `sessions/2026-06-14-thread-pool-lifecycle-monitoring.md`
14. `sessions/2026-06-15-rag-engineering-governance.md`
15. `sessions/2026-06-16-redis-distributed-lock.md`
16. `sessions/2026-06-30-ai-agent-rag-backend-interview.md`
17. `sessions/2026-07-05-langchain-langgraph-agent-runtime.md`
18. `sessions/2026-07-05-langgraph-runtime-demo.md`
19. `sessions/2026-07-06-create-agent-stategraph-boundary.md`
20. `sessions/2026-07-07-langchain-langgraph-learning-summary.md`
21. `sessions/2026-07-07-langchain-langgraph-official-doc-map-gap.md`
22. `sessions/2026-07-07-huashengtong-ai-application-interview-prep.md`
23. `sessions/2026-07-07-huashengtong-ai-application-interview-review.md`
24. `sessions/2026-07-13-kingdee-ai-application-interview-prep.md`
25. `sessions/2026-07-21-java-resume-project-evidence-and-pingan-breakpoint.md`
26. `sessions/2026-07-21-pingan-java-interview-prep-closeout.md`
27. `sessions/2026-07-24-java-ai-resume-and-project-evidence.md`
