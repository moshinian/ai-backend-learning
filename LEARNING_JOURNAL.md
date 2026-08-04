# LEARNING JOURNAL

## 作用

这个文件只负责四类信息：

1. 长期学习画像
2. 阶段性反思和重要变化
3. 长期典型误区模式
4. 已沉淀主题与历史会话索引

它不是当前状态权威文件。

当前恢复学习进度时，只需要优先读取：

1. `START_HERE.md`

任务优先级、状态、验收标准、当前断点和下一步动作以 `LEARNING_BACKLOG.md` 为准。

具体知识笔记和错误纠偏不在本文件展开，只保留索引。

---

## 长期学习画像

- 背景：
  - 有 Java 后端开发经验
  - 做过云服务结算系统
  - 也在做 RAG 知识问答系统
- 当前目标：
  - 以 Java 后端作为求职和长期能力建设主航道，从“会做业务开发”升级为“能讲清机制、能设计系统、能稳定应对 Java 后端面试”
  - 保留 RAG / Agent 应用工程能力作为差异化补充，重点体现模型能力接入业务系统时的后端工程价值，不再把算法型 AI 应用岗位作为主要竞争方向
- 学习偏好：
  - 优先理解本质
  - 优先建立知识结构
  - 优先结合项目和面试表达
  - 不希望直接灌输标准答案

---

## 重要变化

### 2026-07-18 求职与学习主线切回 Java 后端

- 连续的实际求职和 HR 沟通反馈表明，部分 AI 应用岗位更倾向于具备算法、模型训练、检索排序或推理部署背景的候选人。
- 当前更有证据支撑的优势仍是 Java 后端、结算业务、状态流转、幂等、批处理、数据库、缓存和失败恢复。
- 后续职业定位调整为“Java 后端主线 + AI 应用工程补充”：优先竞争 Java 后端、平台后端及偏工程接入的 AI 平台后端岗位。
- 已有 RAG / Agent 学习不作废，但后续只在岗位明确需要或能强化后端差异化时继续投入，不再无边界扩张算法和框架知识面。
- 具体任务优先级和当前断点以 `LEARNING_BACKLOG.md`、`START_HERE.md` 为准。

### 2026-07-21 Java 主线从方向判断进入证据化表达

- 平安产险面试准备把“切回 Java 后端”从求职方向判断推进到实际学习和表达：结算系统不再按功能清单介绍，而是围绕交易流水与核销业务域、真实故障、性能结果和设计边界组织。
- 已确认当前最有竞争力的证据不是技术名词数量，而是三类可追问事实：上游纠错的冲销补偿、N+1 批处理优化、事务边界事故定位与修复。
- Java 基础开始和真实项目互相验证：Spring 代理解释事务事故，SQL 访问模型解释 N+1 性能问题，CAS / 桶级同步解释并发容器，状态抢占与业务幂等解释定时任务唯一性。
- 当前能力仍不均衡：Spring、事务、SQL 和项目证据已完成第一轮结构化；JVM、RocketMQ、Redis 数据结构、`synchronized` / `volatile` / AQS 仍偏面试速答，后续不能把“看过答案”误认为“稳定掌握”。
- 面试表达形成新的校验顺序：先限定本人职责，再讲问题和证据，然后解释机制、结果与复盘；不确定的框架细节、生产效果和他人负责模块明确保留边界。

### 2026-07-24 项目证据形成双版本简历基准

- 结算系统经历从三组代表案例扩展为覆盖性能、可靠性、跨系统状态、主动防错和 JVM 排障的十组可追问证据，并分别归档到交易核销与电子盖章项目文档。
- Java 后端与 AI 应用两份简历不再按技术栈多少区分，而是共享同一组工作事实、按岗位选择不同证据：Java 版突出生产工程能力，AI 版突出 RAG / Agent 链路及 Java / Python 协作边界。
- 简历事实校验形成稳定原则：量化结果必须带真实条件和生产验证；无法确认的 MyBatis 缓存层级、Mapper 结构和待落地优化不写成确定事实；MQ 保持实际使用口径，MCP 只表述为协议理解。
- 两份简历已成为可继续按 JD 定制的投递基准稿；具体任务断点仍以 `BL-006` 和 `START_HERE.md` 为准。

### 2026-07-27 Java 技术栈进入分层建设

- 多次 Java 后端 JD 和真实面试暴露的问题开始收敛到三层能力：MySQL、Redis / Redisson、MQ、JVM、多线程、Linux 属于生产后端核心层；Spring Cloud、Nacos、Sentinel 属于微服务治理层；Docker、Kubernetes 属于应用交付与运行层。
- MySQL 已有事务、锁、索引、SQL 优化和生产案例基础，后续以追问验证和机制补强为主；Redis、MQ、JVM、多线程和 Linux 仍需形成更完整的机制、故障边界与诊断主线。
- Spring Cloud、Nacos、Sentinel、Docker 和 Kubernetes 值得学习，但目标深度不同：先形成可运行的服务治理和容器交付证据；Kubernetes 当前只建设后端开发者所需的部署、观察和排障能力，不扩张到集群平台运维。
- 后续学习不按技术名词逐个背诵，而按“解决的问题 -> 运行机制 -> 失败边界 -> 实验或项目证据 -> 面试表达”推进。具体任务状态和次序仍以 `LEARNING_BACKLOG.md`、`START_HERE.md` 为准。

### 2026-07-28 面试补课从穷举记忆转向最小检索入口

- 韶音科技面试连续从项目事实追问到原子性、MySQL 表空间、RAG 质量和 Spring Bean 生命周期边界。会后最强烈的感受是“最后总会被问到不知道”，容易忽略此前已经回答正确的生产链路和核心机制。
- 后续不以记住所有接口、回调顺序和平台实现为学习目标。每个主题先压缩成三到四个检索入口，再按“问题层次 -> 已确认事实 -> 机制解释 -> 失败边界 -> 当前未知”展开。
- 面试官追问到未知处是能力边界探测，不等于此前回答全部失效；稳定承认未知、说明验证方式，比为不掌握的底层机制继续背书更重要。
- RAG 项目事实完成校准：需求起点来自荣耀财经部门，产品收集后由开发认领；本人离职前完成 RAG 初步搭建，但没有用户试用；离职后围绕同类场景继续个人工程实践并新增 Rerank 和 Agent。当前 Rerank 已集成进个人持续建设的知识库主链路，但不据此声称荣耀内部试用或生产上线效果。
- 本次暴露点已收敛为短周期 `BL-023`，不会为了追上一场面试继续横向扩张整个 Java 技术栈。

### 2026-07-29 项目表达从“证据充足”进入“听众对齐”

- 和生创新技术全栈工程师面试表明，已有结算系统事实和技术证据并不自动等于项目能够被陌生听众理解。面试官多次要求先说明系统全貌、单据链路和个人职责，并明确反馈“讲得太细、没有跟上节奏、难点不清楚”。
- 后续项目表达固定按“系统全貌 -> 核心链路 -> 本人职责 -> 代表难点”逐层缩放。面试官没有建立业务图像前，不提前展开字段、缓存、分页、策略实现和异常分支。
- 技术难点必须包含可观察问题、不可违反的约束、明确机制和结果证据；“方案设计、综合应用、持续适配、抽象兼容”不能单独作为难点。
- 面试压力下再次出现事实边界漂移风险：冲销管道是否从零设计和“一天百万订单”等口径仍需确认；RAG 已明确区分公司需求与初版阶段、离职后个人新增 Rerank / Agent 阶段，不能因为现场追问而把当前整套能力包装为荣耀内部项目成果。
- 本场同时确认 Java 基础仍存在结构性薄弱点：AOP 本质能够理解，但压缩表达不稳；事务传播和 Java 8 之后的版本能力尚未形成可检索入口。具体任务由 `BL-024` 承接。

### 2026-08-02 Spring 学习从注解记忆进入代理调用链

- AOP 认知从“使用注解增加功能”推进到 Advisor、Pointcut、Advice、代理 Bean、拦截器链和 `proceed()` 的完整调用关系；能够说明普通运行时注解为什么不会自动产生 AOP 能力。
- 声明式事务不再只记传播行为名称，而是先判断调用是否经过代理，再区分 `TransactionInterceptor` 的流程组织、`TransactionManager` 的资源管理、物理事务数量、保存点和 `rollback-only` 状态。
- 连续判断中暴露并纠正了两个高价值边界：`NESTED` 内层回滚不必然拖垮外层事务；自调用异常被外层捕获时，因为内层拦截器没有执行，结果可能与跨 Bean 的 `REQUIRED` 调用不同。
- Java 版本学习采用“每版两个入口、每个入口说明解决的问题和边界”的最小卡片方式，已经建立 Java 8、11、17、21 的闭卷检索入口；后续不再用“性能更好、GC 更流畅”等无法验证的笼统表述代替版本事实。

### 2026-08-03 项目可靠性表达从技术叠加进入职责分层

- 平安产险面试准备完成了结算系统从内部业务名词到“服务对象、输入、公共主链路、输出、本人职责”的再次压缩，并确认早期参与 2C 支付和 2B 预装、后期独立负责 2B 商推以及公共流水与核销的职责演进。
- 性能案例开始严格分离：N+1 解决累计数据库往返；2C 支付订单由月分区调整为周分区，使分区粒度匹配一周查询窗口；亿级流水尾页问题由分页拆分、执行计划和联合索引解决。相同的“100 万笔 8 分钟”不能让不同阶段的方案互相替代。
- 任务可靠性形成新的职责图：数据库条件更新负责同名定时父任务抢占；Redis 功能级锁负责手工与定时两个入口互斥；Spring Batch、分片状态和心跳负责执行控制；明细状态、批次事务和幂等负责数据正确与失败续跑。
- 对既有方案的复盘不再停留在“Redis 锁有用或没用”的二选一，而是先确认锁保护的入口、资源和生命周期；也能够说明功能级全局锁与分片状态字符串的简单性收益和扩展代价。
- 当天真实面试新增分布式事务缺口：面试官提到的“二级事务、三级事务”可能指 2PC / 3PC，但原词尚未核对。后续必须区分本地批次事务、跨系统最终一致性和分布式提交协议，不能用 Redis 锁、状态机或补偿机制直接替代协议知识。

### 2026-08-04 Agent 工程学习从功能清单进入状态与事件链

- 颂拓 AI Agent 工程师一面验证了“Java 生产后端能力迁移到 Agent Runtime”的岗位匹配：状态、幂等、恢复、数据库、缓存、消息、压测和排障，比单纯罗列 Agent 框架更接近岗位核心。
- 本场出现新的高价值反差：个人 `rag-system` 已经实现 Run / Step / Action / Event、事件表、事务提交后发布、`Last-Event-ID` 补发、心跳和孤儿 Run 恢复，但现场认知仍停留在“可以增加状态表”。代码实现不能代替本人形成可检索的机制模型。
- SSE 开始按四个维度拆分：Step 级还是 Token 级、实时帧是否持久化、断线后如何补发、单实例广播如何升级为多实例共享通道。只有分别回答这四个问题，才能避免把“流式”说成一个模糊功能。
- 工具治理也需要分层：版本号解决兼容性和可复现性，工具描述、参数约束和评测集决定模型选择质量；MCP 元数据不能替代业务认证与授权。
- Python 多实例部署、容器沙箱、模型工程化、长期记忆和长任务校验仍是当前能力缺口。后续只做与潜在下一轮直接相关的最小补强，不把尚未实践的方案包装成生产经验。
- 该岗位是 Java 后端主线的合理延伸，不改变长期求职定位。当前通过 `BL-026` 短周期补强；未确认下一轮前，不扩张模型训练或平台运维知识面。

---

## 长期典型误区模式

本节只记录长期反复出现的认知模式。具体错误表现、根因和纠正内容，以 `mistakes/`、`backend/`、`fundamentals/`、`interview/` 和 `sessions/` 中的主题文件为准。

### 1. 容易把框架链路当成完整链路

典型表现：

- HTTP 请求只讲到 Controller、Service、DAO，容易漏掉 DNS、TCP、端口、容器、线程和内核协议栈。
- 三次握手、可靠传输、连接复用等边界容易混在一起。

主要索引：

1. `fundamentals/network/http-tcp-request-flow.md`
2. `mistakes/network/request-flow.md`
3. `interview/computer-fundamentals-questions.md`

### 2. 容易把机制名词背熟，但边界说不稳

典型表现：

- MySQL 事务、隔离级别、MVCC、undo log、redo log、binlog 的职责边界容易混淆。
- 快照读、当前读、行锁、间隙锁、Next-Key Lock 容易被统一说成“锁机制”。
- 慢 SQL、索引失效和执行计划容易只背结论，缺少访问路径分析。
- 容易把 SQL 性能问题等同于单条慢 SQL，忽略 N+1、累计调用次数和数据库往返。
- 容易只看到 `@Transactional` 注解，忽略真实代理调用链、异常规则、线程和数据源边界。
- 容易认为运行时注解会自动产生 AOP 能力，或把代理 Bean 理解成所有方法都会执行相同增强，忽略 Advisor、Pointcut 和逐方法匹配。
- 容易把 Java 异常是否被 `catch` 与事务的 `rollback-only` 状态混为一谈，没有先区分跨 Bean 代理调用和同类自调用。
- 容易把 JDBC 回滚异常直接解释成事务未开启或数据库部分提交，缺少对原始异常和最终数据状态的核对。

主要索引：

1. `backend/mysql/transaction.md`
2. `backend/mysql/lock-and-batch-processing.md`
3. `mistakes/database/transaction.md`
4. `interview/mysql-questions.md`
5. `backend/spring/ioc-bean-and-transaction-proxy.md`
6. `mistakes/spring/aop-transaction-proxy-boundaries.md`

### 3. 容易把任务状态、处理权和业务幂等混在一起

典型表现：

- 初始容易只用 `status` 判断任务是否还能推进，忽略 `process_token`、租约、心跳、重试和补偿。
- 外部 ERP 调用超时时，容易把“不知道结果”误判成“失败”。
- Redis 锁、数据库状态机和业务幂等键的职责容易混答。
- 容易只看到数据库抢占和 Redis 锁都在“防并发”，没有先判断前者保护定时任务实例、后者可能保护手工 / 定时跨入口，因此过早把二者判断为完全重复或缺一不可。
- 容易把单库批次事务、任务状态、Redis 锁、重试和补偿统称为“分布式事务”，忽略它们与 2PC / 3PC 等分布式提交协议不在同一层。

主要索引：

1. `backend/mysql/lock-and-batch-processing.md`
2. `backend/redis/distributed-lock.md`
3. `mistakes/distributed/redis-lock.md`
4. `interview/redis-questions.md`
5. `projects/settlement-system/transaction-flow-and-reconciliation.md`
6. `sessions/2026-08-03-pingan-interview-prep-and-project-reliability.md`

### 4. Java 并发容易把执行模型和可靠性问题混在一起

典型表现：

- 线程池提交顺序、队列风险、拒绝策略、`submit/execute` 异常处理、中断语义需要反复稳定。
- 容易把线程数、队列容量、数据库连接池、下游容量和任务可靠性放在一个层次里讲。
- 容易把“线程安全容器”理解为整段业务逻辑自动原子化，忽略单次原子操作与多步复合操作的区别。
- ConcurrentHashMap 容易停留在“分段锁”旧口径，需要区分 Java 7 Segment 和 Java 8 以后 CAS、桶级同步、协作扩容的实现主线。

主要索引：

1. `backend/java/thread-pool.md`
2. `mistakes/concurrency/thread-pool.md`
3. `interview/java-concurrency-questions.md`

### 5. 算法题容易先套分类，后定义状态

典型表现：

- DP 中容易先想公式或背包分类，而不是先定义子问题、状态含义、答案位置和转移依赖。
- 前缀长度、字符下标、`dp[0]` 初始化、一维压缩中的旧值和新值需要持续用语义校验。

主要索引：

1. `fundamentals/algorithm/dp-basic.md`
2. `mistakes/algorithm/dp.md`

### 6. 项目表达容易堆功能，缺少问题分层

典型表现：

- 结算系统容易把业务场景、系统架构、数据流、性能瓶颈和技术栈混在一起。
- RAG 项目容易罗列文档解析、向量化、模型调用等功能，而不是按业务问题、架构、职责、难点和指标组织。
- 面对不熟悉业务的听众，容易在系统全貌尚未建立时进入字段、缓存、分页和异常分支；对方表示没听懂后，又继续增加同层细节。

主要索引：

1. `interview/rag-project-story.md`
2. `interview/ai-application-questions.md`
3. `interview/real-records/2026-06-10-llm-application-engineer.md`
4. `interview/real-records/2026-06-30-ai-agent-rag-backend.md`
5. `mistakes/interview/project-zoom-level-and-listener-alignment.md`
6. `interview/real-records/2026-07-29-hesheng-innovation-fullstack-engineer.md`

### 7. AI Backend 表达容易混淆已实现、设计方案和生产经验

典型表现：

- RAG / Agent 项目没有生产上线时，需要主动说明事实边界，不能虚构生产效果，也不能只说“没上线”。
- 固定 RAG Pipeline、Workflow、Agent、模型选型、工具调用和人工确认容易混答。
- 检索、融合、Rerank、Prompt 和生成层优化需要分层表达。
- LangChain / LangGraph 学习中，容易把框架 runtime 状态、checkpoint、后端业务状态、审批事实和工具执行副作用混成一层，需要持续区分“执行现场”和“业务事实”。
- 学习 LangChain / LangGraph 时，容易只抓住已跑通的 `create_agent`、StateGraph、checkpoint、interrupt 片段，忽略官方文档中的 Core components、Middleware、Runtime、Frontend、Capabilities、Production、Graph API / Functional API 等目录级全貌。
- RAG 工程链路能讲通后，容易在 Rerank、私有语料排序失效、文档结构化解析和前沿算法追问处变成泛化回答，需要把工程链路和检索 / NLP 算法机制接起来。
- RAG 文档切分容易停留在固定窗口 + overlap，面对语义切分、Word / PDF / OCR / 表格等复杂文档结构时，需要主动区分“已落地实现”和“成熟优化方案”，并把结构抽取、语义边界、表格结构和评测闭环讲清。
- 容易把 Step 级事件、Token 级流式、事件持久化和多实例实时广播都简称为 SSE，导致项目已经实现的恢复链路和仍未实现的能力边界一起失真。
- 容易因为代码由协作工具完成并已跑通，就误以为本人已经形成机制理解；面试前仍必须沿入口、状态权威、事件顺序、事务边界、恢复路径和失败边界做一次闭卷还原。
- 容易认为给 MCP 工具或 Skill 增加版本号就能改善模型效果，忽略版本治理解决兼容性，而工具描述、候选集合、参数 Schema 和评测才决定选择质量。
- 容易把 Java 多实例和任务治理经验直接类比成 Python / FastAPI、Kubernetes 和容器沙箱的实际经验；可迁移的是设计方法，具体运行时和交付机制仍要补课并保留经历边界。

主要索引：

1. `interview/rag-project-story.md`
2. `interview/ai-application-questions.md`
3. `interview/real-records/2026-06-30-ai-agent-rag-backend.md`
4. `sessions/2026-06-30-ai-agent-rag-backend-interview.md`
5. `sessions/2026-07-05-langchain-langgraph-agent-runtime.md`
6. `sessions/2026-07-05-langgraph-runtime-demo.md`
7. `labs/langgraph-runtime-demo/README.md`
8. `sessions/2026-07-06-create-agent-stategraph-boundary.md`
9. `sessions/2026-07-07-langchain-langgraph-learning-summary.md`
10. `sessions/2026-07-07-langchain-langgraph-official-doc-map-gap.md`
11. `interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`
12. `mistakes/interview/rag-rerank-algorithm-depth.md`
13. `sessions/2026-07-13-kingdee-ai-application-interview-prep.md`
14. `interview/real-records/2026-07-13-kingdee-ai-application-senior-engineer.md`
15. `backend/distributed-system/agent-sse-event-stream-and-recovery.md`
16. `interview/real-records/2026-08-04-suunto-ai-agent-engineer.md`
17. `mistakes/interview/agent-project-implementation-and-expression-gap.md`
18. `sessions/2026-08-04-suunto-ai-agent-interview-and-sse-review.md`

### 8. 学习管理容易把路线、任务、断点和归档混在一起

典型表现：

- 长期能力地图、当前任务池、会话恢复入口和历史归档容易互相写重复内容。
- 后续维护时要坚持：Roadmap 管能力，Backlog 管任务，Start Here 管当前恢复，Journal 管长期画像和索引，sessions 管单次归档。

主要索引：

1. `AGENTS.md`
2. `LEARNING_ROADMAP.md`
3. `LEARNING_BACKLOG.md`
4. `START_HERE.md`

### 9. 容易把技术栈名称当成工程能力

典型表现：

- 容易把会使用某个注解、客户端或部署命令，直接等同于掌握组件的机制、故障边界和生产治理。
- 容易把 Redisson 当成不再需要理解 Redis 锁语义，把 Spring Cloud 组件罗列当成微服务治理，把使用 Kubernetes 当成平台运维经验。
- 学习范围容易随 JD 技术名词横向扩张，缺少核心层、治理层、交付层的深度区分和真实证据。

主要索引：

1. `LEARNING_ROADMAP.md`
2. `LEARNING_BACKLOG.md`
3. `interview/mock-records/2026-07-13-kingdee-ai-application-senior-engineer-prep.md`
4. `resume/java-backend-resume.md`

### 10. 容易把追问终点等同于整场失败

典型表现：

- 面试官沿一个问题持续追问后，只记住最后答不出的细节，忽略前面已经成立的项目事实、生产经验和核心机制。
- 为了避免再次“不知道”，容易尝试穷举背诵 Bean 回调、数据库实现和中间件细节，导致记忆压力继续上升。
- 回答时容易先为现网方案辩护，没有先承认通用风险并区分事实、推断和未知。

主要索引：

1. `mistakes/interview/follow-up-boundaries-and-memory-pressure.md`
2. `interview/real-records/2026-07-28-shokz-senior-java-supply-chain.md`
3. `sessions/2026-07-28-shokz-interview-review.md`

---

## 已沉淀主题索引

### 网络请求链路

1. `fundamentals/network/http-tcp-request-flow.md`
2. `interview/computer-fundamentals-questions.md`
3. `mistakes/network/request-flow.md`

### 学习计划和文档口径

1. `AGENTS.md`
2. `LEARNING_ROADMAP.md`
3. `LEARNING_BACKLOG.md`
4. `START_HERE.md`

### MySQL 事务

1. `backend/mysql/transaction.md`
2. `interview/mysql-questions.md`
3. `mistakes/database/transaction.md`

### MySQL 锁、批处理和索引访问路径

1. `backend/mysql/lock-and-batch-processing.md`
2. `backend/mysql/sql-performance-analysis.md`
3. `interview/mysql-questions.md`
4. `sessions/2026-06-01-mysql-lock-index-batch-processing.md`
5. `sessions/2026-06-02-mysql-index-explain-lock-path.md`

### 动态规划入门

1. `fundamentals/algorithm/dp-basic.md`
2. `mistakes/algorithm/dp.md`
3. `sessions/2026-06-03-dp-basic.md`
4. `sessions/2026-06-04-dp-knapsack.md`
5. `sessions/2026-06-05-dp-lcs-edit-distance.md`
6. `sessions/2026-06-09-dp-space-optimization-and-review.md`

### RAG 与 AI 应用面试

1. `interview/rag-project-story.md`
2. `interview/ai-application-questions.md`
3. `sessions/2026-06-10-llm-application-interview-preparation.md`
4. `sessions/2026-06-11-llm-application-interview-review.md`
5. `interview/real-records/2026-06-10-llm-application-engineer.md`
6. `sessions/2026-06-15-rag-engineering-governance.md`
7. `interview/real-records/2026-06-30-ai-agent-rag-backend.md`
8. `sessions/2026-06-30-ai-agent-rag-backend-interview.md`
9. `sessions/2026-07-05-langchain-langgraph-agent-runtime.md`
10. `sessions/2026-07-05-langgraph-runtime-demo.md`
11. `labs/langgraph-runtime-demo/README.md`
12. `sessions/2026-07-06-create-agent-stategraph-boundary.md`
13. `sessions/2026-07-07-langchain-langgraph-learning-summary.md`
14. `sessions/2026-07-07-langchain-langgraph-official-doc-map-gap.md`
15. `interview/mock-records/2026-07-07-huashengtong-ai-application-engineer-prep.md`
16. `sessions/2026-07-07-huashengtong-ai-application-interview-prep.md`
17. `interview/real-records/2026-07-07-huashengtong-ai-application-engineer.md`
18. `sessions/2026-07-07-huashengtong-ai-application-interview-review.md`
19. `mistakes/interview/rag-rerank-algorithm-depth.md`
20. `interview/mock-records/2026-07-13-kingdee-ai-application-senior-engineer-prep.md`
21. `sessions/2026-07-13-kingdee-ai-application-interview-prep.md`
22. `interview/real-records/2026-07-13-kingdee-ai-application-senior-engineer.md`
23. `interview/real-records/2026-07-28-shokz-senior-java-supply-chain.md`
24. `sessions/2026-07-28-shokz-interview-review.md`
25. `interview/real-records/2026-08-04-suunto-ai-agent-engineer.md`
26. `backend/distributed-system/agent-sse-event-stream-and-recovery.md`
27. `mistakes/interview/agent-project-implementation-and-expression-gap.md`
28. `sessions/2026-08-04-suunto-ai-agent-interview-and-sse-review.md`

### Agent SSE、状态持久化与恢复

1. `backend/distributed-system/agent-sse-event-stream-and-recovery.md`
2. `interview/ai-application-questions.md`
3. `interview/real-records/2026-08-04-suunto-ai-agent-engineer.md`
4. `mistakes/interview/agent-project-implementation-and-expression-gap.md`
5. `sessions/2026-08-04-suunto-ai-agent-interview-and-sse-review.md`

### Java 线程池与后台任务

1. `backend/java/thread-pool.md`
2. `interview/java-concurrency-questions.md`
3. `mistakes/concurrency/thread-pool.md`
4. `sessions/2026-06-12-thread-pool-task-execution.md`
5. `sessions/2026-06-14-thread-pool-lifecycle-monitoring.md`

### 万级 QPS 容量设计与高并发治理

1. `backend/distributed-system/high-qps-capacity-design.md`
2. `mistakes/distributed/high-qps-and-mq-boundaries.md`
3. `sessions/2026-07-28-high-qps-capacity-design.md`
4. `backend/java/thread-pool.md`
5. `interview/java-concurrency-questions.md`

### Spring IOC、Bean 与事务代理

1. `backend/spring/ioc-bean-and-transaction-proxy.md`
2. `interview/mock-records/2026-07-21-pingan-java-backend-prep.md`
3. `projects/settlement-system/transaction-flow-and-reconciliation.md`
4. `interview/real-records/2026-07-28-shokz-senior-java-supply-chain.md`
5. `mistakes/spring/aop-transaction-proxy-boundaries.md`
6. `sessions/2026-08-02-aop-transaction-propagation-java-version-cards.md`

### Java 版本能力卡

1. `backend/java/java-version-capability-cards.md`
2. `sessions/2026-08-02-aop-transaction-propagation-java-version-cards.md`
3. `interview/real-records/2026-07-29-hesheng-innovation-fullstack-engineer.md`

### 真实面试追问与知识边界

1. `interview/real-records/2026-07-28-shokz-senior-java-supply-chain.md`
2. `mistakes/interview/follow-up-boundaries-and-memory-pressure.md`
3. `sessions/2026-07-28-shokz-interview-review.md`
4. `interview/real-records/2026-08-03-pingan-property-backend-individual-group.md`
5. `sessions/2026-08-03-pingan-interview-prep-and-project-reliability.md`
6. `interview/real-records/2026-08-04-suunto-ai-agent-engineer.md`
7. `mistakes/interview/agent-project-implementation-and-expression-gap.md`

### Java Map 与并发容器

1. `backend/java/map-and-concurrent-hash-map.md`
2. `interview/mock-records/2026-07-21-pingan-java-backend-prep.md`

### 结算系统项目深挖与 Java 求职表达

1. `projects/settlement-system/transaction-flow-and-reconciliation.md`
2. `projects/settlement-system/settlement-document-stamping.md`
3. `sessions/2026-07-24-java-ai-resume-and-project-evidence.md`
4. `sessions/2026-07-21-java-resume-project-evidence-and-pingan-breakpoint.md`
5. `sessions/2026-07-21-pingan-java-interview-prep-closeout.md`
6. `interview/mock-records/2026-07-21-pingan-java-backend-prep.md`
7. `backend/spring/ioc-bean-and-transaction-proxy.md`
8. `backend/java/map-and-concurrent-hash-map.md`
9. `backend/mysql/sql-performance-analysis.md`
10. `resume/java-backend-resume.md`
11. `resume/ai-application-resume.md`
12. `sessions/2026-08-03-pingan-interview-prep-and-project-reliability.md`
13. `interview/real-records/2026-08-03-pingan-property-backend-individual-group.md`

### Redis / 分布式锁

1. `backend/redis/distributed-lock.md`
2. `interview/redis-questions.md`
3. `mistakes/distributed/redis-lock.md`
4. `sessions/2026-06-16-redis-distributed-lock.md`
5. `interview/real-records/2026-06-30-ai-agent-rag-backend.md`
6. `sessions/2026-06-30-ai-agent-rag-backend-interview.md`
7. `projects/settlement-system/transaction-flow-and-reconciliation.md`
8. `sessions/2026-08-03-pingan-interview-prep-and-project-reliability.md`

### 批处理任务、Spring Batch 与分布式事务边界

1. `projects/settlement-system/transaction-flow-and-reconciliation.md`
2. `backend/redis/distributed-lock.md`
3. `mistakes/distributed/redis-lock.md`
4. `sessions/2026-08-03-pingan-interview-prep-and-project-reliability.md`
5. `interview/real-records/2026-08-03-pingan-property-backend-individual-group.md`
6. `LEARNING_BACKLOG.md` 中的 `BL-018`、`BL-025`

---

## 历史会话索引

1. `sessions/2026-05-28-http-tcp-request-flow.md`
2. `sessions/2026-05-29-learning-plan-and-doc-consolidation.md`
3. `sessions/2026-05-29-mysql-transaction-first-pass.md`
4. `sessions/2026-06-01-mysql-lock-index-batch-processing.md`
5. `sessions/2026-06-02-mysql-index-explain-lock-path.md`
6. `sessions/2026-06-03-dp-basic.md`
7. `sessions/2026-06-04-dp-knapsack.md`
8. `sessions/2026-06-05-dp-lcs-edit-distance.md`
9. `sessions/2026-06-09-dp-space-optimization-and-review.md`
10. `sessions/2026-06-10-llm-application-interview-preparation.md`
11. `sessions/2026-06-11-llm-application-interview-review.md`
12. `sessions/2026-06-12-thread-pool-task-execution.md`
13. `sessions/2026-06-14-thread-pool-lifecycle-monitoring.md`
14. `sessions/2026-06-15-rag-engineering-governance.md`
15. `sessions/2026-06-16-redis-distributed-lock.md`
16. `sessions/2026-06-30-ai-agent-rag-backend-interview.md`
17. `sessions/2026-07-05-langchain-langgraph-agent-runtime.md`
18. `sessions/2026-07-05-langgraph-runtime-demo.md`
19. `sessions/2026-07-06-create-agent-stategraph-boundary.md`
20. `sessions/2026-07-07-langchain-langgraph-learning-summary.md`
21. `sessions/2026-07-07-langchain-langgraph-official-doc-map-gap.md`
22. `sessions/2026-07-07-huashengtong-ai-application-interview-prep.md`
23. `sessions/2026-07-07-huashengtong-ai-application-interview-review.md`
24. `sessions/2026-07-13-kingdee-ai-application-interview-prep.md`
25. `sessions/2026-07-21-java-resume-project-evidence-and-pingan-breakpoint.md`
26. `sessions/2026-07-21-pingan-java-interview-prep-closeout.md`
27. `sessions/2026-07-24-java-ai-resume-and-project-evidence.md`
28. `sessions/2026-07-28-high-qps-capacity-design.md`
29. `sessions/2026-07-28-shokz-interview-review.md`
30. `sessions/2026-08-02-aop-transaction-propagation-java-version-cards.md`
31. `sessions/2026-08-03-pingan-interview-prep-and-project-reliability.md`
32. `sessions/2026-08-04-suunto-ai-agent-interview-and-sse-review.md`
