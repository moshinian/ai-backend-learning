# 2026-06-30 AI Agent / RAG 后端真实面试归档

## 本次动作

根据元宝会议助手整理的面试过程，将一次围绕 RAG、Agent、Java/Python 架构、结算系统、Redis 分布式锁和后端工程实践的真实面试归档到仓库。

主记录：

1. `interview/real-records/2026-06-30-ai-agent-rag-backend.md`

## 面试暴露的关键问题

1. Redis 常见数据结构掌握不足，把面试官问的 String / Hash / List / Set / ZSet 误答成底层类型。
2. Redis Hash 和序列化 String 的对象存储边界不清。
3. 分布式锁的目标需要先分类：业务抢占临界区短锁、框架级全周期锁、数据库状态机处理权。
4. RAG 个人项目必须主动说明事实边界：基于真实痛点，但未生产上线。
5. Agent 表达要从“工具和模型”上升到“状态、决策、执行、观察、再决策、人类确认”。
6. 单测和日志链路需要补 TraceId、MQ messageId、外部 requestId 和结构化日志。

## 下次学习入口

优先处理 Redis 数据结构和锁粒度表达：

1. Redis 常见数据结构有哪些？各自适合什么工程场景？
2. Hash 和序列化 String 存对象有什么区别？
3. Redis 锁应该锁整个任务，还是只锁状态变更临界区？

随后整理 RAG 项目事实边界版表达：

1. 这个项目没有生产上线，如何说明工程价值？
2. 固定 RAG Pipeline、RAG Workflow 和 Agent 的区别是什么？
