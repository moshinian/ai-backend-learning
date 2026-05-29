# START HERE

## 1. 这个文件怎么用

这是恢复学习进度的唯一入口文件。Codex 只读取这个文件，也应该能够快速恢复当前学习进度并继续推进。

新开 Codex 会话时，默认只把这个文件喂给 Codex。不要要求用户再手动提供其他状态文件。

建议启动提示词：

```text
先读取 START_HERE.md。
只根据这个文件恢复进度并继续学习。
不要重复已经掌握的内容。
```

---

## 2. 当前执行口径

当前目标：

1. 用 1 个月时间做 Java 后端面试冲刺
2. 每周预计学习 30 小时
3. 总投入约 120 小时
4. 重点不是完整学完所有知识，而是优先补齐面试最高价值短板

计划关系：

1. `LEARNING_ROADMAP.md`：长期能力地图
2. `INTERVIEW_SPRINT_30_DAYS.md`：当前 1 个月执行计划
3. 本月如果两者优先级冲突，以 `INTERVIEW_SPRINT_30_DAYS.md` 为准

---

## 3. 当前学习状态

日期：2026-05-29

当前阶段：

1. 长期 Roadmap：`Phase 1：计算机基础` 已经开始
2. 当前执行模式：`1 个月 / 120 小时面试冲刺`

当前主题：

1. 请求链路与 Tomcat 线程模型第一轮已收尾
2. 下一步进入 MySQL 事务主线
3. 学习恢复入口已合并完成：以后默认只读取 `START_HERE.md`

已经掌握：

1. DNS 负责域名到 IP
2. 端口负责定位机器上的具体服务
3. 客户端真正连接的是 `IP:Port`
4. TCP 负责建立可靠传输通道
5. HTTP 负责请求和响应的格式、语义和规则
6. Tomcat 负责监听端口、接收连接、解析 HTTP 请求
7. `DispatcherServlet` 负责统一分发请求
8. Controller 负责具体业务接口处理
9. `spring-boot-starter-web` 会触发 Web 自动配置和内嵌 Tomcat 启动
10. 慢请求拖垮 Web 服务，很多时候是工作线程被同步阻塞，不一定是 CPU 被打满
11. 当前 1 个月学习策略应是面试冲刺，不是平均推进长期 Roadmap
12. Tomcat、Servlet、`DispatcherServlet`、Controller 的职责边界
13. Keep-Alive 长连接存在不等于一直占用 Tomcat 工作线程
14. Tomcat NIO 中空闲连接主要由 Poller 监听，有请求可读并进入业务处理时才占用工作线程
15. Filter 属于 Servlet 规范，Interceptor 属于 Spring MVC，执行位置不同

仍不稳定：

1. 异步化设计表达：业务线程池、任务队列、SSE、轮询的适用边界
2. Servlet 容器和操作系统线程 / IO 的连接点仍需后续结合 OS 复盘
3. 三次握手和 TCP 整体机制的边界需要后续复习
4. 数据库事务、MVCC、锁和项目一致性表达
5. 动态规划和算法表达

---

## 4. 下次从哪里开始

**数据库事务为什么出现？ACID 分别解决什么真实工程问题？**

不要重复展开以下内容，只需快速确认：

1. DNS 负责域名到 IP
2. 端口负责定位服务
3. TCP 负责可靠传输
4. HTTP 负责请求 / 响应规则
5. Tomcat 负责接请求
6. `DispatcherServlet` 负责分请求
7. Controller 负责处理请求
8. 慢请求会同步阻塞 Tomcat 工作线程
9. Keep-Alive 空闲连接不长期占用 Tomcat 工作线程
10. Filter 在 `DispatcherServlet` 之前，Interceptor 在 `DispatcherServlet` 之后、Controller 之前

---

## 5. 本月优先级

按这个顺序推进：

1. 请求链路收尾：Tomcat、Servlet、`DispatcherServlet`
2. MySQL：事务、隔离级别、MVCC、索引、锁
3. Java 并发 / Spring：线程池、锁、Spring MVC、`@Transactional`
4. Redis / MQ / 分布式：分布式锁、消息可靠性、幂等、最终一致性
5. 项目表达：云服务结算系统、RAG 知识问答系统
6. 算法保底：滑动窗口、二分、动态规划入门
7. 模拟面试和 mistakes 复盘

---

## 6. 是否需要读取其他文件

默认规则：

1. 只读 `START_HERE.md` 就可以恢复进度并开始学习
2. 不要让用户额外喂其他文件
3. 只有在需要更新笔记、核对历史细节或写入沉淀文件时，Codex 再主动读取相关文件

可选参考文件：

1. `INTERVIEW_SPRINT_30_DAYS.md`
   - 用于查看完整 30 天冲刺计划
2. `LEARNING_ROADMAP.md`
   - 用于查看长期能力地图
3. `LEARNING_JOURNAL.md`
   - 用于查看长期画像、典型误区和历史索引

当前网络请求链路主题的可选沉淀文件：

1. `fundamentals/network/http-tcp-request-flow.md`
2. `interview/computer-fundamentals-questions.md`
3. `mistakes/network/request-flow.md`
4. `sessions/2026-05-28-http-tcp-request-flow.md`

当前 MySQL 事务主题的可选沉淀文件：

1. `backend/mysql/transaction.md`
2. `interview/mysql-questions.md`
3. `mistakes/database/transaction.md`

注意：

这些文件不是恢复进度的前置条件。Codex 可以先基于本文件直接继续教学；只有需要补充、修改或核对沉淀内容时再读取。

---

## 7. 文档记述规则

回答和新增笔记统一使用中文。

学习一个知识点时，优先按这个结构推进：

1. 这个机制解决什么真实工程问题
2. 如果没有它会怎样
3. 核心概念是什么
4. 内部机制大概怎么工作
5. 边界和代价是什么
6. 项目里怎么用
7. 面试官可能怎么问
8. 简洁版面试回答

每次学习结束时，优先更新：

1. `START_HERE.md`：更新当前状态和下次断点
2. 对应主题笔记：沉淀机制理解
3. `interview/`：沉淀面试回答
4. `mistakes/`：记录错误、偏差和纠正方式
5. `sessions/`：必要时归档本次会话关键决策和下次起点

状态判断：

1. `TODO`：还没开始
2. `DOING`：正在学习
3. `REVIEW`：学过，但表达或追问不稳
4. `DONE`：能讲清楚、能联系项目、能接住追问
5. `BLOCKED`：明显卡住，需要拆小

不能因为“看过”就标记为 `DONE`。
