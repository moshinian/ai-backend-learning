# LEARNING ROADMAP

## 1. 定位

`LEARNING_ROADMAP.md` 是长期能力地图 / 学习总纲。

它负责回答：

> 长期来看，需要建设哪些能力？

它不负责：

1. 记录当前任务状态
2. 记录当前断点
3. 决定今天具体学什么
4. 替代 `LEARNING_BACKLOG.md`

新增长期学习方向时，应优先登记到本文件。

具体可执行学习任务应进入 `LEARNING_BACKLOG.md`。

---

## 2. 与 Backlog 的关系

1. Roadmap 记录长期能力模块。
2. Backlog 从 Roadmap 中拆分和认领具体任务。
3. Backlog 任务如果来自 Roadmap，必须填写 `RoadmapRef`。
4. 临时问题如果反复出现，或被确认具有长期能力建设价值，需要先回补 Roadmap，再进入 Backlog。

---

## 3. 能力模块

### RM-01 计算机基础

模块目标：

1. 建立网络、操作系统、数据结构和基础算法的共同语言。
2. 能把底层机制和后端工程问题联系起来。

能力边界：

1. 网络请求链路、TCP / HTTP 基础
2. 进程、线程、IO、上下文切换
3. Linux 进程、线程、内存、磁盘、网络、文件与权限基础，以及常见生产诊断入口
4. 常见数据结构和复杂度分析
5. 基础算法思维和代表题表达

典型沉淀位置：

1. `fundamentals/`
2. `interview/`
3. `mistakes/`

### RM-02 数据库核心能力

模块目标：

1. 理解数据库事务、索引、锁、日志和 SQL 性能分析。
2. 能把数据库机制应用到业务状态流转、幂等和批处理并发控制中。

能力边界：

1. 事务、隔离级别、MVCC
2. undo log、redo log、binlog
3. B+ 树索引、联合索引、回表、覆盖索引
4. 行锁、间隙锁、Next-Key Lock、死锁
5. 慢 SQL 和执行计划分析

典型沉淀位置：

1. `backend/mysql/`
2. `interview/mysql-questions.md`
3. `mistakes/database/`

### RM-03 Java / Spring / 并发能力

模块目标：

1. 建立 Java 后端运行时、线程模型、并发控制和 Spring 框架机制的主线。
2. 能解释 Web 请求如何进入业务代码，以及后台任务如何可靠执行。

能力边界：

1. Spring MVC 请求链路
2. IOC、AOP、Bean 生命周期
3. `@Transactional` 原理和失效场景
4. 线程池、锁、CAS、AQS、`volatile`
5. JVM 类加载、运行时内存、对象分配、GC 和运行时问题定位
6. Spring Batch 的 Job / Step、Chunk、事务、重启、跳过、重试和分片机制

典型沉淀位置：

1. `backend/java/`
2. `backend/spring/`
3. `interview/java-concurrency-questions.md`
4. `mistakes/concurrency/`

### RM-04 Redis / MQ / 分布式能力

模块目标：

1. 理解常见分布式组件解决的问题、机制和边界。
2. 能把缓存、锁、消息、幂等和最终一致性讲到项目场景中。

能力边界：

1. Redis 数据结构、持久化、缓存模式和缓存异常治理
2. Redis / Redisson 分布式锁、租约、续期、锁粒度和释放边界
3. MQ 生产、Broker 持久化、消费确认、重试、死信、重复、顺序和积压
4. 幂等、补偿、重试、状态机
5. 分布式一致性和故障恢复

典型沉淀位置：

1. `backend/redis/`
2. `backend/mq/`
3. `backend/distributed-system/`
4. `mistakes/distributed/`

### RM-05 项目深挖与工程表达

模块目标：

1. 将做过的功能升级为工程能力表达。
2. 能围绕并发控制、数据一致性、失败恢复、可观测性和扩展性进行项目复盘。

能力边界：

1. 系统定位和核心链路
2. 状态机、幂等、补偿、重试
3. 批处理吞吐和分片并行
4. 上下游接口、MQ、外部系统不确定状态
5. 项目面试表达

典型沉淀位置：

1. `projects/`
2. `interview/`
3. `sessions/`

### RM-06 AI Backend / RAG / Agent 能力

模块目标：

1. 建立 RAG、Agent、模型调用和 AI 应用工程化的后端能力。
2. 能理解 LangChain / LangGraph 等主流 AI 应用框架的机制、边界和工程使用方式。
3. 能明确区分已实现能力、设计方案和生产化边界。

能力边界：

1. 文档解析、Chunk、Embedding、向量检索
2. 混合检索、融合、Rerank、Prompt、引用链
3. RAG 评测和线上问题回放
4. Agent 状态、决策、工具执行、观察和人工确认
5. LangChain 的 Core components、模型、消息、工具、Agent Harness、Middleware、Runtime context、结构化输出、检索组件和 Agent frontend 基础
6. LangGraph 的 Graph API、Functional API、State、Node、Edge、Reducer、Command、Checkpoint、Store、Interrupt、Streaming、Subgraph、Time travel、持久执行和 human-in-the-loop
7. LangChain / LangGraph 的生产化边界：应用结构、部署配置、测试、观测、前端控制面和 LangSmith 辅助调试
8. 长任务、异步索引、失败重试、权限和可观测性

典型沉淀位置：

1. `projects/`
2. `interview/ai-application-questions.md`
3. `interview/rag-project-story.md`
4. `mistakes/`

### RM-07 算法与问题求解能力

模块目标：

1. 建立基础算法题的分析框架。
2. 能在面试中讲清状态、选择、边界、复杂度和优化过程。

能力边界：

1. 动态规划
2. 滑动窗口
3. 二分查找
4. 回溯和图论基础
5. Java 实现和口述表达

典型沉淀位置：

1. `fundamentals/algorithm/`
2. `mistakes/algorithm/`
3. `interview/`

### RM-08 面试复盘与查漏补缺

模块目标：

1. 通过真实面试和模拟面试发现表达漏洞。
2. 将暴露问题回流到 Backlog、mistakes 和主题笔记中。

能力边界：

1. 真实面试复盘
2. 模拟面试记录
3. 高频错题和表达问题
4. 追问能力验证
5. 学习路线校准

典型沉淀位置：

1. `interview/real-records/`
2. `interview/mock-records/`
3. `mistakes/`
4. `LEARNING_BACKLOG.md`

### RM-09 系统设计、容量与性能工程

模块目标：

1. 能把目标流量、延迟和可用性要求转换为可验证的系统容量方案。
2. 能沿请求链路识别瓶颈，设计扩容、削峰、隔离、降级和故障恢复策略。

能力边界：

1. QPS、并发数、响应时间、吞吐量和资源利用率之间的关系
2. Web 线程、应用线程池、数据库连接池、缓存、MQ 和下游服务的容量预算
3. 无状态扩容、缓存、批量化、异步化、分库分表和读写路径优化
4. 限流、熔断、降级、隔离、背压和过载保护
5. 阶梯压测、P95 / P99、错误率、队列趋势、容量拐点和安全余量
6. 高可用、故障演练、监控、告警和容量复盘

典型沉淀位置：

1. `backend/distributed-system/`
2. `backend/java/`
3. `projects/`
4. `interview/`
5. `mistakes/`

### RM-10 微服务治理与云原生交付

模块目标：

1. 建立 Java 微服务从服务调用、注册配置、流量治理到容器化交付的完整工程主线。
2. 能以应用开发者视角部署、观察和排查服务，同时明确与平台运维、集群管理职责的边界。

能力边界：

1. 服务拆分、同步调用、网关、注册发现和配置管理的职责边界
2. Spring Cloud、OpenFeign、Gateway 的调用链与失败处理
3. Nacos 注册发现、配置发布和服务不可用时的边界
4. Sentinel 限流、熔断、降级、隔离及其与容量设计的关系
5. Docker 镜像、容器、网络、存储、配置、健康检查、日志和 JVM 容器资源边界
6. Kubernetes 的 Pod、Deployment、Service、ConfigMap、Secret、探针、资源限制、日志和滚动发布
7. 应用可观测性、发布验证、回滚和基础故障定位

典型沉淀位置：

1. `backend/spring/`
2. `backend/distributed-system/`
3. `labs/`
4. `projects/`
5. `interview/`
6. `mistakes/`
