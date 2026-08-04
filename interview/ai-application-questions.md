# AI 应用开发面试问题

## 1. 当前边界

本文件记录 AI 应用岗位的高频问题。

回答时必须区分：

1. 已有生产或项目实践
2. 已理解但未实际落地
3. 仅作为后续学习方向

不得把概念理解包装成生产经验。

---

## 2. RAG、Agent、Workflow 和 Multi-Agent

### 简洁版

RAG 解决的是给模型补充外部知识，使回答基于企业资料。Agent 在此基础上增加目标规划、工具选择和行动能力。Workflow 的主要执行路径通常由开发者预先定义，确定性更强。Multi-Agent 则把不同职责交给多个 Agent，通过任务委托和状态协作完成复杂目标。

### 关键边界

1. 不是所有问题都需要 Agent，确定流程优先使用 Workflow。
2. 不是 Agent 越多越好，拆分会增加通信、状态、延迟和错误传播成本。
3. 大模型适合理解、规划和非确定性判断。
4. 权限、状态推进、资金操作和核心业务规则应由确定性服务控制。

---

## 3. MCP、A2A、LangGraph、Spring AI 和 Dify

### MCP

MCP 主要解决模型或 Agent 如何以统一方式发现并调用工具、资源和上下文，降低每个应用单独适配外部系统的成本。

### A2A

A2A 关注 Agent 之间的能力发现、任务委托、进度和结果通信。它解决的是 Agent 与 Agent 的协作问题，不等同于工具调用协议。

### LangGraph

LangGraph 适合表达有状态、可分支、可循环并支持人工介入的 Agent 工作流。重点价值是把 Agent 执行过程显式建模为图和状态，而不只是连续调用 Prompt。

### LangChain 与 LangGraph 的边界

LangChain 更偏上层 Agent 组装，负责模型调用、消息结构、Prompt、工具绑定、Agent loop、middleware 和结构化输出。LangGraph 更偏底层 Agent 编排运行时，把复杂 Agent loop 建模成 Graph、State、Node、Edge，并支持 checkpoint、interrupt、streaming 和 human-in-the-loop。

简单固定 RAG Pipeline 不一定需要 LangGraph；复杂、长时间、可恢复、需要人工介入或多步工具调用的 Agent 更适合使用 LangGraph。

### messages、tool_calls 和 ToolMessage

Agent 不是一次模型调用，而是“决策 -> 工具执行 -> observation -> 再决策”的循环。模型只生成工具调用意图，真正执行工具的是 Agent runtime 或业务代码。

`messages` 是结构化对话状态，不等同于普通 prompt string。`AIMessage` 表示模型输出，可能包含 `tool_calls`；`ToolMessage` 表示工具执行结果，必须用 `tool_call_id` 对应前面某次工具调用。`tool_call_id` 解决的是工具结果归属问题，不等于业务 `requestId`、链路 `traceId` 或任务处理权 `process_token`。

### checkpoint、interrupt 和后端业务状态

LangGraph checkpoint 保存 Agent runtime 执行现场，例如 messages、当前节点、工具 observation 和中断点；后端数据库保存业务事实，例如审批结果、权限校验、副作用执行状态和最终 run 状态。恢复时 checkpoint 决定“从哪里恢复”，后端数据库决定“是否允许继续”。

高风险动作不能只靠 Prompt 约束。模型可以建议动作，LangGraph 通过 interrupt 暂停执行，后端落库待确认 action，前端展示给用户确认；用户确认后后端保存审批结果并校验权限，再通过 resume 恢复图执行。工具真正执行完成后，才生成 ToolMessage。

interrupt 所在 node 在恢复时会从头重放，因此 interrupt 前的数据库写入、日志、外部调用等副作用必须幂等，或者移动到 interrupt 之后的独立节点。

### create_agent 和 StateGraph 怎么选

`create_agent` 是 LangChain 提供的上层 Agent Harness，用来快速组织模型、工具、messages 和常见 tool loop。标准路径是：用户消息进入 Agent，模型输出 `AIMessage.tool_calls`，runtime 根据 tool name 和 args 执行工具，生成 `ToolMessage`，再让模型基于工具结果继续生成最终回答。

手写 StateGraph 适合更强的流程控制，例如审批、恢复、状态机、权限校验和高风险副作用。它让开发者显式定义 State、Node、Edge、interrupt、checkpoint 和 resume。

选型原则：

1. 标准模型工具调用、查询和建议生成，优先使用 `create_agent`。
2. 强业务流程、人工确认、可恢复执行和高风险副作用，优先使用 StateGraph / 后端状态机。
3. 两者可以配合，但不要让 `create_agent` 直接主导支付、退款、删除等不可逆业务动作。

### LangChain 和 LangGraph 如何配合

LangChain 和 LangGraph 是不同层的能力。LangChain 更偏 LLM 应用组件层，LangGraph 更偏状态化运行时。当前 LangChain 的 Agent 能力会使用 LangGraph runtime，例如 `create_agent()` 返回的是基于 LangGraph 的 compiled graph。

在工程中可以采用外层 StateGraph、内层 LangChain 的方式：

1. StateGraph 负责支付、退款、审批、状态机和恢复。
2. LangChain / `create_agent` 在某些 node 内负责查询、解释、总结、结构化抽取或建议生成。
3. node 将业务 State 投影成 LangChain messages，再将 LLM 输出映射回结构化业务字段。
4. 不应把所有 LangChain messages 直接塞进外层业务 State，避免业务事实、对话历史和工具 trace 混在一起。

### 高风险工具执行边界

模型可以建议动作，但不应直接执行高风险副作用工具。以退款为例，`create_agent` 可以查询订单并生成退款建议，但 `refund_tool` 应只存在于受控执行节点：

1. 后端创建 `WAITING_CONFIRMATION` action。
2. LangGraph `interrupt()` 暂停并把审批 payload 暴露给调用方。
3. 用户确认后，后端保存审批结果并校验权限、金额、状态和幂等键。
4. StateGraph resume 后再次查询后端业务事实。
5. 只有 action 仍为 `APPROVED` 时，受控节点才调用 `refund_tool`。

面试表达：

> 我会把模型 Agent 和业务执行边界拆开。查询、解释和建议生成可以用 `create_agent` 组织模型、工具和 messages loop；但退款、删除、支付这类高风险副作用不会直接暴露给模型执行，而是进入 StateGraph / Java 后端控制的审批流程。LangGraph checkpoint 负责运行时恢复，Java DB 负责审批状态、权限和最终执行事实。

### Spring AI

Spring AI 为 Java/Spring 应用提供模型调用、Prompt、Tool Calling、Embedding、向量存储和 RAG 等抽象，适合把 AI 能力集成进现有 Java 企业应用。

### Dify

Dify 更偏可视化的大模型应用编排和运营平台，适合快速搭建 Workflow、知识库和模型应用。复杂业务规则、深度定制和既有 Java 系统整合仍可能需要代码服务配合。

---

## 4. 没有相关生产经验时怎么回答

推荐结构：

> 这项技术我目前没有生产实践。我理解它主要解决的是……我过去在结算系统或 RAG 项目中处理过的相近问题是……如果需要落地，我会先通过一个小范围场景验证……并重点关注……指标。

示例：

> 我目前没有 Multi-Agent 的生产实践，但理解它不仅是多个模型互相对话，更重要的是任务边界、共享状态、失败恢复、权限和可观测性。我过去在结算系统中做过任务拆分、状态机、MQ 协作、幂等和补偿，这些可靠性能力可以迁移到 Agent 编排层。如果落地，我会先选择一个边界清晰、风险可控的物流异常分析场景验证，而不会一开始让 Agent 直接执行不可逆业务操作。

---

## 5. Agent Run、Step、Action、Event 与 SSE

### 对象关系

1. Run：一次完整 Agent 执行，是状态、恢复、取消和审计的根对象。
2. Step：Run 中一个可观察阶段，例如检索、模型决策或工具执行。
3. Action：需要用户确认或具有业务副作用的动作，不等于所有 Step。
4. Event：运行中发生的事实，通常包含 `runId`、单调递增 `sequence`、`eventType` 和 payload，是 SSE 推送与断线补发的单位。

### 面试表达

> 我的 Agent 链路有两段 SSE：Python Runtime 向 Java 返回步骤事件，Java 先将完整事件写入事件表，事务提交后再发布给前端。前端重连时携带 `Last-Event-ID`，Java 先按 Run 和序号补发数据库中的缺失事件，再接实时流。当前项目已经做到 Step 级事件持久化和断线恢复，但不是逐 Token 输出；实时通道还是单实例内存广播，多实例需要 Redis Pub/Sub 或 MQ 等共享通道。

### 关键边界

1. SSE 是服务器向客户端单向推送的 HTTP 长连接，不负责业务状态持久化。
2. 一次 SSE `data` 帧不必对应一个字，也不必对应一次数据库写入。
3. 当前项目按完整业务 Event 入库，不按 Token 入库；Token 可以只实时推送，并按时间或字符数批量形成快照。
4. 数据库事件表负责可恢复历史，实时广播负责低延迟，两者职责不同。
5. 事件应在事务提交后发布，避免前端收到尚未提交或最终回滚的数据。

正式机制见 `backend/distributed-system/agent-sse-event-stream-and-recovery.md`。

---

## 6. Agent 多实例与生产化边界

多实例不是简单把 FastAPI 或 Java 服务复制几份。需要同时处理：

1. 服务实例尽量无状态，Run、Event、Checkpoint 和任务归属进入共享存储。
2. Redis / MQ 承担任务队列、租约或跨实例实时广播，数据库事件表承担断线补发。
3. Kubernetes Service / Ingress 负责路由，readiness、liveness、startup probe 分别服务于接流量、重启判断和慢启动保护。
4. 实例退出时先摘流量、停止领取新任务，再等待在途请求或释放任务租约，避免重复执行。
5. 压测先定义并发、P95 / P99、错误率、Token 速率和下游配额，再验证水平扩展、限流、降级、杀实例和恢复。

当前项目仍是单实例实时广播、Step 级事件流，没有用户主动取消和完整生产认证 / 指标体系，不能包装为已落地的高可用集群。

---

## 7. MCP / Skill 版本与工具选择质量

需要拆成两个问题：

1. 兼容性和可复现性：显式记录 MCP 协议版本、工具 Schema 版本、Skill / Prompt 版本和模型版本，通过契约测试、灰度和回滚治理。
2. 工具选择质量：检查工具名称和描述是否重叠、参数约束是否清楚、候选工具是否过多、示例是否具有区分度，并用固定评测集度量选择准确率和参数正确率。

版本号可以帮助重放一次调用，但不会自动提升模型的工具选择能力。MCP `annotations` 是工具行为提示元数据，也不能代替后端的认证、授权和业务校验。

---

## 8. 后续待验证问题

1. 如何设计物流异常处理 Multi-Agent 系统？
2. 长期记忆如何表示来源、有效时间、置信度、冲突与版本？
3. 如何通过检查点、确定性校验器和按风险触发的 LLM Judge 防止长任务跑偏？
4. 工具调用如何做权限、幂等、超时和审计？
5. 哪些操作必须 Human-in-the-loop？
6. 如何评估 Agent 的任务成功率、成本和稳定性？
7. LangGraph 与普通业务 Workflow 应该如何选型？
8. FastAPI 多实例下如何实现任务租约、优雅退出与 SSE 共享广播？
9. 不可信代码执行容器如何限制用户、文件系统、网络、资源、时间和凭证？
