# NEXT SESSION

## 作用

这是“下次从哪里直接开始”的断点文件。

它不负责记录长期状态，只负责回答：

1. 下次先做什么
2. 不要重复什么
3. 当前有哪些开放问题

---

## START_WITH

从这个问题直接开始：

**Tomcat 为什么能同时处理很多请求，它和线程是什么关系？**

---

## DO_NOT_REPEAT

以下内容已经讲过一轮，下次不要从零重讲：

1. DNS 负责域名到 IP
2. 端口负责定位服务
3. TCP 负责可靠传输
4. HTTP 负责请求 / 响应规则
5. Tomcat 负责接请求
6. `DispatcherServlet` 负责分请求
7. Controller 负责处理请求

---

## OPEN_QUESTIONS

1. Tomcat 为什么能同时处理很多请求
2. Tomcat 和线程模型、线程池的关系
3. Keep-Alive / 长连接与请求处理的关系
4. Servlet 容器和操作系统线程 / IO 的连接点
5. 三次握手 vs TCP 整体机制

---

## READ_IF_CONTINUING_CURRENT_TOPIC

1. `fundamentals/network/http-tcp-request-flow.md`
2. `interview/computer-fundamentals-questions.md`
3. `mistakes/network/request-flow.md`
4. `sessions/2026-05-28-http-tcp-request-flow.md`
