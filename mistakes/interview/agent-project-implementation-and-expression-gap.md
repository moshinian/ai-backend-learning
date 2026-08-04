# Agent 项目实现与认知表达脱节

## 1. 错误表现

1. 项目代码已经实现 Event 持久化、Run / Step / Action 状态、`Last-Event-ID` 补发和 Runtime heartbeat，但面试现场把“建立状态表、断线恢复”说成后续建议。
2. 把 Step 级流式、Token 级流式、事件持久化和多实例广播混成一个“当前 SSE 不完整”的问题。
3. 不能立即说明 Run、Step、Action、Event 分别是什么，以及哪个对象是最小传输和入库单位。
4. 把 MCP 协议中的 `annotations` 元数据表述成“Java 扫描注解设置权限”，与当前 `McpTool` 接口和 `McpToolRegistry` 实现不一致。
5. 面对 MCP / Skill 效果下降、长期记忆和长任务检查问题时，过早提出版本号、翻译模块或更强模型，没有先区分兼容性、工具选择质量、记忆冲突和执行校验各自属于哪一层。

## 2. 根因

1. 功能主要通过多轮代码协作完成，验收时关注“是否跑通”，没有把对象关系和调用链转换成自己的机制模型。
2. 面试前以项目功能和技术栈为检索入口，没有按“请求方向、状态所有权、持久化时机、失败边界”复述真实代码。
3. 听到陌生问题后急于给方案，缺少“先定义问题层次，再区分已实现、推断和设计”的停顿。
4. 对协议字段名、Java 注解和业务元数据使用了相似词，未回到代码确认真实实现。

## 3. 正确理解

1. Python Runtime 产生完整 Event；Java 校验并逐条持久化 Event，再更新对应的 Run、Step 或 Action。
2. Run 是整体任务，Step 是执行步骤，Action 是受控业务动作，Event 是有序变化事实；最小流式和历史补发单位是 Event。
3. 当前已实现 Step 级事件流、事件表、事务后推送、断线补发和孤儿 Run 恢复。
4. 当前未实现的是最终回答 Token streaming、在线订阅多实例广播、完整用户取消协议和生产认证授权，不应把已实现与未实现混为一谈。
5. MCP 协议版本、工具契约版本、Skill / Prompt 版本和模型工具选择效果是四个问题。版本治理解决兼容和回滚，不能单独解决模型选错工具或输出质量下降。
6. 当前 Java 工具通过 `McpTool` 实现和 `McpToolRegistry` 汇总；协议 `annotations` 是工具能力元数据，不是 Java 注解扫描事实。

## 4. 复盘触发条件

出现以下情况时，先停止给方案并画真实调用链：

1. 面试官问“你这个项目具体怎么实现”。
2. 回答中出现“应该有、可以加、建议做”，但仓库可能已经实现对应能力。
3. 同时出现流式粒度、持久化、重连、多实例和取消等多个维度。
4. 使用“注解、版本、状态、记忆”等抽象词，但不能指出具体对象、字段或所有者。
5. 准备把个人工程实现包装成生产效果，或反过来把已验证实现说成只有设计。

## 5. 关联主题

1. `backend/distributed-system/agent-sse-event-stream-and-recovery.md`
2. `interview/real-records/2026-08-04-suunto-ai-agent-engineer.md`
3. `interview/ai-application-questions.md`
4. `LEARNING_BACKLOG.md` 中的 `BL-026`
