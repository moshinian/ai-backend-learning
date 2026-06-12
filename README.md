# AI BACKEND LEARNING

这个仓库用于沉淀我的 AI Backend / Java 后端学习过程。

目标不是堆资料，而是把零散经验整理成：

1. 可复盘的知识结构
2. 可复用的面试表达
3. 可持续更新的项目深挖材料
4. 可追踪的错误记录和学习进度

---

## 使用方式

开始学习前，优先读取：

1. `START_HERE.md`

这个文件负责恢复当前学习进度、下次断点、当前执行计划和文档记述规则。

- `START_HERE.md`
  - 新会话恢复学习的单入口
- `AGENTS.md`
  - 规定 Codex 如何和我协作
- `LEARNING_JOURNAL.md`
  - 记录长期学习画像、典型误区和历史会话索引
- `LEARNING_ROADMAP.md`
  - 规定学习阶段、任务状态和推进顺序
- `INTERVIEW_SPRINT_30_DAYS.md`
  - 规定当前 1 个月 / 120 小时面试冲刺计划

---

## 知识点归档规则

每学完一个知识点，按职责拆开沉淀，不要把同一份内容复制到多个文件。

| 内容类型 | 写到哪里 | 作用 |
|---|---|---|
| 当前进度、下次断点、不要重复讲的内容 | `START_HERE.md` | 新会话恢复入口 |
| 长期阶段、任务状态、验收标准 | `LEARNING_ROADMAP.md` | 长期能力地图 |
| 本月冲刺优先级和周计划 | `INTERVIEW_SPRINT_30_DAYS.md` | 当前执行计划 |
| 机制、本质、原理、边界 | `fundamentals/` 或 `backend/` | 主知识笔记 |
| 面试简洁版和深挖版回答 | `interview/` | 面试输出材料 |
| 真实面试的原题、现场回答、评价和修正版 | `interview/real-records/` | 真实面试复盘 |
| 模拟面试过程和评分 | `interview/mock-records/` | 模拟面试训练 |
| 错误、术语混淆、表达偏差 | `mistakes/` | 复盘和纠错 |
| 单次学习过程摘要 | `sessions/` | 历史归档 |
| 项目链路、设计取舍、工程亮点 | `projects/` | 项目深挖 |

使用原则：

1. `START_HERE.md` 只记录状态和断点，不写成长篇知识笔记。
2. `sessions/` 只做历史归档，不作为新会话恢复主入口。
3. `LEARNING_JOURNAL.md` 只记录长期画像、长期误区和主题索引，不记录每日进度。
4. 主笔记讲机制，`interview/` 讲怎么回答，`mistakes/` 记录哪里错过。
5. 不为每个小概念新建目录，优先按模块聚合，例如 MySQL 统一放在 `backend/mysql/`。

示例：

```text
学习 MySQL 事务
├── START_HERE.md                         # 更新当前状态和下次断点
├── backend/mysql/transaction.md          # 事务机制主笔记
├── interview/mysql-questions.md          # 面试回答
├── mistakes/database/transaction.md      # 错误和纠偏
└── sessions/YYYY-MM-DD-xxx.md            # 必要时记录本次会话摘要
```

---

## 目录说明

```text
ai-backend-learning/
├── AGENTS.md
├── START_HERE.md
├── LEARNING_ROADMAP.md
├── INTERVIEW_SPRINT_30_DAYS.md
├── README.md
├── LEARNING_JOURNAL.md
├── sessions/
├── fundamentals/
├── backend/
├── projects/
├── interview/
├── prompts/
├── mistakes/
└── weekly-review/
```

各目录用途：

- `fundamentals/`
  - 计算机基础、算法、操作系统、网络、数据库基础
- `backend/`
  - Java、Spring、MySQL、Redis、MQ、JVM、分布式系统
- `projects/`
  - 结算系统、RAG 系统复盘与深挖
- `interview/`
  - 面试问答、项目表达、真实面试记录和模拟面试记录
- `prompts/`
  - 可复用学习提示词
- `mistakes/`
  - 学习和面试中暴露的问题与纠错记录
- `sessions/`
  - 单次学习会话归档
- `weekly-review/`
  - 每周复盘

---

## 当前状态

- 学习规则：已建立
- 学习路线：已建立
- 互动记录：已建立
- 仓库骨架：已建立
- 恢复学习状态机制：已建立
- 单入口恢复文件：已建立
- 当前执行模式：
  - `1 个月 / 120 小时面试冲刺`
- 当前优先方向：
  - 数据库事务、隔离级别、MVCC
  - MySQL 索引和锁
  - Java 并发 / Spring MVC / `@Transactional`
  - Redis / MQ / 分布式一致性
  - 结算系统和 RAG 项目表达
  - 算法保底
