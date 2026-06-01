# MySQL 锁与批处理并发控制

## 1. 当前状态

任务状态：REVIEW

本文件沉淀 MySQL 当前读、行锁、间隙锁、Next-Key Lock，以及它们和批处理任务抢占、补偿、幂等设计的关系。

当前已完成第一轮：

1. 区分快照读和当前读
2. 理解普通快照读在 RR 下主要依赖 MVCC，不是依赖 Next-Key Lock
3. 理解当前读、行锁、间隙锁、Next-Key Lock 的作用边界
4. 能把锁机制联系到结算系统的任务抢占、状态流转、补偿恢复和外部 ERP 幂等

下一步继续补：

**索引如何影响锁范围？为什么没有合适索引会导致锁范围扩大？**

---

## 2. 快照读和当前读

快照读解决的问题是：

> 普通查询如何看到一个一致的数据版本，同时尽量减少读写阻塞。

典型 SQL：

```sql
select * from settlement_order where id = 100;
```

在 InnoDB 的 `Repeatable Read` 下，普通 `select` 通常是快照读，主要依赖 MVCC、Read View 和 undo log，不会因为要防幻读就给普通查询加 Next-Key Lock。

当前读解决的问题是：

> 我要基于最新数据做判断或修改，必须控制并发写入和并发插入。

典型 SQL：

```sql
select * from settlement_order where id = 100 for update;
update settlement_order set status = 'PROCESSING' where id = 100;
delete from settlement_order where id = 100;
```

`update`、`delete`、`select ... for update` 都属于当前读语义。它们不能基于历史快照做判断，而要读取最新已提交版本，并根据访问路径加锁。

---

## 3. 行锁、间隙锁、Next-Key Lock

| 锁 | 解决的问题 | 典型场景 |
|---|---|---|
| 记录锁 | 防止多个事务同时修改同一条索引记录 | 按主键更新订单状态 |
| 间隙锁 | 防止其他事务往索引区间插入新记录 | 范围当前读防止插入幻影行 |
| Next-Key Lock | 记录锁 + 间隙锁 | RR 下范围当前读控制幻读 |

容易混淆点：

1. 普通快照读不靠 Next-Key Lock 防幻读，而是靠 MVCC 的一致性视图。
2. 当前读需要读最新数据，范围当前读才可能通过 Next-Key Lock 锁住记录和区间。
3. Next-Key Lock 不是全表禁写，但锁范围越大，并发越差。
4. InnoDB 的锁依赖索引访问路径；没有合适索引时，扫描范围变大，锁住的记录也可能变多。

---

## 4. 为什么先 select 再处理不安全

错误模型：

```sql
select id
from settlement_order
where status = 'INIT'
order by id
limit 1000;
```

然后应用层逐条处理。

问题在于：

> 查询候选数据和声明处理权不是一个原子动作。

多个节点可能同时查到同一批 `INIT` 数据，后续重复处理、重复生成辅账、重复推送 ERP。

分片字段可以减少冲突，例如：

```sql
where status = 'INIT'
  and shard_no = ?
order by id
limit 100
```

但分片只能提高吞吐、降低扫描重叠，不能替代数据库层面的原子抢占。只要存在多节点、补偿、重跑或同分片并发，仍然需要状态条件更新。

---

## 5. 更稳的任务抢占模型

推荐模型：

> 短事务抢占，长任务事务外处理，结果再短事务落库。

单条抢占：

```sql
update settlement_order
set status = 'PROCESSING',
    worker_id = ?,
    process_token = ?,
    process_start_time = now(),
    heartbeat_time = now()
where id = ?
  and status = 'INIT';
```

通过影响行数判断是否抢占成功：

1. 影响 1 行：当前 worker 拿到处理权。
2. 影响 0 行：数据已经被其他 worker 抢走或状态变化。

批量抢占可以先查候选 ID，再用带状态条件的批量更新：

```sql
update settlement_order
set status = 'PROCESSING',
    batch_id = ?,
    worker_id = ?,
    process_token = ?,
    process_start_time = now(),
    heartbeat_time = now()
where id in (...)
  and status = 'INIT';
```

批量场景要注意：

1. select 出来的只是候选集合。
2. 真正抢到哪些数据，以 update 影响行数和后续状态查询为准。
3. 不建议把 `select ... for update` 和长耗时处理放在一个大事务里，否则会长时间占用数据库连接和锁。

---

## 6. PROCESSING 卡住后的恢复

`PROCESSING` 不应该表示永久归属某个 worker，而应该理解成：

> 某个 worker 在一个租约时间窗口内临时持有处理权。

常见字段：

| 字段 | 作用 |
|---|---|
| `status` | INIT / PROCESSING / SUCCESS / FAILED / RETRY |
| `worker_id` | 当前处理者 |
| `process_token` | 本次处理权令牌 |
| `process_start_time` | 开始处理时间 |
| `heartbeat_time` | 最近续约时间 |
| `retry_count` | 重试次数 |
| `next_retry_time` | 下次允许重试时间 |
| `error_msg` | 失败原因 |

补偿任务可以扫描超时未续约的数据：

```sql
select id
from settlement_order
where status = 'PROCESSING'
  and heartbeat_time < now() - interval 10 minute
  and retry_count < 3
limit 100;
```

恢复时必须带状态和时间条件：

```sql
update settlement_order
set status = 'INIT',
    worker_id = null,
    process_token = null,
    retry_count = retry_count + 1,
    next_retry_time = now() + interval 10 minute
where id = ?
  and status = 'PROCESSING'
  and heartbeat_time < now() - interval 10 minute;
```

这类恢复应该在线完成，不应该停业务、禁止其他 SQL 后再人工修复。

---

## 7. 为什么需要 process_token

只加：

```sql
where id = ?
  and status = 'PROCESSING'
```

仍然不够。

因为旧 worker 可能处理很慢，补偿任务把它恢复成 `INIT`，新 worker 又抢占为 `PROCESSING`。此时旧 worker 如果最后执行：

```sql
update settlement_order
set status = 'SUCCESS'
where id = ?
  and status = 'PROCESSING';
```

仍可能把新 worker 的处理状态覆盖。

更稳的写法：

```sql
update settlement_order
set status = 'SUCCESS'
where id = ?
  and status = 'PROCESSING'
  and process_token = ?;
```

核心原则：

> 状态只能说明任务处于哪个阶段，token 才能说明当前是谁有资格推进这个阶段。

token 不一定叫 `process_token`，也可能叫 `attempt_id`、`batch_id`、`lease_version`、`job_instance_id` 或 `request_id`。关键是后续所有异步处理、心跳、成功、失败回写，都必须带上本次处理权标识。

---

## 8. 外部 ERP 推送的不确定状态

场景：

1. 本系统调用 ERP。
2. ERP 实际已经成功入账。
3. 本系统还没来得及把本地状态改为 `SUCCESS`。
4. 服务宕机。
5. 补偿任务重试。

这是本地事务和外部系统调用之间的不确定状态。不能只靠数据库事务解决。

需要三层保障：

| 层次 | 手段 |
|---|---|
| 下游幂等 | ERP 按业务唯一键或 `request_id` 幂等处理 |
| 本地记录 | 维护 ERP 推送记录表，记录请求、状态、重试次数和响应 |
| 查询 / 对账 | 优先按请求号查询 ERP 结果，财务场景做对账兜底 |

ERP 侧更合理的幂等语义：

1. 同一个幂等键，内容一致：返回已成功。
2. 同一个幂等键，内容不一致：拒绝并告警。

本地可以维护：

```text
erp_push_record
```

核心字段：

| 字段 | 作用 |
|---|---|
| `request_id` | ERP 幂等请求号 |
| `biz_no` | 结算单号或辅账业务号 |
| `payload_hash` | 请求内容摘要 |
| `status` | INIT / SENDING / SUCCESS / FAILED / UNKNOWN |
| `retry_count` | 重试次数 |
| `last_error` | 最近错误 |
| `erp_response_no` | ERP 返回流水 |

---

## 9. 项目表达

在云服务结算系统里，批处理状态流转不能只靠普通 `select` 查 `INIT` 数据后处理。普通查询只是拿到候选集合，不代表当前节点已经获得处理权。

更合理的设计是：

1. 用短事务和状态条件更新抢占任务，把 `INIT` 改为 `PROCESSING`。
2. 抢占时写入 `worker_id`、`batch_id`、`process_token`、心跳时间和重试次数。
3. 长耗时结算、文件处理、ERP 推送放在事务外执行，避免长时间持有数据库锁。
4. 成功或失败回写时带上 `status` 和 `process_token`，防止过期 worker 覆盖新状态。
5. 超时任务通过补偿任务在线恢复，不停业务。
6. ERP、MQ、辅账生成等跨系统动作通过业务唯一键、请求流水号、消息 ID 和对账保证幂等。

---

## 10. 面试简洁回答

InnoDB 的普通 `select` 是快照读，RR 下主要依赖 MVCC、Read View 和 undo log 读取一致性视图，一般不加 Next-Key Lock。`select for update`、`update`、`delete` 属于当前读，要读取最新数据并加锁。行锁防止并发修改同一行，间隙锁防止往索引区间插入新记录，Next-Key Lock 是记录锁加间隙锁，常用于 RR 下范围当前读防止幻读。

在批处理项目里，不能只 `select` 一批 `INIT` 数据后直接处理，因为多个节点可能查到同一批数据。更稳的是用 `update ... where status='INIT'` 做原子抢占，通过影响行数确认处理权。长耗时处理放在事务外，成功或失败回写时带上 `status` 和 `process_token`，避免过期 worker 覆盖状态。对于 ERP、MQ 这类外部调用，还要通过请求唯一键、推送记录表、查询或对账保证幂等和最终一致。
