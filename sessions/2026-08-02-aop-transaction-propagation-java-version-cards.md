# 2026-08-02 AOP、事务传播与 Java 版本能力卡

## 日期

2026-08-02

## 主题

围绕 `BL-024` 完成 AOP 代理、Advisor / Pointcut、拦截器链、声明式事务传播和 Java 8、11、17、21 代表能力的第一轮学习与闭卷复述。

## 本次做了什么

1. 从“自定义注解为什么不会自动产生 AOP 能力”出发，建立注解、Pointcut、Advice、Advisor、候选 Advisor 与自动代理创建器之间的关系。
2. 使用 `Proxy.newProxyInstance()` 拆解 JDK 动态代理的类加载器、接口列表和 `InvocationHandler`，确认 `Method` 由代理运行时根据接口调用自动传入，目标对象由创建代理的代码持有。
3. 区分 JDK 动态代理和 CGLIB：前者基于接口，后者基于子类覆盖，因此受 `final` 类和 `final` 方法限制。
4. 梳理拦截器链的来源、`proceed()` 的递归推进作用和 `@Order` 的外层 / 内层顺序，纠正“日志、权限、事务是固定内置链”的理解。
5. 拆分 `TransactionInterceptor` 与 `TransactionManager` 职责：前者读取事务属性并组织调用，后者创建、加入、挂起、恢复、提交和回滚真实事务。
6. 通过连续判断题区分 `REQUIRED`、`REQUIRES_NEW`、`NESTED`，以及共享事务、独立事务和保存点的提交回滚边界。
7. 结合 `rollback-only`、`UnexpectedRollbackException`、同类自调用和异常捕获，验证“异常是否到达拦截器”比“代码里有没有 catch”更关键。
8. 完成 Java 8、11、17、21 最小版本卡，并闭卷说出每个版本的一到两个代表能力及作用。

## 关键结论

1. 普通注解只有元数据能力；要形成 AOP 增强，必须有对应的 Advisor / Aspect、Pointcut、Advice 和自动代理基础设施。
2. Spring 代理的是 Bean 的调用入口，每个方法仍会匹配自己的拦截器链；同类自调用直接进入目标对象，不会再次穿过代理。
3. `ProceedingJoinPoint.proceed()` 和 `MethodInvocation.proceed()` 决定是否继续执行后续链路；不调用时可以直接阻断目标方法。
4. `REQUIRED` 有事务就加入；`REQUIRES_NEW` 挂起外层并创建独立事务；`NESTED` 在同一事务中使用保存点，内层可局部回滚但不能独立提交。
5. 外层捕获异常不能清除内层拦截器已经设置的 `rollback-only`；但自调用绕过内层拦截器且异常被外层捕获时，外层事务可能正常提交。
6. 默认回滚规则看异常类型而不是是否属于 SQL：运行时异常和 `Error` 默认回滚，普通 checked exception 默认提交。
7. Java 8 建立 Lambda / Stream 入口；Java 11 建立 String API / HttpClient 入口；Java 17 建立密封类型 / JDK 内部强封装入口；Java 21 建立虚拟线程 / `switch` 模式匹配入口。
8. 虚拟线程降低阻塞式任务的线程成本，但不扩大 CPU、数据库连接池或下游系统容量。

## 下次入口

1. `BL-024` 的技术补强已经完成第一轮，结算系统 90 秒口述和代表难点 60 秒口述仍按用户要求暂时跳过，因此任务保持 `DOING`。
2. 如果恢复 `BL-024`，先不看项目笔记，用“服务对象、输入、主链路、输出、本人职责”完成结算系统口述，再选择一个证据明确的代表难点。
3. 如果继续暂缓项目表达，则回到 `BL-016`，闭卷完成万级 QPS 的 60 至 90 秒压缩口述，但不要把 `BL-024` 误标为完成。

## 关联文件

1. `backend/spring/ioc-bean-and-transaction-proxy.md`
2. `backend/java/java-version-capability-cards.md`
3. `mistakes/spring/aop-transaction-proxy-boundaries.md`
4. `interview/real-records/2026-07-29-hesheng-innovation-fullstack-engineer.md`
5. `LEARNING_BACKLOG.md`
6. `START_HERE.md`
