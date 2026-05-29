# Request Flow Mistakes

## 1. 当前主题

浏览器请求到 Spring Boot / Spring MVC 的完整链路。

---

## 2. 本次暴露出的错误和偏差

### 错误 1：把请求链路理解成只发生在 Spring MVC 内部

错误倾向：

- 认为请求主要是 URL 进来后由 Controller 分发和处理

问题：

- 忽略了 DNS、IP、端口、TCP、Tomcat、内核协议栈

修正：

- 请求链路不是从 Controller 开始，而是从客户端网络访问开始

---

### 错误 2：认为 DNS 能解决服务定位问题

错误倾向：

- 只知道 DNS 解析域名，但没有区分 IP 和端口的作用

修正：

- DNS 负责域名到 IP
- 端口负责定位机器上的具体服务

记忆法：

- IP 找机器
- 端口找服务

---

### 错误 3：把 TCP 三次握手和 TCP 整体机制混在一起

错误倾向：

- 说三次握手不仅确认连接，还包括失败重试机制

问题：

- 三次握手主要负责建立连接
- 重传、顺序保证、可靠传输属于 TCP 的整体机制

修正：

- 三次握手解决建连
- TCP 整体机制解决可靠传输

---

### 错误 4：把“先 TCP 再 HTTP”的原因解释成服务端忙不忙

错误倾向：

- 认为先 TCP 后 HTTP 是因为要先看看服务端能不能处理请求

问题：

- 这不是核心本质

修正：

- 先 TCP 再 HTTP，是因为 HTTP 报文要依附在已建立的 TCP 连接上传输
- 这是协议分层关系决定的

---

### 错误 5：误认为 Spring MVC 在 Tomcat 之前

错误倾向：

- 把 Spring MVC 和 Tomcat 说成前后顺序关系

问题：

- 这会混淆容器层和框架层

修正：

- Tomcat 是 Web 容器
- Spring MVC 是运行在 Tomcat 之上的 Web 框架

---

### 错误 6：把 Controller 说成处理“事务”

错误倾向：

- 把业务处理泛化为“事务”

问题：

- “事务”在后端语境里通常指数据库事务，不能随便替代“业务逻辑”

修正：

- Controller 是业务接口入口
- 真正事务语义要谨慎使用

---

### 错误 7：把 Tomcat 说成参与 TCP 三次握手确认

错误倾向：

- 说“Tomcat 和客户端进行 TCP 确认”

问题：

- TCP 三次握手主要由操作系统内核协议栈完成
- Tomcat 监听端口并处理连接上的应用层数据，不是亲自处理每个握手包

修正：

- 内核协议栈完成 TCP 建连
- Tomcat 作为监听该端口的进程，接收已建立连接上的请求数据

---

### 错误 8：把 socket 字节流说成字节码

错误倾向：

- 说“Tomcat 监听 TCP 连接上的字节码”

问题：

- 字节码通常指 JVM 执行的 `.class` 指令
- 网络连接上传输的是字节流

修正：

- Tomcat 监听 socket 上的字节流，并解析成 HTTP 请求

---

### 错误 9：认为 Keep-Alive 长连接会一直占用 Tomcat 工作线程

错误倾向：

- 把 TCP 连接存在和工作线程占用绑定在一起

修正：

- TCP 连接存在不等于工作线程一直占用
- Tomcat NIO 下，空闲 Keep-Alive 连接主要由 Poller 监听 IO 事件
- 有请求数据可读并进入业务处理时，才占用工作线程

---

### 错误 10：把 Filter 说成 Tomcat 内部方法

错误倾向：

- 说 Filter 是 Tomcat 内部的方法，所有请求都会无一例外走 Filter

问题：

- Filter 属于 Servlet 规范，不是 Tomcat 私有方法
- 请求是否经过某个 Filter，取决于该 Filter 的 URL 匹配规则

修正：

- Filter 是 Servlet 容器层机制，在 `DispatcherServlet` 之前执行
- Interceptor 是 Spring MVC 层机制，在 `DispatcherServlet` 之后、Controller 之前执行

---

## 3. 当前已经建立的正确理解

1. DNS 负责把域名解析成 IP
2. 端口用于定位具体服务
3. TCP 负责建立可靠传输通道
4. HTTP 负责请求和响应的格式、语义和规则
5. Tomcat 负责接收请求
6. `DispatcherServlet` 负责分发请求
7. Controller 负责处理请求
8. `spring-boot-starter-web` 会触发 Web 自动配置和内嵌 Tomcat 启动
9. TCP 三次握手主要由操作系统内核协议栈完成
10. Keep-Alive 空闲连接不长期占用 Tomcat 工作线程
11. Filter 属于 Servlet 规范，Interceptor 属于 Spring MVC

---

## 4. 后续复习重点

1. 三次握手为什么不是两次
2. 异步化设计表达：业务线程池、MQ、SSE、轮询分别适合什么场景
3. Tomcat 与操作系统 IO、线程调度的连接点
4. 请求链路如何迁移到 MySQL 事务和一致性表达
