# START HERE

## 1. 用法

新会话优先读取本文件，用于快速恢复当前学习上下文。

本文件只记录恢复入口，不写长篇知识内容。

---

## 2. 当前候选最高优先级

当前候选任务：

- `BL-028`：Agent Harness 架构与项目证据闭环

说明：

- 2026-08-05 兔展 AI 平台后端技术一面已完成，结果尚未确认；`BL-027` 进入 `REVIEW`，事实审计完成后封盘。
- 本场没有改变“Java 后端主线 + AI 应用工程补充”，当前恢复入口切换到完整 Agent Harness 的实现证据与架构表达。
- 其他暴露项已登记到 `BL-029`、`BL-030` 和 `BL-027`；具体优先级、状态和验收标准以 `LEARNING_BACKLOG.md` 为准。
- 2026-08-05 晚间转转集团全栈工程师面试已归档；限时编码、ToC 订单设计和 6 小时 Redis 锁分别回流 `BL-009`、`BL-031`、`BL-002`，均不替换当前 P0 入口。

---

## 3. 当前断点

当前断点：

1. `BL-028` 状态为 `DOING`。代码证据审计已完成，下一步是把真实实现画成不依赖框架名的 Harness 主链路并闭卷表达。
2. 已实现与未实现边界、代码证据和验收要求统一记录在 `LEARNING_BACKLOG.md` 的 `BL-028`；对应认知纠偏见 `mistakes/interview/agent-project-implementation-and-expression-gap.md`。
3. 多轮 RAG、MySQL ICP 和面试事实审计分别由 `BL-029`、`BL-030`、`BL-027` 承接，不在本文件展开知识结论。

---

## 4. 最近学习位置

最新转转面试与复盘：

1. `interview/real-records/2026-08-05-zhuanzhuan-fullstack-engineer.md`
2. `sessions/2026-08-05-zhuanzhuan-interview-review.md`
3. `mistakes/algorithm/adjacent-swap-live-coding.md`
4. `mistakes/distributed/toc-order-design-without-access-path.md`

此前兔展面试与复盘：

1. `interview/real-records/2026-08-05-tuzhan-ai-platform-backend.md`
2. `sessions/2026-08-05-tuzhan-interview-review-and-capability-map.md`
3. `interview/mock-records/2026-08-05-tuzhan-ai-platform-backend-prep.md`
4. `mistakes/interview/agent-project-implementation-and-expression-gap.md`
5. `mistakes/interview/rag-multi-turn-query-rewrite.md`
6. `mistakes/database/composite-index-range-and-icp.md`
7. `mistakes/interview/career-transition-negative-narrative.md`

暂停前断点：

1. `LEARNING_BACKLOG.md` 中的 `BL-026`
2. `sessions/2026-08-04-suunto-ai-agent-interview-and-sse-review.md`

---

## 5. 下一步动作

建议下一步：

1. 先回答：“如果只有 DeepSeek API Key，怎样从零实现一个 Claude Code 类单 Agent？”只讲最小主链路，不先讲 QPS、Kubernetes 或多 Agent。
2. 沿真实代码核对 Model、Messages、Tool Registry、Tool Call、ToolMessage、Action、State、Event 和 Java / Python 边界。
3. 再补 Context / 短期记忆 / 长期记忆 / Skill / Router / Subagent / Sandbox / Evaluation，逐项说明是否需要及其代价。
4. 完成 Harness 闭卷表达后，进入 `BL-029` 的多轮 Query 改写；`BL-030` 用小实验验证联合索引与 ICP。
5. 在下一次投递或面试前完成 `BL-027` 的五组事实审计和职业转向表达修订。
6. 转转面试暴露项的具体断点保留在 `BL-009`、`BL-031`、`BL-002`，当前不抢占 `BL-028`。

---

## 6. 优先读取文件

1. `LEARNING_BACKLOG.md` 中的 `BL-028`
2. `interview/real-records/2026-08-05-tuzhan-ai-platform-backend.md`
3. `mistakes/interview/agent-project-implementation-and-expression-gap.md`
4. `interview/ai-application-questions.md`
5. `backend/distributed-system/agent-sse-event-stream-and-recovery.md`
6. `sessions/2026-08-05-tuzhan-interview-review-and-capability-map.md`

需要判断长期能力方向时，再读取：

1. `LEARNING_ROADMAP.md`

需要确认文档规则时，再读取：

1. `AGENTS.md`
