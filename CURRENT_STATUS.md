# CURRENT STATUS

## 作用

这是当前状态的唯一权威面板。

新会话要判断“现在学到哪里、下一步是什么”，优先以这个文件为准。

---

## Snapshot

- 日期：2026-05-28
- 当前 Phase：
  - `Phase 0：建立学习仓库和协作机制`
  - `Phase 1：计算机基础`
- 当前主题：
  - 浏览器请求到 Spring Boot Controller 的完整链路
- 当前状态：
  - 已完成第一轮主链路理解
  - 正准备进入 Tomcat 与线程模型
- 当前最高优先级：
  - 继续网络请求链路主题，过渡到 Tomcat 与线程

---

## 已经掌握

1. DNS 负责域名到 IP 的映射
2. 端口负责定位机器上的具体服务
3. 客户端真正连接的是 `IP:Port`
4. TCP 负责建立可靠传输通道
5. HTTP 负责请求和响应的格式、语义和规则
6. Tomcat 负责监听端口、接收连接、解析 HTTP 请求
7. `DispatcherServlet` 负责统一分发请求
8. Controller 负责具体业务接口处理
9. `spring-boot-starter-web` 会触发 Web 自动配置和内嵌 Tomcat 启动

---

## 仍不稳定

1. 三次握手和 TCP 整体机制的边界
2. Tomcat、Servlet、`DispatcherServlet` 三者的调用关系
3. Tomcat 如何处理高并发请求，以及它和线程池的关系
4. 面试表达还需要进一步压缩和打磨

---

## 当前短板

1. 计算机网络基础刚开始建立主链路，细节还不稳
2. 操作系统中的线程、IO 模型、阻塞 / 非阻塞还未系统展开
3. 数据库事务仍然是已知高优先级短板，但本轮尚未正式攻克

---

## 当前优先级

1. 完成请求链路主题的第一轮闭环
2. 进入 Tomcat 与线程模型
3. 再接操作系统中的线程 / IO 基础
4. 后续回到数据库事务主线

---

## 当前主题文件

1. `fundamentals/network/http-tcp-request-flow.md`
2. `interview/computer-fundamentals-questions.md`
3. `mistakes/network/request-flow.md`
4. `sessions/2026-05-28-http-tcp-request-flow.md`
