# START HERE

## 1. 用法

新会话优先读取本文件，用于快速恢复当前学习上下文。

本文件只记录恢复入口，不写长篇知识内容。

---

## 2. 当前候选最高优先级

当前候选任务：

- `BL-026`：颂拓 AI Agent 一面复盘与生产化补强

说明：

- 2026-08-04 已完成颂拓 AI Agent 工程师技术一面。面试官表示可能安排 AI 算法负责人继续交流，但面试结果和下一轮均尚未确认。
- 本场验证了“Java 后端主线 + AI 应用工程补充”与生产化 Agent 后端岗位的匹配，不改变长期求职定位。
- 当前最高收益不是扩张新的 Agent 框架，而是准确讲清个人项目已经实现的 SSE 事件链路，并补齐长期任务、多实例和容器隔离的最小边界。
- `BL-025` 分布式事务补强保持 `TODO`，暂降为 P1；完成 `BL-026` 当前最小验收后，或新的 Java 金融后端面试需要时再恢复。
- `BL-016` 万级 QPS 保持 `REVIEW`，`BL-018` Spring Batch 保持 `TODO`，均未因本场面试提前改变状态。

---

## 3. 当前断点

当前断点：

1. `BL-026` 状态为 `DOING`，一面纪要审计和 SSE 第一轮机制归纳已经完成，尚缺闭卷口述及后续主题的最小验证。
2. 已确认 Run 是一次完整执行，Step 是可观察阶段，Action 是需要确认或产生副作用的业务动作，Event 是按 Run 排序、用于持久化和推送的事实。
3. 已确认个人项目存在两段流：Python Runtime 到 Java 的运行时 SSE，以及 Java 到前端的业务 SSE；Java 按完整 Event 入库，事务提交后发布，重连时按 `Last-Event-ID` 补发，并通过心跳与恢复任务处理孤儿 Run。
4. 当前实现边界是 Step 级而非 Token 级；实时通道仍为单实例内存广播，尚无用户主动取消，也不能声称具备完整生产认证、指标、告警和多实例高可用。
5. 下一层待补内容是长期记忆冲突与版本、长任务检查点与校验、MCP / Skill 版本和工具选择质量、FastAPI 多实例共享状态与广播、容器沙箱隔离。
6. 会议纪要可能存在转写误差：`Bn25` 很可能是 BM25，`Rank` 很可能是 Rerank，`NCM` 很可能是 MCP，`ASROPI` 暂无法确认；会议助手对面试官态度的判断不作为结果事实。
7. 项目时间线继续保持原边界：公司阶段只有离职前的 RAG 初步搭建且没有用户试用；Rerank、Agent、事件恢复和后续工程能力属于离职后的个人持续建设。

---

## 4. 最近学习位置

本次一面与机制沉淀：

1. `sessions/2026-08-04-suunto-ai-agent-interview-and-sse-review.md`
2. `interview/real-records/2026-08-04-suunto-ai-agent-engineer.md`
3. `backend/distributed-system/agent-sse-event-stream-and-recovery.md`
4. `mistakes/interview/agent-project-implementation-and-expression-gap.md`
5. `interview/ai-application-questions.md`

此前 Java 主线断点：

1. `LEARNING_BACKLOG.md` 中的 `BL-025`
2. `interview/real-records/2026-08-03-pingan-property-backend-individual-group.md`
3. `sessions/2026-08-03-pingan-interview-prep-and-project-reliability.md`

---

## 5. 下一步动作

建议下一步：

1. 不看笔记，用 60 至 90 秒讲清 Run / Step / Action / Event、两段 SSE、事件入库、事务提交后发布、`Last-Event-ID` 补发和当前边界。
2. 回答“Python 每返回一个字，Java 是否都要入库”时，明确 Token、SSE 帧和业务 Event 不是同一粒度；当前项目按完整业务 Event 入库。
3. 依次完成长期记忆与长任务校验、MCP / Skill 版本与工具评测、FastAPI 多实例与容器沙箱的最小回答卡。
4. 若确认进入算法负责人下一轮，再按本场问题做一次闭卷模拟；未确认前不扩张模型训练、推理框架或 Kubernetes 平台运维细节。
5. `BL-026` 达到最小验收后，根据真实面试安排恢复 `BL-025` 或 `BL-016`。

---

## 6. 优先读取文件

1. `LEARNING_BACKLOG.md` 中的 `BL-026`
2. `backend/distributed-system/agent-sse-event-stream-and-recovery.md`
3. `interview/real-records/2026-08-04-suunto-ai-agent-engineer.md`
4. `mistakes/interview/agent-project-implementation-and-expression-gap.md`
5. `interview/ai-application-questions.md`
6. `sessions/2026-08-04-suunto-ai-agent-interview-and-sse-review.md`

需要判断长期能力方向时，再读取：

1. `LEARNING_ROADMAP.md`

需要确认文档规则时，再读取：

1. `AGENTS.md`
