# LEARNING ROADMAP

## 0. 这个计划的目的

这个学习计划不是为了单纯刷八股，也不是为了堆题量。

目标是帮助我从：

> 会做业务开发的 Java 后端

逐步升级为：

> 能理解后端系统本质、能讲清楚技术机制、能通过后端面试、能向 AI Backend / AI 应用工程方向发展的工程师。

这个计划需要和 `AGENTS.md` 一起使用。

* `AGENTS.md` 规定你如何与我协作。
* `LEARNING_ROADMAP.md` 规定我们按什么阶段推进学习。
* `INTERVIEW_SPRINT_30_DAYS.md` 规定当前 1 个月面试冲刺如何执行。
* 每次学习开始前，请先读取这两个文件。
* 每次学习结束后，请帮我更新当前阶段进展、遗留问题和下一步任务。

当前执行口径：

1. `LEARNING_ROADMAP.md` 是长期能力地图。
2. `INTERVIEW_SPRINT_30_DAYS.md` 是当前 1 个月执行计划。
3. 如果两者优先级冲突，本月先执行冲刺计划，长期 Roadmap 不废弃。

---

# 1. 总体推进原则

## 1.1 不追求一次学完

每个知识点分三层掌握：

1. 听懂：知道它大概是什么。
2. 讲清：能用自己的话解释。
3. 应用：能联系项目、面试、代码或系统设计。

只有达到第 2 层以上，才算当前阶段基本通过。

---

## 1.2 不允许只学“答案”

每个核心知识点都必须回答：

1. 它为什么出现？
2. 它解决什么问题？
3. 如果没有它，会发生什么？
4. 它的核心机制是什么？
5. 它有什么代价和边界？
6. 面试官会怎么问？
7. 我如何结合自己的项目回答？

---

## 1.3 学习节奏

默认按 7 个阶段推进。

如果我时间充足，可以加速。

如果我理解困难，可以放慢。

不要为了赶进度牺牲理解质量。

---

# 2. 进度状态规则

每个任务都使用下面的状态：

* TODO：还没开始
* DOING：正在学习
* REVIEW：已经学过，但需要复盘
* DONE：已经能讲清楚，并能应对面试追问
* BLOCKED：卡住，需要重新拆解

每次学习结束后，请更新对应任务状态。

---

# 3. 每次学习的固定流程

每次启动 Codex 后，请按下面流程推进。

## 3.1 开始前

你需要先问我：

1. 今天可用时间是多少？
2. 今天想学哪个阶段或哪个知识点？
3. 是偏理解、偏面试，还是偏代码练习？
4. 上次遗留问题是什么？

如果我没有明确选择，请优先根据当前 Roadmap 推荐最该推进的任务。

---

## 3.2 学习中

你需要按照以下方式陪我学习：

1. 先解释本质，不要直接背答案。
2. 然后用简单例子说明。
3. 再联系我的项目经验。
4. 再整理成面试回答。
5. 最后用 3 到 5 个追问检查我是否真的理解。

---

## 3.3 结束时

每次学习结束，请输出：

1. 今日学习内容
2. 我真正掌握的部分
3. 我还模糊的部分
4. 需要进入 mistakes/ 的错误
5. 下一次建议学习内容
6. 是否需要更新 Roadmap 状态

---

# 4. 阶段总览

## Phase 0：建立学习仓库和协作机制

目标：

建立一个长期可维护的 AI 后端学习仓库。

重点不是学技术，而是建立学习系统。

目录建议：

```text
ai-backend-learning/
├── AGENTS.md
├── LEARNING_ROADMAP.md
├── README.md
├── START_HERE.md
├── LEARNING_JOURNAL.md
├── INTERVIEW_SPRINT_30_DAYS.md
├── fundamentals/
│   ├── algorithm/
│   ├── data-structure/
│   ├── os/
│   ├── network/
│   └── database/
├── backend/
│   ├── java/
│   ├── spring/
│   ├── mysql/
│   ├── redis/
│   ├── mq/
│   ├── jvm/
│   └── distributed-system/
├── projects/
│   ├── settlement-system/
│   └── rag-system/
├── interview/
│   ├── self-introduction.md
│   ├── project-story.md
│   ├── mysql-questions.md
│   ├── redis-questions.md
│   ├── mq-questions.md
│   └── algorithm-questions.md
├── prompts/
│   ├── dp-coach.md
│   ├── mock-interview.md
│   ├── project-deep-dive.md
│   └── backend-review.md
├── sessions/
├── mistakes/
│   ├── algorithm/
│   ├── database/
│   ├── concurrency/
│   └── interview/
└── weekly-review/
```

阶段验收标准：

* 仓库结构建立完成
* AGENTS.md 完成
* LEARNING_ROADMAP.md 完成
* 恢复学习状态机制建立完成
* 能够用 Codex 开始一次结构化学习

状态：

* Phase 0：DONE

完成依据：

1. 仓库已经形成 `START_HERE.md` 单入口恢复机制。
2. `AGENTS.md`、长期 Roadmap、30 天冲刺计划和学习日志职责已经拆分。
3. 已建立主笔记、面试问答、mistakes、sessions 的实际协作闭环。
4. 已完成多次结构化学习、状态恢复、进度更新和 GitHub 提交。

---

# 5. Phase 1：计算机基础

优先级：高

原因：

如果计算机基础薄弱，后面学数据库、并发、网络、分布式时很容易变成背结论。

本阶段目标：

让我先补齐操作系统、计算机网络、数据结构这些底层知识，形成后续后端学习的共同语言。

---

## 5.1 数据结构基础

任务状态：TODO

必须掌握：

1. 数组、链表、栈、队列分别解决什么问题
2. 哈希表为什么快，代价是什么
3. 树和堆分别适合什么场景
4. 图的基本表示方法
5. 时间复杂度和空间复杂度如何分析
6. 常见结构在真实工程中的使用场景

阶段输出文件：

```text
fundamentals/data-structure/basic.md
mistakes/algorithm/data-structure.md
```

验收标准：

我需要能回答：

1. 数组和链表的本质区别是什么？
2. 哈希表为什么能做到平均 O(1)？
3. 栈和队列在工程里分别常见在哪？
4. 为什么复杂度分析不是纸上谈兵？

---

## 5.2 操作系统基础

任务状态：TODO

必须掌握：

1. 进程和线程的区别
2. 用户态和内核态
3. 上下文切换为什么昂贵
4. 内存管理、虚拟内存、页表的基本概念
5. 文件 IO 和网络 IO 的基本路径
6. 阻塞、非阻塞、同步、异步

阶段输出文件：

```text
fundamentals/os/process-thread.md
fundamentals/os/memory.md
fundamentals/os/io-model.md
mistakes/concurrency/os-basics.md
```

验收标准：

我需要能回答：

1. 进程和线程分别适合解决什么问题？
2. 为什么线程切换不是免费的？
3. 用户态和内核态切换在系统调用里怎么体现？
4. Java 里的线程池问题为什么本质上和 OS 调度有关？

---

## 5.3 计算机网络基础

任务状态：REVIEW

必须掌握：

1. 为什么需要分层
2. TCP 和 UDP 的区别
3. TCP 三次握手和四次挥手
4. TCP 可靠传输依赖什么机制
5. HTTP/1.1、HTTP/2 的关键差异
6. HTTPS 为什么安全
7. 从浏览器发起请求到服务端响应的大致链路

阶段输出文件：

```text
fundamentals/network/tcp.md
fundamentals/network/http.md
mistakes/network/request-link.md
```

验收标准：

我需要能回答：

1. 为什么连接建立需要三次握手？
2. TCP 如何保证可靠传输？
3. HTTP 和 TCP 分别处于什么层，解决什么问题？
4. 一个 HTTP 请求从客户端到服务端大概经历了什么？

---

## 5.4 计算机基础与后端工程的连接

任务状态：DOING

必须掌握：

1. 网络基础如何支撑 API、RPC、MQ 理解
2. OS 基础如何支撑并发、线程池、锁、IO 模型理解
3. 数据结构如何支撑 Redis、数据库索引、算法理解
4. 为什么后端面试总会反复追问这些底层知识

阶段输出文件：

```text
fundamentals/README.md
interview/computer-fundamentals-questions.md
```

验收标准：

我需要能回答：

1. 为什么计算机基础不是和后端开发分离的知识？
2. 线程池、Redis、MySQL、MQ 背后分别依赖了哪些基础概念？
3. 面试官问基础题时，我如何把它和项目经验连起来？

---

# 6. Phase 2：数据库核心基础

优先级：最高

原因：

我在面试中暴露出数据库事务理解薄弱。

本阶段目标：

让我能够系统理解数据库事务、索引、锁、MVCC，并能结合自己的结算系统回答面试问题。

---

## 6.1 数据库事务

任务状态：REVIEW

必须掌握：

1. 事务为什么存在
2. ACID 的本质
3. 原子性、一致性、隔离性、持久性分别解决什么问题
4. 脏读、不可重复读、幻读是什么
5. 四种隔离级别是什么
6. MySQL 默认隔离级别
7. MVCC 为什么出现
8. undo log 和 redo log 的作用
9. 事务和业务幂等、状态机、补偿的关系

必须联系我的项目：

* 云服务结算系统里的 ERP 推送
* 结算状态流转
* 异常回滚
* 重跑补偿
* 幂等控制

阶段输出文件：

```text
backend/mysql/transaction.md
interview/mysql-questions.md
mistakes/database/transaction.md
```

验收标准：

我需要能回答：

1. 什么是事务？
2. ACID 分别是什么意思？
3. 什么是脏读、不可重复读、幻读？
4. 为什么需要隔离级别？
5. MVCC 解决了什么问题？
6. 事务和分布式一致性有什么区别？
7. 你项目里哪些地方体现了事务思想？

---

## 6.2 索引和 B+ 树

任务状态：REVIEW

必须掌握：

1. 索引为什么出现
2. B+ 树为什么适合数据库索引
3. 聚簇索引和非聚簇索引
4. 覆盖索引
5. 最左前缀原则
6. 索引失效场景
7. 回表是什么
8. 慢查询如何分析

阶段输出文件：

```text
backend/mysql/index.md
interview/mysql-questions.md
mistakes/database/index.md
```

验收标准：

我需要能回答：

1. 为什么数据库不用普通二叉树？
2. 为什么 MySQL 常用 B+ 树？
3. 什么情况下索引会失效？
4. 联合索引怎么设计？
5. 如何优化一条慢 SQL？

---

## 6.3 数据库锁

任务状态：REVIEW

必须掌握：

1. 共享锁和排他锁
2. 行锁和表锁
3. 间隙锁
4. Next-Key Lock
5. 死锁
6. 乐观锁和悲观锁
7. 数据库锁和 Redis 分布式锁的区别

阶段输出文件：

```text
backend/mysql/lock.md
interview/mysql-questions.md
mistakes/database/lock.md
```

验收标准：

我需要能回答：

1. MySQL 有哪些锁？
2. 什么情况下会死锁？
3. 如何排查死锁？
4. 乐观锁和悲观锁怎么选？
5. 为什么你的项目用了 Redis 锁，而不是只用数据库锁？

---

# 7. Phase 3：算法基础，重点攻克动态规划

优先级：最高

原因：

我在面试中遇到动态规划题没有做出来。

本阶段目标：

不追求刷很多题，而是建立算法题的思维框架。

---

## 7.1 动态规划入门

任务状态：REVIEW

必须掌握：

1. 什么问题适合动态规划
2. 什么是重叠子问题
3. 什么是最优子结构
4. 状态定义怎么来
5. 状态转移怎么推
6. 边界条件怎么找
7. 递归、记忆化搜索、动态规划表格之间的关系

阶段输出文件：

```text
fundamentals/algorithm/dp-basic.md
mistakes/algorithm/dp.md
```

验收标准：

我需要能用人话解释：

1. DP 的本质是什么？
2. 为什么编辑距离可以用 DP？
3. dp[i][j] 到底代表什么？
4. 为什么状态转移是从前面的子问题推出来的？

---

## 7.2 编辑距离

任务状态：REVIEW

这是我已经接触过、但需要彻底吃透的一题。

必须掌握：

1. 插入、删除、替换分别意味着什么
2. dp[i][j] 的含义
3. 为什么从 dp[i-1][j]、dp[i][j-1]、dp[i-1][j-1] 转移
4. 为什么不是简单贪心
5. 如何画表格理解

阶段输出文件：

```text
fundamentals/algorithm/edit-distance.md
mistakes/algorithm/edit-distance.md
```

验收标准：

我需要能独立讲清楚编辑距离的状态定义和转移逻辑。

---

## 7.3 滑动窗口

任务状态：TODO

必须掌握：

1. 滑动窗口解决什么问题
2. 左右指针分别代表什么
3. 什么时候扩大窗口
4. 什么时候收缩窗口
5. valid 变量的意义
6. 异位词问题为什么适合滑动窗口

阶段输出文件：

```text
fundamentals/algorithm/sliding-window.md
mistakes/algorithm/sliding-window.md
```

验收标准：

我需要能独立写出：

1. 找到字符串中所有字母异位词
2. 最小覆盖子串
3. 无重复字符最长子串

---

## 7.4 二分查找

任务状态：TODO

必须掌握：

1. 二分查找的本质
2. 为什么不是只能查数组
3. 左闭右闭、左闭右开区别
4. 搜索边界
5. 在答案空间上二分

阶段输出文件：

```text
fundamentals/algorithm/binary-search.md
mistakes/algorithm/binary-search.md
```

验收标准：

我需要能回答：

1. 二分的本质是什么？
2. 怎么找左边界？
3. 怎么找右边界？
4. 什么题可以在答案空间上二分？

---

# 8. Phase 4：Java、JVM、并发、Spring

优先级：高

目标：

补齐 Java 后端工程师的核心基础。

---

## 8.1 Java 并发基础

任务状态：DOING

必须掌握：

1. 线程和进程
2. synchronized
3. volatile
4. CAS
5. AQS
6. Lock
7. ThreadLocal
8. 线程池
9. 并发安全问题

阶段输出文件：

```text
backend/java/concurrency.md
backend/java/thread-pool.md
interview/java-concurrency-questions.md
```

验收标准：

我需要能回答：

1. synchronized 和 Lock 的区别
2. volatile 能保证什么，不能保证什么
3. CAS 有什么问题
4. 线程池核心参数是什么
5. 线程池如何用于我的 RAG 索引任务

---

## 8.2 JVM

任务状态：TODO

必须掌握：

1. JVM 内存结构
2. 堆、栈、方法区
3. GC Roots
4. 垃圾回收算法
5. 常见垃圾回收器
6. OOM 排查思路
7. Full GC 问题

阶段输出文件：

```text
backend/jvm/jvm-memory.md
backend/jvm/gc.md
interview/jvm-questions.md
```

验收标准：

我需要能回答：

1. JVM 内存区域有哪些？
2. 什么对象会被回收？
3. Minor GC 和 Full GC 区别？
4. 如何排查 OOM？

---

## 8.3 Spring / Spring Boot

任务状态：DOING

必须掌握：

1. IOC
2. AOP
3. Bean 生命周期
4. Spring MVC 请求链路
5. Filter 和 Interceptor
6. 自动装配
7. 事务注解 @Transactional
8. 全局异常处理

必须联系我的 RAG 项目：

* DocumentController
* GlobalExceptionHandler
* RequestIdFilter
* ThreadPoolTaskExecutor
* Flyway
* API 分层设计

阶段输出文件：

```text
backend/spring/spring-core.md
backend/spring/spring-mvc.md
backend/spring/spring-boot.md
interview/spring-questions.md
```

验收标准：

我需要能回答：

1. IOC 是什么？
2. AOP 为什么能实现？
3. Bean 生命周期是什么？
4. 一个 HTTP 请求进入 Spring MVC 后发生什么？
5. Filter 和 Interceptor 有什么区别？
6. @Transactional 什么时候失效？

---

# 9. Phase 5：Redis、MQ、分布式系统

优先级：高

目标：

把我的项目经验和分布式理论连接起来。

---

## 9.1 Redis

任务状态：TODO

必须掌握：

1. Redis 为什么快
2. Redis 数据结构
3. 持久化 RDB / AOF
4. 缓存穿透、击穿、雪崩
5. Redis 分布式锁
6. setnx 的问题
7. RedLock 的争议
8. Redis 和数据库一致性

必须联系我的项目：

* 多节点结算任务抢占
* Redis 分布式锁
* 状态机兜底
* 幂等控制

阶段输出文件：

```text
backend/redis/redis-core.md
backend/redis/distributed-lock.md
interview/redis-questions.md
```

验收标准：

我需要能回答：

1. Redis 为什么快？
2. Redis 分布式锁怎么实现？
3. 为什么不能只靠 Redis 锁保证一致性？
4. 缓存和数据库如何保持一致？
5. 缓存雪崩、击穿、穿透怎么解决？

---

## 9.2 MQ

任务状态：TODO

必须掌握：

1. MQ 为什么出现
2. 解耦、削峰、异步
3. 消息可靠性
4. 重复消费
5. 幂等消费
6. 顺序消息
7. 消息积压
8. 最终一致性

必须联系我的项目：

* ERP 回写
* MQ 消费
* posting result 回写
* 重试与补偿

阶段输出文件：

```text
backend/mq/mq-core.md
backend/mq/reliable-message.md
interview/mq-questions.md
```

验收标准：

我需要能回答：

1. 为什么要用 MQ？
2. 如何保证消息不丢？
3. 如何处理重复消费？
4. MQ 如何实现最终一致性？
5. 消息积压怎么处理？

---

## 9.3 分布式系统基础

任务状态：DOING

必须掌握：

1. 分布式系统为什么复杂
2. CAP
3. BASE
4. 一致性模型
5. 幂等
6. 分布式事务
7. TCC / Saga / 本地消息表
8. 任务分片
9. 分布式调度

阶段输出文件：

```text
backend/distributed-system/core.md
backend/distributed-system/idempotency.md
backend/distributed-system/consistency.md
interview/distributed-questions.md
```

验收标准：

我需要能回答：

1. 什么是分布式一致性？
2. 什么是最终一致性？
3. 幂等为什么重要？
4. 你的结算系统如何保证失败后可恢复？
5. 分布式事务有哪些方案？

---

# 10. Phase 6：项目深挖与面试表达

优先级：最高

目标：

把我的真实项目经历包装成能打动面试官的工程表达。

---

## 10.1 云服务结算系统项目复盘

任务状态：DOING

必须整理：

1. 项目背景
2. 业务流程
3. 系统架构
4. 我的职责
5. 核心难点
6. 技术方案
7. 数据一致性设计
8. 幂等设计
9. 补偿和重跑设计
10. 性能优化
11. 可观测性
12. 项目成果
13. 面试官可能追问

阶段输出文件：

```text
projects/settlement-system/project-overview.md
projects/settlement-system/idempotency.md
projects/settlement-system/consistency.md
projects/settlement-system/batch-processing.md
interview/project-story.md
```

验收标准：

我需要能用 3 个版本讲这个项目：

1. 30 秒简历版
2. 2 分钟面试介绍版
3. 10 分钟深挖版

---

## 10.2 RAG 知识问答系统项目复盘

任务状态：TODO

必须整理：

1. 项目目标
2. 系统架构
3. 文档上传
4. 解析
5. chunk
6. embedding
7. pgvector
8. TopK 检索
9. prompt 拼接
10. LLM 回答
11. 引用来源
12. 问答记录
13. 异步索引任务
14. 错误处理和重试
15. 后续优化方向

阶段输出文件：

```text
projects/rag-system/project-overview.md
projects/rag-system/indexing-pipeline.md
projects/rag-system/retrieval.md
projects/rag-system/qa-api.md
interview/rag-project-story.md
```

验收标准：

我需要能回答：

1. 什么是 RAG？
2. 为什么 RAG 更可控？
3. 为什么需要 chunk？
4. 为什么用向量数据库？
5. TopK 检索有什么问题？
6. 如何评估回答质量？
7. 如何把这个项目写进简历？

---

# 11. Phase 7：模拟面试与查漏补缺

优先级：最高

目标：

把知识转化成面试表现。

---

## 11.1 八股模拟面试

任务状态：TODO

每轮模拟面试包括：

1. MySQL
2. Redis
3. MQ
4. Java 并发
5. JVM
6. Spring
7. 分布式
8. 项目深挖

输出文件：

```text
interview/real-records/
interview/mock-records/
mistakes/interview/
```

验收标准：

每次模拟后要记录：

1. 哪些问题没答出来
2. 哪些问题答得不结构化
3. 哪些地方暴露了知识漏洞
4. 更好的回答方式是什么
5. 下次复习任务是什么

---

## 11.2 算法模拟面试

任务状态：TODO

每轮模拟包括：

1. 读题
2. 复述题意
3. 讲思路
4. 写代码
5. 自测样例
6. 复杂度分析
7. 复盘卡点

优先题型：

1. 滑动窗口
2. 哈希表
3. 双指针
4. 二分
5. 动态规划
6. 树
7. 图

验收标准：

我需要能在不看答案的情况下完成中等难度算法题，并能讲清楚思路。

---

# 12. 每周复盘机制

每周至少生成一个复盘文件。

路径：

```text
weekly-review/week-N.md
```

每周复盘模板：

```text
# Week N Review

## 1. 本周学习内容

## 2. 已掌握内容

## 3. 仍然模糊的内容

## 4. 本周暴露的问题

## 5. 进入 mistakes/ 的问题

## 6. 项目表达提升

## 7. 下周重点

## 8. 当前阶段进度

Phase 0：
Phase 1：
Phase 2：
Phase 3：
Phase 4：
Phase 5：
Phase 6：
Phase 7：
```

---

# 13. 总进度看板

更新时间：2026-06-12

进度不是按文件数量计算，而是综合判断：

1. 是否完成机制学习
2. 是否有自己的复述和追问记录
3. 是否形成主笔记、面试表达和 mistakes 闭环
4. 是否达到本阶段验收标准

| Phase | 状态 | 进度 | 当前判断 |
|---|---|---:|---|
| Phase 0：学习仓库和协作机制 | DONE | 100% | 单入口恢复、文档分工、会话归档和 Git 协作已经实际运行 |
| Phase 1：计算机基础 | DOING | 20% | 请求链路已完成第一轮；数据结构、OS、完整 TCP/HTTP 基础仍缺失 |
| Phase 2：数据库核心基础 | REVIEW | 65% | 事务、MVCC、索引、锁和批处理项目化训练已完成第一轮，仍需补死锁、锁分类和慢 SQL 实战 |
| Phase 3：算法基础与动态规划 | DOING | 45% | DP 已完成四轮训练；表达精度仍需巩固，滑动窗口和二分尚未开始 |
| Phase 4：Java / JVM / 并发 / Spring | DOING | 18% | 已学习 Spring MVC 请求链路、Tomcat 线程模型，以及线程池容量边界和后台任务可靠执行第一轮；锁、CAS、AQS、Spring 核心和 JVM 未展开 |
| Phase 5：Redis / MQ / 分布式 | DOING | 10% | 已通过批处理学习幂等、补偿、租约、分片和最终一致性边界；Redis、MQ 和分布式理论主线未开始 |
| Phase 6：项目深挖与面试表达 | DOING | 15% | 结算系统已有批处理并发与 ERP 一致性素材，但完整项目故事和 RAG 复盘未形成 |
| Phase 7：模拟面试与查漏补缺 | TODO | 0% | 尚无正式八股模拟或完整算法模拟记录 |

## 13.1 当前任务状态汇总

### 已完成

1. Phase 0：学习仓库和协作机制

### 已学习，等待复盘验证

1. 计算机网络请求链路
2. MySQL 事务与 MVCC
3. MySQL 索引基础、联合索引和访问路径
4. MySQL 当前读、锁与批处理并发控制
5. 动态规划入门与背包分类
6. 编辑距离二维 DP 和一维空间优化

### 正在推进

1. 计算机基础与后端工程的连接
2. Spring MVC / Tomcat 请求与线程模型
3. 分布式任务中的幂等、补偿、租约和处理权
4. 云服务结算系统项目深挖
5. Java 线程池与 RAG 后台任务执行

### 尚未开始

1. 数据结构基础
2. 操作系统基础
3. 滑动窗口、二分查找
4. Java 并发中的锁、CAS、AQS、ThreadLocal，以及 JVM
5. Redis、MQ 完整主线
6. RAG 项目系统复盘
7. 正式模拟面试

## 13.2 当前最关键缺口

1. **项目表达没有闭环**
   - MySQL 和批处理知识已经很多，但还没有形成结算系统 30 秒、2 分钟、10 分钟三个版本。
2. **MySQL 仍缺稳定追问能力**
   - 死锁产生与排查、共享锁/排他锁、乐观锁/悲观锁、数据库锁和 Redis 锁边界仍未完整训练。
3. **计算机基础结构不完整**
   - 当前网络学习偏请求链路，TCP 可靠传输、挥手、HTTP 版本、HTTPS，以及 OS、数据结构仍有明显空白。
4. **DP 处于理解后但输出不稳定阶段**
   - 能理解状态和转移，但下标、边界、答案位置仍可能混用不同状态模型，且缺少独立 Java 实现验证。
5. **冲刺计划后半程尚未启动**
   - Redis、MQ、Java 并发、Spring 核心、JVM 和模拟面试尚无系统沉淀。

---

# 14. 优先级规则

如果我不知道今天学什么，请按下面优先级推荐：

1. 面试中已经暴露的问题
2. 计算机基础中的短板
3. 数据库事务
4. 动态规划
5. 项目深挖
6. MySQL 索引和锁
7. Redis 分布式锁
8. MQ 可靠性
9. Java 并发
10. Spring MVC / Spring Boot
11. JVM

当前最优先任务：

1. 云服务结算系统 2 分钟项目表达
2. MySQL 事务、索引、锁的面试追问复盘
3. Java 并发与 Spring 高频主线
4. Redis / MQ / 分布式一致性
5. 动态规划短时口述与代码验证
6. 计算机基础中的 OS、TCP 和数据结构缺口

---

# 15. Codex 每次推进时的行为要求

你每次和我学习时，请主动维护进度。

不要只是回答我的问题。

你需要像一个学习项目的技术负责人一样，帮助我判断：

1. 当前阶段是否完成
2. 是否应该继续深入
3. 是否可以进入下一阶段
4. 哪些问题需要记录到 mistakes/
5. 哪些内容需要沉淀到 interview/
6. 哪些项目经验可以用于简历和面试

---

# 15. 阶段推进条件

不要因为“我看过了”就判定完成。

只有满足下面条件，才能把任务标记为 DONE：

1. 我能用自己的话解释
2. 我能回答 3 个以上追问
3. 我能联系项目场景
4. 我能给出面试版回答
5. 我能指出常见误区

如果只是大概听懂，请标记为 REVIEW。

如果我明显卡住，请标记为 BLOCKED，并重新拆小任务。

---

# 16. 当前起点

最初暴露的两个问题是：

1. 数据库事务讲不清楚。
2. 动态规划题没有做出来。

截至 2026-06-09，这两个主题都已经完成多轮学习，当前状态是 `REVIEW`，不再适合作为从零起点。

当前实际断点：

```text
Step 1：把结算系统批处理并发安全、幂等、失败恢复整理成 2 分钟回答
Step 2：用追问验证 MySQL 事务、MVCC、索引和锁是否能稳定输出
Step 3：补齐 Java 并发与 Spring 高频知识
Step 4：进入 Redis、MQ 和分布式一致性主线
Step 5：DP 只做短时复述和独立代码验证，不继续扩展复杂题型
Step 6：面试冲刺后回补 OS、TCP、数据结构等长期基础
```

---

# 17. 最终目标

最终这个仓库应该沉淀出三类能力：

## 17.1 知识能力

我能讲清楚后端核心机制：

* MySQL
* Redis
* MQ
* Java 并发
* JVM
* Spring
* 分布式系统
* 算法

## 17.2 项目能力

我能把真实项目讲成有技术深度的工程案例：

* 为什么这么设计
* 解决了什么问题
* 有什么权衡
* 如何保证正确性
* 如何提升性能
* 如何处理失败

## 17.3 面试能力

我能在压力场景下结构化表达：

* 先讲本质
* 再讲机制
* 再讲项目
* 再讲权衡
* 最后回答追问

这才是本计划的核心目标。
