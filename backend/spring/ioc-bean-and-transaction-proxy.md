# Spring IOC、Bean 与事务代理

## 1. 本质

Spring IOC 的核心不是减少 `new`，而是把对象创建、依赖装配、生命周期和扩展入口交给容器统一管理。

依赖注入是 IOC 的实现方式之一：业务对象声明自己依赖什么，由容器提供实际对象。事务、缓存、权限、日志等横切能力则通常通过 AOP 代理围绕 Bean 方法调用生效。

## 2. 解决的问题

1. 降低业务类和具体实现之间的耦合。
2. 统一管理对象生命周期和作用域。
3. 方便替换实现、隔离测试和集中配置。
4. 为事务、缓存和其他 AOP 能力提供代理入口。

依赖注入本身不保证设计合理。一个 Bean 依赖过多对象，仍然可能说明职责过重。

## 3. Bean 创建与生命周期机制

默认非懒加载 singleton Bean 通常在 `ApplicationContext` 初始化过程中创建；`@Lazy` singleton 通常在首次获取或依赖解析时创建；prototype Bean 在每次向容器请求时创建。

常见生命周期主线：

```text
实例化
-> 属性填充和依赖注入
-> Aware 回调
-> BeanPostProcessor 初始化前处理
-> @PostConstruct 等初始化回调
-> BeanPostProcessor 初始化后处理
-> 必要时暴露代理对象
-> Bean 对外使用
-> 容器关闭时执行受管理的销毁回调
```

作用域常见边界：

1. `singleton`：同一容器、同一 Bean 定义通常共享一个实例。
2. `prototype`：每次请求 Bean 通常创建新实例。
3. Web 环境还可能有 request、session 等作用域。

Spring 对 prototype 通常只负责创建、依赖注入和初始化，不自动跟踪实例直至销毁。文件、连接、线程等外部资源应由使用方通过 `try-with-resources`、`close()` 或独立生命周期组件释放。

## 4. AOP 与事务代理机制

### 4.1 注解、Pointcut、Advisor 和代理 Bean

AOP 解决的是日志、事务、权限、缓存、监控等逻辑在多个业务方法中重复出现的问题。它把这些横切逻辑从业务方法中拆出，并在符合条件的方法调用前后统一执行。

一个普通注解只有元数据能力，不会天然产生 AOP 增强。注解要具备 AOP 能力，必须有对应的 Spring 基础设施：

1. 有代码扫描类或方法上的注解，并把它转换为可执行的 Advice。
2. 有 Pointcut 判断哪些 Bean、哪些方法匹配。
3. 有 Advisor 把“在哪里增强”和“执行什么增强”组合起来。
4. 自动代理创建器在 Bean 生命周期的后处理阶段，为命中 Advisor 的 Bean 返回代理对象。

可以先把三个概念压缩为：

```text
Pointcut：选择在哪里增强
Advice：定义增强时执行什么
Advisor：把 Pointcut 和 Advice 组合起来
```

`candidateAdvisors` 不是写死的一组系统拦截器，而是当前容器中可能参与匹配的 Advisor 候选。它们既可能来自 Spring 事务、缓存等基础设施，也可能来自用户声明的 `@Aspect`。`@Before`、`@Around`、`@After` 等表示不同的 Advice 执行时机；同一个 `@Aspect` 可以声明多个 Advice，Spring 会把相应切面方法转换为可参与匹配和排序的 Advisor。

“代理整个 Bean”是指容器对外暴露的是包裹目标对象的代理对象，而不是为某一个方法单独创建对象。代理对象可以接收这个 Bean 的多个方法调用，但每次调用仍会按当前方法重新匹配拦截器链；没有命中 Pointcut 的方法可以直接进入目标方法，不代表 Bean 上所有方法都会执行相同增强。

### 4.2 JDK 动态代理与 CGLIB

JDK 动态代理根据接口创建代理对象，核心 API 可以简化为：

```java
Service proxy = (Service) Proxy.newProxyInstance(
        Service.class.getClassLoader(),
        new Class<?>[]{Service.class},
        (proxyObject, method, methodArgs) -> {
            // 调用前增强
            Object result = method.invoke(target, methodArgs);
            // 调用后增强
            return result;
        }
);
```

调用 `proxy.hello()` 时，JDK 代理会自动把本次调用对应的 `Method`、参数和代理对象传给 `InvocationHandler`。`Method` 变量叫什么由开发者决定，不存在 JVM 默认生成一个 `helloMethod` 名称的规则；真正的映射依据是代理接口的方法签名。`target` 也不是由 `InvocationHandler` 自动寻找，通常由创建 Handler 的代码显式持有，Spring 则在内部替开发者完成代理创建和目标对象绑定。

CGLIB 通过生成目标类的子类并覆盖可增强方法实现代理，因此不要求业务类实现接口，但 `final` 类不能被继承，`final` 方法也不能被覆盖增强。Spring 容器会根据配置、接口和目标类情况选择代理方式，业务代码通常不会直接出现 `Proxy.newProxyInstance()`。

### 4.3 拦截器链与顺序

代理方法被调用后，Spring 会为当前方法找到所有匹配的 Advisor，并把 Advice 适配成一条拦截器链。可以把执行过程理解为：

```text
代理方法
-> 拦截器 1
-> 拦截器 2
-> 拦截器 3
-> 目标方法
-> 拦截器 3 返回
-> 拦截器 2 返回
-> 拦截器 1 返回
```

`MethodInvocation.proceed()` 或 `ProceedingJoinPoint.proceed()` 的作用不是走过场，而是把控制权交给链中的下一个拦截器；当链中没有剩余拦截器时，才调用目标方法。如果 `@Around` Advice 在条件校验失败时不调用 `proceed()`，后续拦截器和目标方法都不会执行。

拦截器不是固定内置的“日志、权限、事务”三件套。事务拦截器由声明式事务基础设施注册；日志、权限和自定义注解校验是否存在，取决于项目是否声明了对应的 Aspect、Advisor 或框架组件。

多个切面需要显式使用 `@Order`、`Ordered` 或框架提供的顺序配置表达优先级。通常数值越小优先级越高，在调用链外层先进入、后退出；没有声明顺序时不要依赖偶然观察到的执行先后，同优先级也不应承载有严格依赖的业务语义。

### 4.4 TransactionInterceptor 与 TransactionManager

声明式事务的典型调用链：

```text
调用方
-> Spring 代理对象
-> TransactionInterceptor 读取事务属性并组织调用
-> TransactionManager 创建、加入、挂起或恢复事务
-> 目标方法
-> 根据正常返回或异常规则提交 / 回滚
```

`TransactionInterceptor` 主要负责读取 `@Transactional` 对应的传播行为、隔离级别、只读、超时和回滚规则，选择事务管理器，并在事务边界内调用 `invocation.proceed()`。`TransactionManager` 才负责管理真实事务资源。以 JDBC 事务管理器为例，数据库连接通常绑定到当前线程，创建、提交和回滚最终由事务管理器完成，而不是由拦截器直接操作 JDBC。

三种常见传播行为：

| 传播行为 | 当前没有事务 | 当前已有事务 |
|---|---|---|
| `REQUIRED` | 创建新事务 | 加入当前事务 |
| `REQUIRES_NEW` | 创建新事务 | 挂起当前事务并创建独立事务，完成后恢复外层事务 |
| `NESTED` | 通常创建新事务 | 在同一物理事务中建立保存点，内层可回滚到保存点 |

`REQUIRES_NEW` 的内层事务独立提交后，外层事务随后回滚不会撤销它。`NESTED` 不是独立提交：内层失败且异常被外层正确处理时，可以只回滚保存点后的修改；外层事务最终回滚时，内层修改仍会一起回滚。`NESTED` 还依赖事务管理器和底层资源支持保存点。

事务异常需要区分“Java 异常是否被捕获”和“事务是否已经标记为 `rollback-only`”：

1. 跨 Bean 的 `REQUIRED` 内层方法经过自己的事务拦截器，抛出运行时异常时可能把共享事务标记为 `rollback-only`。外层即使捕获异常，也不能清除这个标记；外层正常返回并请求提交时，会回滚并可能抛出 `UnexpectedRollbackException`。
2. 同类自调用绕过内层事务拦截器。如果外层捕获普通运行时异常，且底层资源没有自行标记事务失败，外层拦截器只看到正常返回，事务可能提交。
3. 如果自调用抛出的运行时异常继续离开外层事务方法，外层事务拦截器仍会看到异常并回滚外层事务。
4. Spring 默认对 `RuntimeException` 和 `Error` 回滚，普通 checked exception 默认不回滚；可通过 `rollbackFor` 和 `noRollbackFor` 调整。

因此，`@Transactional` 只是事务元数据。调用是否经过代理、传播行为选择了哪个事务、异常是否到达拦截器、事务是否已经被标记为只能回滚，以及操作是否使用正确事务管理器，才共同决定最终结果。

常见失效或预期不一致场景：

1. 同类内部自调用绕过代理。
2. 对象由 `new` 创建，不是 Spring Bean。
3. `private`、`final`、`static` 等方法不适合作为代理事务入口。
4. 异常被捕获后没有继续抛出。
5. 默认情况下 checked exception 没有命中回滚规则。
6. 新线程或异步任务越过线程绑定的事务上下文。
7. 使用错误的数据源或事务管理器。
8. `REQUIRES_NEW` 等传播行为与业务预期不一致。
9. Redis、MQ、HTTP、文件等外部副作用不属于普通数据库本地事务。

同类自调用需要进一步区分：如果外层方法已经开启事务，内层数据库操作仍可能加入外层事务，但内层方法自己的传播级别等事务配置不会被重新拦截；如果外层没有事务，内层注解又被绕过，则不会建立预期事务。

## 5. 边界

1. Spring singleton 是容器作用域，不等同于所有 GoF 单例实现细节。
2. Bean 由 Spring 管理，不代表所有方法调用都会经过代理。
3. `Could not roll back JDBC transaction` 表示 JDBC 回滚动作本身出现异常，不能单独证明事务从未开启，也不能直接证明数据库已经部分提交；最终结果仍需结合原始异常、连接状态和数据核对。
4. 本地数据库事务不能覆盖跨系统链路，仍需状态机、幂等、重试、补偿和对账。

## 6. 项目或工程关联

结算系统曾出现状态显示已生成但辅账缺失，以及辅账重复生成的问题。日志中同时存在数据库锁等待和 JDBC 回滚异常。代码检查发现，预期保护状态更新与辅账生成的方法存在同类内部调用。

修复时将一致性方法迁移到独立 Spring Service，通过 Bean 之间的外部调用进入事务代理，并在测试中验证异常情况下共同提交或回滚。该案例说明事务设计首先要确认真实调用链，而不能只检查方法上是否存在注解。

## 7. 面试表达入口

> Spring 依赖注入把对象创建、依赖装配和生命周期交给容器，使业务类可以依赖接口并方便替换和测试。对象成为 Bean 后，Spring 还可以通过代理统一提供事务和缓存等横切能力。以事务为例，调用必须经过代理，代理才能在方法前后开启、提交或回滚事务；所以同类自调用、异常被吞掉、checked exception、新线程和错误事务管理器都会造成事务失效或范围不符合预期。
