# Computer Fundamentals Interview Questions

## 1. 一次请求从浏览器到 Spring Controller，大概经历了什么？

### 简洁版

“浏览器先通过 DNS 把域名解析成目标 IP，再根据协议或 URL 确定端口，然后向目标 `IP:Port` 发起 TCP 连接。三次握手成功后，在连接上发送 HTTP 请求。服务端 Tomcat 监听端口并解析 HTTP 请求，再交给 Spring MVC 的 `DispatcherServlet` 分发到具体 Controller。”

### 深挖版

可以从两层回答：

1. 网络层
   - DNS 解析域名
   - IP 定位目标机器
   - 端口定位机器上的具体服务
   - TCP 建立可靠连接
   - HTTP 定义请求 / 响应内容
2. 框架层
   - Tomcat 接收请求并解析 HTTP
   - `DispatcherServlet` 做统一调度
   - Controller 处理业务逻辑

---

## 2. DNS 和端口分别解决什么问题？

### 简洁版

“DNS 负责把域名解析成 IP，解决的是如何找到目标机器；端口负责定位一台机器上的具体服务，解决的是请求交给哪个进程处理。”

### 深挖版

可以记成一句话：

- IP 找机器
- 端口找服务

补充：

1. DNS 不决定端口
2. 端口可能来自协议默认约定，也可能来自显式配置

---

## 3. 为什么先 TCP 再 HTTP？

### 简洁版

“因为 HTTP 是应用层协议，TCP 是传输层协议。对基于 TCP 的 HTTP 来说，必须先建立好 TCP 连接，HTTP 报文才能在这条连接上传输。”

### 深挖版

不要答成“因为服务端忙不忙”。

本质是：

1. TCP 先提供可靠传输通道
2. HTTP 再在这个通道上定义请求和响应格式

所以这体现的是协议分层关系。

---

## 4. 如果 TCP 已经能传数据了，为什么还需要 HTTP？

### 简洁版

“因为 TCP 只解决可靠传输，不解决应用层语义问题。HTTP 进一步定义了请求方法、路径、头部、状态码、消息体这些规则，让双方能够把字节流解释成标准的 Web 请求和响应。”

### 深挖版

只有 TCP 也能通信，但没有 HTTP 时：

1. 双方只能传字节流
2. 没有统一的请求 / 响应语义
3. 无法形成标准化的 Web 交互模型

HTTP 的价值不是替代 TCP，而是在 TCP 之上建立统一应用层协议。

---

## 5. 为什么互联网里广泛使用 HTTP，而不是每个系统都自定义协议？

### 简洁版

“因为 HTTP 是标准化协议，能显著降低系统之间的互通成本，而且浏览器、网关、代理、调试工具和服务框架都有成熟支持，所以生态优势很强。”

### 深挖版

核心原因有三点：

1. 标准化
   - 不需要每个系统单独适配私有协议
2. 生态成熟
   - 浏览器、Nginx、Tomcat、Postman、curl 等都支持
3. 语义统一
   - 方法、状态码、头部、消息体都有共同规则

---

## 6. Tomcat、DispatcherServlet、Controller 分别负责什么？

### 简洁版

- Tomcat：监听端口、接收连接、解析 HTTP 请求
- `DispatcherServlet`：统一接收并分发请求
- Controller：处理具体业务接口

### 深挖版

职责边界：

1. Tomcat 是 Web 容器，负责承载 Web 请求
2. `DispatcherServlet` 是 Spring MVC 前端控制器，负责调度处理链
3. Controller 是业务入口，不负责监听网络，也不负责底层协议解析

---

## 7. Tomcat、Servlet、DispatcherServlet 三者是什么关系？

### 简洁版

“Tomcat 是 Servlet 容器，Servlet 是 Java Web 处理请求的规范，`DispatcherServlet` 是 Spring MVC 基于 Servlet 规范实现的统一请求入口。请求先到 Tomcat，再由 Tomcat 调用 Servlet 链路，最后进入 `DispatcherServlet` 分发到 Controller。”

### 深挖版

可以这样拆：

1. Tomcat 负责监听端口、接收连接、解析 HTTP，并管理 Servlet 生命周期
2. Servlet 定义了 Java Web 请求处理组件的标准接口
3. `DispatcherServlet` 是 Spring MVC 的核心 Servlet，不负责网络 IO，只负责 MVC 层的路由、参数绑定、拦截器、返回值和异常处理
4. Controller 是 Spring MVC 分发后的业务方法，不是 Servlet

---

## 8. 为什么没有 Tomcat，浏览器通常不能直接访问 Spring MVC + Controller？

### 简洁版

“因为 Spring MVC 和 Controller 不具备监听端口、接收 TCP 连接和解析 HTTP 请求的能力，它们依赖 Tomcat 这类 Web 容器先把请求接住，再分发到框架层。”

### 深挖版

没有 Tomcat 时，通常缺少：

1. 端口监听
2. HTTP 报文解析
3. Servlet 容器承载环境
4. 请求接入和响应返回能力

所以 Controller 不是直接面向网络的组件。

---

## 9. 为什么 Spring Boot 没手写监听代码也能通过 `localhost:8080` 被访问？

### 简洁版

“因为引入 `spring-boot-starter-web` 后，Spring Boot 会自动配置 Web 环境，并启动内嵌 Tomcat。真正监听 `8080` 的是 Tomcat，不是 Controller。”

### 深挖版

核心链路：

1. 引入 `spring-boot-starter-web`
2. Spring Boot 识别当前应用是 Web 应用
3. 自动配置 Spring MVC
4. 自动装配并启动内嵌 Tomcat
5. 注册 `DispatcherServlet`
6. 请求因此可以从端口进入并分发到 Controller

---

## 10. Keep-Alive 长连接会一直占用 Tomcat 工作线程吗？

### 简洁版

“不会。TCP 连接存在不等于 Tomcat 工作线程一直被占用。Tomcat NIO 模型下，Keep-Alive 空闲连接主要由 Poller 监听 IO 事件，只有连接上有请求数据可读，并进入 HTTP 解析、Servlet、Controller 业务处理时，才会占用工作线程。”

### 深挖版

真正容易拖垮 Tomcat 的不是空闲长连接，而是大量同步慢请求。

例如 RAG 问答接口同步等待大模型 20 秒：

1. 每个请求会长时间占用一个 Tomcat 工作线程
2. 工作线程被占满后，新请求只能排队
3. CPU 不一定高，但接口会变慢、超时甚至不可用

优化方向：

1. 对问答生成使用 SSE 流式响应或异步客户端
2. 对文档解析、知识库构建使用 taskId + 后台任务 + 状态轮询
3. 配合限流、超时、熔断、独立业务线程池或 MQ

---

## 11. Filter 和 Interceptor 有什么区别？

### 简洁版

“Filter 属于 Servlet 规范，由 Tomcat 这类容器执行，位置在 `DispatcherServlet` 之前。Interceptor 属于 Spring MVC，位置在 `DispatcherServlet` 之后、Controller 之前。Filter 更偏容器层，Interceptor 更偏业务框架层。”

### 深挖版

执行顺序：

```text
Tomcat
  -> Filter 链
  -> DispatcherServlet
  -> Interceptor.preHandle()
  -> Controller
  -> Interceptor.postHandle()
  -> Interceptor.afterCompletion()
  -> Filter 返回阶段
```

常见用途：

1. Filter：编码、CORS、日志、请求包装、认证入口
2. Interceptor：登录校验、权限、接口耗时、业务上下文

注意：

1. Filter 不是 Tomcat 私有方法，而是 Servlet 规范的一部分
2. Filter 是否执行取决于 URL 匹配规则
3. Interceptor 主要拦截进入 Spring MVC 并匹配到 Handler 的请求

---

## 12. 面试官可能继续追问什么？

1. 三次握手为什么不是两次？
2. TCP 和 HTTP 分别位于哪一层？
3. 如果只有 IP 没有端口会怎样？
4. Tomcat 为什么能监听端口？
5. `DispatcherServlet` 为什么不是直接业务代码？
6. `spring-boot-starter-web` 去掉后项目会发生什么？
7. Keep-Alive 空闲连接为什么不一直占用工作线程？
8. RAG 大模型调用很慢时，如何避免 Tomcat 工作线程被打满？
9. Filter、Interceptor、Controller 的执行顺序是什么？
