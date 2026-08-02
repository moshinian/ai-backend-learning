# AOP、代理与事务传播边界纠偏

## 错误表现

1. 认为只要自定义一个运行时注解，Spring 就会自动为方法创建 AOP 代理。
2. 把“代理整个 Bean”理解成 Bean 的所有方法都会执行同一组增强。
3. 认为 `InvocationHandler` 中的 `Method` 需要业务代码提前逐个建立方法名映射，或者 JVM 会默认生成 `helloMethod` 变量。
4. 把日志、权限、事务理解成 Spring 固定内置且顺序固定的一条拦截器链。
5. 认为 `NESTED` 内层一旦回滚，外层事务必然一起回滚。
6. 认为外层 `catch` 住异常后，共享事务一定可以继续提交；或者反过来认为只要捕获过运行时异常，事务就一定回滚。
7. 认为事务是否回滚主要看异常是不是 SQL 异常。

## 根因

1. 只看到注解和业务方法，没有建立 Advisor、Pointcut、Advice、代理对象和拦截器链之间的完整关系。
2. 把 Java 异常控制流和事务内部的 `rollback-only` 状态混成一个概念。
3. 没有先判断调用是否经过代理，再讨论传播行为和回滚规则。
4. 把 `REQUIRES_NEW` 的独立事务、`NESTED` 的保存点和 `REQUIRED` 的共享事务统一理解成“新开一层事务”。

## 正确理解

1. 注解只是元数据。只有存在对应 Advisor / Aspect 等基础设施，且 Pointcut 命中 Bean 与方法，自动代理创建器才会创建代理并加入 Advice。
2. 容器对外暴露代理 Bean，但每次方法调用都会匹配自己的拦截器链；未命中的方法不会执行对应增强。
3. JDK 代理依据接口方法签名识别调用，并把 `Method` 和参数自动传给 `InvocationHandler`；变量名由开发者决定，目标对象由代理创建逻辑显式绑定。
4. 拦截器链来自当前方法匹配到的 Advisor，不是固定三件套。顺序需要用 `@Order`、`Ordered` 或框架配置表达，不能依赖未声明顺序。
5. `REQUIRED` 共享事务；`REQUIRES_NEW` 挂起外层并创建独立事务；`NESTED` 通常在同一物理事务中建立保存点。
6. `NESTED` 内层失败且异常被外层处理时，可以只回滚到保存点；外层事务最终回滚时，内层修改仍会一起回滚。
7. 跨 Bean 的 `REQUIRED` 内层拦截器可能先把共享事务标记为 `rollback-only`，外层 `catch` 不能清除该状态。自调用绕过内层拦截器时，如果外层捕获普通异常且底层资源未标记失败，外层事务反而可能提交。
8. 默认回滚规则依据异常类型：`RuntimeException` 和 `Error` 默认回滚，普通 checked exception 默认提交；可以使用 `rollbackFor`、`noRollbackFor` 调整。

## 复盘触发条件

1. 看到自定义注解时，先问“谁把它转换成 Advisor 或拦截器”。
2. 看到 `@Transactional` 时，先画真实调用链，确认调用是否穿过代理。
3. 看到 `catch` 时，同时检查异常是否已经经过内层事务拦截器，以及事务是否被标记为 `rollback-only`。
4. 看到传播行为时，分别回答物理事务数量、外层是否挂起、是否独立提交、是否依赖保存点。
5. 看到多个切面时，检查顺序配置，不根据一次日志输出推断稳定顺序。

## 关联主题

1. `backend/spring/ioc-bean-and-transaction-proxy.md`
2. `backend/mysql/transaction.md`
3. `mistakes/database/transaction.md`
4. `projects/settlement-system/transaction-flow-and-reconciliation.md`
5. `LEARNING_BACKLOG.md` 中的 `BL-005`、`BL-024`
