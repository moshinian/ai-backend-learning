# 2026-07-07 华盛通大模型应用工程师面试准备

## 日期

2026-07-07

## 主题

围绕华盛通 SZ-大模型应用工程师 JD，进行 20:00 真实面试前的临场复习和表达压缩。

## 本次做了什么

1. 读取并分析 JD：岗位同时要求大模型应用、LangChain / Dify、向量检索、Spring / FastAPI、Redis / MQ、CUDA / TensorRT 推理优化。
2. 明确面试定位：Java 后端 + RAG 应用落地 + 大模型应用工程化，不包装成 CUDA 推理专家，也不把 Agent 说成简历中的生产经验。
3. 逐题训练 RAG 项目主线、Chunk、Embedding、召回排查、pgvector、权限隔离、幻觉控制、索引任务失败、版本冲突、金融场景风险。
4. 训练 LangChain / Dify / LangGraph 的边界表达，以及 CUDA / TensorRT 不熟时的诚实防守答案。
5. 将本次准备内容整理到 `interview/mock-records/2026-07-07-huashengtong-ai-application-engineer-prep.md`。

## 关键结论

1. 今晚面试主线是 RAG + 后端工程 + 金融可信落地，不是补全所有 JD 关键词。
2. RAG 项目表达必须按“离线索引链路 + 在线问答链路 + 工程难点”组织。
3. 金融场景要反复强调：权限隔离、证据链、引用溯源、审计记录、问题回放、无依据拒答。
4. 简历只有 RAG 时，Agent / LangGraph 只能说成近期学习和扩展方向；Dify 可以说有接触但不是深度生产经验；CUDA / TensorRT 要诚实说明不是强项。
5. 后端工程优势要主动迁移到大模型应用：异步索引、任务状态、失败重试、幂等、Redis 并发控制、MQ 削峰、Spring 业务权威、FastAPI AI 适配层。

## 下次入口

1. 面试前只复习 `interview/mock-records/2026-07-07-huashengtong-ai-application-engineer-prep.md` 中的开场定位、RAG 主线、金融可信 RAG 和短板防守。
2. 面试结束后，立即归档真实问题、现场回答、追问卡点和自评。
3. 根据真实表现更新 `interview/real-records/`、`mistakes/` 和 `LEARNING_BACKLOG.md`。

## 关联文件

1. `LEARNING_BACKLOG.md`
2. `START_HERE.md`
3. `interview/mock-records/2026-07-07-huashengtong-ai-application-engineer-prep.md`
4. `interview/rag-project-story.md`
5. `interview/ai-application-questions.md`
6. `interview/redis-questions.md`
7. `backend/redis/distributed-lock.md`
