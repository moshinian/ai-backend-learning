# LEARNING BACKLOG

## 1. 定位

`LEARNING_BACKLOG.md` 是柔性学习任务池。

它负责回答：

> 现在具体要推进哪些学习任务？

它不负责写长篇知识笔记。正式知识沉淀应写入 `backend/`、`fundamentals/`、`projects/`、`interview/`、`mistakes/` 等对应位置。

---

## 2. 任务来源

Backlog 任务可以来自：

1. `LEARNING_ROADMAP.md`
2. 真实面试暴露
3. 项目表达短板
4. 临时技术问题
5. 个人主动学习
6. 长期基础补课
7. 旧冲刺计划迁移

规则：

1. 来自 Roadmap 的任务必须填写 `RoadmapRef`。
2. 有长期价值但 Roadmap 缺节点时，先补 Roadmap 能力节点，再加入 Backlog。
3. 临时问题可以只进入 Backlog。
4. 临时问题反复出现或被确认有长期能力价值时，需要回补 Roadmap。

---

## 3. 优先级和状态

优先级：

1. P0：当前最想学、最有动力、最应该优先推进的知识
2. P1：面试、项目表达、实际问题暴露出的短板
3. P2：长期重要但不紧急的基础知识

状态：

1. TODO：待学习
2. DOING：正在学习
3. REVIEW：已学完一轮，等待复盘或表达验证
4. DONE：已完成当前验收标准
5. BLOCKED：暂时卡住或等待外部信息

任务暂停时必须更新：

1. 状态
2. 当前断点
3. 下一步动作
4. 关联文件

任务完成时必须更新：

1. 状态
2. 验收结果
3. 关联沉淀文件
4. 是否需要回补 `LEARNING_ROADMAP.md` 或 `mistakes/`

---

## 4. 任务条目格式

每个任务至少包含：

1. ID
2. 优先级
3. 来源
4. RoadmapRef
5. 状态
6. 主题
7. 学习目标
8. 验收标准
9. 当前断点
10. 关联文件
11. 下一步动作

---

## 5. 当前任务池

### BL-024 和生创新技术全栈工程师面试复盘与最小补强

- ID：BL-024
- 优先级：P0
- 来源：真实面试暴露
- RoadmapRef：RM-03 Java / Spring / 并发能力；RM-05 项目深挖与工程表达；RM-08 面试复盘与查漏补缺
- 状态：DOING
- 主题：围绕和生创新技术全栈工程师面试暴露的项目缩放表达、AOP / 事务传播和 Java 版本能力完成最小补强
- 学习目标：面对不熟悉结算领域的面试官，能够按“系统全貌、核心链路、本人职责、代表难点”逐层展开；先回答技术问题本身，再使用一个短案例证明；对不知道的版本和框架事实保持明确边界。
- 验收标准：能用 90 秒讲清结算系统的服务对象、输入、主链路、输出和本人职责；能用 60 秒讲清一个项目难点的现象、约束、机制、结果与个人边界；能用 30 至 60 秒回答 AOP 的用途、代理机制和自调用边界；能区分 `REQUIRED`、`REQUIRES_NEW`、`NESTED` 并说明事务拦截器的执行过程；能说出 Java 8、11、17、21 各一到两个代表能力；能按真实时间线说明 RAG 项目的发起背景、公司阶段、离职节点和离职后开发边界。
- 当前断点：2026-08-02 已完成技术补强第一轮。能够从 Advisor、Pointcut、Advice、代理 Bean、JDK 动态代理 / CGLIB 和拦截器链解释 AOP，能够说明 `TransactionInterceptor` 与 `TransactionManager` 的职责，并通过连续判断区分 `REQUIRED`、`REQUIRES_NEW`、`NESTED`、`rollback-only`、`UnexpectedRollbackException`、自调用和 checked exception 回滚规则；已闭卷说出 Java 8 的 Lambda / Stream、Java 11 的 String API / HttpClient、Java 17 的密封类型 / JDK 内部强封装、Java 21 的虚拟线程 / `switch` 模式匹配。结算系统 90 秒口述和代表难点 60 秒口述由用户明确暂时跳过，因此任务保持 `DOING`，不因技术部分通过而提前标记完成。RAG 时间线和冲销管道个人贡献继续保持既有事实边界。
- 关联文件：`interview/real-records/2026-07-29-hesheng-innovation-fullstack-engineer.md`、`mistakes/interview/project-zoom-level-and-listener-alignment.md`、`projects/settlement-system/transaction-flow-and-reconciliation.md`、`backend/spring/ioc-bean-and-transaction-proxy.md`、`backend/java/java-version-capability-cards.md`、`mistakes/spring/aop-transaction-proxy-boundaries.md`、`sessions/2026-08-02-aop-transaction-propagation-java-version-cards.md`、`resume/java-backend-resume.md`、`resume/ai-application-resume.md`
- 下一步动作：默认恢复时先询问是否继续此前暂缓的项目表达；若恢复，则闭卷完成结算系统 90 秒口述和一个代表难点 60 秒口述，达到后将 `BL-024` 标记为 `DONE`。若仍暂缓，则保留本断点并切回 `BL-016` 的高并发压缩口述，不重复学习已经通过的 AOP、事务传播和 Java 版本卡。

### BL-023 韶音面试数据准确性与基础机制复核

- ID：BL-023
- 优先级：P0
- 来源：真实面试暴露
- RoadmapRef：RM-02 数据库核心能力；RM-03 Java / Spring / 并发能力；RM-04 Redis / MQ / 分布式能力；RM-05 项目深挖与工程表达；RM-06 AI Backend / RAG / Agent 能力；RM-08 面试复盘与查漏补缺
- 状态：DONE
- 主题：围绕韶音科技面试暴露的幂等原子性、MySQL 表空间、RAG 回答质量和 Spring Bean 生命周期，形成少量可检索的回答入口
- 学习目标：不通过穷举背诵补面试细节，而是建立“先识别问题层次，再说明已确认事实、机制边界和当前未知”的稳定回答方式。
- 验收标准：能用 30 至 60 秒分别回答“单执行者为什么不等于原子和幂等”“DELETE 后空间去了哪里”“如何保证 RAG 回答与问题对应”“Spring Bean 生命周期”；能区分 InnoDB 页复用、数据文件、操作系统磁盘和云平台指标，且不为未知平台机制背书；能稳定表述“Rerank 已集成进离职后个人持续建设的 RAG 主链路，不包装为荣耀内部试用或生产上线效果”；遇到未知追问时能区分事实、推断和待验证项。
- 当前断点：2026-07-29 已完成四个验收问题。原子性 / 幂等能够区分 Redis 锁、条件更新、批次事务、业务唯一键和下游幂等；MySQL 回答能够区分页复用、数据文件、操作系统磁盘和云平台指标，并保留具体平台机制未知的边界；RAG 能按召回、排序、生成和评测分层，且已校准 Rerank 主链路事实；Spring Bean 已完成连续口述，能够说明实例化、依赖注入、初始化、`BeanPostProcessor` 代理、方法调用时的 AOP 增强、同类自调用失效以及 prototype 资源所有权。和生创新技术面试进一步暴露的项目表达、AOP 压缩口述和事务传播深度转交 `BL-024` 与 `BL-005`，不延长本任务。
- 关联文件：`interview/real-records/2026-07-28-shokz-senior-java-supply-chain.md`、`sessions/2026-07-28-shokz-interview-review.md`、`mistakes/interview/follow-up-boundaries-and-memory-pressure.md`、`interview/rag-project-story.md`、`mistakes/interview/rag-rerank-algorithm-depth.md`、`backend/spring/ioc-bean-and-transaction-proxy.md`、`projects/settlement-system/transaction-flow-and-reconciliation.md`
- 下一步动作：本任务已完成。后续项目表达、AOP 和事务传播由 `BL-024` 承接；万级 QPS 复盘仍保留在 `BL-016`，待本次真实面试短周期复盘结束后恢复。

### BL-016 万级 QPS 容量设计与高并发治理

- ID：BL-016
- 优先级：P0
- 来源：真实面试暴露 + 个人主动学习
- RoadmapRef：RM-09 系统设计、容量与性能工程
- 状态：REVIEW
- 主题：面对 10000 QPS 目标时，如何完成场景澄清、容量估算、链路拆解、瓶颈治理和压测验证
- 学习目标：建立一套可以迁移到不同业务的高并发系统设计方法，不把“加缓存、加 MQ、加机器”当成脱离业务约束的固定答案。
- 验收标准：能先澄清读写比例、请求耗时、数据大小、峰值持续时间、一致性和 SLA；能解释 QPS、响应时间、并发数与实例容量的关系；能沿网关、Web 线程、业务线程池、缓存、数据库、MQ 和下游服务分配容量预算；能设计限流、削峰、降级、隔离和扩容方案；能说明如何通过阶梯压测、P95 / P99、错误率和资源指标验证 10000 QPS，而不是只给理论架构图。
- 当前断点：2026-07-28 已完成第一轮学习和综合口述。已经能区分“更新成功”与“请求已受理”，使用目标 QPS、响应时间、单实例安全吞吐、数据库 SQL/s 和故障余量估算容量；能够解释热点读缓存、写分片、热点行、MQ 批量聚合、消费幂等、事务型 Outbox、入口限流、有界队列、退避重试、非核心降级和故障压测。综合回答仍需稳定四个边界：分片必须是数据库写容量不足后的条件性方案；队列按最大允许等待时间而不是最低处理时延或 `Xmx` 计算；MQ 只能削峰和支持批量处理，不能减少总工作量或替代同步核心事务；缓存失效与 MQ 消费都要明确一致性和幂等机制。本次最后一段因疲劳按提示原句抄写，用户明确不将其视为独立口述通过证据，因此任务保持 `REVIEW`。
- 关联文件：`backend/distributed-system/high-qps-capacity-design.md`、`mistakes/distributed/high-qps-and-mq-boundaries.md`、`sessions/2026-07-28-high-qps-capacity-design.md`、`backend/java/thread-pool.md`、`interview/java-concurrency-questions.md`、`fundamentals/network/http-tcp-request-flow.md`、`mistakes/concurrency/thread-pool.md`、`projects/settlement-system/transaction-flow-and-reconciliation.md`
- 下一步动作：休息充分后先不读取提示，闭卷回忆“数据库、缓存、分片、MQ”四句话；能够用自己的语言说清条件和边界后，再用 60 至 90 秒完成一次整体口述。通过后标记为 `DONE`，再进入 `BL-017`。

### BL-017 JVM 运行机制与故障诊断

- ID：BL-017
- 优先级：P0
- 来源：真实面试暴露 + Java 后端主线补课
- RoadmapRef：RM-03 Java / Spring / 并发能力
- 状态：TODO
- 主题：类加载、运行时内存、对象分配、垃圾回收和 JVM 故障诊断
- 学习目标：建立从 Java 代码运行到对象分配、回收和故障定位的 JVM 主线，并能把机制与真实 OOM 排查证据连接起来。
- 验收标准：能讲清类加载过程和双亲委派的作用；能区分堆、虚拟机栈、方法区 / 元空间、程序计数器和本地方法栈；能解释对象分配、可达性分析、分代回收和常见 GC 触发；能区分内存泄漏、内存溢出、频繁 Full GC、CPU 高和线程阻塞；能围绕 Heap Dump、线程栈、GC 日志和监控指标给出诊断顺序。
- 当前断点：已有通过 Heap Dump 定位 MyBatis 缓存长期持有大对象并导致 OOM 的真实案例，也完成过 JVM 面试速答，但尚未系统连接类加载、运行时内存、对象生命周期、GC 和诊断工具。Java 内存模型中的可见性、有序性和 happens-before 归 `BL-004`，不在本任务重复展开。
- 关联文件：`projects/settlement-system/transaction-flow-and-reconciliation.md`、`interview/mock-records/2026-07-21-pingan-java-backend-prep.md`、`LEARNING_ROADMAP.md`
- 下一步动作：从“一段 Java 代码从类被加载到对象进入堆，再到对象被回收”建立第一张 JVM 运行主线图。

### BL-018 Spring Batch 批处理框架

- ID：BL-018
- 优先级：P1
- 来源：真实面试暴露
- RoadmapRef：RM-03 Java / Spring / 并发能力；RM-05 项目深挖与工程表达
- 状态：TODO
- 主题：Spring Batch 的作业模型、Chunk 事务、状态持久化、失败重启、跳过重试和并行分片
- 学习目标：理解 Spring Batch 相比自定义定时任务解决了哪些批处理工程问题，并能将其机制与现有百万级流水、Checkpoint 和中断续跑经验进行对照。
- 验收标准：能讲清 Job、JobInstance、JobExecution、Step、StepExecution 和 JobRepository 的关系；能区分 Tasklet 与 Chunk；能解释 ItemReader、ItemProcessor、ItemWriter 和 Chunk 事务边界；能说明 restart、skip、retry、listener、partition 和并行 Step 的作用与风险；能判断什么场景应该使用 Spring Batch，什么场景自定义任务更合适。
- 当前断点：已有自定义批处理、任务分片、批次事务、数据库状态抢占和明细级 Checkpoint 的生产经验，但尚未系统学习或使用 Spring Batch，不能把自研任务机制表述为 Spring Batch 经验。
- 关联文件：`projects/settlement-system/transaction-flow-and-reconciliation.md`、`backend/java/thread-pool.md`、`LEARNING_ROADMAP.md`
- 下一步动作：先比较普通 `@Scheduled` + 自定义任务表与 Spring Batch 的职责边界，再进入 Job / Step / JobRepository。

### BL-019 Linux 生产问题诊断主线

- ID：BL-019
- 优先级：P1
- 来源：目标岗位要求 + Java 后端主线补课
- RoadmapRef：RM-01 计算机基础；RM-03 Java / Spring / 并发能力
- 状态：TODO
- 主题：从服务异常现象出发，定位 Linux 进程、线程、CPU、内存、磁盘、网络和日志问题
- 学习目标：建立“现象 -> 指标 -> 进程 / 线程 -> 资源 -> 应用证据”的生产诊断顺序，不把 Linux 学习退化成命令背诵。
- 验收标准：能针对 CPU 高、内存上涨、磁盘 IO 高、端口不通、连接堆积和日志异常给出排查顺序；能使用并解释 `ps`、`top`、`pidstat`、`vmstat`、`iostat`、`ss`、`lsof` 等常见工具的关键输出；能把 Linux 证据与 JVM 线程栈、Heap Dump、GC 日志和应用监控连接起来。
- 当前断点：日常能使用部分 Linux 命令，也有 JVM OOM 排障经验，但尚未形成跨操作系统资源、JVM 和应用链路的稳定诊断方法。
- 关联文件：`fundamentals/`、`backend/java/thread-pool.md`、`projects/settlement-system/transaction-flow-and-reconciliation.md`、`LEARNING_ROADMAP.md`
- 下一步动作：从“Java 服务响应变慢”开始，按 CPU、内存、磁盘、网络、线程和日志六个方向建立第一张排查路径。

### BL-020 Spring Cloud / Nacos / Sentinel 微服务治理实验

- ID：BL-020
- 优先级：P1
- 来源：目标岗位要求 + 长期 Java 后端能力建设
- RoadmapRef：RM-09 系统设计、容量与性能工程；RM-10 微服务治理与云原生交付
- 状态：TODO
- 主题：使用 Spring Cloud、Nacos 和 Sentinel 验证服务调用、注册配置与流量治理
- 学习目标：理解各组件解决的具体问题、运行链路和失败边界，并形成可运行证据，而不是只记组件名称和注解。
- 验收标准：能讲清 Gateway、OpenFeign、Nacos 注册发现 / 配置管理和 Sentinel 限流 / 熔断 / 降级各自职责；能说明服务实例下线、配置变更、调用超时和流量过载时的行为；能完成一个包含至少两个服务的最小实验，并验证一次注册发现、一次配置变更、一次限流或熔断。
- 当前断点：有 Spring Boot、服务调用和部分微服务概念基础，但尚无覆盖 Nacos 与 Sentinel 运行边界的系统学习和可运行实验；不能将其包装为生产治理经验。
- 关联文件：`backend/spring/`、`backend/distributed-system/`、`labs/`、`LEARNING_ROADMAP.md`
- 下一步动作：先画清客户端、网关、服务提供者、Nacos 和 Sentinel 的职责图，再确定最小实验的服务边界与版本组合。

### BL-021 Docker 化 Java 服务

- ID：BL-021
- 优先级：P1
- 来源：目标岗位要求 + 长期 Java 后端能力建设
- RoadmapRef：RM-10 微服务治理与云原生交付
- 状态：TODO
- 主题：把 Java 服务构建为可配置、可观察、可验证的容器镜像
- 学习目标：掌握 Java 应用从构建产物到容器运行的关键边界，为微服务实验和后续 Kubernetes 学习提供真实交付载体。
- 验收标准：能编写并解释 Java 服务 Dockerfile；能说明镜像层、容器生命周期、端口、网络、环境变量、挂载、健康检查和日志；能设置合理的 JVM 容器内存边界；能使用 Compose 启动服务及其至少一个依赖，并完成健康与日志验证。
- 当前断点：已有容器使用经验，但尚未在本仓库形成面向 Java 服务交付的系统学习任务和可复用实验。
- 关联文件：`labs/`、`backend/distributed-system/`、`LEARNING_ROADMAP.md`
- 下一步动作：选择一个最小 Spring Boot 服务，先明确构建产物、运行参数、外部配置和健康检查，再编写 Dockerfile。

### BL-022 Kubernetes 的 Java 开发者视角

- ID：BL-022
- 优先级：P2
- 来源：目标岗位要求 + 长期 Java 后端能力建设
- RoadmapRef：RM-10 微服务治理与云原生交付
- 状态：TODO
- 主题：Java 服务在 Kubernetes 中的部署、配置、观察和基础故障定位
- 学习目标：达到后端开发者能够部署和排查自己服务的深度，不把集群搭建、网络插件和平台运维作为当前主线。
- 验收标准：能解释 Pod、Deployment、Service、ConfigMap、Secret、readiness / liveness 探针和资源 requests / limits；能完成一次 Java 服务部署、配置注入、日志查看、滚动更新和回滚；能根据 Pod 状态、事件、日志和探针结果定位常见启动或流量接入问题。
- 当前断点：尚未建立 Kubernetes 系统知识和可运行证据，当前只规划开发者侧必需能力。
- 关联文件：`labs/`、`backend/distributed-system/`、`LEARNING_ROADMAP.md`
- 下一步动作：在 `BL-021` 形成稳定容器镜像后，再从 Pod、Deployment 和 Service 三个对象开始最小部署实验。

### BL-015 平安系 Java 后端面试准备

- ID：BL-015
- 优先级：P0
- 来源：真实面试准备 + HR 明确建议 + 求职主线调整
- RoadmapRef：RM-02 数据库核心能力；RM-03 Java / Spring / 并发能力；RM-04 Redis / MQ / 分布式能力；RM-05 项目深挖与工程表达；RM-06 AI Backend / RAG / Agent 能力；RM-08 面试复盘与查漏补缺
- 状态：DONE
- 主题：围绕 2026-07-21 平安系 Java 后端面试，准备项目表达、Java / Spring / MySQL 高频题、生产排障和 AI 工程补充问题
- 学习目标：以 Java 后端为主身份完成本次面试准备；能用真实项目证据回答设计模式、生产问题、SQL 优化、线程与任务可靠性问题，并能以补充能力回答 Nebula、RAG 文件切分和 AI Coding。
- 验收标准：完成 60 秒自我介绍和两个代表项目的 2 分钟版本；每个项目至少准备一个真实难点、一个设计选择、一个故障或风险处理和一个复盘改进；能回答 HashMap / ConcurrentHashMap / Hashtable、依赖注入、Bean 创建时机与作用域、`@Transactional` 失效、SQL 优化和生产事故排查；能诚实说明 Nebula 使用边界；能回答 RAG 文件切分和 AI Coding 的实际使用；完成至少一轮按真实追问方式进行的模拟面试。
- 验收结果：已完成 HR 三组建议的第一轮覆盖、60 秒自我介绍口述纠偏，以及项目证据、Spring、Java Map、ConcurrentHashMap、SQL 优化、RAG 文件切分和 AI Coding 等面试准备。两个项目的正式 2 分钟口述和完整综合模拟没有在本任务内完成，分别由 `BL-006` 和 `BL-010` 承接，不视为本次面试复盘的遗留阻塞。
- 当前断点：2026-07-23 已确认平安产险面试完成且未通过。2026-07-27 用户确认本次面试内容与前几次大体相同，没有新增差异化问题，继续还原完整问答的边际收益较低，因此决定封盘，不再单独复盘，也不再分析未通过原因。
- 关联文件：`interview/mock-records/2026-07-21-pingan-java-backend-prep.md`、`projects/settlement-system/transaction-flow-and-reconciliation.md`、`sessions/2026-07-21-java-resume-project-evidence-and-pingan-breakpoint.md`、`sessions/2026-07-21-pingan-java-interview-prep-closeout.md`、`resume/java-backend-resume.md`、`backend/spring/ioc-bean-and-transaction-proxy.md`、`backend/java/map-and-concurrent-hash-map.md`、`backend/java/thread-pool.md`、`backend/mysql/sql-performance-analysis.md`、`backend/mysql/transaction.md`、`backend/mysql/lock-and-batch-processing.md`、`interview/mysql-questions.md`、`backend/redis/distributed-lock.md`、`interview/redis-questions.md`、`interview/rag-project-story.md`、`interview/ai-application-questions.md`
- 下一步动作：任务已封盘；已有共性短板继续由 `BL-004`、`BL-005`、`BL-006`、`BL-010` 等任务承接，不再为本次平安产险面试新增独立复盘。

### BL-014 金蝶 AI 应用开发高级工程师面试准备

- ID：BL-014
- 优先级：P0
- 来源：真实面试准备 + 目标岗位要求
- RoadmapRef：RM-03 Java / Spring / 并发能力；RM-04 Redis / MQ / 分布式能力；RM-05 项目深挖与工程表达；RM-06 AI Backend / RAG / Agent 能力；RM-08 面试复盘与查漏补缺
- 状态：DONE
- 主题：围绕金蝶软件中国 AI 应用开发高级工程师岗位，压缩 Java 后端、ERP 对接、Harness、Skill / MCP / API 工程化、Agent 和服务治理表达
- 学习目标：在 2026-07-13 19:00 面试前，把个人优势定位为“Java 后端工程化 + RAG / Agent 工具生态接入”，能把结算系统、RAG + Agent 系统、LangGraph / MCP / 工具调用学习、Redis / MQ / Spring / 微服务经验迁移到金蝶的 ERP 外部生态、Harness 工具研发、Skill / MCP / API 标准化和服务治理场景。
- 验收标准：能完成 60 秒自我介绍；能解释 Harness / Skill / MCP / API 在企业 AI 应用中的工程定位；能回答如何把 ERP、第三方 API 或 MCP Server 接入 Agent 工具体系；能说明工具调用的权限、幂等、超时、审计、灰度和高风险 human-in-the-loop；能处理“AI 项目是否正式上线”的边界追问；能把 Redis、Kafka / MQ、Docker、SpringCloud、MyBatis、MySQL / SQL Server、CI/CD 等关键词落到可靠服务治理，而不是堆栈罗列。
- 当前断点：2026-07-13 已完成金蝶软件中国 AI 应用开发高级工程师面试准备和真实面试归档。准备阶段完成新版简历口径、Harness / Skill / MCP / API、ERP Tool 接入、安全治理、持续交付、Agent 诊断流程、工具失败处理、重复入账、RAG 评测、Hybrid / Rerank、语义切分和表格 chunk 的口述准备。真实面试实际重心仍落在 RAG 项目深挖，暴露文档解析、chunk、Rerank、私有语料排序失效、模型部署和前沿算法跟踪短板，已回流到 `BL-013`。
- 关联文件：`interview/mock-records/2026-07-13-kingdee-ai-application-senior-engineer-prep.md`、`sessions/2026-07-13-kingdee-ai-application-interview-prep.md`、`interview/real-records/2026-07-13-kingdee-ai-application-senior-engineer.md`、`interview/rag-project-story.md`、`interview/ai-application-questions.md`、`backend/redis/distributed-lock.md`、`backend/java/thread-pool.md`、`mistakes/interview/rag-rerank-algorithm-depth.md`
- 下一步动作：任务已完成；面试暴露问题当时已回流到 `BL-013`，当前全局恢复入口以 `START_HERE.md` 为准。

### BL-013 RAG 检索、重排与文档结构化解析补课

- ID：BL-013
- 优先级：P1
- 来源：真实面试暴露
- RoadmapRef：RM-06 AI Backend / RAG / Agent 能力；RM-08 面试复盘与查漏补缺
- 状态：REVIEW
- 主题：补齐 RAG 从工程链路进入算法追问时的关键短板
- 学习目标：理解混合检索、结果融合、Rerank、私有语料排序失效、结构化文档解析、语义切分、PDF / OCR 和 RAG 评测的机制边界，能把工程实现和算法原理连接起来。
- 验收标准：能讲清关键词检索、向量检索、RRF / 加权融合和 Rerank 的区别；能解释 cross-encoder rerank 的基本机制及其和 embedding 双塔召回的差异；能回答“最相关片段被排在最后怎么办”；能说明 Word 标题层级、表格、图片、PDF / OCR 对文档解析和切分的影响；能用 Recall@K、MRR、NDCG、faithfulness、引用准确性组织 RAG 评测。
- 当前断点：2026-07-21 已在 `BL-015` 中完成 RAG 文件切分答案梳理：常见方式包括长度、递归、结构、语义和父子多粒度切分；当前项目事实仍是固定窗口 + overlap + 自然边界兜底，其他方式属于优化方向。2026-07-28 韶音面试再次验证了“追踪、召回、排序、生成”容易混答；2026-07-29 已完成四层口述并确认 Rerank 已集成进离职后个人持续建设的 RAG 主链路，在 Hybrid Retrieval 与融合后执行二阶段排序。荣耀内部阶段只完成 RAG 初步搭建且没有用户试用，不能将 Rerank 或 Agent 包装成公司内部能力；语义切分、表格 chunk、领域 Reranker 适配和专项评测尚未继续展开，任务保持 AI 补充能力 REVIEW。
- 关联文件：`interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`、`sessions/2026-07-07-huashengtong-ai-application-interview-review.md`、`interview/real-records/2026-07-13-kingdee-ai-application-senior-engineer.md`、`sessions/2026-07-13-kingdee-ai-application-interview-prep.md`、`interview/real-records/2026-07-28-shokz-senior-java-supply-chain.md`、`sessions/2026-07-28-shokz-interview-review.md`、`mistakes/interview/rag-rerank-algorithm-depth.md`、`interview/mock-records/2026-07-07-huashengtong-ai-application-engineer-prep.md`、`interview/mock-records/2026-07-13-kingdee-ai-application-senior-engineer-prep.md`、`interview/ai-application-questions.md`、`interview/rag-project-story.md`
- 下一步动作：只有后续目标岗位明确要求检索算法深度时，再做文件切分口述追问，并恢复语义切分、表格 chunk 和 Rerank 专项建设。

### BL-012 华盛通大模型应用工程师面试专项准备

- ID：BL-012
- 优先级：P0
- 来源：真实面试准备 + 目标岗位要求
- RoadmapRef：RM-06 AI Backend / RAG / Agent 能力；RM-08 面试复盘与查漏补缺
- 状态：DONE
- 主题：围绕华盛通 SZ-大模型应用工程师 JD，压缩 RAG、LangChain / Dify、后端工程和推理加速边界表达
- 学习目标：在真实面试前，把个人简历中的 RAG 项目表达、后端工程迁移能力、金融场景可信 RAG 风险控制、LangChain / Dify / LangGraph 边界、CUDA / TensorRT 短板防守整理成可口述答案。
- 验收标准：能完成 60 秒自我介绍；能讲清企业知识库 RAG 的离线索引链路和在线问答链路；能回答 Chunk、Embedding、向量检索、召回排查、pgvector、权限隔离、幻觉控制、索引任务失败、版本冲突、金融场景风险；能诚实说明 RAG 未生产上线、Agent / LangGraph / Dify / CUDA 不是简历主经验；能把优势落到 Java 后端 + RAG 应用工程化。
- 当前断点：2026-07-07 已完成面试前准备和 20:00 华盛通真实面试验证。准备内容覆盖开场介绍、RAG 项目主线、RAG 排查链路、金融可信 RAG、LangChain / Dify 定位、Redis / MQ / Spring / FastAPI 后端支撑、CUDA / TensorRT 防守表达。面试后已归档真实复盘，新增 `BL-013` 处理 Rerank、检索融合和文档结构化解析短板。
- 关联文件：`interview/mock-records/2026-07-07-huashengtong-ai-application-engineer-prep.md`、`sessions/2026-07-07-huashengtong-ai-application-interview-prep.md`、`interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`、`sessions/2026-07-07-huashengtong-ai-application-interview-review.md`、`interview/rag-project-story.md`、`interview/ai-application-questions.md`、`interview/redis-questions.md`、`backend/redis/distributed-lock.md`
- 下一步动作：任务已完成；面试暴露问题当时已回流到 `BL-013`，当前全局恢复入口以 `START_HERE.md` 为准。

### BL-011 LangChain / LangGraph 机制梳理

- ID：BL-011
- 优先级：P2
- 来源：个人主动学习 + 目标岗位要求
- RoadmapRef：RM-06 AI Backend / RAG / Agent 能力
- 状态：TODO
- 主题：LangChain / LangGraph 的核心机制、边界和工程使用方式
- 学习目标：系统梳理 LangChain 与 LangGraph 分别解决什么问题，掌握 LangChain 的 Core components、Middleware、Runtime、Frontend、Advanced usage 目录层级，以及 LangGraph 的 Capabilities、Production、Frontend、Graph API / Functional API 等目录层级；能把这些内容压缩成工程可用的框架地图，而不是只记零散 API。
- 验收标准：能说明 LangChain、LangGraph、LangSmith 的职责边界；能按官方目录画出 LangChain / LangGraph 的学习地图；能解释 `create_agent`、Middleware、Runtime context、Graph API、Functional API、checkpoint、store、interrupt、streaming、subgraph、time travel 的作用和边界；能结合个人 RAG / Agent 项目说明什么时候用框架、什么时候保留业务状态在 Java 后端。
- 当前断点：2026-07-07 已完成第一轮机制梳理和实验验证，已验证 interrupt / resume、node 重放与幂等、调用方循环处理 interrupt、业务状态冲突校验、streaming、checkpoint 存储边界、标准模型工具调用 loop 和高风险副作用受控执行边界。尚缺 LangChain / LangGraph 官方目录地图级全貌。2026-07-18 因求职和学习主线切回 Java 后端，本任务降为 P2 TODO，保留现有实验与断点，不继续扩张框架目录。
- 关联文件：`LEARNING_ROADMAP.md`、`interview/ai-application-questions.md`、`sessions/2026-07-05-langchain-langgraph-agent-runtime.md`、`sessions/2026-07-05-langgraph-runtime-demo.md`、`sessions/2026-07-06-create-agent-stategraph-boundary.md`、`sessions/2026-07-07-langchain-langgraph-learning-summary.md`、`sessions/2026-07-07-langchain-langgraph-official-doc-map-gap.md`、`labs/langgraph-runtime-demo/README.md`、`labs/langgraph-runtime-demo/approval_flow_demo.py`、`labs/langgraph-runtime-demo/streaming_demo.py`、`labs/langgraph-runtime-demo/checkpoint_demo.py`、`labs/langgraph-runtime-demo/create_agent_demo.py`、`labs/langgraph-runtime-demo/hybrid_agent_graph_demo.py`、LangChain 官方文档：`https://docs.langchain.com/oss/python/langchain/overview`、LangGraph 官方文档：`https://docs.langchain.com/oss/python/langgraph/overview`
- 下一步动作：仅在目标岗位明确要求 LangChain / LangGraph，或 Java 主线稳定后，再恢复官方目录地图和 2 到 3 分钟口述验证。

### BL-001 Redis 数据结构、对象存储与缓存边界

- ID：BL-001
- 优先级：P0
- 来源：真实面试暴露 + 旧冲刺计划迁移
- RoadmapRef：RM-04 Redis / MQ / 分布式能力
- 状态：TODO
- 主题：Redis 常见数据结构、Hash 与序列化 String 的对象存储边界，以及缓存读写与异常治理
- 学习目标：能讲清 Redis 对外数据类型的典型场景、对象存储取舍和缓存职责边界。
- 验收标准：能用 1 分钟回答 Redis 常见数据结构；能比较 Hash 与序列化 String；能解释 Cache Aside 的读写链路以及缓存穿透、击穿、雪崩的差异；能解释为什么分布式锁通常使用 String。
- 当前断点：2026-06-30 真实面试暴露 Redis 数据结构回答偏底层实现，未先回答对外数据类型。
- 关联文件：`interview/real-records/2026-06-30-ai-agent-rag-backend.md`、`interview/redis-questions.md`
- 下一步动作：先复盘 String、Hash、List、Set、ZSet、Stream 的工程场景，再整理 Hash 与 String 存对象以及 Cache Aside 的面试回答。

### BL-002 Redis / Redisson 分布式锁与锁粒度表达

- ID：BL-002
- 优先级：P0
- 来源：真实面试暴露 + 旧冲刺计划迁移
- RoadmapRef：RM-04 Redis / MQ / 分布式能力
- 状态：REVIEW
- 主题：Redis 原生锁、Redisson 锁、业务抢占锁、数据库状态机处理权的边界
- 学习目标：能先区分锁的目标，再回答锁应该覆盖短临界区还是整个任务周期，并理解 Redisson 对加锁、续期和释放的封装边界。
- 验收标准：能用 1 分钟讲清 `SET NX PX`、唯一 owner token 与安全释放；能解释 Redisson `RLock`、可重入、watchdog / lease time 和持有者释放约束；能解释为什么不能只依赖 Redis / Redisson 锁保证任务只处理一次；能结合数据库 `process_token` 和状态机回答长任务场景。
- 当前断点：Redis 分布式锁第一轮已学习，但面试中锁粒度表达出现摇摆。
- 关联文件：`backend/redis/distributed-lock.md`、`interview/redis-questions.md`、`mistakes/distributed/redis-lock.md`
- 下一步动作：先对照原生 Redis 锁与 Redisson `RLock` 的加锁、续期和释放机制，再重写“锁整个任务还是只锁临界区”的面试回答。

### BL-003 MQ 可靠性主线

- ID：BL-003
- 优先级：P1
- 来源：旧冲刺计划迁移
- RoadmapRef：RM-04 Redis / MQ / 分布式能力
- 状态：TODO
- 主题：生产发送、Broker 持久化、消费确认、重试死信、重复消费、顺序消息和消息积压
- 学习目标：建立从生产者到 Broker、消费者和业务落库的 MQ 可靠性主线，并能落到项目状态流转和补偿场景。
- 验收标准：能解释 MQ 解决的工程问题和异步化代价；能分生产发送、Broker 持久化、消费确认三段回答消息不丢；能解释至少一次投递为什么仍需要消费幂等；能说明重试、死信、顺序和积压的治理方法；能结合幂等键、状态机和补偿讲项目实践。
- 当前断点：2026-07-28 已在 `BL-016` 中完成生产者、Broker、消费者、至少一次投递、消费幂等、ACK、Outbox、重试和死信的第一轮场景学习，但尚未按 MQ 产品机制形成独立主线。韶音面试官明确反馈消息可靠性细节不足，说明已有场景理解还没有转换成稳定的端到端表达。
- 关联文件：`LEARNING_ROADMAP.md`、`backend/distributed-system/high-qps-capacity-design.md`、`mistakes/distributed/high-qps-and-mq-boundaries.md`、`interview/real-records/2026-07-28-shokz-senior-java-supply-chain.md`
- 下一步动作：从“MQ 解决什么工程问题”开始，建立生产者、Broker、消费者和业务幂等的链路。

### BL-004 Java 并发锁体系

- ID：BL-004
- 优先级：P0
- 来源：旧冲刺计划迁移
- RoadmapRef：RM-03 Java / Spring / 并发能力
- 状态：TODO
- 主题：`synchronized`、`volatile`、CAS、AQS
- 学习目标：补齐 Java 并发锁体系，并和线程池、任务执行、分布式锁边界连接起来。
- 验收标准：能区分互斥、可见性、原子性和同步队列；能回答至少 2 个并发追问；能说明单 JVM 锁和分布式锁边界。
- 当前断点：线程池主线已完成第一轮；2026-07-21 通过 ConcurrentHashMap 补了 CAS 空桶插入、桶级 `synchronized`、可见性、协作扩容和复合操作原子性的入口，但尚未系统学习 `synchronized`、`volatile`、CAS 通用问题和 AQS。2026-07-27 `BL-006` 暂缓后曾将本任务设为当前入口；在正式开始前，用户补充了万级 QPS、JVM 和 Spring Batch 三个真实面试学习点，当前先推进 `BL-016`，本任务保留原断点等待恢复。
- 关联文件：`backend/java/thread-pool.md`、`backend/java/map-and-concurrent-hash-map.md`、`interview/java-concurrency-questions.md`、`mistakes/concurrency/thread-pool.md`
- 下一步动作：先从 `synchronized` 解决什么问题开始，再进入 `volatile`、CAS、AQS。

### BL-005 Spring 核心机制

- ID：BL-005
- 优先级：P0
- 来源：旧冲刺计划迁移
- RoadmapRef：RM-03 Java / Spring / 并发能力
- 状态：DONE
- 主题：IOC、AOP、Bean 生命周期、`@Transactional` 失效场景
- 学习目标：建立 Spring 核心机制和 Web 请求链路的连接。
- 验收标准：能讲清 IOC 和 AOP 解决的问题；能说明 Bean 生命周期关键阶段；能回答 `@Transactional` 常见失效场景。
- 验收结果：已能讲清 IOC / DI 解决的对象创建与依赖装配问题，能够说明实例化、注入、初始化、BeanPostProcessor、代理和销毁阶段；能够从 Advisor / Pointcut / Advice、JDK 动态代理 / CGLIB、拦截器链解释 AOP，并能回答同类自调用、异常捕获、默认回滚规则、`rollback-only` 和事务传播边界。已达到本任务当前验收标准；循环依赖、事务管理器实现差异和 AOP 源码级细节属于后续按需深挖，不延长本任务。
- 当前断点：2026-08-02 完成 AOP 与声明式事务连续追问和闭卷压缩。能够说明普通运行时注解不会自动产生 AOP 能力，代理 Bean 不代表所有方法都执行相同增强，`proceed()` 负责推进拦截器链；能够区分 `TransactionInterceptor` 的流程组织与 `TransactionManager` 的资源管理，并结合项目事务事故解释外部代理调用与同类自调用的差异。
- 关联文件：`backend/spring/ioc-bean-and-transaction-proxy.md`、`mistakes/spring/aop-transaction-proxy-boundaries.md`、`sessions/2026-08-02-aop-transaction-propagation-java-version-cards.md`、`interview/mock-records/2026-07-21-pingan-java-backend-prep.md`、`interview/real-records/2026-07-28-shokz-senior-java-supply-chain.md`、`projects/settlement-system/transaction-flow-and-reconciliation.md`、`fundamentals/network/http-tcp-request-flow.md`、`interview/computer-fundamentals-questions.md`
- 下一步动作：任务已完成。后续只在真实面试再次暴露循环依赖、事务管理器差异或源码级代理问题时，新建小任务或回补对应主题，不重复当前基础主线。

### BL-006 结算系统项目表达与双版本简历完善

- ID：BL-006
- 优先级：P0
- 来源：项目表达短板 + 旧冲刺计划迁移
- RoadmapRef：RM-05 项目深挖与工程表达
- 状态：TODO
- 主题：结算系统 2 分钟和 10 分钟项目表达，以及 Java 后端 / AI 应用双版本简历完善
- 学习目标：把业务功能表达升级为工程能力表达，并形成事实一致、重点不同、可以按目标岗位继续定制的两份投递基准稿。
- 验收标准：Java 和 AI 两份简历的工作时间、项目事实与量化数据保持一致，分别突出 Java 生产工程能力和 RAG / Agent 应用能力；能用 2 分钟讲清结算系统定位、核心链路、异步状态、幂等恢复和规模瓶颈；能用 10 分钟展开一致性或幂等设计。
- 当前断点：2026-07-21 已将主职责统一为“交易流水处理与核销业务域”，并还原 FFP 文件集成、流水处理、订单匹配、辅账、ERP、待对账池和核销链路。已确认十组项目证据：三年不少于 50 次上游流水纠错、N+1 改造后达到 100 万笔 8 分钟以内、对账辅账事故涉及数千笔辅账及百万级关联明细、主动发现 ERP 发票/收据凭证 ID 命名空间碰撞并以“凭证 ID + 接口名”组合业务键修复、设计未对账池批量终止与恢复能力并实现受控状态流转和逐笔审计、通过动态 MySQL 分区查询范围将对账池生成任务由接近 40 分钟缩短至约 8 分钟并修复部分命中漏数据问题、通过分页与总数解耦和联合索引修复将亿级流水表尾页查询从超过 120 秒降至 3 秒以内、通过抢占式调度、Redis 锁、批次事务和明细级 Checkpoint 实现对账池任务中断续跑、独立设计结算单电子盖章模块并实现批量异步申请、跨系统回调关联、幂等状态更新、超时恢复和文件版本切换且上线运行 3 个月未发生生产故障或数据错误、通过 Heap Dump 定位 `ReconcileData` 及关联对象占用或保留内存超过 10GB且被 MyBatis 缓存长期持有，关闭对应查询缓存后经低内存对照测试与生产三个月运行均未再发生 OOM。2026-07-24 已完成 Java 后端和 AI 应用两份可投递基准稿及终稿审校：Java 版从十组证据中筛选六组最适合简历的生产案例，按职责、性能、可靠性、OOM 排障、主动防错和独立交付组织；AI 版突出 RAG 全链路、Java / Python 边界和受控 Agent，同时保留四年 Java 生产经验作为工程可信度。两份简历已删除期望薪资，避免过早锚定；MCP 明确为协议理解，MQ 只保留实际使用口径，不包装为中间件建设经验；公司时间、项目时间、规模与量化结果已校验一致。当前基准稿可以用于投递，获得具体 JD 后再调整关键词与案例顺序。结算系统 2 分钟和 10 分钟口述版本尚未完成。2026-07-27 用户决定暂缓本任务，先投入新知识点学习；现有简历、项目证据和事实边界均保留，不重复整理。
- 关联文件：`projects/settlement-system/transaction-flow-and-reconciliation.md`、`projects/settlement-system/settlement-document-stamping.md`、`sessions/2026-07-24-java-ai-resume-and-project-evidence.md`、`sessions/2026-07-21-java-resume-project-evidence-and-pingan-breakpoint.md`、`sessions/2026-07-21-pingan-java-interview-prep-closeout.md`、`interview/mock-records/2026-07-21-pingan-java-backend-prep.md`、`backend/mysql/sql-performance-analysis.md`、`backend/spring/ioc-bean-and-transaction-proxy.md`、`resume/java-backend-resume.md`、`resume/ai-application-resume.md`、`interview/real-records/2026-06-10-llm-application-engineer.md`、`interview/real-records/2026-06-30-ai-agent-rag-backend.md`
- 下一步动作：临近明确面试并获得具体 JD 后恢复本任务；届时结合 JD 一次性校验两份简历的技能关键词和项目证据顺序，再按“系统定位 -> 核心链路 -> 一致性 -> 失败恢复 -> 性能 -> 复盘”完成结算系统 2 分钟和 10 分钟口述版本。Map 构建、配置缓存和场景 ID 优先级语义仍作为待确认事实，不写入简历。

### BL-007 RAG / Agent 项目事实边界表达

- ID：BL-007
- 优先级：P1
- 来源：真实面试暴露
- RoadmapRef：RM-06 AI Backend / RAG / Agent 能力
- 状态：TODO
- 主题：未生产上线的 RAG / Agent 项目如何表达工程价值
- 学习目标：明确区分已实现能力、个人实践、生产化设计和未落地边界。
- 验收标准：能回答“没有生产上线为什么仍能证明能力”；能区分固定 Pipeline、Workflow 和 Agent；能避免把设计方案包装成生产经验。
- 当前断点：2026-07-29 已确认项目时间线：需求起点来自荣耀财经部门，由产品收集后交给开发认领；本人离职前完成 RAG 初步搭建，但没有用户试用；离职后围绕同类场景继续个人工程实践并新增 Rerank 和 Agent。后续事实边界应区分公司需求背景、公司阶段初版、个人后续实现和未生产验证。
- 关联文件：`interview/rag-project-story.md`、`interview/ai-application-questions.md`、`interview/real-records/2026-06-30-ai-agent-rag-backend.md`
- 下一步动作：恢复本任务时，直接用“财经需求 -> 认领初版 -> 未试用 -> 离职后 Rerank / Agent -> 非生产验证”完成 30 至 60 秒事实边界口述。

### BL-008 MySQL 追问复盘

- ID：BL-008
- 优先级：P2
- 来源：旧冲刺计划迁移
- RoadmapRef：RM-02 数据库核心能力
- 状态：REVIEW
- 主题：死锁、锁分类、慢 SQL 和事务日志边界
- 学习目标：把已学 MySQL 主线转成稳定追问能力。
- 验收标准：能回答死锁产生与排查；能区分共享锁、排他锁、乐观锁、悲观锁、Redis 锁和数据库锁；能用执行计划反推访问路径。
- 当前断点：事务、MVCC、索引和锁已完成第一轮；2026-07-21 又通过真实 N+1 案例梳理了“单条 SQL 耗时、调用次数、扫描范围、锁等待和整体访问模型”的 SQL 优化主线，并快速复盘 Join、Group By、Distinct、Union 和重复属性查询。2026-07-28 韶音面试暴露新的存储边界：能够确认云平台删除历史数据后存储指标下降，但尚不能区分 InnoDB 页复用、`.ibd` 文件缩小、操作系统磁盘回收和云平台治理机制。死锁、执行计划和表空间追问稳定性仍需验证。
- 关联文件：`backend/mysql/transaction.md`、`backend/mysql/lock-and-batch-processing.md`、`backend/mysql/sql-performance-analysis.md`、`interview/mysql-questions.md`、`interview/mock-records/2026-07-21-pingan-java-backend-prep.md`、`interview/real-records/2026-07-28-shokz-senior-java-supply-chain.md`、`mistakes/database/transaction.md`
- 下一步动作：本任务恢复时直接用 3 到 5 个追问验证死锁、锁分类、慢 SQL 访问路径和表空间边界；对云平台物理回收机制继续保持未知边界，不从现象反推实现。

### BL-009 算法保底

- ID：BL-009
- 优先级：P2
- 来源：旧冲刺计划迁移
- RoadmapRef：RM-07 算法与问题求解能力
- 状态：TODO
- 主题：滑动窗口、二分、DP 代表题复述
- 学习目标：建立算法面试保底表达能力。
- 验收标准：完成至少 3 道代表题的思路复述；能讲清状态、选择、边界、复杂度；能独立写出基础 Java 实现。
- 当前断点：DP 已完成多轮学习，滑动窗口和二分尚未开始。
- 关联文件：`fundamentals/algorithm/dp-basic.md`、`mistakes/algorithm/dp.md`
- 下一步动作：先短时复述 DP 代表题，再选择滑动窗口或二分开始第一轮。

### BL-010 综合模拟面试与错题清单

- ID：BL-010
- 优先级：P2
- 来源：旧冲刺计划迁移
- RoadmapRef：RM-08 面试复盘与查漏补缺
- 状态：TODO
- 主题：综合模拟面试、评分、错题和表达问题清单
- 学习目标：通过模拟面试检验后端基础、项目表达和算法表达。
- 验收标准：完成至少一轮综合模拟面试；形成高频错题和表达问题清单；将反复错误回补到 `mistakes/` 或 Backlog。
- 当前断点：2026-07-21 开始平安产险模拟面试，仅完成一题 60 秒自我介绍并获得 8/10 评价；主要问题是职责范围偏大、AI 技术名词过密和结尾岗位匹配偏弱。尚未完成项目介绍和正式综合模拟。
- 关联文件：`interview/real-records/`、`mistakes/`
- 下一步动作：在 Redis 和项目表达补齐后，安排一轮 Java 后端综合模拟面试。
