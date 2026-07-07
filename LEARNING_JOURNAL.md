# LEARNING JOURNAL

## 作用

这个文件只负责三类信息：

1. 长期学习画像
2. 长期典型误区模式
3. 已沉淀主题与历史会话索引

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
  - 从“会做业务开发”升级为“能讲清楚机制、能设计系统、能应对后端 / AI Backend 面试”
- 学习偏好：
  - 优先理解本质
  - 优先建立知识结构
  - 优先结合项目和面试表达
  - 不希望直接灌输标准答案

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
2. `interview/mysql-questions.md`
3. `sessions/2026-06-01-mysql-lock-index-batch-processing.md`
4. `sessions/2026-06-02-mysql-index-explain-lock-path.md`

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

### Java 线程池与后台任务

1. `backend/java/thread-pool.md`
2. `interview/java-concurrency-questions.md`
3. `mistakes/concurrency/thread-pool.md`
4. `sessions/2026-06-12-thread-pool-task-execution.md`
5. `sessions/2026-06-14-thread-pool-lifecycle-monitoring.md`

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
