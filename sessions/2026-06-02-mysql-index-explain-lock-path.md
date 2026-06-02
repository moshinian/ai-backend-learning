# 2026-06-02 MySQL 索引、Explain 与锁访问路径

## 本次学习主题

本次从 `START_HERE.md` 的断点继续，学习 MySQL 索引基础，并进一步连接到慢 SQL、`EXPLAIN` 和批处理当前读锁范围。

主线：

1. B+ 树为什么适合数据库索引
2. 聚簇索引、二级索引、回表、覆盖索引
3. 联合索引、最左前缀、排序与 `limit`
4. 常见索引失效与慢 SQL 判断
5. `EXPLAIN` 中 `type`、`key`、`rows`、`Extra` 的第一轮识别
6. 索引访问路径如何影响 `for update` / `update` 的锁范围
7. 批处理任务抢占、`process_token`、ERP 外部调用不确定状态

---

## 已形成的关键理解

### 1. 索引的本质

索引不是简单等于“让查询变快”，而是数据库为了减少扫描范围、快速定位数据、降低排序和锁冲突成本而维护的有序数据结构。

对批处理 SQL：

```sql
select id
from settlement_task
where shard_no = ?
  and status = 'INIT'
order by created_at, id
limit 100;
```

理想访问路径是先定位到 `shard_no + status` 的连续小区间，再按 `created_at, id` 顺序扫描，拿够 100 条就停止。

推荐索引：

```sql
(shard_no, status, created_at, id)
```

---

### 2. B+ 树为什么适合数据库

数据库索引的核心瓶颈通常不是 CPU 比较，而是磁盘 IO 和页访问。

B+ 树适合数据库的原因：

1. 非叶子节点主要存 key 和指针，一个页能放很多 key，分叉高。
2. 树高低，定位到叶子节点需要的随机 IO 少。
3. 叶子节点有序并通过链表连接，适合范围扫描。
4. 能支持 `order by + limit` 这种有序扫描和提前停止。

面试表达：

> B+ 树适合数据库，不是因为算法复杂度看起来最漂亮，而是因为它贴合磁盘页和 Buffer Pool 的 IO 模型。它分叉高、树高低，可以减少随机 IO；叶子节点有序连接，适合范围扫描和排序。

---

### 3. 聚簇索引、二级索引、回表、覆盖索引

InnoDB 主键索引是聚簇索引，叶子节点存整行数据。

二级索引叶子节点存：

```text
二级索引列 + 主键值
```

通过二级索引找到主键后，再回到主键索引取完整行，这叫回表。

覆盖索引不是新的索引类型，而是查询需要的字段都在二级索引里，不需要回表。

例子：

```sql
idx_status_created_id(status, created_at, id)
```

```sql
select id, status, created_at
from settlement_task
where status = 'INIT'
order by created_at, id
limit 100;
```

这类查询可能走覆盖索引，不需要回表。

---

### 4. 联合索引和最左前缀

联合索引：

```sql
(shard_no, status, created_at, id)
```

整体有序规则是：

```text
先按 shard_no 排
shard_no 相同，再按 status 排
status 相同，再按 created_at 排
created_at 相同，再按 id 排
```

因此：

```sql
where status = 'INIT'
order by created_at, id
limit 100;
```

不能很好利用该索引排序，因为缺少最左列 `shard_no`，`status=INIT` 的数据分散在多个 `shard_no` 区间。

```sql
where shard_no = 3
order by created_at, id
limit 100;
```

也不能很好利用该索引排序，因为中间的 `status` 没有被等值固定，`created_at, id` 只能在每个 status 内部有序，跨 status 不保证全局有序。

核心规则：

> 联合索引用于排序时，前面的列要么已经通过等值条件固定住，要么就会打断后续排序字段的全局有序性。

---

### 5. 索引失效与慢 SQL 排查

索引失效不是说索引完全不能用，而是 SQL 不能充分利用索引的有序结构来减少扫描范围、避免排序或减少回表。

常见原因：

1. 联合索引不符合最左前缀
2. 对索引列做函数计算
3. 隐式类型转换
4. 前置模糊匹配 `like '%abc'`
5. 范围条件后面的列难以继续形成精准连续范围或全局排序
6. `or` 两边索引条件不完整

慢 SQL 排查重点看 `EXPLAIN`：

| 字段 | 关注点 |
|---|---|
| `type` | 是否退化为 `ALL`，是否扫描范围过大 |
| `key` | 是否命中预期索引 |
| `rows` | 优化器估算扫描行数，不是返回行数 |
| `Extra` | 是否有 `Using filesort`、`Using temporary`、`Using index` |

注意：

1. `Using filesort` 表示额外排序，不一定真的写磁盘文件。
2. `Using index` 表示覆盖索引。
3. `rows` 是估算扫描行数，不是最终返回行数。

---

### 6. 函数和隐式类型转换

有索引：

```sql
idx_created(created_at)
```

不推荐：

```sql
where date(created_at) = '2026-06-02'
```

因为普通索引维护的是 `created_at` 原始值顺序，不维护 `date(created_at)` 的函数结果顺序。

推荐：

```sql
where created_at >= '2026-06-02 00:00:00'
  and created_at <  '2026-06-03 00:00:00'
```

隐式类型转换例子：

```sql
phone varchar(20)
```

不推荐：

```sql
where phone = 13800138000
```

推荐：

```sql
where phone = '13800138000'
```

因为 MySQL 可能把字符串列转换成数字再比较，相当于对索引列做函数处理，导致普通字符串索引难以高效定位。

---

### 7. 索引访问路径影响锁范围

关键理解：

> InnoDB 的锁不是直接加在 `where` 条件上，而是沿实际访问到的索引路径加锁。

同一条 SQL：

```sql
select id
from settlement_task
where shard_no = 3
  and status = 'INIT'
order by created_at, id
limit 100
for update;
```

方案 A：

```sql
(shard_no, status, created_at, id)
```

方案 B：

```sql
(status, created_at, id)
```

方案 B 的问题：

1. 只能先进入 `status=INIT` 的大区间。
2. 索引里没有 `shard_no`，需要扫描后回表过滤。
3. 为了找到 100 条 `shard_no=3`，可能访问很多其他 shard 的 INIT 任务。
4. 当前读会沿实际访问路径加锁，可能锁住其他 shard 的记录或相关间隙。
5. 多个 worker 本来按 shard 并行，却可能在同一个 `status=INIT` 大区间里互相阻塞。

方案 A 更好，因为它先把扫描和锁影响收敛到当前 worker 负责的分片和状态小区间。

---

### 8. 条件 update 抢占任务

相比先：

```sql
select ... for update
```

再逐条更新，批处理抢占任务更推荐直接用带状态条件的更新：

```sql
update settlement_task
set status = 'PROCESSING',
    process_token = ?
where shard_no = 3
  and status = 'INIT'
order by created_at, id
limit 100;
```

核心优势不是简单“更快”，而是：

> 把筛选候选任务和声明处理权合并成一个原子数据库操作。

抢占后再通过：

```sql
select id
from settlement_task
where process_token = ?;
```

查询本 worker 抢到的任务列表。

---

### 9. process_token 和过期 worker

成功回写不能只写：

```sql
update settlement_task
set status = 'DONE'
where id = ?;
```

应该带上：

```sql
where id = ?
  and process_token = ?
  and status = 'PROCESSING'
```

原因：

1. Worker A 抢到任务后处理很慢。
2. 任务超时后被补偿回收，Worker B 重新抢占。
3. Worker A 后续又完成，如果只按 `id` 回写，会覆盖 Worker B 的处理状态。

`process_token` 是处理权标识，`status='PROCESSING'` 是状态阶段校验。影响行数为 0 时，说明处理权已失效，旧 worker 不能再推进状态。

---

### 10. ERP 外部调用不确定状态

场景：

Worker A 调 ERP 成功，但本地更新 `DONE` 前宕机。本地只看到任务仍是 `PROCESSING`。

这不能简单当失败重试，因为 ERP 可能已经成功。

处理思路：

1. 把它定义为外部调用不确定状态。
2. 本地设计 `erp_push_record` / `external_call_record`，记录幂等业务键、请求内容、payload hash、调用状态、返回结果、重试次数、trace id。
3. 补偿任务发现 `PROCESSING` 超时后，先查本地调用记录。
4. 明确成功：补写本地 `DONE`。
5. 明确失败：进入 `RETRY` 或重新释放。
6. 状态不确定：优先调用 ERP 查询接口确认；没有查询接口时，依赖幂等键谨慎重推。
7. 长期不确定或金额状态不一致，进入对账或人工处理。

面试核心句：

> 本地事务只能保证数据库内状态更新，不能保证 ERP 调用和本地状态原子一致。外部调用不确定状态需要本地调用记录、业务幂等键、查询确认、补偿任务和对账兜底共同处理。

---

## 本次暴露的问题

1. 一开始容易把慢 SQL 原因停留在“没有索引 / 没命中索引”，没有拆成扫描、过滤、排序、回表、锁范围。
2. 对 `date(created_at)` 的理解有偏差，误以为普通时间索引可以直接按日期截断结果命中。
3. 容易把 `IN`、范围条件、非等值条件简单归类为索引失效，需要改成“是否还能形成连续小区间和全局有序扫描”。
4. `EXPLAIN` 字段已能初步识别，但还需要继续练习从执行计划反推访问路径。
5. 对 `select ... for update` 和条件 `update` 的区别，初始只想到性能，没有先抓住处理权原子性。
6. ERP 推送成功但本地未更新时，不能马上复原为 `INIT`，要先确认外部调用状态。

---

## 当前状态判断

| 主题 | 状态 |
|---|---|
| MySQL 索引基础 | REVIEW |
| 联合索引和最左前缀 | REVIEW |
| 索引失效 | REVIEW |
| `EXPLAIN` 慢 SQL 分析 | DOING |
| 索引访问路径和锁范围 | REVIEW |
| 批处理抢占、处理权、补偿恢复 | REVIEW |
| ERP 外部调用不确定状态 | REVIEW |

不能标记为 `DONE`，因为当前仍需要通过模拟追问验证表达稳定性。

---

## 下次学习建议

用户已表示想休息，并希望暂时保留下面这个完整项目故事问题：

> 你们结算系统的批处理任务是如何保证并发安全、幂等和失败恢复的？

下次建议从这个问题开始，把今天内容整合成 2 分钟项目表达，覆盖：

1. 状态机
2. 条件更新抢占
3. `process_token`
4. 租约、心跳、超时回收
5. 成功 / 失败回写的状态条件
6. ERP 幂等业务键
7. 外部调用记录
8. 查询确认和对账兜底

如果用户状态不适合项目表达，也可以改做 10 分钟 `EXPLAIN` 小测，继续巩固慢 SQL 访问路径判断。
