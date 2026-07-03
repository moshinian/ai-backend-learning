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

## 13. 空闲线程回收和预热

默认情况下，`keepAliveTime` 只控制超过 `corePoolSize` 的空闲线程：

```text
poolSize = 16
corePoolSize = 8
空闲时间超过 keepAliveTime
-> 最多回收到 8 个线程
```

开启：

```java
executor.allowCoreThreadTimeOut(true);
```

后，核心线程也允许超时回收。所有任务结束且线程持续空闲时，线程池可以降到 0 个线程。

`keepAliveTime` 计算的是线程等待新任务的空闲时间，不是任务执行时间。一个任务执行 10 分钟，不会因为 `keepAliveTime=60s` 而在第 60 秒被回收。

线程池默认懒创建线程。可以预热：

```java
executor.prestartCoreThread();
executor.prestartAllCoreThreads();
```

如果同时开启核心线程超时，预热线程长期空闲后仍会被回收。

## 14. ThreadFactory、execute 和 submit

职责边界：

```text
Runnable：描述业务任务要做什么
Thread：执行任务的载体
ThreadFactory：规定工作线程如何创建
Executor：接收任务并调度
```

`ThreadFactory` 创建的是线程池内部复用的工作线程，不是为每个业务任务创建一个线程。

异常边界：

```text
execute：未捕获异常会逃出任务，可能触发 UncaughtExceptionHandler
submit：异常被 FutureTask 捕获并保存在 Future 中
```

提交线程不能通过包围 `execute()` 的 `try-catch` 捕获另一个工作线程稍后抛出的异常。对于持久化后台任务，业务主路径仍应在任务内部捕获异常并更新状态表。线程级 Handler 只是兜底，`Future` 只是单 JVM 内的临时执行凭证。

## 15. Future 的边界

```java
Future<Result> future = executor.submit(task);
Result result = future.get();
```

`submit()` 通常立即返回，真正可能阻塞的是 `future.get()`。如果 RAG 上传接口调用 `get()` 等待数分钟，Tomcat 请求线程仍会被占用。

长任务更适合：

```text
POST 上传文档 -> 持久化任务 -> 返回 taskId
GET 查询任务 -> 返回 PENDING / PROCESSING / SUCCESS / FAILED
```

## 16. 优雅关闭和中断

`shutdown()` 停止接收新任务，继续执行正在运行和队列中的任务。

```java
if (!executor.awaitTermination(30, TimeUnit.SECONDS)) {
    List<Runnable> notStarted = executor.shutdownNow();
}
```

`awaitTermination` 只让调用线程最多等待指定时间。`shutdownNow()` 返回队列中尚未开始的任务，并对正在执行任务的线程调用 `interrupt()`，但不保证任务立即停止。

中断是协作式停止请求。阻塞方法收到中断后可能抛出 `InterruptedException` 并清除中断标志，不能空 `catch`：

```java
try {
    Thread.sleep(10_000);
} catch (InterruptedException e) {
    Thread.currentThread().interrupt();
    return;
}
```

## 17. 参数压测和瓶颈判断

估算公式只能作为初始值：

```text
线程数约等于 CPU 核数 * (1 + 等待时间 / 计算时间)
```

IO 等待期间线程通常不持续占用 CPU，因此 IO 密集任务可以配置超过 CPU 核数的线程；最终并发仍受数据库连接池、外部服务和内存限制。

压测应使用多档线程数，同时观察：

```text
完成吞吐量
新增速率与完成速率
排队耗时 P95/P99
执行耗时 P95/P99
错误率与拒绝数
CPU、队列趋势
数据库连接等待和外部服务限流
```

选择吞吐量开始趋平，而延迟、连接等待或错误率尚未明显恶化的拐点，并保留生产余量。排队耗时下降不一定代表系统变好，任务可能只是转移到工作线程内部等待数据库连接。

数据库连接等待升高时，需要检查连接池指标、SQL 次数和耗时、事务范围、锁等待、数据库 CPU/IO、连接泄漏和 N+1 查询。

N+1 查询是先查询 N 条主记录，再逐条查询关联数据，产生 `1+N` 次 SQL。可先去重关联 ID，再批量查询并在内存中建立映射。

## 18. 表达验证入口

本节保留线程池主题的表达验证方向，不表示当前任务状态。当前任务状态、断点和下一步动作以 `LEARNING_BACKLOG.md` 为准。

1. 线程池核心知识的完整面试复述
2. 与 `synchronized`、`volatile`、CAS、AQS 等并发主线衔接
3. 真实项目中的参数、监控指标和故障数据验证

## 19. 线程池、连接池和事务边界

假设：

```text
线程池 activeCount = 32
数据库连接池 active = 20
数据库连接池 pending = 12
CPU = 35%
```

`pending=12` 表示 12 个工作线程正在等待从连接池取得连接，尚不能直接表述为正在等待数据库 IO。此时数据库链路的实际并发上限是 20，继续增加工作线程通常只会增加连接等待。

不能仅因为 CPU 较低就继续增加线程。瓶颈可能位于：

```text
连接池容量
SQL 执行时间
事务持有连接时间
锁等待
数据库 CPU / IO
外部服务容量
```

扩大连接池前，需要确认数据库仍有处理余量，并验证增加连接后吞吐量是否增长，而不是仅增加锁竞争、连接等待和错误率。

事务中不应包含长时间外部调用：

```text
不推荐：
开启事务并访问数据库
-> 持有连接
-> 等待 Embedding 4 秒
-> 执行 SQL 1 秒
-> 提交

推荐：
事务外调用 Embedding
-> 获得结果
-> 开启短事务
-> 写入数据库
-> 提交
```

本地事务不能回滚已经完成的 Embedding 调用。若数据库写入失败，应优先重试持久化；若进程宕机导致内存结果丢失，则需要重新计算或将中间结果放入可靠存储。

重试任务应记录：

```text
status
retry_count
next_retry_at
last_error
model_version
```

向量写入应使用稳定业务键和唯一约束保证幂等，例如：

```text
knowledge_base_id
+ document_id
+ chunk_index
+ embedding_model_version
```
