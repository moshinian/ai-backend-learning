# 2026-06-12 Java 线程池与后台任务执行

## 1. 本次学习内容

1. Tomcat 请求线程执行长任务的风险
2. `ThreadPoolExecutor` 的核心线程、队列、最大线程和拒绝顺序
3. 大队列与小队列的扩容、等待、内存和拒绝差异
4. `AbortPolicy`、`CallerRunsPolicy`、`DiscardPolicy`、`DiscardOldestPolicy`
5. `newFixedThreadPool` 和 `newCachedThreadPool` 的风险边界
6. 线程池容量与 CPU、数据库连接池、Embedding 服务并发的关系
7. PDF 解析、Embedding、向量入库的线程池隔离
8. 数据库任务认领、`FOR UPDATE SKIP LOCKED`、`process_token`
9. 租约、独立心跳、协作取消和幂等
10. 高低水位、P95/P99、最老任务等待时间
11. 毒任务、指数退避、随机抖动和 `DEAD` 状态

## 2. 已经稳定的部分

1. 能判断长任务不能继续占用 Tomcat 请求线程。
2. 能说明线程池提交顺序是“核心线程 -> 队列 -> 非核心线程 -> 拒绝”。
3. 能区分 `newFixedThreadPool` 的无界队列风险和 `newCachedThreadPool` 的线程膨胀风险。
4. 能说明线程池并发必须考虑下游容量。
5. 能提出 CPU、模型调用和数据库入库拆池的故障隔离价值。
6. 能理解 `SKIP LOCKED`、`process_token`、租约和心跳的处理权语义。
7. 能识别高低水位、毒任务、退避和随机抖动解决的实际问题。

## 3. 本次暴露的问题

1. 初始误以为核心线程满后会先扩容到最大线程数。
2. 初始误判大队列内存风险更小。
3. 初始误以为 `CallerRunsPolicy` 会增加一条线程，并称为两个线程池复用。
4. 初始误以为 `newFixedThreadPool` 会大量创建线程。
5. 一开始把批次 `LIMIT` 当成避免积压的机制。
6. 对 P95/P99、高低水位和限流的认知尚未建立。
7. 租约最初倾向于按总任务耗时乘安全系数，需要继续区分总耗时和失联检测窗口。

## 4. 当前状态

Java 线程池进入 `DOING`。

已经完成线程池容量边界和后台任务可靠执行的第一轮，但核心参数尚未学完，不能进入 `REVIEW`。

## 5. 下次恢复入口

继续回答：

> `corePoolSize=8`、`maximumPoolSize=16`、`queueCapacity=100`。流量回落后，16 个线程中只有 3 个仍在执行，其余线程长期空闲。哪些线程会被回收？由哪个参数控制？

接下来学习：

1. `keepAliveTime`
2. 核心线程和非核心线程的回收
3. `allowCoreThreadTimeOut`
4. 线程工厂、异常处理、监控和优雅关闭
