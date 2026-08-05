# 2026-08-05 转转集团全栈工程师面试复盘

## 日期

2026-08-05

## 主题

复盘转转集团全栈工程师的限时算法、MySQL 扩展、ToC 订单设计、长任务锁、RAG 排查和表达反馈，并将暴露项回流长期能力与具体任务。

## 本次做了什么

1. 区分会议助手的主观修辞、候选人回答摘要和面试官明确反馈，不把自动纪要评价当作逐字事实。
2. 结合屏幕共享草稿确认相邻交换题的 `X - x` 推导正确，问题在于没有从两阶段 Map 伪代码收敛为一遍扫描的可运行 Java。
3. 将分区批处理经验与 ToC 用户订单列表 / 详情访问路径分开，识别分片键、路由、分页、冷热、跨分片和 SLA 缺口。
4. 重新拆分 6 小时 Redis 锁、数据库长期执行权、任务最大时间和明细幂等的职责。
5. 保留 RAG 分层排查表现，并校准 `Recall@K` 等转写术语。
6. 记录面试官明确提出的表达过长与缺少 ToC 经验，不因单场全栈岗位立即扩张完整前端长期路线。
7. 更新 `RM-05`、`RM-07`、`RM-09`，新增 `BL-031`，并回补 `BL-009`、`BL-002` 与相关 mistakes。

## 关键结论

1. 算法题不是没有找到核心公式，而是正确推导没有在限时内形成可编译、可测试的最终交付。
2. ToC 系统设计必须先从用户列表、详情、峰值 SLA 和降级结果出发，分区、路由表和分库分表只是后续机制。
3. 分区裁剪只能排除无关分区，不能消除跨月查询对全部命中数据的处理成本。
4. 固定 6 小时 TTL 同时存在宕机后长时间阻塞和任务超时后提前失锁两种风险，不能只讲心跳或人工停止。
5. 面试澄清应服务于方案；对方要求独立设计后，应主动声明假设并给出第一版，而不是等待现有架构信息。
6. 当前求职定位不因单场全栈面试改变，前端保持事实边界；算法交付与 ToC 系统设计则具有跨岗位长期价值。

## 下次入口

1. `BL-009`：15 分钟独立重写相邻交换题。
2. `BL-031`：画用户订单列表、详情、运营查询三条访问路径并闭卷设计。
3. `BL-002`：用四层结构重答 6 小时 Redis 锁问题。
4. 当前任务状态与推进顺序以 `LEARNING_BACKLOG.md`、`START_HERE.md` 为准。

## 关联文件

1. `interview/real-records/2026-08-05-zhuanzhuan-fullstack-engineer.md`
2. `mistakes/algorithm/adjacent-swap-live-coding.md`
3. `mistakes/distributed/toc-order-design-without-access-path.md`
4. `mistakes/distributed/redis-lock.md`
5. `mistakes/interview/project-zoom-level-and-listener-alignment.md`
6. `LEARNING_ROADMAP.md`
7. `LEARNING_BACKLOG.md`
8. `START_HERE.md`
