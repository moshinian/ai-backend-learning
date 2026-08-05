# 2026-08-05 兔展面试复盘与能力地图回流

## 日期

2026-08-05

## 主题

审计兔展 AI 平台后端技术一面完整转写，结合个人 `rag-system` 代码判断哪些是表达缺口、真实实现缺口和事实风险，并把长期能力回流到 Roadmap 与 Backlog。

## 本次做了什么

1. 按对话逻辑校准说话人和 RAG / Agent / MCP / OOM 等转写错误，不把自动标注当成绝对事实。
2. 逐题复盘文档解析、pgvector、数据规模与延迟、多轮 RAG、Agent Runtime、Claude Code 类 Agent、视觉实习、职业转向、部署和 MySQL 联合索引。
3. 对照 `rag-system` 代码确认已经实现单 Agent `StateGraph`、模型工具循环、`ToolMessage`、只读工具与 Action 分流、Java `McpToolRegistry` 和 Run / Event 审计。
4. 确认当前没有多轮 Query rewrite、长期记忆、Skill 管理、多 Agent / 意图路由和通用文件 / Shell 沙箱。
5. 核对个人项目当前文档处理代码只确认支持 MD、TXT 和原生文本 PDF；PDF 使用 PDFBox，Chunk 使用固定窗口、overlap 和自然边界兜底。
6. 使用 MySQL 8.4 官方文档校正联合索引范围访问、覆盖索引和 ICP 的边界。
7. 更新 `RM-02`、`RM-06`、`RM-10`，新增 `BL-028` 至 `BL-030`，并将 Kubernetes 开发者视角由 P2 调整为 P1。
8. 归档 Agent Harness、Query rewrite、ICP 和职业转向四类表达 / 认知问题。

## 关键结论

1. 面试官反馈有事实基础，但不能简化为“项目没有 Agent”。当前项目已有可运行的单 Agent Harness，缺口是架构表达和更完整的 Context / Memory / Skill / Router / Sandbox 能力。
2. 下一步先补单 Agent Harness 主链路，不从多 Agent 名词或框架目录开始；只有最小模型—工具循环稳定后，才讨论 Router 和 Subagent。
3. 多轮 RAG 的关键是把历史与当前追问改写成独立 Query，再检索；生成 Prompt 是否携带历史是后一个问题。
4. 文档解析必须先分原生文本、扫描件、版面和表格；当前个人项目不支持 Word / OCR 的代码事实不能被现场成熟方案覆盖。
5. `(A,B,C)` 在 A 等值、B 范围、C 等值场景并非完全不可用；要区分搜索区间、索引记录过滤、覆盖索引和 ICP。
6. 现场给出的文档量、字符量、延迟、模型平台和视觉项目细节需要证据复核，不能直接写回简历或项目笔记。
7. 职业转向应从“组织安排造成的遗憾”改成“岗位调整、四年后端积累、主动迁移 AI 平台后端”。

## 下次入口

1. 从 `BL-028` 开始，闭卷画出只有模型 API 时的单 Agent Harness。
2. 对照个人代码完成“已实现 / 未实现 / 后续设计”三列证据表。
3. Harness 通过后进入 `BL-029`，再用可运行 MySQL 实验完成 `BL-030`。
4. 在下一次面试前完成 `BL-027` 的事实审计。

## 关联文件

1. `interview/real-records/2026-08-05-tuzhan-ai-platform-backend.md`
2. `LEARNING_ROADMAP.md`
3. `LEARNING_BACKLOG.md`
4. `START_HERE.md`
5. `mistakes/interview/agent-project-implementation-and-expression-gap.md`
6. `mistakes/interview/rag-multi-turn-query-rewrite.md`
7. `mistakes/database/composite-index-range-and-icp.md`
8. `mistakes/interview/career-transition-negative-narrative.md`
