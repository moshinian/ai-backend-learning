# 2026-06-01 MySQL 锁、索引与批处理并发控制

## 1. 本次学习主题

本次围绕 MySQL 当前读、锁机制、批处理任务抢占和索引访问路径展开。

重点不是背锁名，而是理解：

> 数据库如何找到数据，决定了它锁住哪些索引记录；批处理如何抢任务，决定了多节点会不会重复处理。

---

## 2. 已纠正的关键误区

### 2.1 普通快照读不会因为 RR 就加 Next-Key Lock

错误理解：

> RR 下普通快照读会加 Next-Key Lock 来防幻读。

修正：

> RR 下普通 `select` 通常是快照读，主要依赖 MVCC、Read View 和 undo log 读取一致性视图。Next-Key Lock 主要讨论当前读和范围加锁读。

### 2.2 不能把 PROCESSING 恢复设计成停业务维护

错误方向：

> 先禁止其他业务 SQL，再扫描恢复卡住的 PROCESSING 数据。

修正：

> 在线系统应通过租约、心跳、超时回收、重试次数和补偿任务恢复卡住数据，同时用幂等保证重跑安全。

### 2.3 `where id=? and status='PROCESSING'` 不足以防旧 worker 回写

修正：

> 长链路异步处理需要 `process_token`、`attempt_id` 或类似处理权标识。成功、失败、心跳回写都要带 token，防止过期 worker 覆盖新状态。

---

## 3. 核心机制沉淀

### 3.1 快照读和当前读

| 类型 | 典型 SQL | 主要机制 |
|---|---|---|
| 快照读 | 普通 `select` | MVCC、Read View、undo log |
| 当前读 | `select ... for update`、`update`、`delete` | 最新版本读取 + 加锁 |

RR 下防幻读要分两类：

1. 普通快照读：靠 MVCC 的一致性视图。
2. 当前读：靠行锁、间隙锁、Next-Key Lock 控制范围插入。

### 3.2 批处理抢占

不能只：

```sql
select id
from settlement_order
where status = 'INIT'
limit 100;
```

因为查询候选数据和获得处理权不是原子动作。

更稳的模型：

```text
短事务抢占 -> commit -> 事务外处理 -> 短事务回写 SUCCESS / FAILED
```

抢占可以通过：

```sql
update settlement_order
set status = 'PROCESSING',
    worker_id = ?,
    process_token = ?,
    heartbeat_time = now()
where id = ?
  and status = 'INIT';
```

通过影响行数判断是否抢到。

### 3.3 process_token

核心原则：

> 状态只能说明任务处于哪个阶段，token 才能说明当前是谁有资格推进这个阶段。

成功回写：

```sql
update settlement_order
set status = 'SUCCESS'
where id = ?
  and status = 'PROCESSING'
  and process_token = ?;
```

如果旧 worker 的任务已经被补偿回收并由新 worker 重新抢占，旧 token 会失效，回写影响 0 行。

### 3.4 ERP 外部调用不确定状态

场景：

1. ERP 已成功。
2. 本地还没改 `SUCCESS`。
3. 服务宕机。
4. 重试任务再次推送。

设计：

1. ERP 侧支持业务唯一键或 `request_id` 幂等。
2. 本地维护 ERP 推送记录表。
3. 优先按请求号查询 ERP 结果，不能查询时依赖幂等重推。
4. 财务类系统用对账兜底。

---

## 4. 索引与锁范围

核心句：

> InnoDB 的锁不是直接加在 `where` 条件上，而是加在实际访问到的索引记录上。

没有合适索引时，当前读可能扫描大量聚簇索引记录，并对访问路径上的记录加锁。结果不是逻辑上升级成表锁，而是表现上接近大范围阻塞。

示例：

```sql
select id
from settlement_order
where status = 'INIT'
order by id
limit 100
for update;
```

如果没有 `(status, id)`，多 worker 会扫描更多记录，锁竞争更严重。

即使有 `(status, id)`，多个 worker 仍可能从同一 `INIT` 区间开头竞争。索引减少扫描和锁范围，但不会自动分配任务。

---

## 5. 分片批处理联合索引

目标 SQL：

```sql
where shard_no = ?
  and status = 'INIT'
order by created_at, id
limit 100
```

建议索引：

```sql
(shard_no, status, created_at, id)
```

原因：

1. `shard_no` 先限定 worker 分片。
2. `status` 找待处理任务。
3. `created_at, id` 支持稳定排序和 limit。
4. 减少不同 worker 的扫描重叠和锁竞争。

不要只按字段选择性决定顺序。索引顺序还要服务并发模型和访问路径。

---

## 6. 稳定排序

只按：

```sql
order by created_at
limit 100
```

不稳定，因为 `created_at` 不唯一。

更稳：

```sql
order by created_at, id
limit 100
```

如果要续扫，记录：

```text
last_created_at + last_id
```

下一页：

```sql
where shard_no = ?
  and status = 'INIT'
  and (
    created_at > ?
    or (created_at = ? and id > ?)
  )
order by created_at, id
limit 100;
```

---

## 7. 下次学习断点

进入 MySQL 索引基础：

1. B+ 树为什么适合数据库索引
2. 聚簇索引和非聚簇索引
3. 回表
4. 覆盖索引
5. 最左前缀原则
6. 索引失效和慢 SQL 分析
