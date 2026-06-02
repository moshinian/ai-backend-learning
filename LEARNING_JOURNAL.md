# LEARNING JOURNAL

## 作用

这个文件只负责三类信息：

1. 长期学习画像
2. 长期典型误区
3. 已沉淀主题与历史会话索引

它不是当前状态权威文件。

当前恢复学习进度时，只需要优先读取：

1. `START_HERE.md`

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

## 长期典型误区

### 1. 容易把请求链路只理解到框架内部

容易只想到：

- URL 路由
- Controller 分发
- 业务处理
- 响应返回

后续要持续提醒自己补全：

- DNS
- IP / 端口
- TCP
- 容器层
- 内核协议栈

### 2. 容易把三次握手和 TCP 整体机制混淆

要反复区分：

- 三次握手负责建立连接
- TCP 整体机制负责可靠传输、重传、顺序控制等

### 3. 操作系统基础是长期短板

当前尤其要补：

- 进程和线程
- 阻塞 / 非阻塞
- 同步 / 异步
- 线程与 IO 模型

### 4. 面试表达容易“方向对，但精度不够”

后续要持续训练：

- 术语边界
- 机制表达
- 从“我懂”到“我能清楚讲给面试官听”

### 5. 容易把长期路线和短期冲刺混在一起

长期路线图用于建立完整能力地图。

当前 1 个月目标是面试冲刺，应该优先处理高频短板和项目表达，不平均推进所有 Phase。

### 6. MySQL 日志职责边界容易混淆

已暴露的问题：

- 把 undo log 说成负责事务提交后的持久性
- 把 binlog 说成天然保证主从一致
- 把事务表达成保证业务逻辑一定正确

后续复盘时要反复区分：

- undo log：回滚、MVCC 旧版本
- redo log：崩溃恢复、持久性
- binlog：复制、恢复、订阅
- 本地事务：保证数据库内操作边界，不保证跨系统最终一致

### 7. 容易把快照读、当前读和锁机制混在一起

已暴露的问题：

- 误以为 RR 下普通快照读会加 Next-Key Lock
- 容易把“RR 防幻读”统一理解成靠锁解决
- 对普通 `select`、`select ... for update`、`update` 的语义边界一开始不够清晰

后续复盘时要反复区分：

- 普通快照读：主要依赖 MVCC、Read View、undo log
- 当前读：读取最新版本，并通过锁控制并发修改或插入
- 行锁：控制已有索引记录的并发修改
- 间隙锁 / Next-Key Lock：控制范围当前读下的插入幻影行

### 8. 批处理并发控制容易先想到“停业务修复”

已暴露的问题：

- 对 `PROCESSING` 卡住的初始想法是禁止其他业务 SQL 后扫描恢复
- 容易把恢复卡住任务理解成维护动作，而不是在线补偿机制

后续要强化：

- `PROCESSING` 应理解成带租约的处理中状态
- 需要 `worker_id`、心跳时间、重试次数、超时回收
- 补偿任务应在线恢复，不应依赖停业务
- 超时不等于失败，必须配合幂等重试

### 9. 状态条件更新还不够，需要处理权标识

已暴露的问题：

- 初始回答中只想到 `where status='PROCESSING'`
- 对慢 worker、补偿回收、新 worker 重新抢占后的旧 worker 回写风险认识不够

后续要强化：

- 状态只能说明任务阶段，不能说明谁有资格推进状态
- 长链路异步任务需要 `process_token`、`attempt_id`、`batch_id` 或类似 fencing token
- 成功、失败、心跳回写都要带处理权标识
- 防止过期 worker 覆盖新 worker 的状态

### 10. 索引设计不能只看字段选择性

已暴露的问题：

- 设计联合索引时容易先从字段选择性出发
- 对 worker 分片模型、锁范围、扫描路径和排序稳定性的综合考虑还需要继续训练

后续要强化：

- InnoDB 的锁和索引访问路径强相关
- 锁不是直接加在 `where` 条件上，而是加在实际访问到的索引记录上
- 没有合适索引时，当前读可能扫描并锁住大量记录，表现上接近大范围阻塞
- 分片批处理索引应贴合 `shard_no`、`status`、排序字段和 `limit`
- `created_at` 不唯一，批处理排序应考虑 `created_at, id`

### 11. 索引失效不能机械背结论

已暴露的问题：

- 一开始容易把慢 SQL 归结为“没有索引 / 没命中索引”
- 误以为 `date(created_at)` 可以直接命中普通 `created_at` 索引
- 容易把 `IN`、范围条件、非等值条件简单归类为索引失效
- 对 `EXPLAIN` 的理解目前能看字段，但还需要训练从执行计划反推访问路径

后续要强化：

- 索引失效不是索引完全不能用，而是不能充分利用索引有序结构减少扫描、排序和回表
- 普通 B+ 树索引维护的是列原始值，不维护函数计算结果
- 联合索引前导列没有等值固定时，后续排序字段通常不能保证全局有序
- 多状态条件比 `status <> 'DONE'` 语义更明确，但仍可能破坏跨状态全局排序
- 慢 SQL 排查要同时看 `type`、`key`、`rows`、`Extra`、回表和业务访问路径

### 12. 外部调用不确定状态不能简单重试

已暴露的问题：

- 对 ERP 推送成功但本地未更新的场景，初始容易先想到超时后复原为 `INIT`
- 容易把幂等键当成唯一兜底，而不是配合本地调用记录和查询确认

后续要强化：

- 本地事务不能覆盖跨系统一致性，外部调用和本地状态更新之间天然可能出现不确定状态
- `PROCESSING` 超时后不能盲目重推，应先查外部调用记录
- 明确成功则补写本地 `DONE`，明确失败再重试，不确定时优先查询外部系统
- 幂等键和 payload hash 用于重复请求一致性校验
- 对账是最终兜底，不是替代主流程的正常路径

---

## 已沉淀主题索引

### 网络请求链路

1. `fundamentals/network/http-tcp-request-flow.md`
2. `interview/computer-fundamentals-questions.md`
3. `mistakes/network/request-flow.md`

### 学习计划和文档口径

1. `LEARNING_ROADMAP.md`
2. `INTERVIEW_SPRINT_30_DAYS.md`
3. `START_HERE.md`

### MySQL 事务

1. `backend/mysql/transaction.md`
2. `interview/mysql-questions.md`
3. `mistakes/database/transaction.md`

### MySQL 锁、批处理和索引访问路径

1. `backend/mysql/lock-and-batch-processing.md`
2. `interview/mysql-questions.md`
3. `sessions/2026-06-01-mysql-lock-index-batch-processing.md`
4. `sessions/2026-06-02-mysql-index-explain-lock-path.md`

---

## 历史会话索引

1. `sessions/2026-05-28-http-tcp-request-flow.md`
2. `sessions/2026-05-29-learning-plan-and-doc-consolidation.md`
3. `sessions/2026-05-29-mysql-transaction-first-pass.md`
4. `sessions/2026-06-01-mysql-lock-index-batch-processing.md`
5. `sessions/2026-06-02-mysql-index-explain-lock-path.md`
