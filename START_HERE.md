# START HERE

## 1. 用法

新会话优先读取本文件，用于快速恢复当前学习上下文。

本文件只记录恢复入口，不写长篇知识内容。

---

## 2. 当前候选最高优先级

当前候选任务：

- `BL-024`：和生创新技术全栈工程师面试复盘与最小补强

说明：

- 2026-07-18 已确认将求职和学习主航道从算法倾向的 AI 应用岗位切回 Java 后端。
- 新定位是“Java 后端主线 + AI 应用工程补充”，已有 RAG / Agent 学习继续作为差异化能力，不再作为主要竞争方向无限扩张。
- 2026-07-27 用户决定将平安产险面试复盘封盘，`BL-015` 已完成，不再单独还原相似面试内容。
- `BL-006` 已完成双版本简历基准稿和项目证据整理，但暂缓项目口述与 JD 定制，等临近明确面试时结合具体 JD 统一恢复。
- 2026-07-27 用户补充三个真实面试学习点：万级 QPS、JVM 机制和 Spring Batch，已分别建立 `BL-016`、`BL-017`、`BL-018`。
- 2026-07-27 已将目标技术栈整理为生产后端核心层、微服务治理层和应用交付层；复用已有 MySQL、Redis、MQ、JVM、并发任务，并新增 Linux、Spring Cloud / Nacos / Sentinel、Docker、Kubernetes 任务。
- 2026-07-28 已完成 `BL-016` 第一轮学习，任务保持 `REVIEW`，等待 60 至 90 秒压缩口述。
- 2026-07-28 韶音科技高级 Java 工程师（供应链）面试暴露幂等原子性、MySQL 表空间、RAG 质量分层和 Spring Bean 生命周期表达问题，已建立短周期 `BL-023`。
- 2026-07-29 已完成 `BL-023` 的原子性 / 幂等、MySQL 存储边界、RAG 质量分层和 Spring Bean 生命周期最小回答卡。
- 2026-07-29 已完成 RAG 回答质量四层口述，并确认 Rerank 已集成进离职后个人持续建设的知识库主链路，不声称荣耀内部试用或生产上线效果。
- 2026-07-29 已完成 Spring Bean 生命周期连续口述，`BL-023` 达到当前验收标准并标记为 `DONE`。
- 2026-07-29 和生创新技术全栈工程师面试再次暴露项目缩放表达、AOP 压缩回答、事务传播和 Java 版本能力问题，已建立短周期 `BL-024`。
- 2026-08-02 已完成 `BL-024` 的 AOP、事务传播和 Java 8 / 11 / 17 / 21 最小版本卡；结算系统口述和代表难点由用户明确暂时跳过，因此 `BL-024` 保持 `DOING`。
- `BL-005` 的 IOC、Bean 生命周期、AOP 和事务代理已经完成机制学习、口述和追问验证，达到当前验收标准并标记为 `DONE`。
- 当前优先确认是否恢复 `BL-024` 剩余的项目口述；若继续暂缓，则保留断点并回到 `BL-016`，`BL-017` JVM 和 `BL-004` Java 并发锁体系等待后续恢复。

---

## 3. 当前断点

当前断点：

1. `BL-024` 状态为 `DOING`。技术部分已经完成第一轮：能够解释 Advisor / Pointcut / Advice、JDK 动态代理 / CGLIB、代理 Bean 和拦截器链，并能说明事务拦截器与事务管理器的职责。
2. 已能区分 `REQUIRED`、`REQUIRES_NEW`、`NESTED`，以及 `rollback-only`、`UnexpectedRollbackException`、跨 Bean 调用、自调用、异常捕获和默认回滚规则的组合边界。
3. 已闭卷说出 Java 8 的 Lambda / Stream、Java 11 的 String API / HttpClient、Java 17 的密封类型 / JDK 内部强封装、Java 21 的虚拟线程 / `switch` 模式匹配，并能说明主要作用和边界。
4. `BL-024` 尚未完成的只有结算系统 90 秒口述和代表难点 60 秒口述；这是用户明确暂时跳过的内容，不重复学习已经通过的技术部分。
5. 项目表达恢复时仍按“系统全貌、核心链路、本人职责、代表难点”逐层缩放；冲销管道只表述为后续场景适配、缺陷修复和长期维护，不改写为完全从零设计。
6. RAG 项目继续保持真实时间线：离职前完成初步搭建但没有用户试用，Rerank 和 Agent 是离职后个人持续实践，不包装为公司生产成果。
7. `BL-005` 和 `BL-023` 已完成；`BL-016` 保持 `REVIEW`，如果继续暂缓项目表达，下一轮从高并发闭卷口述恢复。

---

## 4. 最近学习位置

最近一次归档：

1. `sessions/2026-08-02-aop-transaction-propagation-java-version-cards.md`
2. `interview/real-records/2026-07-29-hesheng-innovation-fullstack-engineer.md`
3. `sessions/2026-07-28-shokz-interview-review.md`

本次 AOP、事务传播和 Java 版本已有沉淀：

1. `backend/spring/ioc-bean-and-transaction-proxy.md`
2. `backend/java/java-version-capability-cards.md`
3. `mistakes/spring/aop-transaction-proxy-boundaries.md`
4. `sessions/2026-08-02-aop-transaction-propagation-java-version-cards.md`

本次和生创新技术面试已有沉淀：

1. `interview/real-records/2026-07-29-hesheng-innovation-fullstack-engineer.md`
2. `mistakes/interview/project-zoom-level-and-listener-alignment.md`

本次韶音面试已有沉淀：

1. `interview/real-records/2026-07-28-shokz-senior-java-supply-chain.md`
2. `mistakes/interview/follow-up-boundaries-and-memory-pressure.md`
3. `interview/rag-project-story.md`
4. `backend/spring/ioc-bean-and-transaction-proxy.md`
5. `projects/settlement-system/transaction-flow-and-reconciliation.md`

高并发主题已有沉淀：

1. `backend/distributed-system/high-qps-capacity-design.md`
2. `mistakes/distributed/high-qps-and-mq-boundaries.md`
3. `sessions/2026-07-28-high-qps-capacity-design.md`

---

## 5. 下一步动作

建议下一步：

1. 先确认是否恢复此前主动暂缓的结算系统项目表达，不重复复习 AOP、事务传播和 Java 版本卡
2. 如果恢复 `BL-024`，不读取项目笔记，用“服务对象、输入、主链路、输出、本人职责”完成 90 秒口述
3. 再选择 N+1 批处理、ERP 凭证 ID 碰撞或可恢复批处理中的一个，用“现象、约束、机制、结果、个人边界”完成 60 秒口述
4. 两段口述通过后将 `BL-024` 标记为 `DONE`
5. 如果继续暂缓项目表达，则保留 `BL-024` 断点并回到 `BL-016`，闭卷完成高并发 60 至 90 秒口述

---

## 6. 优先读取文件

1. `LEARNING_BACKLOG.md`
2. `sessions/2026-08-02-aop-transaction-propagation-java-version-cards.md`
3. `backend/spring/ioc-bean-and-transaction-proxy.md`
4. `backend/java/java-version-capability-cards.md`
5. `mistakes/spring/aop-transaction-proxy-boundaries.md`
6. `interview/real-records/2026-07-29-hesheng-innovation-fullstack-engineer.md`
7. `mistakes/interview/project-zoom-level-and-listener-alignment.md`
8. `projects/settlement-system/transaction-flow-and-reconciliation.md`
9. `backend/distributed-system/high-qps-capacity-design.md`
10. `mistakes/distributed/high-qps-and-mq-boundaries.md`

需要判断长期能力方向时，再读取：

1. `LEARNING_ROADMAP.md`

需要确认文档规则时，再读取：

1. `AGENTS.md`
