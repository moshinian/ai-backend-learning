# START HERE

## 1. 用法

新会话优先读取本文件，用于快速恢复当前学习上下文。

本文件只记录恢复入口，不写长篇知识内容。

---

## 2. 当前候选最高优先级

当前候选任务：

- `BL-006`：结算系统项目表达与双版本简历完善

说明：

- 2026-07-18 已确认将求职和学习主航道从算法倾向的 AI 应用岗位切回 Java 后端。
- 新定位是“Java 后端主线 + AI 应用工程补充”，已有 RAG / Agent 学习继续作为差异化能力，不再作为主要竞争方向无限扩张。
- 2026-07-23 已确认平安产险面试完成且未通过；用户明确暂不复盘该场面试，`BL-015` 保持 REVIEW。
- 当前先推进 `BL-006`；Java 后端和 AI 应用两份可投递基准稿已经完成，下一步是用户通读确认、按具体 JD 定制，并完成项目口述版本。

---

## 3. 当前断点

当前断点：

1. `BL-006` 为当前任务：2026-07-24 已完成 Java 后端和 AI 应用两份可投递基准稿及终稿审校。Java 版从十组结算系统证据中筛选六组最适合简历的生产案例，突出性能、可靠性、OOM 排障、主动防错和独立交付；AI 版突出 RAG 全链路、Java / Python 协作边界和受控 Agent，并用四年 Java 生产经验提供工程可信度。两份简历已移除期望薪资，MCP 明确为协议理解，MQ 只保留实际使用口径；当前基准稿可以用于投递，获得具体 JD 后再进行岗位定制。
2. 结算系统职责已统一为“交易流水处理与核销业务域”，完整事实归档在 `projects/settlement-system/transaction-flow-and-reconciliation.md`。
3. 已确认十个高价值案例：三年不少于 50 次上游流水纠错的冲销补偿管道；将逐笔查询改为 1000 笔批量查询和 Map 匹配、达到 100 万笔 8 分钟以内；对账辅账重复 / 漏生成事务事故及独立 Service 事务边界修复；主动发现 ERP 发票/收据凭证 ID 命名空间碰撞，通过“凭证 ID + 接口名”组合业务键修复并经真实重推场景验证；设计未对账池批量终止 / 恢复能力，每账期约使用 5 次、每次处理几十笔辅账，并提供状态约束与逐笔审计；以动态 MySQL 分区查询范围替代固定月份回溯，将对账池生成任务由接近 40 分钟缩短至约 8 分钟，并规避部分订单命中后漏入池；通过分页数据与总数解耦、延迟回表和联合索引修复，将亿级流水表尾页查询从超过 120 秒降至稳定 3 秒以内；通过抢占式调度、Redis 锁、批次事务和明细级 Checkpoint 实现对账池任务中断续跑，并完成主动中断与生产重启验证；独立设计结算单电子盖章模块，通过持久化请求唯一标识与 `docId` 关联两阶段同步申请和外部异步回调（本端由 Spring Web 接口接收），支持单请求最多 20 笔、有界线程池执行、原子状态抢占、条件回写防止重复或迟到回调覆盖、1 小时超时恢复和原始 / 盖章文件版本切换，上线运行 3 个月未发生生产故障或数据错误；通过 Heap Dump 定位 `ReconcileData` 及关联对象占用或保留内存超过 10GB且被 MyBatis 缓存长期持有，关闭对应查询缓存后经低内存对照测试与生产三个月运行均未再发生 OOM。
4. `Could not roll back JDBC transaction` 只能说明 Spring 调用 JDBC 回滚时发生异常，不能直接证明数据库部分提交；面试中要区分触发条件、事务边界根因和连接层异常证据。
5. 规则系统已确认使用配置驱动的策略模式：不同规则类实现统一接口，由配置表 `match` 选出规则 ID，再从 Spring Bean `Map` 注册表取得实现并调用；Map 构建和配置缓存方式仍待确认。
6. Java 和 AI 两份平行简历均已完成投递基准稿及终稿审校；公司时间、项目时间、规模与量化结果已经校验一致。Java 版不再铺开全部案例，未入选证据继续保留在项目深挖文档；AI 版未把待验证方案或未落地的 Rerank 写成项目成果。
7. 已完成机制梳理的范围包括：策略模式、Nebula 与 MySQL、Spring DI 与 Bean、事务代理、Java Map 与 ConcurrentHashMap、生产排障、SQL 优化、RAG 文件切分和 AI Coding；JVM、RocketMQ、缓存和通用 SQL 题只完成快速覆盖。
8. 两个项目的正式 2 分钟口述和完整综合模拟尚未完成；不能把面试前快速覆盖等同于系统掌握。

---

## 4. 最近学习位置

最近一次归档：

1. `sessions/2026-07-24-java-ai-resume-and-project-evidence.md`
2. `projects/settlement-system/transaction-flow-and-reconciliation.md`
3. `projects/settlement-system/settlement-document-stamping.md`
4. `resume/java-backend-resume.md`
5. `resume/ai-application-resume.md`
6. `sessions/2026-07-21-pingan-java-interview-prep-closeout.md`
7. `sessions/2026-07-21-java-resume-project-evidence-and-pingan-breakpoint.md`
8. `interview/mock-records/2026-07-21-pingan-java-backend-prep.md`

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

1. 读取 `LEARNING_BACKLOG.md` 中的 `BL-006`
2. 读取 `resume/java-backend-resume.md` 和 `resume/ai-application-resume.md`
3. 由用户通读确认专业技能中的 Java、MQ、MCP、LangGraph 等关键词均能接受现场追问，继续纠正任何所有权或事实边界
4. 收到具体 Java 或 AI 应用 JD 后，分别调整求职意向、个人优势、技能关键词和项目证据顺序
5. 在仓库外补充真实联系方式并导出 PDF / Word 投递文件，不将敏感信息写入版本控制
6. 按“系统定位 -> 核心链路 -> 一致性 -> 失败恢复 -> 性能 -> 复盘”完成结算系统 2 分钟和 10 分钟版本
7. 完成 `BL-006` 当前验收后，再决定是否恢复 `BL-015` 面试复盘，或进入 `BL-005` / `BL-004`

---

## 6. 优先读取文件

1. `LEARNING_BACKLOG.md`
2. `resume/java-backend-resume.md`
3. `resume/ai-application-resume.md`
4. `projects/settlement-system/transaction-flow-and-reconciliation.md`
5. `projects/settlement-system/settlement-document-stamping.md`
6. `sessions/2026-07-24-java-ai-resume-and-project-evidence.md`
7. `sessions/2026-07-21-java-resume-project-evidence-and-pingan-breakpoint.md`
8. `backend/spring/ioc-bean-and-transaction-proxy.md`
9. `backend/java/map-and-concurrent-hash-map.md`
10. `backend/mysql/sql-performance-analysis.md`
11. `interview/mock-records/2026-07-21-pingan-java-backend-prep.md`
12. `backend/java/thread-pool.md`
13. `interview/java-concurrency-questions.md`
14. `backend/mysql/transaction.md`
15. `backend/mysql/lock-and-batch-processing.md`
16. `interview/mysql-questions.md`
17. `backend/redis/distributed-lock.md`
18. `interview/redis-questions.md`
19. `interview/rag-project-story.md`
20. `interview/ai-application-questions.md`
21. `LEARNING_ROADMAP.md`

需要判断长期能力方向时，再读取：

1. `LEARNING_ROADMAP.md`

需要确认文档规则时，再读取：

1. `AGENTS.md`
