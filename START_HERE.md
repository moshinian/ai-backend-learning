# START HERE

## 1. 用法

新会话优先读取本文件，用于快速恢复当前学习上下文。

本文件只记录恢复入口，不写长篇知识内容。

---

## 2. 当前候选最高优先级

当前候选任务：

- `BL-015`：平安系 Java 后端面试准备

说明：

- 2026-07-18 已确认将求职和学习主航道从算法倾向的 AI 应用岗位切回 Java 后端。
- 新定位是“Java 后端主线 + AI 应用工程补充”，已有 RAG / Agent 学习继续作为差异化能力，不再作为主要竞争方向无限扩张。
- 2026-07-21 已完成平安产险后端开发面试前准备收口；当前尚未归档真实面试结果。
- `BL-006`、`BL-004`、`BL-005` 已提升为 Java 主线 P0；本次先由 `BL-015` 统一组织面试前准备。

---

## 3. 当前断点

当前断点：

1. `BL-015` 已进入 REVIEW：HR 三组问题完成第一轮覆盖，自我介绍完成一次口述并获得 8/10 评价；当前尚未确认平安产险面试是否已经结束。
2. 结算系统职责已统一为“交易流水处理与核销业务域”，完整事实归档在 `projects/settlement-system/transaction-flow-and-reconciliation.md`。
3. 已确认三个高价值案例：三年不少于 50 次上游流水纠错的冲销补偿管道；将逐笔查询改为 1000 笔批量查询和 Map 匹配、达到 100 万笔 8 分钟以内；对账辅账重复 / 漏生成事务事故及独立 Service 事务边界修复。
4. `Could not roll back JDBC transaction` 只能说明 Spring 调用 JDBC 回滚时发生异常，不能直接证明数据库部分提交；面试中要区分触发条件、事务边界根因和连接层异常证据。
5. 规则系统已确认使用配置驱动的策略模式：不同规则类实现统一接口，由配置表 `match` 选出规则 ID，再从 Spring Bean `Map` 注册表取得实现并调用；Map 构建和配置缓存方式仍待确认。
6. Java 和 AI 两份平行简历已经归档；已确认案例暂未仓促写回 Java 简历，面试后再统一更新。
7. 已完成机制梳理的范围包括：策略模式、Nebula 与 MySQL、Spring DI 与 Bean、事务代理、Java Map 与 ConcurrentHashMap、生产排障、SQL 优化、RAG 文件切分和 AI Coding；JVM、RocketMQ、缓存和通用 SQL 题只完成快速覆盖。
8. 两个项目的正式 2 分钟口述和完整综合模拟尚未完成；不能把面试前快速覆盖等同于系统掌握。

---

## 4. 最近学习位置

最近一次归档：

1. `sessions/2026-07-21-pingan-java-interview-prep-closeout.md`
2. `sessions/2026-07-21-java-resume-project-evidence-and-pingan-breakpoint.md`
3. `projects/settlement-system/transaction-flow-and-reconciliation.md`
4. `interview/mock-records/2026-07-21-pingan-java-backend-prep.md`
5. `resume/java-backend-resume.md`
6. `resume/ai-application-resume.md`

相关主题已有沉淀：

1. `backend/spring/ioc-bean-and-transaction-proxy.md`
2. `backend/java/map-and-concurrent-hash-map.md`
3. `backend/java/thread-pool.md`
4. `backend/mysql/sql-performance-analysis.md`
5. `backend/mysql/transaction.md`
6. `backend/mysql/lock-and-batch-processing.md`
7. `interview/java-concurrency-questions.md`
8. `interview/mysql-questions.md`
9. `backend/redis/distributed-lock.md`
10. `interview/redis-questions.md`
11. `interview/rag-project-story.md`
12. `interview/ai-application-questions.md`

---

## 5. 下一步动作

建议下一步：

1. 读取 `LEARNING_BACKLOG.md` 中的 `BL-015`
2. 读取 `interview/mock-records/2026-07-21-pingan-java-backend-prep.md`
3. 先确认平安产险面试是否已经完成；如果完成，新增独立真实面试记录，先还原真实问题和现场回答，不与其他公司记录合并
4. 如果面试尚未进行，从“介绍最熟悉的 Java 项目、具体职责和挑战”恢复模拟
5. 面试事件收口后，恢复 `BL-006` 两个项目的 2 分钟版本和 Java 简历证据更新
6. 随后用 3 至 5 个追问复核 `BL-005` Spring 机制，再推进 `BL-004` Java 并发锁体系

---

## 6. 优先读取文件

1. `LEARNING_BACKLOG.md`
2. `interview/mock-records/2026-07-21-pingan-java-backend-prep.md`
3. `sessions/2026-07-21-pingan-java-interview-prep-closeout.md`
4. `projects/settlement-system/transaction-flow-and-reconciliation.md`
5. `backend/spring/ioc-bean-and-transaction-proxy.md`
6. `backend/java/map-and-concurrent-hash-map.md`
7. `backend/mysql/sql-performance-analysis.md`
8. `sessions/2026-07-21-java-resume-project-evidence-and-pingan-breakpoint.md`
9. `backend/java/thread-pool.md`
10. `interview/java-concurrency-questions.md`
11. `backend/mysql/transaction.md`
12. `backend/mysql/lock-and-batch-processing.md`
13. `interview/mysql-questions.md`
14. `backend/redis/distributed-lock.md`
15. `interview/redis-questions.md`
16. `interview/rag-project-story.md`
17. `interview/ai-application-questions.md`
18. `LEARNING_ROADMAP.md`

需要判断长期能力方向时，再读取：

1. `LEARNING_ROADMAP.md`

需要确认文档规则时，再读取：

1. `AGENTS.md`
