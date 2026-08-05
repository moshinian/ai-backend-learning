# 相邻交换题中正确推导未收敛为可运行代码

## 1. 错误表现

1. 已经推导出“第 x 个 `a` 当前在位置 X，移动次数为 `X - x`”，但仍使用 `HashMap<Integer, Integer>` 保存所有位置并二次遍历。
2. 15 分钟结束时仍是 `for i from`、`for (key, value) from map` 等伪代码，没有形成可以编译运行的 Java 方法。
3. 题目使用小写 `a`、`b`，草稿使用大写 `A`；空串判断也沿用了集合式伪代码。
4. 没有主动说明交换次数最坏可达到平方量级，返回值应优先使用 `long`。

## 2. 根因

1. 正确数学关系出现后没有立即消除中间结构，仍沿着“先记录、再汇总”的业务代码习惯实现。
2. 久未限时编码，注意力停留在推导和修正示例，没有预留编译、自测和口述时间。
3. 把“思路正确”当成主要完成条件，没有把可运行代码视为笔试的最终交付物。

## 3. 正确理解

第 `countA` 个 `a` 最终应该位于下标 `countA`。扫描到当前位置 `i` 的 `a` 时，它需要跨过前面的 `b`，移动次数就是 `i - countA`，可以一遍完成：

```java
public static long minAdjacentSwaps(String s) {
    if (s == null || s.isEmpty()) {
        return 0L;
    }

    long steps = 0L;
    int countA = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s.charAt(i) == 'a') {
            steps += i - countA;
            countA++;
        }
    }
    return steps;
}
```

这与累计每个 `a` 前面的 `b` 数量等价，时间复杂度 `O(n)`，额外空间 `O(1)`。如果题目要求输出实际交换过程而不只是最少次数，则需要另行维护字符数组和操作序列，不能只返回总数。

## 4. 复盘触发条件

1. 已经得到位置差、计数或不变量，却准备建立 Map / List 保存全部中间结果。
2. 限时题过去一半时间仍没有方法签名和可执行循环。
3. 草稿中还存在伪代码、大小写不一致或未确认返回值范围。
4. 只验证一个交替样例，没有检查空串、全 `a`、全 `b` 和无需交换的输入。

## 5. 关联主题

1. `LEARNING_BACKLOG.md` 中的 `BL-009`
2. `interview/real-records/2026-08-05-zhuanzhuan-fullstack-engineer.md`
3. `sessions/2026-08-05-zhuanzhuan-interview-review.md`
