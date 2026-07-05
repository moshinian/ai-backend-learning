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

## 5. 后续待验证问题

1. 如何设计物流异常处理 Multi-Agent 系统？
2. Agent 状态由谁维护？
3. 如何防止 Agent 循环调用和任务失控？
4. 工具调用如何做权限、幂等、超时和审计？
5. 哪些操作必须 Human-in-the-loop？
6. 如何评估 Agent 的任务成功率、成本和稳定性？
7. LangGraph 与普通业务 Workflow 应该如何选型？
