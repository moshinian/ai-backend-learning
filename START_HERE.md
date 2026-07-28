# START HERE

## 1. 用法

新会话优先读取本文件，用于快速恢复当前学习上下文。

本文件只记录恢复入口，不写长篇知识内容。

---

## 2. 当前候选最高优先级

当前候选任务：

- `BL-023`：韶音面试数据准确性与基础机制复核（已完成逐题还原，等待最小口述和 MySQL 实验）

说明：

- 2026-07-18 已确认将求职和学习主航道从算法倾向的 AI 应用岗位切回 Java 后端。
- 新定位是“Java 后端主线 + AI 应用工程补充”，已有 RAG / Agent 学习继续作为差异化能力，不再作为主要竞争方向无限扩张。
- 2026-07-27 用户决定将平安产险面试复盘封盘，`BL-015` 已完成，不再单独还原相似面试内容。
- `BL-006` 已完成双版本简历基准稿和项目证据整理，但暂缓项目口述与 JD 定制，等临近明确面试时结合具体 JD 统一恢复。
- 2026-07-27 用户补充三个真实面试学习点：万级 QPS、JVM 机制和 Spring Batch，已分别建立 `BL-016`、`BL-017`、`BL-018`。
- 2026-07-27 已将目标技术栈整理为生产后端核心层、微服务治理层和应用交付层；复用已有 MySQL、Redis、MQ、JVM、并发任务，并新增 Linux、Spring Cloud / Nacos / Sentinel、Docker、Kubernetes 任务。
- 2026-07-28 已完成 `BL-016` 第一轮学习，任务保持 `REVIEW`，等待 60 至 90 秒压缩口述。
- 2026-07-28 韶音科技高级 Java 工程师（供应链）面试暴露幂等原子性、MySQL 表空间、RAG 质量分层和 Spring Bean 生命周期表达问题，已建立短周期 `BL-023`。
- 当前先用最小回答卡和一个 MySQL 实验收口 `BL-023`，完成后回到 `BL-016`；`BL-017` JVM 和 `BL-004` Java 并发锁体系保留原断点等待恢复。

---

## 3. 当前断点

当前断点：

1. `BL-023` 状态为 `DOING`，韶音面试四道题已经逐题还原并完成第一轮纠偏，但尚未闭卷口述。
2. 幂等问题已能区分单批次单执行者、数据库原子条件和业务幂等；下一次只用“单执行者、原子条件、业务唯一键、重试”四个词回答。
3. MySQL 问题已确认必须区分页可复用、`.ibd` 文件缩小、操作系统磁盘回收和云平台指标；具体云平台机制未知，本地最小实验尚未执行。
4. RAG 回答已区分追踪、召回、排序、生成和评测；Rerank 的准确边界是独立分支 Demo 已尝试，正式主链路未落地。
5. Spring Bean 现场回答的作用域边界基本正确；尚需用“创建、注入、增强、销毁”完成一次 30 至 60 秒完整口述。
6. 本次学习方法不再追求穷举背诵：面试官追问到未知处不等于整场失败，回答时要区分已确认事实、合理推断和当前未知。
7. `BL-016` 继续保持 `REVIEW`；`BL-023` 完成后回到高并发压缩口述，再进入 `BL-017` JVM。

---

## 4. 最近学习位置

最近一次归档：

1. `sessions/2026-07-28-shokz-interview-review.md`
2. `sessions/2026-07-28-high-qps-capacity-design.md`

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

1. 休息充分后，只复核幂等第一题，不读取完整答案
2. 使用“单执行者、原子条件、业务唯一键、重试”四个词回答 30 至 60 秒
3. 回答稳定后，执行 MySQL `DELETE`、`TRUNCATE`、`OPTIMIZE TABLE` 最小实验
4. 再分别复核 RAG 的“召回、排序、生成、评测”和 Bean 的“创建、注入、增强、销毁”
5. `BL-023` 完成后回到 `BL-016`，闭卷完成高并发 60 至 90 秒口述

---

## 6. 优先读取文件

1. `LEARNING_BACKLOG.md`
2. `interview/real-records/2026-07-28-shokz-senior-java-supply-chain.md`
3. `mistakes/interview/follow-up-boundaries-and-memory-pressure.md`
4. `sessions/2026-07-28-shokz-interview-review.md`
5. `interview/rag-project-story.md`
6. `backend/spring/ioc-bean-and-transaction-proxy.md`
7. `projects/settlement-system/transaction-flow-and-reconciliation.md`
8. `backend/distributed-system/high-qps-capacity-design.md`
9. `mistakes/distributed/high-qps-and-mq-boundaries.md`

需要判断长期能力方向时，再读取：

1. `LEARNING_ROADMAP.md`

需要确认文档规则时，再读取：

1. `AGENTS.md`
