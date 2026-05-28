# Session 2026-05-28

## 主题

浏览器请求到 Spring Boot Controller 的完整链路。

---

## 本次核心收获

1. 建立了 `DNS -> IP -> 端口 -> TCP -> HTTP -> Tomcat -> DispatcherServlet -> Controller` 的完整主链路
2. 区分了 TCP 和 HTTP 的职责边界
3. 区分了 Tomcat、`DispatcherServlet`、Controller 的职责边界
4. 理解了为什么 Spring Boot 不手写监听代码也能通过 `localhost:8080` 提供 HTTP 服务

---

## 本次暴露的误区

1. 容易把请求链路只理解成 Spring MVC 内部流程
2. 容易把三次握手和 TCP 整体机制混在一起
3. 容易把“先 TCP 再 HTTP”解释成服务端忙不忙，而不是协议分层
4. 对 Tomcat、Servlet、`DispatcherServlet` 的关系还没有完全内化

---

## 当前掌握程度

### 已能讲清

1. DNS 和端口分别解决什么问题
2. 为什么先 TCP 再 HTTP
3. 为什么没有 Tomcat 浏览器通常不能直接访问 Controller
4. Tomcat、`DispatcherServlet`、Controller 的基础分工

### 仍需继续

1. Tomcat 如何处理高并发请求
2. Tomcat 与线程模型、线程池的关系
3. Keep-Alive / 长连接与请求处理

---

## 下次起点

直接进入：

**Tomcat 为什么能同时处理很多请求，它和线程是什么关系？**
