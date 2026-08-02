# Java 8、11、17、21 最小版本能力卡

## 1. 本质

Java 版本学习的目标不是背完整 JEP 清单，而是为常见 LTS 版本建立少量可检索入口：知道代表能力解决什么问题、代码如何表达，以及哪些特性容易说错版本或夸大边界。

本笔记选择 Java 8、11、17、21 各一到两个高复用能力，服务于 Java 后端开发、版本升级判断和面试表达。

## 2. 解决的问题

1. 避免只用“性能更好、GC 更稳定”等模糊语言描述版本差异。
2. 能从代码可读性、标准库、类型建模、模块封装和并发执行模型解释版本价值。
3. 面对不知道的完整版本清单时，仍能先给出少量准确事实，再说明需要从构建配置、父 POM 或 BOM 核实项目版本。

## 3. 机制

### 3.1 Java 8：Lambda 与 Stream

Lambda 是函数式接口实现的简洁写法。它不限于 `Runnable`，只要目标接口只有一个抽象方法，就可以用 Lambda 提供该方法的实现。

```java
Runnable task = () -> System.out.println("执行任务");

task.run();
```

给变量赋值时只创建并保存行为，不会立刻执行，也不会自动创建新线程。`task.run()` 由当前线程普通调用；`new Thread(task).start()` 才会启动新线程。

Stream 为集合处理提供声明式流水线：

```java
int total = orders.stream()
        .filter(order -> order.isPaid())
        .mapToInt(order -> order.getAmount())
        .sum();
```

```text
filter：决定是否保留元素
map：把元素转换成另一种表示
sum / collect：触发流水线并产生最终结果
```

Stream 默认读取和处理原数据，不会因为 `filter()` 自动删除原集合中的元素。代码仍应避免在流水线中加入难以推理的共享可变状态和副作用。

### 3.2 Java 11：String API 与标准 HttpClient

Java 11 增加了常用字符串能力：

```java
"   ".isEmpty(); // false，只判断长度是否为 0
"   ".isBlank(); // true，空串或只包含空白字符

"  hello  ".strip();
"ab".repeat(3);
"a\nb".lines();
```

Java 11 还标准化了 `java.net.http.HttpClient`：

```java
HttpClient client = HttpClient.newHttpClient();

HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://example.com"))
        .GET()
        .build();

HttpResponse<String> response = client.send(
        request,
        HttpResponse.BodyHandlers.ofString()
);
```

`send()` 同步等待响应；`sendAsync()` 返回 `CompletableFuture<HttpResponse<T>>`。`CompletableFuture` 表示未来才会完成的结果，并支持使用 `thenApply()`、`thenRun()`、`allOf()` 等方式组合异步步骤。`get()` 或 `join()` 会等待结果，但 `CompletableFuture` 本身不等于并发安全，也不保证每个任务都创建新线程。

### 3.3 Java 17：密封类型与 JDK 内部强封装

密封类和密封接口通过 `sealed` 与 `permits` 限定允许的子类型：

```java
public sealed interface PaymentResult
        permits PaymentSuccess, PaymentFailure {
}

public final class PaymentSuccess implements PaymentResult {
}

public final class PaymentFailure implements PaymentResult {
}
```

被允许的直接子类型必须继续声明为 `final`、`sealed` 或 `non-sealed`，明确继承层级是否关闭、继续受限或重新开放。它适合支付结果、指令类型等合法分支有限的领域模型。

Java 17 还进一步强封装 JDK 内部实现。旧框架如果通过深度反射访问 `java.base` 中未开放的包，可能出现 `InaccessibleObjectException`。优先处理方式是升级依赖并改用公开 API；`--add-opens` 只适合作为兼容旧依赖的临时措施。

强封装不等于禁止所有反射。普通 classpath 项目通常仍可反射访问自己的业务类；重点限制的是未经开放就跨模块深度访问 JDK 内部实现。还要注意版本归属：Records 和 `instanceof` 模式匹配在 Java 16 正式发布，不能严格说成 Java 17 首次引入。

### 3.4 Java 21：虚拟线程与 switch 模式匹配

虚拟线程是由 JDK 实现、JVM 调度的轻量级线程。大量虚拟线程可以在较少的平台线程上执行；阻塞式 I/O 等待期间，运行时可以挂起虚拟线程，让承载线程执行其他任务。

```java
Thread.startVirtualThread(() -> callRemoteService());

try (ExecutorService executor =
             Executors.newVirtualThreadPerTaskExecutor()) {
    executor.submit(() -> callRemoteService());
    executor.submit(() -> queryDatabase());
}
```

虚拟线程降低大量阻塞式任务的线程资源成本，使传统同步代码更容易扩展到高并发 I/O 场景。它不会让 CPU 密集计算自动变快，也不会扩大数据库连接池、下游接口和磁盘的容量；连接池、限流、超时和并发安全仍然需要独立设计。

Java 21 的 `switch` 模式匹配允许直接按对象类型匹配并绑定变量：

```java
return switch (result) {
    case PaymentSuccess success -> success.getReceiptNo();
    case PaymentFailure failure -> failure.getReason();
};
```

`case PaymentSuccess success` 同时完成类型判断和变量绑定，不需要再手动执行强制类型转换。它与密封类型配合时，编译器还能检查合法子类型是否被完整覆盖。

## 4. 边界

1. 不把“当前项目运行在某版本”与“某特性首次在该版本发布”混为一谈。
2. Lambda 不代表异步，Stream 不代表并行；是否并发取决于调用方式和执行器。
3. `CompletableFuture` 用于表示和编排异步结果，不替代锁、信号量、限流和业务幂等。
4. Java 17 强封装不等于完全禁止反射；`--add-opens` 也不是长期依赖治理方案。
5. 虚拟线程优化的是高并发阻塞任务的线程成本，不消除 CPU、数据库连接和下游容量上限。
6. Preview 和 Incubator 能力不能直接包装为稳定生产特性；严格回答版本问题时应核对官方发布清单。

## 5. 工程关联

1. Lambda 和 Stream 适合表达集合筛选、转换和聚合，但结算批处理中仍要评估可读性、异常处理、内存占用和副作用。
2. Java 11 `HttpClient` 可以作为标准 HTTP 接入入口；生产场景仍需补齐连接复用、超时、重试、幂等、鉴权和可观测性。
3. Java 17 升级时，旧版 Spring、ORM、序列化或字节码框架可能因为深度反射 JDK 内部实现而暴露兼容问题，应先核对依赖矩阵。
4. Java 21 虚拟线程适合大量 HTTP、JDBC 等阻塞式调用，但结算系统仍必须用连接池、状态机、批次边界和下游限流保护真实资源。

## 6. 面试表达入口

> Java 8 的代表能力是 Lambda 和 Stream，前者简化函数式接口实现并支持传递行为，后者提供声明式的数据筛选、转换和聚合。Java 11 增强了 String API，并标准化了支持同步和异步调用的 HttpClient。Java 17 引入密封类型，通过 `sealed` 和 `permits` 限制继承范围，同时加强了 JDK 内部实现的封装。Java 21 正式引入虚拟线程，降低大量阻塞式 I/O 任务的线程成本；还支持 `switch` 模式匹配，可以按对象类型匹配并直接绑定变量。

关联任务：`LEARNING_BACKLOG.md` 中的 `BL-024`。
