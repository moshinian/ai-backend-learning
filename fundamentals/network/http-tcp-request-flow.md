# HTTP / TCP / 请求链路

## 1. 这个知识点在解决什么问题

做 Java 后端时，如果只知道“请求到了 Controller”，会很难判断这些真实问题：

1. 为什么接口超时了？
2. 为什么域名能访问，但 IP 或端口不对就访问不了？
3. 为什么 Spring Boot 没写监听代码，却能通过浏览器访问？
4. 为什么 Tomcat、Spring MVC、Controller 明明都在处理请求，但职责不同？

这个主题的目标，就是把：

- DNS
- IP
- 端口
- TCP
- HTTP
- Tomcat
- Spring MVC
- Controller

串成一条完整链路。

---

## 2. 一次请求的完整主链路

以这个地址为例：

```text
https://example.com/api/order
```

大致过程如下：

1. 浏览器先解析域名 `example.com`
2. DNS 返回目标 IP
3. 浏览器根据 `https` 知道默认端口是 `443`
4. 浏览器向目标 `IP:443` 发起 TCP 连接
5. 三次握手成功，连接建立
6. 浏览器在这条 TCP 连接上发送 HTTP 请求
7. 服务端网卡收到数据
8. 操作系统内核处理网络协议栈
9. 内核根据目标端口把请求交给监听该端口的进程
10. 例如 Tomcat 接收并解析 HTTP 请求
11. Tomcat 把请求交给 Spring MVC 的 `DispatcherServlet`
12. `DispatcherServlet` 再路由到具体 Controller
13. Controller 调用业务逻辑并返回结果
14. 响应再沿原链路返回客户端

---

## 3. URL 里的信息分别有什么作用

以：

```text
https://example.com/api/order
```

为例：

| 部分 | 示例 | 作用 |
|---|---|---|
| 协议 | `https` | 指定应用层通信规则，并提供默认端口信息 |
| 主机名 | `example.com` | 需要通过 DNS 解析成 IP |
| 路径 | `/api/order` | 请求进入应用后，用于路由分发 |

关键点：

1. 机器真正通信靠的是 IP，不是域名
2. 路径不是给 DNS 或 TCP 用的，而是给 HTTP / Spring MVC 路由用的
3. 协议不仅决定“怎么通信”，还常常隐含默认端口

---

## 4. DNS、IP、端口分别解决什么问题

### 4.1 DNS

本质：

DNS 负责把域名解析成 IP。

它解决的问题是：

- 人适合记域名
- 机器适合按 IP 通信

注意：

- DNS 不负责决定端口
- DNS 只解决“去哪台机器”

### 4.2 IP

本质：

IP 用于定位目标机器。

### 4.3 端口

本质：

端口用于定位一台机器上的具体服务。

可以这样记：

- IP 找机器
- 端口找机器上的服务

端口来源可能有三种：

1. 协议默认端口
   - HTTP 默认 `80`
   - HTTPS 默认 `443`
2. URL 显式指定
   - `http://127.0.0.1:8080`
3. 服务自身配置的监听端口
   - 例如 Spring Boot 配置 `server.port=8080`

---

## 5. TCP 和 HTTP 分别解决什么问题

| 协议 | 层次 | 解决的问题 |
|---|---|---|
| TCP | 传输层 | 建立可靠传输通道 |
| HTTP | 应用层 | 定义请求和响应的格式、语义和交互规则 |

### 5.1 TCP

TCP 主要解决：

1. 连接怎么建立
2. 数据怎么可靠送达
3. 顺序怎么保证
4. 丢包后怎么重传

一句话：

TCP 负责“把数据稳定送过去”。

### 5.2 HTTP

HTTP 主要解决：

1. 请求方法怎么表达
2. 资源路径怎么表达
3. 请求头和请求体怎么组织
4. 响应状态怎么表达
5. 返回结果如何标准化

一句话：

HTTP 负责“送过去的数据该怎么理解”。

### 5.3 为什么只有 TCP 还不够

只有 TCP 也能通信，因为 TCP 本身就能传输字节流。

但如果没有 HTTP：

1. 双方虽然能传字节
2. 却没有统一的应用层语义
3. 不知道哪些字节代表请求方法、路径、状态码、消息体

所以：

TCP 不替代 HTTP，HTTP 也不替代 TCP。

两者是分层协作关系。

---

## 6. TCP 为什么先于 HTTP

对基于 TCP 的 HTTP 来说：

1. 先建立 TCP 连接
2. 再在连接上发送 HTTP 请求

原因不是“服务端忙不忙”，而是：

1. HTTP 是应用层协议
2. TCP 是传输层协议
3. HTTP 报文必须依附在已建立好的 TCP 连接上传输

所以“先 TCP 再 HTTP”本质上是协议分层决定的。

---

## 7. 三次握手在解决什么问题

三次握手不是简单打招呼。

它主要解决：

1. 双方确认连接建立
2. 双方确认基本具备发送和接收能力
3. 避免历史残留连接请求造成误判

注意：

- 三次握手负责建立连接
- 重传、顺序保证等是 TCP 的整体机制，不是三次握手单独完成的

---

## 8. Tomcat、DispatcherServlet、Controller 的职责边界

### 8.1 Tomcat

Tomcat 负责：

1. 监听端口
2. 接收 TCP 连接
3. 解析 HTTP 请求
4. 按 Servlet 规范承载请求

### 8.2 DispatcherServlet

`DispatcherServlet` 是 Spring MVC 的统一入口，负责：

1. 接收容器转交的请求
2. 路由到合适的处理链
3. 参数绑定
4. 调用 Controller
5. 处理返回值和异常

### 8.3 Controller

Controller 负责：

1. 接收已经进入框架层的请求
2. 作为业务接口入口
3. 调用 Service 完成业务逻辑
4. 返回响应结果

一句话总结：

- Tomcat 负责接请求
- `DispatcherServlet` 负责分请求
- Controller 负责处理请求

---

## 9. 为什么 Spring Boot 没手写监听代码也能对外提供 HTTP 服务

因为引入了：

```text
spring-boot-starter-web
```

Spring Boot 会把应用识别成 Web 应用，并自动完成：

1. Web 环境自动配置
2. Spring MVC 自动配置
3. 内嵌 Tomcat 自动装配与启动
4. `DispatcherServlet` 注册

所以真正监听端口的不是 Controller，而是内嵌 Tomcat。

如果去掉 `spring-boot-starter-web`：

1. 应用可能只剩下普通 Spring Bean 和 Controller 定义
2. 但没有完整的 Web 容器支持
3. 没有端口监听
4. 没有请求分发链路
5. `localhost:8080` 很可能访问不了

---

## 10. 结合项目怎么表达

在 Spring Boot 项目里，例如一个 `DocumentController`：

错误表达：

- 请求到了 Controller，然后处理返回

更好的工程表达：

- 客户端通过 HTTP 请求访问服务端监听端口
- 请求先由内嵌 Tomcat 接收并解析
- 再交给 Spring MVC 的 `DispatcherServlet`
- 由它根据路径分发到具体 Controller
- Controller 再调用业务逻辑并返回结果

这类表达更能体现你理解的是完整请求链路，而不只是框架表面。

---

## 11. 面试回答模板

### 11.1 简洁版

“浏览器访问 Spring Boot 接口时，先通过 DNS 把域名解析成目标 IP，再根据协议或显式配置确定目标端口。客户端随后向目标 `IP:Port` 发起 TCP 连接，三次握手成功后，在这条连接上发送 HTTP 请求。服务端由 Tomcat 这类 Web 容器监听端口、接收连接并解析 HTTP 请求，再把请求交给 Spring MVC 的 `DispatcherServlet` 做统一分发，最后路由到具体的 Controller 处理业务逻辑并返回响应。”

### 11.2 深挖版

“这个过程可以分成网络层和框架层。网络层上，DNS 负责域名到 IP 的映射，端口负责定位机器上的具体服务，TCP 负责建立可靠连接，HTTP 负责定义请求和响应的语义与格式。框架层上，Tomcat 作为 Web 容器负责监听端口、接收 TCP 连接并解析 HTTP 报文，然后按 Servlet 规范把请求交给 Spring MVC 的 `DispatcherServlet`。`DispatcherServlet` 作为前端控制器负责路由匹配、参数绑定、拦截器执行、调用 Controller、返回值处理和异常处理，最终再把结果响应给客户端。”
