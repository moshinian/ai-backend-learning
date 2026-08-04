# Agent SSE 事件流、状态持久化与恢复

## 1. 本质

Agent 流式执行的本质不是“把模型生成的每个字立刻写入数据库”，而是把一次长任务拆成可识别的业务事件，在运行过程中持续传输、持久化和展示。

当前项目采用两段 SSE：

```text
Python Agent Runtime --内部 SSE--> Java 状态权威 --前端 SSE--> React
```

Python 负责产生运行事件；Java 负责校验、持久化、归并业务状态并在事务提交后推送；React 只消费 Java 已确认的事件。

## 2. 解决的问题

1. Agent 长时间执行时，普通同步 HTTP 容易超时且无法展示中间过程。
2. 浏览器刷新或网络断开后，单纯依赖长连接会丢失已经展示过的进度。
3. Python Runtime 产生的运行结果不能直接等同于最终业务事实。
4. 高风险工具调用需要等待 Java 侧权限校验和人工确认。
5. Runtime 或服务异常时，需要识别长期停留在 `RUNNING` 的孤儿任务。

## 3. 机制

### 3.1 Run、Step、Action 和 Event

1. `Run`：一次完整 Agent 任务，记录目标、发起人、整体状态和起止时间。
2. `Step`：Run 内的一次模型决策、节点执行或工具调用记录。
3. `Action`：Agent 推荐但需要受控确认或执行的业务动作。
4. `Event`：描述“刚刚发生了什么”的有序事实，是流式传输和历史补发的最小业务单位。

一个 Step 可以对应多条 Event：

```text
STEP_STARTED
  -> 创建或更新 Step 为 RUNNING

TOOL_CALL_COMPLETED
  -> 保存工具结果

STEP_COMPLETED
  -> 更新 Step 为 SUCCEEDED
```

`ACTION_RECOMMENDED` 会创建 Action，`RUN_COMPLETED` 或 `RUN_FAILED` 会更新 Run。不是每条 Event 都创建 Step，也不是每个 Step 都产生 Action。

### 3.2 完整执行链路

```text
React POST 创建 Run
  -> Java 持久化 RUNNING Run 并返回 runCode
  -> Java 后台 POST Python /v1/agent/runs/stream
  -> Python 执行 LangGraph 并输出完整 SSE Event
  -> Java 逐帧解析、校验并反序列化
  -> Java 在事务中插入 agent_run_event，并更新 Run / Step / Action
  -> AFTER_COMMIT 后通过 SseEmitter 推送 React
```

Python 不是主动向 Java 发起另一条请求，而是在 Java 发起的流式 HTTP 请求中持续返回 SSE 响应。

### 3.3 SSE 帧与数据库写入粒度

一条 SSE 帧包含：

```text
id: AR-001-000003
event: STEP_COMPLETED
data: {"runCode":"AR-001","stepCode":"STEP-002"}

```

底层 TCP 可以把文本拆成任意字节块，但 Java 的解析器会先累计 `id`、`event` 和 `data`，只有读到空行、得到完整帧后才处理一次业务事件。当前是 Step 级事件流，不是字符或 Token 级入库。

Java 对每条完整事件校验：

1. SSE `id` 与 JSON `eventId` 一致。
2. SSE `event` 与 JSON 事件类型一致。
3. 事件 `runCode` 与当前请求一致。
4. `event_code` 唯一，重复事件不重复生效。

### 3.4 为什么事务提交后再推送

Java 在同一个事务内插入 Event 并更新领域状态，然后通过 `@TransactionalEventListener(AFTER_COMMIT)` 推送前端。

如果提交前先推送，数据库随后回滚，前端就会看到不存在的成功状态。提交后推送保证实时展示与数据库事实一致。

### 3.5 断线补发

`agent_run_event` 按数据库 `id` 保存稳定顺序。前端短暂断线重连时，浏览器携带最后收到的 `Last-Event-ID`；Java 将其解析为事件记录，查询同一 Run 中数据库 `id` 更大的事件并补发，然后继续推送实时事件。

如果整个页面刷新、浏览器没有旧游标，Java 可以补发该 Run 的全部历史事件。数据库 Event 是恢复依据，SSE 只是实时通知通道。

### 3.6 心跳与孤儿 Run 恢复

Python 等待 LLM 或工具时发送 SSE comment：

```text
: heartbeat

```

心跳不进入 `agent_run_event`，也不推送 React。Java 节流更新 `runtime_heartbeat_at`。Recovery Scheduler 扫描同时满足以下条件的 Run：

1. 仍为 `RUNNING`。
2. 执行时间超过阈值。
3. Runtime 心跳过期。
4. 最近没有业务 Event。
5. 没有终态 Event。

恢复服务通过条件更新再次校验状态，并在同一事务内把 Run 标记为 `FAILED`、写入终态 Event，避免扫描后刚恢复活跃的任务被误杀。

## 4. 边界

1. 当前只做 Step 级事件流，不做最终回答 Token streaming。
2. 当前 Java 到 React 的在线订阅保存在单实例内存中；多实例需要 Redis Pub/Sub 或 MQ，把提交后的事件广播到持有连接的实例。
3. Python 取消是协作式的，只能在节点边界阻止后续执行，不能强制中断正在阻塞的 LLM 或工具调用。
4. 当前没有面向用户的完整任务取消协议。
5. SSE 是服务器到客户端的单向通道；确认、拒绝等反向操作仍使用普通 HTTP POST。
6. 如果未来做 Token streaming，不应逐 Token 入库；可以实时转发、内存合并，并按时间窗口或最终答案批量持久化。
7. 当前项目是可运行的个人工程版本，不代表已完成生产多实例、认证授权、容量验证和完整 Metrics / Tracing。

## 5. 项目或工程关联

当前 `rag-system` 已实现：

1. React 原生 `EventSource` 与自动重连。
2. Spring MVC `SseEmitter`、历史补发和 Run 级订阅锁。
3. FastAPI `StreamingResponse`、Python Generator、Thread、Queue 和 heartbeat。
4. Java `HttpURLConnection`、`BufferedReader` 和自定义 `SseEventParser`。
5. `agent_run_event`、`agent_step`、`agent_action`、`agent_run` 持久化。
6. Event 幂等、事务后推送、Runtime heartbeat 和 Recovery Scheduler。

代码事实来源：`https://github.com/moshinian/rag-system`。

## 6. 面试表达入口

> 当前系统采用两段 SSE。前端创建 Run 后，Java 先持久化任务并返回 runCode，再由后台线程调用 Python 的流式 Agent Runtime。Python 以完整 Event 而不是字符为单位返回决策和工具执行过程；Java 逐帧校验，在事务中写入 Event 并更新 Run、Step、Action，提交后再通过 SseEmitter 推送前端。浏览器断线后可以按 Last-Event-ID 从数据库补发。当前边界是 Step 级而非 Token 级流式，在线订阅仍是单 Java 实例，多实例需要 Redis Pub/Sub 或 MQ 广播。
