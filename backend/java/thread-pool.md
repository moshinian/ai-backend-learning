# Java 线程池与后台任务执行

## 1. 线程池解决什么问题

直接为每个任务创建线程会带来：

1. 线程创建和销毁成本
2. 线程栈等内存开销
3. 线程过多导致调度和上下文切换成本
4. 无法明确限制系统并发能力
5. 容易把压力直接传递给数据库和外部服务

线程池的本质不是让任务无限并行，而是：

> 复用有限线程，并通过线程数、队列和拒绝策略建立容量边界。

## 2. ThreadPoolExecutor 提交顺序

典型参数：

```text
corePoolSize = 4
maximumPoolSize = 8
queueCapacity = 100
```

任务提交顺序：

```text
核心线程
-> 工作队列
-> 非核心线程
-> 拒绝策略
```

瞬间提交 110 个长任务时：

```text
任务 1~4：核心线程执行
任务 5~104：进入队列
任务 105~108：扩容到 8 个线程
任务 109~110：触发拒绝策略
```

队列过大时，`maximumPoolSize` 可能长期不起作用；队列过小时，会更快扩容和拒绝，也会更快把压力传递给下游。

## 3. 队列容量的真实代价

大队列：

1. 扩容慢
2. 任务等待时间长
3. 拒绝较晚
4. 任务对象及其引用大量积压，内存风险高

小队列：

1. 更快扩容
2. 更早暴露过载
3. 队列内存风险较低
4. 更容易拒绝任务
5. 可能增加数据库和模型服务的瞬时压力

## 4. 常见拒绝策略

| 策略 | 行为 | 主要风险 |
|---|---|---|
| `AbortPolicy` | 抛出 `RejectedExecutionException` | 调用方必须显式处理 |
| `CallerRunsPolicy` | 提交任务的线程执行任务 | 破坏线程池隔离，调用线程被阻塞 |
| `DiscardPolicy` | 静默丢弃任务 | 任务可能无感丢失 |
| `DiscardOldestPolicy` | 丢弃队头任务后重试 | 老任务可能被静默丢弃 |

三分钟的文档任务不适合使用 `CallerRunsPolicy`：

```text
Tomcat 请求线程提交失败
-> 请求线程自己解析 PDF、调用 Embedding、向量入库
-> 异步接口退化为同步接口
-> Web 请求线程可能耗尽
```

对于已经持久化的后台任务，更适合：

```text
AbortPolicy 感知拒绝
-> 任务进入 RETRY_WAIT
-> 设置 next_retry_at
-> 稍后重新调度
-> 租约超时作为最终兜底
```

## 5. 为什么不直接使用 Executors 工厂方法

### newFixedThreadPool

特点：

```text
线程数固定
使用近似无界 LinkedBlockingQueue
```

任务提交速度长期大于处理速度时，不会无限创建线程，而是任务持续积压，导致等待时间失控和 OOM 风险。

它可以用于任务总量明确、程序处理完成后退出的场景，但不适合持续接收无上限流量的 Web 服务。

### newCachedThreadPool

特点：

```text
corePoolSize = 0
maximumPoolSize 接近无限
SynchronousQueue 基本不保存任务
```

大量长任务到来时会持续尝试创建线程，可能导致：

1. 原生线程创建失败
2. 线程栈占用大量内存
3. 上下文切换频繁
4. 数据库连接池和模型服务过载

生产系统通常显式创建 `ThreadPoolExecutor`，明确配置：

```text
核心线程数
最大线程数
有界队列
线程工厂
拒绝策略
监控指标
```

## 6. 线程数不能只看 CPU 核数

文档处理链路可能包含：

```text
PDF 解析：CPU 密集
Embedding：网络 IO 和模型服务
向量入库：数据库 IO
```

有效并发受整条调用链中最窄的资源约束：

```text
本机 CPU
数据库连接池
Embedding 服务并发
网络和其他下游容量
```

线程更多不代表吞吐更高。大量线程等待连接、限流许可或网络响应，只会增加内存、等待和超时。

## 7. 是否拆分线程池

当各阶段资源模型和故障边界明显不同时，可以拆分：

```text
PDF 解析池
Embedding 调用池
向量入库池
```

价值：

1. 分别配置并发、队列和拒绝策略
2. 防止 Embedding 变慢拖死解析和入库
3. 根据 CPU、模型服务和数据库容量独立调优

代价：

1. 状态传递和队列管理更复杂
2. 阶段间仍可能积压
3. 需要反压和失败恢复

任务量较小时不必机械拆池。

## 8. 持久化任务认领

推荐流程：

```text
先取得本机执行许可
-> 短事务认领数据库任务
-> 写入 PROCESSING、process_token、worker_id、lease_expire_at
-> 提交事务
-> 立即提交线程池并执行
-> 带 token 回写结果
```

多实例认领可以使用：

```sql
SELECT id
FROM task
WHERE status = 'PENDING'
ORDER BY id
LIMIT 100
FOR UPDATE SKIP LOCKED;
```

`SKIP LOCKED` 会跳过其他事务已经锁定的行，避免 Worker 之间等待。

耗时任务不能放在认领事务中，否则会长期持有数据库连接和锁。

## 9. process_token、租约和心跳

`process_token` 用于证明当前 Worker 仍然拥有本轮处理权：

```sql
UPDATE task
SET status = 'SUCCESS'
WHERE id = ?
  AND status = 'PROCESSING'
  AND process_token = ?;
```

租约不是预计总耗时，而是 Worker 失联后系统等待多久可以回收任务。

```text
租约长度：5 分钟
心跳间隔：1 分钟
任务耗时：可以超过 20 分钟
```

续租：

```sql
UPDATE task
SET heartbeat_at = NOW(),
    lease_expire_at = NOW() + INTERVAL 5 MINUTE
WHERE id = ?
  AND status = 'PROCESSING'
  AND process_token = ?;
```

影响行数为 0，说明 Worker 已失去处理权，应停止产生新的副作用。

独立心跳线程应在任务开始时注册，在 `finally` 中取消。还必须设置任务最大执行时间和外部调用超时，避免任务线程卡死但心跳无限续租。

## 10. 阶段反压

状态表和 `LIMIT` 只能实现持久化缓冲与分批消费，不能阻止积压：

```text
解析每分钟产生 1000 个 Chunk
Embedding 每分钟处理 300 个
每分钟仍新增 700 个 PENDING
```

可以使用高低水位：

```text
PENDING < 2000：正常解析
2000~5000：降低解析并发
PENDING >= 5000：暂停领取新的 PDF
下降到 2000：恢复解析
```

高低两个阈值用于避免在临界值附近频繁暂停和恢复。

限流不等于把任务标记为失败：

```text
没有执行许可
-> 暂不认领
-> 保持 PENDING
-> 有许可后再处理
```

## 11. 任务监控

不能只看 `PENDING` 数量，还应监控：

```text
最老任务等待时间
每分钟新增量和完成量
失败与重试次数
任务排队时间 P95/P99
任务完成时间 P95/P99
线程池 activeCount、queueSize、rejectCount
```

`P95` 表示 95% 的样本不超过该值，`P99` 表示 99% 的样本不超过该值，用于观察少数慢任务和尾部风险。

## 12. 毒任务和重试

任务失败后不能立即无限重试：

```text
失败
-> retry_count + 1
-> 写入 last_error
-> 设置 next_retry_at
-> 状态改为 RETRY_WAIT
```

调度条件：

```sql
WHERE status IN ('PENDING', 'RETRY_WAIT')
  AND retry_count < ?
  AND next_retry_at <= NOW()
ORDER BY next_retry_at, created_at
LIMIT 100
FOR UPDATE SKIP LOCKED;
```

可恢复错误使用指数退避和随机抖动，永久错误快速进入 `DEAD`。超过最大重试次数后告警并人工处理，不能静默丢弃。

随机抖动用于避免大量失败任务同时恢复，形成惊群效应。

## 13. 当前未完成

下一步继续学习：

1. `keepAliveTime` 如何回收非核心线程
2. `allowCoreThreadTimeOut`
3. 线程工厂和异常处理
4. 线程池监控与优雅关闭
5. CPU 密集与 IO 密集任务的参数估算和压测修正
