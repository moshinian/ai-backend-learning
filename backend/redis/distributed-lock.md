# Redis 分布式锁

## 1. 分布式锁解决什么问题

`synchronized` 只能约束同一个 JVM 内竞争同一把 Monitor 的线程。多实例部署时，每个实例都有自己的堆内存和锁对象：

```text
实例 A synchronized 加锁
实例 B / C 不受影响
```

Redis 分布式锁用于在多个服务实例之间建立临时互斥，降低多个 Worker 同时处理同一资源的概率。

但分布式锁不是业务状态事实来源。任务是否已处理、谁有处理权、是否需要补偿，应以数据库状态机、`process_token`、租约和幂等记录为准。

## 2. 获取锁

推荐使用单条原子命令：

```redis
SET lock_key unique_value NX PX 30000
```

含义：

```text
NX：只有 key 不存在时才写入
PX：设置毫秒级过期时间
unique_value：当前持锁者的唯一标识
```

不要拆成：

```redis
SETNX lock_key unique_value
EXPIRE lock_key 30
```

因为：

1. `SETNX` 成功后、`EXPIRE` 前实例宕机，会造成无过期时间的死锁。
2. 如果代码未严格检查 `SETNX` 返回值，可能给别人的锁续期。

## 3. 释放锁

不能直接：

```redis
DEL lock_key
```

因为锁可能已经过期并被其他实例重新获取。旧 Worker 直接删除会误删新 Worker 的锁。

释放锁要用 Lua 原子判断 value 再删除：

```lua
if redis.call("GET", KEYS[1]) == ARGV[1] then
    return redis.call("DEL", KEYS[1])
else
    return 0
end
```

`GET` 和 `DEL` 必须原子执行，否则中间可能发生锁过期和新锁创建。

## 4. 续期和看门狗

任务耗时超过锁租期时，可以使用短租约加定期续期：

```text
锁租期：30 秒
续期间隔：10 秒
```

续期也必须校验 `unique_value`：

```lua
if redis.call("GET", KEYS[1]) == ARGV[1] then
    return redis.call("PEXPIRE", KEYS[1], ARGV[2])
else
    return 0
end
```

如果不校验，旧 Worker 的看门狗可能给新 Worker 的锁续期。

看门狗只是定时续期线程，不能证明业务任务健康。业务线程可能已经：

```text
死循环
卡在外部调用
阻塞在不可中断 IO
```

所以还需要：

1. 外部调用超时
2. 任务最大执行时间
3. 业务心跳
4. 超时回收
5. `process_token`
6. 幂等和补偿

## 5. Redis 锁和数据库 process_token

Redis 锁丢失后，Worker 不应继续产生新的外部副作用。

Worker 可以通过以下方式感知锁丢失：

1. 看门狗续期返回失败
2. 关键步骤前主动校验锁 value
3. 数据库条件更新影响行数为 0

最终数据库回写必须带 `process_token`：

```sql
UPDATE task
SET status = 'DONE'
WHERE id = ?
  AND status = 'PROCESSING'
  AND process_token = ?;
```

`process_token` 解决的是当前 Worker 是否仍有处理权；Redis 锁解决的是临时互斥。二者都不能替代外部系统幂等。

## 6. 外部调用幂等

`process_token` 每次认领都会变化，不能作为 ERP 幂等键。

ERP 调用应使用稳定业务幂等键：

```text
settlement_order_id
posting_request_id
```

如果同一个幂等键对应不同请求内容，例如：

```text
第一次 amount = 100
第二次 amount = 120
```

应拒绝并告警，而不是覆盖或返回第一次成功结果。

服务端应保存：

```text
idempotency_key
request_hash
processing_status
response_result
```

处理逻辑：

```text
key 不存在：创建记录并执行业务
key 已存在且 hash 相同：返回已有状态或结果
key 已存在但 hash 不同：拒绝并告警
```

## 7. 外部调用超时

调用 ERP 超时只代表调用方没有收到结果，不代表 ERP 没执行。

推荐状态流转：

```text
PROCESSING
-> ERP_TIMEOUT_UNKNOWN
-> 查询 ERP 状态
   -> SUCCESS：本地补写 DONE
   -> FAILED：使用原幂等键重试或标记失败
   -> UNKNOWN：进入 RETRY_WAIT / CONFIRMING，稍后查询或对账
```

不能：

1. 直接标记失败
2. 换新幂等键重试
3. 只依赖 Redis 锁判断外部调用结果

## 8. 任务处理权主依据

更推荐：

```sql
UPDATE task
SET status = 'PROCESSING',
    process_token = ?
WHERE id = ?
  AND status = 'INIT';
```

作为任务处理权的主依据，而不是只依赖 Redis 锁。

原因：

1. 任务状态事实在数据库中。
2. 条件更新能把抢占和状态变更原子化。
3. 服务宕机后，数据库仍保留状态、Token、租约、重试次数和错误信息。
4. 最终回写可用 Token 防止旧 Worker 覆盖新 Worker。
5. Redis 锁过期后，锁信息会消失，不能表达业务生命周期。

面试中可以这样表达：

> Redis 分布式锁可以降低多实例同时进入临界区的概率，但不能作为任务处理结果的唯一事实来源。我会把数据库条件更新和状态机作为任务处理权主依据，再用 Redis 锁辅助跨实例互斥。最终还要结合 `process_token`、租约、心跳、外部幂等键和补偿对账，才能覆盖锁过期、实例宕机和外部调用不确定状态。
