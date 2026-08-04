# 2026-08-04 颂拓 AI Agent 一面与 SSE 机制复盘

## 日期

2026-08-04

## 主题

围绕颂拓运动科技 AI Agent 工程师一面完成岗位对齐、真实面试复盘，并把 Agent Run、Step、Action、Event、双段 SSE、事件持久化和断线恢复从项目标签推进到可解释机制。

## 本次做了什么

1. 按 JD 将岗位识别为“AI Agent 场景下的生产后端工程岗”，准备四年 Java 生产后端、结算可靠性和个人 RAG / Agent 工程三类证据。
2. 基于 `rag-system` 公开仓库核对 Java 状态权威、Python LangGraph Runtime、React 工作台、MCP 工具、Human-in-the-loop 和 Agent SSE 实现。
3. 梳理 Run、Step、Action、Event 的职责，确认最小流式和补发单位是 Event，而不是字符、Token 或整个 Step。
4. 还原两段 SSE：Java 请求 Python 流式接口并消费 Runtime Event；Java 事务化持久化后再向 React 推送前端 Event。
5. 解释 SSE 文本帧、空行提交、Java 逐行组装、完整事件入库、heartbeat 与业务事件分离，以及 `Last-Event-ID` 历史补发。
6. 对照代码确认当前已经实现 `agent_run_event`、Run / Step / Action、事务后推送、Runtime heartbeat 和孤儿 Run 恢复。
7. 复盘一面中数据库性能、Agent 多语言、MCP / Skill 版本、长期记忆、长任务偏航、FastAPI 多实例、压测、模型部署、Docker 隔离和 Transformer 等讨论。
8. 识别会议助手可能的转写错误：`Bn25` 很可能是 `BM25`，`Rank` 应为 `Rerank`，`NCM` 可能是 `MCP`，`ASROPI` 无法确认；自动生成的“认可、满意”等评价不作为结果事实。

## 关键结论

1. 本场验证了“Java 生产后端能力 + Agent 工程迁移”与岗位方向匹配，但下一轮如果由算法负责人面试，会进一步验证 AI 机制深度，而不是重复 Java 项目。
2. 当前 SSE 的真实边界应拆成四层：Step 级而非 Token 级；Event 已持久化；断线补发已实现；在线订阅仍是单 Java 实例，多实例需要 Redis Pub/Sub 或 MQ。
3. Python 是 Java 请求的 SSE 响应方，不是主动向 Java 发送另一条业务请求；Java收到完整 Event 后才入库，不会按字符写数据库。
4. 项目最大的短板不是没有实现状态表，而是实现证据尚未内化为稳定表达，导致现场把已实现能力说成建议方案。
5. MCP 协议版本、工具 Schema 版本、Skill / Prompt 版本和模型工具选择效果必须分层；版本号不能修复模型决策质量。
6. 长期记忆不能只靠时间戳，需要后续补齐来源、有效时间、置信度、冲突处理、派生快照、检索范围和回滚。
7. 长任务检查不能只依赖更强模型持续监督，应优先建立确定性约束和 Checkpoint，在高风险节点按需使用 LLM Judge，并限制重规划次数和成本。
8. FastAPI 多实例、SSE 跨实例广播、代码执行容器隔离、本地模型工程化部署仍是明确短板，不能用 Java 经验直接等同为 Python 生产实践。

## 下次入口

1. 先闭卷用 60 至 90 秒讲清 Agent 完整链路和 SSE 四层边界。
2. 再按“事实存储、冲突处理、摘要生成、检索注入、评测回滚”建立长期记忆最小方案。
3. 补 FastAPI 无状态多实例、共享状态、SSE 广播、健康探针、优雅停机和压测主线。
4. 补代码执行容器的非 root、只读文件系统、网络、CPU / 内存 / PID / 超时和沙箱边界。
5. 等待是否安排 AI 算法负责人下一轮；当前任务状态以 `LEARNING_BACKLOG.md` 的 `BL-026` 为准。

## 关联文件

1. `interview/real-records/2026-08-04-suunto-ai-agent-engineer.md`
2. `backend/distributed-system/agent-sse-event-stream-and-recovery.md`
3. `mistakes/interview/agent-project-implementation-and-expression-gap.md`
4. `interview/ai-application-questions.md`
5. `LEARNING_BACKLOG.md`
6. `START_HERE.md`
