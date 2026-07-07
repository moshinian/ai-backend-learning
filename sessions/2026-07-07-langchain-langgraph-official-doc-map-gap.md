# 2026-07-07 LangChain / LangGraph 官方目录补课校准

## 日期

2026-07-07

## 主题

校准 `BL-011 LangChain / LangGraph 机制梳理` 的学习范围：从已跑通的 runtime 片段，补回官方文档目录级全貌。

## 本次做了什么

1. 对照 LangChain 官方 overview，确认当前学习不能只停留在 `create_agent` 和工具调用 loop。
2. 对照 LangGraph 官方 overview，确认当前学习不能只停留在 `StateGraph`、checkpoint、interrupt 和 streaming。
3. 将 `BL-011` 从 REVIEW 拉回 DOING，增加官方目录地图级补课要求。
4. 同步更新 `LEARNING_ROADMAP.md`、`LEARNING_BACKLOG.md`、`START_HERE.md` 和 `LEARNING_JOURNAL.md`。

## 关键结论

1. LangChain 需要按 Core components、Middleware、Runtime、Frontend、Advanced usage 建立全貌。
2. LangGraph 需要按 Capabilities、Production、Frontend、Graph API / Functional API 建立全貌。
3. 之前已验证的 `create_agent`、StateGraph、checkpoint、interrupt、streaming 是重要 runtime 片段，但不足以代表完整框架能力。
4. `BL-011` 的验收应增加“能按官方目录画出学习地图”，否则容易只会局部 API，不能解释框架工程价值。
5. 仍要保持原有项目边界：模型负责建议，runtime 负责流程，Java DB / 后端数据库负责业务事实、权限、审批和副作用状态。

## 下次入口

继续 `BL-011` 的 DOING 阶段：

1. 先整理 LangChain 官方目录地图：Core components、Middleware、Runtime、Frontend、Advanced usage。
2. 再整理 LangGraph 官方目录地图：Capabilities、Graph API / Functional API、Production、Frontend。
3. 最后压缩成 2 到 3 分钟口述表达，并回到个人 RAG / Agent 项目边界。

## 关联文件

1. `LEARNING_BACKLOG.md`
2. `START_HERE.md`
3. `LEARNING_ROADMAP.md`
4. `LEARNING_JOURNAL.md`
5. `sessions/2026-07-07-langchain-langgraph-learning-summary.md`
6. LangChain 官方文档：`https://docs.langchain.com/oss/python/langchain/overview`
7. LangGraph 官方文档：`https://docs.langchain.com/oss/python/langgraph/overview`
