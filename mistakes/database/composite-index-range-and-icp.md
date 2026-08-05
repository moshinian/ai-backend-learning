# 联合索引范围访问、覆盖索引与 ICP 混淆

## 1. 错误表现

1. 对 `WHERE A = 1 AND B > 2 AND C = 3` 能给出 `(A,C,B)`，但使用“物理分区、扫描层次更低”等不准确语言解释联合索引。
2. 把 `(A,B,C)` 直接判断为“不行”，随后又改成 A、B 会走而 C 不走，没有区分搜索区间和索引记录过滤。
3. 不知道 Index Condition Pushdown，并把“使用索引、覆盖索引、ICP、是否回表”混在同一个“走不走索引”问题里。

## 2. 根因

1. 联合索引知识停留在“等值在前、范围在后”的口诀，没有还原 B+ 树按复合 Key 排序后的扫描区间。
2. “走索引”这个词过于模糊，没有拆成定位扫描范围、利用索引列过滤、覆盖查询和读取完整行。
3. 缺少对同一 SQL 在 `(A,C,B)`、`(A,B,C)` 以及 `SELECT A,B,C` / `SELECT *` 下的 `EXPLAIN` 对照实验。

## 3. 正确理解

1. `(A,C,B)` 可以使用 A、C 两个等值条件形成更窄的复合前缀，再对 B 使用范围条件；对这条孤立查询通常比 `(A,B,C)` 更适合。
2. `(A,B,C)` 不是完全不可用。MySQL 可以使用 A 等值和 B 范围构造扫描区间；范围后的 C 通常不能继续缩小这个区间，但 C 仍在索引记录中，可以参与后续过滤。
3. ICP 的目标是：当查询需要读取完整表行时，把只依赖索引列的部分条件交给存储引擎先在索引记录上判断，只对满足条件的记录读取完整行，从而减少回表和引擎 / Server 交互。
4. `SELECT A,B,C` 在 `(A,B,C)` 上可能是覆盖查询，所需列都在二级索引中，本身不需要为了返回列读取聚簇索引。此时不能机械复述“C 通过 ICP 避免回表”；应以实际执行计划为准。
5. `EXPLAIN` 中 `key_len` 用于观察可用于访问的 Key Prefix，`Using index` 常表示覆盖索引，`Using index condition` 表示使用 ICP。三者回答的是不同问题。

官方依据：MySQL 8.4 Reference Manual 的 Index Condition Pushdown 和 Range Optimization 章节。

## 4. 复盘触发条件

1. 联合索引同时出现等值条件和范围条件。
2. 准备说“范围条件之后全部失效”或“某字段不走索引”时。
3. 面试官追问 `key_len`、`Using index`、`Using index condition`、覆盖索引或回表时。
4. 只根据索引列顺序下结论，没有查看选择列、数据分布、排序需求和执行计划时。

## 5. 关联主题

1. `backend/mysql/sql-performance-analysis.md`
2. `interview/mysql-questions.md`
3. `interview/real-records/2026-08-05-tuzhan-ai-platform-backend.md`
4. `LEARNING_BACKLOG.md` 中的 `BL-030`
