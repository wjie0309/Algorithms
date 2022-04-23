## 知识梳理
### 递归
递归是一个非常有趣的算法, 一个函数通过调用自己进行不断的循环, 从而通过简单的几行代码实现复杂的功能.

### 递归的要求
1. 实现一个自己调用自己的函数
2. 设立一个出口, 需要 return , 否则会出现死递归

### 递归的复杂度
递归的复杂度非常恐怖, 因此一定需要谨慎使用递归.

### 递归的应用
使用递归可以实现非常多实用的功能和算法.

比如实现二叉树, 广度优先搜索, 深度优先搜索等.

具体的实现过程我们放在后面的解题中来看.

## 解题报告
### [172. 阶乘后的零](https://leetcode-cn.com/problems/factorial-trailing-zeroes/)
	给定一个整数 `n` ，返回 `n!` 结果中尾随零的数量。
	
	提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1

#### 通过截图
![](pics/Pasted%20image%2020220405215651.png)

#### 思路解析
1. 阶乘结果为出现 0 的情况就是在乘以 5 的情况下才会出现, 因为阶乘中有 ```n//2``` 个偶数, 因此只要统计 5 的因数个数就可以了, 5 的因数个数即为 0 的个数.
2. 这里需要注意的是 25 , 125 等有多个因数 5 .

#### 代码
```Python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        for i in range(5, n + 1, 5):
            while i % 5 == 0:
                i //= 5
                ans += 1
        return ans
```

### [1342. 将数字变成 0 的操作次数](https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-to-zero/)
	给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。

#### 通过截图
![](pics/Pasted%20image%2020220405220518.png)

#### 思路解析
构造一个数字迭代策略, 然后进行递归即可

#### 代码
```Python
class Solution:
    def numberOfSteps(self, num):
        def numberOfStep(num):
            if num == 0:
                return 0
            if num%2:
                return numberOfStep(num-1) + 1
            else:
                return numberOfStep(num//2) + 1
        return numberOfStep(num)
```

### [222. 完全二叉树的节点个数](https://leetcode-cn.com/problems/count-complete-tree-nodes/)
	给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
	
	完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

#### 通过截图
![](pics/Pasted%20image%2020220405222157.png)

#### 思路解析
使用递归向上遍历每一层的树节点, 这样可以节省时间

#### 代码
```Python
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```

### [LCP 44. 开幕式焰火](https://leetcode-cn.com/problems/sZ59z6/)
	「力扣挑战赛」开幕式开始了，空中绽放了一颗二叉树形的巨型焰火。
	给定一棵二叉树 root 代表焰火，节点值表示巨型焰火这一位置的颜色种类。请帮小扣计算巨型焰火有多少种不同的颜色。

#### 通过截图
![](pics/Pasted%20image%2020220405225243.png)

#### 思路解析
同样与上题相似

#### 代码
```Python
class Solution:
    def numColor(self, root: TreeNode) -> int:
        res = set()
        def dfs(a):
            if not a:return
            dfs(a.left)
            dfs(a.right)
            res.add(a.val)
        dfs(root)
        return len(res)
```
