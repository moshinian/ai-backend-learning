# 2026-07-21 平安产险 Java 后端面试准备收口

## 日期

2026-07-21

## 主题

围绕平安产险 HR 提供的三组建议完成 Java 后端面试前收口，并将项目事实、Spring、并发容器、SQL、生产排障和 AI 补充问题整理为可恢复的学习进度。

## 本次做了什么

1. 将求职表达稳定为“Java 后端主线 + RAG / Agent 工程能力补充”，归档 Java 和 AI 两份平行简历源稿。
2. 还原交易流水处理与核销业务域，确认冲销补偿、N+1 批处理优化、事务事故和配置驱动策略模式四组真实项目证据。
3. 完成 HR 第一组问题：项目介绍、设计模式、Nebula 与 MySQL、Spring 依赖注入、Bean 创建时机和生命周期、singleton / prototype、RAG 文件切分。
4. 完成 HR 第二组问题：HashMap / ConcurrentHashMap / Hashtable、CAS 与桶级同步、`@Transactional` 失效、生产事故排查、SQL 优化和 AI Coding。
5. 快速覆盖第三组问题：JVM 边界、Join / Group By / Distinct / Union、MySQL 锁、缓存与缓存击穿、RocketMQ 消费、定时任务唯一性、SQL 注入、MyBatis 批量查询、异常体系、Oracle 存储过程边界、DeepSeek、大模型与小模型以及 1 万条数据传输接口。
6. 完成一次 60 秒自我介绍口述，评价为 8/10；主要纠偏是明确 Java 主身份、把职责限定为交易流水与核销业务域、减少 AI 技术名词堆叠并强化结尾岗位匹配。

## 关键结论

1. Spring DI 解决对象创建和协作，AOP 代理才是事务、缓存等横切能力生效的入口；同类自调用要沿真实代理调用链分析。
2. `Could not roll back JDBC transaction` 只表示 JDBC 回滚动作异常，不能直接推出事务未开启或数据库一定部分提交。
3. Java 8 以后 ConcurrentHashMap 的高并发来自无锁读、空桶 CAS、桶级同步、协作扩容和分散计数；线程安全容器不保证多步业务逻辑自动原子化。
4. SQL 优化不能只看单条慢 SQL 和索引，还要看调用次数、数据库往返、扫描范围、锁等待和整体数据访问模型。
5. 定时任务唯一性需要区分执行权和业务幂等：Redis 锁只能控制一段时间内的执行权，数据库状态抢占、process token、租约和唯一键承担不同职责。
6. RAG 切分必须区分已落地与优化方向：当前实现是固定窗口 + overlap + 自然边界兜底，结构、语义和父子切分属于扩展方案。
7. AI Coding 是受控工程工具，生成结果必须经过代码审查、编译测试、真实调用和安全检查；敏感生产数据不能直接交给未批准的外部模型。

## 尚未完成

1. 两个代表项目的正式 2 分钟口述尚未完整演练。
2. 综合模拟面试只完成自我介绍一题，未形成完整评分和错题清单。
3. 规则 Bean Map 的构建方式、配置是否缓存、场景 ID 是否实际承担优先级仍待确认。
4. JVM、RocketMQ、Redis 数据结构、Java `synchronized` / `volatile` / AQS 仍只是快速覆盖，不应表述为系统掌握。
5. 当前没有平安产险真实面试问题和现场回答，不能提前建立真实面试记录。

## 下次入口

1. 如果面试已经结束，先按独立公司和场次建立平安产险真实面试记录，区分真实问题、现场回答和事后补充。
2. 如果面试尚未进行，从“介绍最熟悉的 Java 项目、具体职责和挑战”继续模拟。
3. 面试事件收口后，恢复 `BL-006` 项目 2 分钟表达和 `BL-005` Spring 机制口述验证，再推进 `BL-004` Java 并发锁体系。

## 关联文件

1. `LEARNING_BACKLOG.md`
2. `START_HERE.md`
3. `LEARNING_JOURNAL.md`
4. `interview/mock-records/2026-07-21-pingan-java-backend-prep.md`
5. `projects/settlement-system/transaction-flow-and-reconciliation.md`
6. `backend/spring/ioc-bean-and-transaction-proxy.md`
7. `backend/java/map-and-concurrent-hash-map.md`
8. `backend/mysql/sql-performance-analysis.md`
9. `resume/java-backend-resume.md`
10. `resume/ai-application-resume.md`
