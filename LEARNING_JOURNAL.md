# LEARNING JOURNAL

## 作用

这个文件只负责三类信息：

1. 长期学习画像
2. 长期典型误区
3. 已沉淀主题与历史会话索引

它不是当前状态权威文件。

当前恢复学习进度时，只需要优先读取：

1. `START_HERE.md`

---

## 长期学习画像

- 背景：
  - 有 Java 后端开发经验
  - 做过云服务结算系统
  - 也在做 RAG 知识问答系统
- 当前目标：
  - 从“会做业务开发”升级为“能讲清楚机制、能设计系统、能应对后端 / AI Backend 面试”
- 学习偏好：
  - 优先理解本质
  - 优先建立知识结构
  - 优先结合项目和面试表达
  - 不希望直接灌输标准答案

---

## 长期典型误区

### 1. 容易把请求链路只理解到框架内部

容易只想到：

- URL 路由
- Controller 分发
- 业务处理
- 响应返回

后续要持续提醒自己补全：

- DNS
- IP / 端口
- TCP
- 容器层
- 内核协议栈

### 2. 容易把三次握手和 TCP 整体机制混淆

要反复区分：

- 三次握手负责建立连接
- TCP 整体机制负责可靠传输、重传、顺序控制等

### 3. 操作系统基础是长期短板

当前尤其要补：

- 进程和线程
- 阻塞 / 非阻塞
- 同步 / 异步
- 线程与 IO 模型

### 4. 面试表达容易“方向对，但精度不够”

后续要持续训练：

- 术语边界
- 机制表达
- 从“我懂”到“我能清楚讲给面试官听”

### 5. 容易把长期路线和短期冲刺混在一起

长期路线图用于建立完整能力地图。

当前 1 个月目标是面试冲刺，应该优先处理高频短板和项目表达，不平均推进所有 Phase。

### 6. MySQL 日志职责边界容易混淆

已暴露的问题：

- 把 undo log 说成负责事务提交后的持久性
- 把 binlog 说成天然保证主从一致
- 把事务表达成保证业务逻辑一定正确

后续复盘时要反复区分：

- undo log：回滚、MVCC 旧版本
- redo log：崩溃恢复、持久性
- binlog：复制、恢复、订阅
- 本地事务：保证数据库内操作边界，不保证跨系统最终一致

### 7. 容易把快照读、当前读和锁机制混在一起

已暴露的问题：

- 误以为 RR 下普通快照读会加 Next-Key Lock
- 容易把“RR 防幻读”统一理解成靠锁解决
- 对普通 `select`、`select ... for update`、`update` 的语义边界一开始不够清晰

后续复盘时要反复区分：

- 普通快照读：主要依赖 MVCC、Read View、undo log
- 当前读：读取最新版本，并通过锁控制并发修改或插入
- 行锁：控制已有索引记录的并发修改
- 间隙锁 / Next-Key Lock：控制范围当前读下的插入幻影行

### 8. 批处理并发控制容易先想到“停业务修复”

已暴露的问题：

- 对 `PROCESSING` 卡住的初始想法是禁止其他业务 SQL 后扫描恢复
- 容易把恢复卡住任务理解成维护动作，而不是在线补偿机制

后续要强化：

- `PROCESSING` 应理解成带租约的处理中状态
- 需要 `worker_id`、心跳时间、重试次数、超时回收
- 补偿任务应在线恢复，不应依赖停业务
- 超时不等于失败，必须配合幂等重试

### 9. 状态条件更新还不够，需要处理权标识

已暴露的问题：

- 初始回答中只想到 `where status='PROCESSING'`
- 对慢 worker、补偿回收、新 worker 重新抢占后的旧 worker 回写风险认识不够

后续要强化：

- 状态只能说明任务阶段，不能说明谁有资格推进状态
- 长链路异步任务需要 `process_token`、`attempt_id`、`batch_id` 或类似 fencing token
- 成功、失败、心跳回写都要带处理权标识
- 防止过期 worker 覆盖新 worker 的状态

### 10. 索引设计不能只看字段选择性

已暴露的问题：

- 设计联合索引时容易先从字段选择性出发
- 对 worker 分片模型、锁范围、扫描路径和排序稳定性的综合考虑还需要继续训练

后续要强化：

- InnoDB 的锁和索引访问路径强相关
- 锁不是直接加在 `where` 条件上，而是加在实际访问到的索引记录上
- 没有合适索引时，当前读可能扫描并锁住大量记录，表现上接近大范围阻塞
- 分片批处理索引应贴合 `shard_no`、`status`、排序字段和 `limit`
- `created_at` 不唯一，批处理排序应考虑 `created_at, id`

### 11. 索引失效不能机械背结论

已暴露的问题：

- 一开始容易把慢 SQL 归结为“没有索引 / 没命中索引”
- 误以为 `date(created_at)` 可以直接命中普通 `created_at` 索引
- 容易把 `IN`、范围条件、非等值条件简单归类为索引失效
- 对 `EXPLAIN` 的理解目前能看字段，但还需要训练从执行计划反推访问路径

后续要强化：

- 索引失效不是索引完全不能用，而是不能充分利用索引有序结构减少扫描、排序和回表
- 普通 B+ 树索引维护的是列原始值，不维护函数计算结果
- 联合索引前导列没有等值固定时，后续排序字段通常不能保证全局有序
- 多状态条件比 `status <> 'DONE'` 语义更明确，但仍可能破坏跨状态全局排序
- 慢 SQL 排查要同时看 `type`、`key`、`rows`、`Extra`、回表和业务访问路径

### 12. 外部调用不确定状态不能简单重试

已暴露的问题：

- 对 ERP 推送成功但本地未更新的场景，初始容易先想到超时后复原为 `INIT`
- 容易把幂等键当成唯一兜底，而不是配合本地调用记录和查询确认

后续要强化：

- 本地事务不能覆盖跨系统一致性，外部调用和本地状态更新之间天然可能出现不确定状态
- `PROCESSING` 超时后不能盲目重推，应先查外部调用记录
- 明确成功则补写本地 `DONE`，明确失败再重试，不确定时优先查询外部系统
- 幂等键和 payload hash 用于重复请求一致性校验
- 对账是最终兜底，不是替代主流程的正常路径

### 13. DP 状态定义容易和题目目标错配

已暴露的问题：

- 爬楼梯方法数题，一开始把 `dp[i]` 定义成“最少步数”
- 最小花费爬楼梯中混淆 `cost[0]`、`dp[0]`、台阶 0、位置 0
- LIS 中一度把能否接上的比较对象说成 `dp`，实际应比较 `nums`
- 对 `dp[n-1]` 和 `max(dp)` 的判断需要继续巩固

后续要强化：

- 先问题目目标，再定义状态
- 状态定义必须同时表达子问题答案，并保留转移所需信息
- 方法数通常相加，最小代价取 `min`，最大收益取 `max`
- `dp[i] = 考虑 0..i 的全局最优` 时，答案通常是 `dp[n-1]`
- `dp[i] = 以 nums[i] 结尾的局部最优` 时，答案通常是 `max(dp)`
- 不要用“哲学思想”解释不能背公式，要落到状态定义、边界和转移一致性

### 14. 背包 DP 容易混淆物品次数和题目目标

已暴露的问题：

- 零钱兑换 II 中一开始把 `dp[0]` 说成 0，没有意识到它是方案数转移种子
- 组合数题一开始尝试按“最后一个硬币是谁”写转移，容易把组合数算成排列数
- 完全背包二维转移一开始误选 `dp[i-1][j-coin]`，这会变成 0/1 背包
- 完全背包可达性中一度忘记旧的 `true` 状态会被保留
- 背包分类时容易只看循环形式，而没有先判断“物品使用次数 + 题目目标”
- 背包分类小测中，完全背包 + 最小值仍把 `dp[0]` 误写成 1
- 零钱兑换 I 的最终判断一度写成 `dp[i]`，应明确检查目标状态 `dp[amount]`

后续要强化：

- 0/1 背包容量倒序：防止当前物品重复使用
- 完全背包容量正序：允许当前物品重复使用
- 组合数外层遍历物品：固定物品顺序，避免排列重复
- `dp[0]` 必须从状态定义推出：数量为 0、方案种子为 1、可达性为 true
- 每道背包题先说清“0/1 还是完全背包 + 可达性 / 方案数 / 最小值 / 最大值”
- 分类稳定后，继续训练完整题表达：状态定义、边界、转移、循环方向、复杂度和返回值

### 15. 二维字符串 DP 容易混淆前缀长度和字符下标

已暴露的问题：

- LCS 手算时把 `dp[0][0]` 当成两个第 0 个字符的比较结果
- 编辑距离中把插入后的字符串实际长度误认为新的 DP 下标
- 手写完整转移时把字符相等和不相等的分支写反
- 抄写三个相邻状态时出现重复下标，结果碰巧未受影响

后续要强化：

- `dp[i][j]` 描述的是两个原始字符串前缀的子问题，不是操作后字符串的实时长度
- 前缀长度 `i` 对应末尾字符下标 `i-1`
- LCS 字符不等时是舍弃一个末尾字符后取最大值
- 编辑距离中上方是删除、左方是插入、左上是替换
- 写完公式后用语义检查：相等不操作，不等才加 1
- 编辑距离一维压缩中，更新前 `dp[j]` 是上方，更新后 `dp[j-1]` 是左方，`prev` 是左上
- 每列先用 `temp` 保存上方旧值，更新后再执行 `prev=temp`

### 16. 容易把 DP 通用分析缩窄成背包分类

已暴露的问题：

- 回答“如何分析一道 DP”时，主要罗列了 0/1、完全背包以及可达性、方案数、最值公式
- 打家劫舍中混用了“必须偷第 i 间房”和“考虑前 i 间房”两套状态的边界与答案

后续要强化：

- 先回答题目目标、子问题、状态保留信息和最后一步选择
- 状态定义、转移、边界、遍历顺序和答案位置必须属于同一模型
- 背包分类只是“从物品中选择”这一类 DP 的后续判断，不是所有 DP 的统一入口
- LIS 和最大子数组和通过“以 i 结尾”分别保留结尾元素和连续性

### 17. RAG 项目表达容易堆功能，缺少问题分层

已暴露的问题：

- 自我介绍容易用“我觉得能够胜任”代替项目和能力证据
- RAG 项目介绍容易罗列文档集成、向量化、模型调用等功能，没有按业务问题、架构、职责、难点和指标组织
- 一开始把 `Top3` 扩大为 `Top5` 当成准确率问题已经得到解决
- 评价 RAG 时容易混合检索指标、生成指标和系统容量指标
- 检索融合和 Chunk 参数容易先给经验结论，没有先说明标注测试集、指标和实验依据

后续要强化：

- 项目表达使用“业务问题 -> 两条核心链路 -> 技术架构 -> 个人职责 -> 难点 -> 指标和优化”结构
- `TopK` 变大只是召回与噪声之间的权衡，不等于排序和生成问题已经解决
- 检索层看 `Recall@K`、MRR、NDCG，生成层看正确性、忠实度、引用和拒答，工程层看延迟、吞吐、错误率和成本
- BM25 与向量分数不能直接比较，需要归一化加权、RRF 或 Rerank
- 明确区分已实现能力和 Parent-Child Retrieval、Rerank 等后续优化方向

### 18. AI 应用岗位需要明确区分理解和生产实践

已暴露的问题：

- 当前缺少 Multi-Agent、MCP、A2A、LangGraph、Flink、Hive、K8s 和推理优化的生产实践
- 面对跨度很大的 JD，容易因为无法完全匹配而否定已有后端和 RAG 积累

后续要强化：

- 不虚构生产经验，使用“当前边界 -> 已理解的问题 -> 可迁移经验 -> 落地验证方案”回答
- 结算系统中的任务拆分、状态机、MQ、幂等、补偿和多节点协作可以迁移为 Agent 系统可靠性能力
- 单次临时面试先作为市场验证，不立即改变主学习路线
- 等真实面试问题和反馈归档后，再判断是否提高 Multi-Agent 和 RAG 工程化优先级

### 19. RAG 面试中容易混淆召回、融合、重排和生成

已暴露的问题：

- 把归一化加权融合称为 Rerank
- 把 Prompt、模型温度和模型选型放进“混合检索优化”
- 把 `Recall@K` 说成正确文档的平均排名
- 把分级相关性评分说成 MRR

后续要强化：

- 全文检索和向量检索负责候选召回
- 归一化加权或 RRF 负责两路结果融合
- Cross-Encoder Rerank 只对已召回候选重新排序
- `Recall@K` 看是否召回，MRR 看第一个相关结果排名，NDCG 看分级相关性和整体排序
- Prompt 和生成模型优化属于生成层，不能和检索层混答

### 20. Agent 问题容易回答成模型选型

已暴露的问题：

- 面试官询问用户问答如何嵌入 Agent 和 AI Pipeline 时，回答转向本地 Qwen 与 DeepSeek API 的选型
- 初始判断 Agent 时把工具数量当成关键条件

后续要强化：

- 当前项目是固定 RAG Pipeline，步骤由代码预定义，LLM 只负责生成
- Agent 的判断标准是模型是否能根据 State 动态决策工具、参数、重试和终止
- 工具数量不是根本标准，一个工具也可以形成基础 Agent 闭环
- 没有 Agent 生产经验时，先声明边界，再说明可迁移的状态机、幂等、补偿和任务编排能力

### 21. 项目架构与性能瓶颈需要证据链

已暴露的问题：

- 结算系统回答中业务场景、系统架构、技术栈和性能优化混在一起
- 多次把“技术栈”口误成“技术债”
- 从批处理耗时高和 JDBC 调用耗时高直接跳到“数据库是瓶颈”

后续要强化：

- 架构回答按系统定位、业务场景、上下游、核心数据流、可靠性和规模组织
- 批处理超时先分解阶段耗时，再看 SQL 次数、单次耗时、扫描行数、锁等待、连接等待、CPU 和 IO
- “单条 SQL 不慢但累计访问耗时高”不等于数据库算力不足，需要继续定位访问模型和总工作量

### 22. 线程池容易把线程数量、队列容量和任务可靠性混在一起

已暴露的问题：

- 初始认为核心线程满后会先扩容到最大线程数
- 认为大队列因为线程较少而内存风险更低
- 把 `CallerRunsPolicy` 理解为增加新线程或复用两个线程池
- 认为 `newFixedThreadPool` 会无限创建线程
- 把批次 `LIMIT` 当成防止任务积压的反压机制
- 初始不了解 P95/P99、高低水位和任务限流
- 误以为 `keepAliveTime` 默认控制核心线程
- 不清楚 `ThreadFactory`、Worker 和业务 `Runnable` 的调用关系
- 误以为不调用 `Future.get()` 时异常没有被保存
- 吞掉 `InterruptedException` 后仍以为下一轮可以看到中断标志
- 把 P99 耗时当成生产和消费速率
- 一度认为线程数超过 CPU 核数一定无效

后续要强化：

- 固定提交顺序：核心线程、队列、非核心线程、拒绝
- 队列中的任务对象及其引用是重要内存风险
- 拒绝策略决定过载压力由谁承担，长任务不能回退到 Tomcat 线程
- 线程池并发要受数据库连接池、模型服务和其他下游容量约束
- 状态表解决持久化和恢复，高低水位或许可才负责阶段反压
- 租约、心跳、Token、幂等和重试分别解决不同可靠性问题
- `keepAliveTime` 默认只控制核心线程数以上的空闲 Worker
- `ThreadFactory` 创建和配置工作线程，业务任务由 `execute/submit` 提交
- `execute` 的未捕获异常可能到达线程级 Handler，`submit` 的异常保存在 `Future`
- 中断是协作式协议，阻塞方法抛出 `InterruptedException` 时可能清除中断标志
- 判断积压要比较新增速率和完成速率，P95/P99 用于观察耗时分布
- IO 密集线程数可以超过 CPU 核数，但最终受连接池和下游容量约束
- 下一步用 1 分钟口述验收线程池主线，再切回结算系统项目表达

### 23. RAG 工程化容易从单点优化扩展成无边界设计

本轮新增理解：

- 线程池大于连接池时，多余线程可能只是在等待连接，CPU 低不代表还能继续增加并发
- 外部 Embedding 调用不应放在持有数据库连接的长事务中
- Embedding 模型版本、维度和 Chunk 策略需要进入任务快照和向量元数据
- 向量模型升级更适合蓝绿重建、双写、完整性校验、灰度和回滚
- 离线 `Recall@K` 提升不代表线上回答一定改善，需要逐层回放召回、融合、重排、Prompt 和生成
- 权限过滤必须尽量发生在检索前，TopK 应是授权集合中的 TopK
- 多分区召回后需要统一去重和 Rerank，不能机械平均分配最终名额
- 版本规则需要按业务事件时间和有效期检索，必要时执行多阶段检索
- MMR 用于在相关性和重复度之间权衡，但业务条件和相邻证据完整性优先
- 规则压缩必须保留条件关系、否定词、时间口径和证明要求

仍需警惕：

- 容易在一个 RAG 追问上连续扩展到权限、版本、法规和规则引擎，偏离 Java 后端冲刺主线
- 理解了设计原则，不等于当前项目已经实际实现权限分区、蓝绿向量索引、MMR 或线上追踪
- 后续面试表达必须明确区分“当前实现”和“生产化设计方案”

### 24. Redis 分布式锁不能替代状态机和幂等

本轮新增理解：

- `synchronized` 只能控制单 JVM 内线程，不能控制多实例并发
- `SET key value NX PX` 中 `NX` 负责不存在才写入，`PX` 负责毫秒级过期
- `SETNX` 和 `EXPIRE` 分开执行存在原子性窗口
- 解锁不能直接 `DEL`，必须用 Lua 原子校验 value 再删除
- 看门狗用于续期，但只能证明续期逻辑运行，不能证明业务任务健康
- 续期也要校验 value，防止旧 Worker 给新 Worker 的锁续期
- Redis 锁丢失后应停止新的外部副作用，并依赖数据库 Token 条件回写兜底
- `process_token` 解决当前处理权，不能作为 ERP 业务幂等键
- ERP 超时是结果不确定，不应直接标记失败或换新幂等键重试
- 数据库条件更新和状态机应作为任务处理权主依据，Redis 锁只作为辅助互斥

仍需警惕：

- 容易把“加了 Redis 锁”误认为任务绝对只处理一次
- 容易混淆锁健康、Worker 健康和业务副作用是否成功
- 后续还要学习 Redis 基础、缓存问题、RedLock 争议和缓存一致性

---

## 已沉淀主题索引

### 网络请求链路

1. `fundamentals/network/http-tcp-request-flow.md`
2. `interview/computer-fundamentals-questions.md`
3. `mistakes/network/request-flow.md`

### 学习计划和文档口径

1. `LEARNING_ROADMAP.md`
2. `INTERVIEW_SPRINT_30_DAYS.md`
3. `START_HERE.md`

### MySQL 事务

1. `backend/mysql/transaction.md`
2. `interview/mysql-questions.md`
3. `mistakes/database/transaction.md`

### MySQL 锁、批处理和索引访问路径

1. `backend/mysql/lock-and-batch-processing.md`
2. `interview/mysql-questions.md`
3. `sessions/2026-06-01-mysql-lock-index-batch-processing.md`
4. `sessions/2026-06-02-mysql-index-explain-lock-path.md`

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

### Java 线程池与后台任务

1. `backend/java/thread-pool.md`
2. `interview/java-concurrency-questions.md`
3. `mistakes/concurrency/thread-pool.md`
4. `sessions/2026-06-12-thread-pool-task-execution.md`
5. `sessions/2026-06-14-thread-pool-lifecycle-monitoring.md`

### Redis / 分布式锁

1. `backend/redis/distributed-lock.md`
2. `interview/redis-questions.md`
3. `mistakes/distributed/redis-lock.md`
4. `sessions/2026-06-16-redis-distributed-lock.md`

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
