# START HERE

## 作用

这是恢复学习进度的单入口文件。

新开 Codex 会话时，优先读取这个文件，不要先扫完整聊天历史。

---

## 恢复顺序

按这个顺序读取：

1. `AGENTS.md`
2. `START_HERE.md`
3. `CURRENT_STATUS.md`
4. `NEXT_SESSION.md`

如果当前主题是网络请求链路，再读取：

5. `fundamentals/network/http-tcp-request-flow.md`
6. `interview/computer-fundamentals-questions.md`
7. `mistakes/network/request-flow.md`

---

## 当前快照

- 当前 Phase：
  - `Phase 0：建立学习仓库和协作机制`，接近完成
  - `Phase 1：计算机基础`，已经开始
- 当前主题：
  - 浏览器请求到 Spring Boot Controller 的完整链路
- 当前下一步：
  - `Tomcat 为什么能同时处理很多请求，它和线程是什么关系？`

---

## 不要重复讲

以下内容已经讲过一轮，下次只需要快速确认，不要从定义重新讲起：

1. DNS 负责域名到 IP
2. 端口负责定位服务
3. TCP 负责可靠传输通道
4. HTTP 负责请求 / 响应规则
5. Tomcat 负责接请求
6. `DispatcherServlet` 负责分请求
7. Controller 负责处理请求

---

## 当前开放问题

1. Tomcat 如何同时处理很多请求
2. Tomcat 和线程、线程池的关系
3. 三次握手 vs TCP 整体机制的边界
4. Tomcat、Servlet、`DispatcherServlet` 的调用关系

---

## 推荐启动提示词

新开 Codex 时，直接输入这段：

```text
先读取 AGENTS.md、START_HERE.md、CURRENT_STATUS.md、NEXT_SESSION.md。
如果当前主题还是网络请求链路，再读取：
fundamentals/network/http-tcp-request-flow.md、
interview/computer-fundamentals-questions.md、
mistakes/network/request-flow.md。
然后继续上次的学习，不要重复讲已经掌握的主链路，
直接从“Tomcat 为什么能同时处理很多请求，它和线程是什么关系”开始。
```
