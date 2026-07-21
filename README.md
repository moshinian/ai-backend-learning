# AI BACKEND LEARNING

这个仓库用于沉淀 AI Backend / Java 后端学习过程。

目标不是堆资料，而是把学习过程整理成：

1. 长期能力地图
2. 柔性学习任务池
3. 可恢复的学习断点
4. 可复盘的知识笔记
5. 可复用的面试表达
6. 可追踪的错误记录
7. 可维护的求职简历源稿

---

## 1. 当前文档机制

当前仓库采用：

```text
AGENTS.md
+ START_HERE.md
+ LEARNING_ROADMAP.md
+ LEARNING_BACKLOG.md
+ LEARNING_JOURNAL.md
```

五个核心 / 支撑文件协作。

| 文件 | 职责 |
|---|---|
| `AGENTS.md` | 文档规则中心，定义文件职责、最小格式和归档规则 |
| `START_HERE.md` | 新会话恢复入口，记录当前候选任务、断点和下一步 |
| `LEARNING_ROADMAP.md` | 长期能力地图，记录长期需要建设的能力模块 |
| `LEARNING_BACKLOG.md` | 柔性学习任务池，记录当前可执行任务和验收标准 |
| `LEARNING_JOURNAL.md` | 长期学习画像、阶段性反思、长期误区和历史索引 |

当前状态权威顺序：

1. 新会话恢复入口以 `START_HERE.md` 为准。
2. 任务优先级、状态、验收标准、当前断点和下一步动作以 `LEARNING_BACKLOG.md` 为准。
3. `sessions/`、`interview/real-records/` 中的“下次入口 / 后续任务”只表示当次历史归档，不表示当前仍然有效。

---

## 2. 新会话恢复方式

开始新会话时，优先读取：

1. `START_HERE.md`
2. `LEARNING_BACKLOG.md`

需要判断长期能力方向时，再读取：

1. `LEARNING_ROADMAP.md`

需要确认文档写法时，再读取：

1. `AGENTS.md`

---

## 3. 文档流转规则

| 内容类型 | 写入位置 |
|---|---|
| 长期能力方向 | `LEARNING_ROADMAP.md` |
| 具体可执行学习任务 | `LEARNING_BACKLOG.md` |
| 当前恢复状态 | `START_HERE.md` |
| 单次学习摘要 | `sessions/` |
| 后端技术主笔记 | `backend/` |
| 基础知识主笔记 | `fundamentals/` |
| 项目深挖 | `projects/` |
| 面试表达、真实面试复盘、模拟面试 | `interview/` |
| 求职简历源稿 | `resume/` |
| 错误、误区、纠偏 | `mistakes/` |
| 长期学习画像、阶段性反思、历史索引 | `LEARNING_JOURNAL.md` |
| 可运行学习实验代码 | `labs/` |

---

## 4. 目录职责

- `backend/`
  - 后端技术主笔记，例如 Java、Spring、MySQL、Redis、MQ、JVM、分布式系统
- `fundamentals/`
  - 基础知识主笔记，例如算法、数据结构、操作系统、网络、数据库基础
- `projects/`
  - 项目链路、设计取舍、工程亮点和项目深挖
- `interview/`
  - 面试问答、项目表达、真实面试记录、模拟面试记录
- `resume/`
  - Java 后端和 AI 应用等平行岗位版本的求职简历源稿；版本控制中不保存私人联系方式
- `mistakes/`
  - 学习和面试中暴露的问题、误区和纠偏
- `sessions/`
  - 单次学习会话摘要和历史归档
- `labs/`
  - 可运行学习实验代码，只用于验证机制，不替代正式项目深挖或主题知识笔记

---

## 5. 使用原则

1. `START_HERE.md` 只做恢复入口，不写长篇知识内容。
2. `LEARNING_BACKLOG.md` 负责当前任务调度，不写成长篇知识笔记。
3. `LEARNING_ROADMAP.md` 负责长期能力地图，不写任务状态和断点。
4. `LEARNING_JOURNAL.md` 负责长期画像和反思，不做任务调度。
5. 主题知识沉淀到对应目录，避免复制到多个文件。
