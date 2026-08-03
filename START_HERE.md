# START HERE

## 1. 用法

新会话优先读取本文件，用于快速恢复当前学习上下文。

本文件只记录恢复入口，不写长篇知识内容。

---

## 2. 当前候选最高优先级

当前候选任务：

- `BL-025`：平安产险面试复盘与分布式事务最小补强

说明：

- 2026-07-18 已确认将求职和学习主航道从算法倾向的 AI 应用岗位切回 Java 后端。
- 新定位是“Java 后端主线 + AI 应用工程补充”，已有 RAG / Agent 学习继续作为差异化能力，不再作为主要竞争方向无限扩张。
- 2026-08-03 已完成平安产险面试前的自我介绍、结算系统全貌、分区性能案例和可恢复分片任务口述；`BL-024` 的技术补强和项目表达均达到当前验收标准，已标记为 `DONE`。
- 当天真实面试新增分布式事务知识缺口：面试官提到候选人记忆中的“二级事务、三级事务”，当前只能推断可能指 2PC / 3PC，原词和机制都尚未核对。
- 2026-08-03 重新确认项目实际使用过 Spring Batch。当前能够解释 Chunk、分片、心跳、协作式停止和失败续跑，但具体版本、Job / Step 拓扑和准确停止 API 仍需保持历史记忆边界，`BL-018` 继续为 `TODO`。
- `BL-016` 万级 QPS 仍为 `REVIEW`，尚缺一次独立闭卷口述；不因今天的面试速答提前标记完成。
- 用户今晚停止学习并休息，2026-08-04 还有两场面试。下一会话先按两场面试的 JD 和时间做最小取舍，不扩张完整分布式事务或 Spring Batch 目录。

---

## 3. 当前断点

当前断点：

1. `BL-025` 状态为 `TODO`。只确认面试暴露了分布式事务陌生问题，尚不能把“二级 / 三级事务”直接等同为 2PC / 3PC，更不能把未学习的协议写成已掌握。
2. 下一轮最小学习入口是：本地事务与分布式事务的边界、2PC 流程和阻塞 / 不确定状态、3PC 增加阶段与仍存在的网络分区边界，再比较 TCC、Saga、事务型 Outbox / 本地消息表。
3. 已稳定区分项目可靠性层次：数据库条件更新负责同名定时父任务抢占；Redis 功能级锁负责手工与定时跨入口互斥；Spring Batch 和分片心跳负责执行控制；明细状态、批次事务和幂等负责数据正确与续跑。
4. 已确认 2C 支付订单表以 `business_day` 做日期分区，早期按月、后期按周；单次匹配通常查询一周，改造后 100 万笔从约半小时恢复到约 8 分钟。准确 `RANGE` DDL 和扫描行数变化没有历史证据，不补写。
5. 已确认分片任务使用类似 `p1-T,p2-T,p3-T,p4-T` 的汇总状态；该实现能够收口固定分片，但状态表达和并发更新仍有结构化改进空间。
6. RAG 项目继续保持真实时间线：离职前完成初步搭建但没有用户试用，Rerank 和 Agent 是离职后个人持续实践，不包装为公司生产成果。

---

## 4. 最近学习位置

最近一次归档：

1. `sessions/2026-08-03-pingan-interview-prep-and-project-reliability.md`
2. `interview/real-records/2026-08-03-pingan-property-backend-individual-group.md`
3. `sessions/2026-08-02-aop-transaction-propagation-java-version-cards.md`

本次项目表达与任务可靠性已有沉淀：

1. `projects/settlement-system/transaction-flow-and-reconciliation.md`
2. `backend/redis/distributed-lock.md`
3. `mistakes/distributed/redis-lock.md`
4. `sessions/2026-08-03-pingan-interview-prep-and-project-reliability.md`

本次平安产险真实面试已有沉淀：

1. `interview/real-records/2026-08-03-pingan-property-backend-individual-group.md`
2. `LEARNING_BACKLOG.md` 中的 `BL-025`

高并发主题已有沉淀：

1. `backend/distributed-system/high-qps-capacity-design.md`
2. `mistakes/distributed/high-qps-and-mq-boundaries.md`
3. `sessions/2026-07-28-high-qps-capacity-design.md`

---

## 5. 下一步动作

建议下一步：

1. 今晚停止学习并休息，不再展开新知识。
2. 明天新会话先提供两场面试的 JD、时间和形式，按岗位要求决定是否在面试前投入 `BL-025`。
3. 若有 20 至 30 分钟补强时间，先确认“二级 / 三级事务”是否指 2PC / 3PC，再完成 30 至 60 秒最小回答；只覆盖本质、阶段、失败边界、替代方案和结算项目映射。
4. 面试前不学习 Seata 源码、完整 Spring Batch 目录或分布式事务产品配置。
5. 两场面试结束后，再根据真实暴露点决定继续 `BL-025`，还是回到 `BL-016` 的高并发闭卷验证。

---

## 6. 优先读取文件

1. `LEARNING_BACKLOG.md` 中的 `BL-025`
2. `sessions/2026-08-03-pingan-interview-prep-and-project-reliability.md`
3. `interview/real-records/2026-08-03-pingan-property-backend-individual-group.md`
4. `projects/settlement-system/transaction-flow-and-reconciliation.md`
5. `backend/redis/distributed-lock.md`
6. `mistakes/distributed/redis-lock.md`
7. `LEARNING_BACKLOG.md` 中的 `BL-018`

需要判断长期能力方向时，再读取：

1. `LEARNING_ROADMAP.md`

需要确认文档规则时，再读取：

1. `AGENTS.md`
