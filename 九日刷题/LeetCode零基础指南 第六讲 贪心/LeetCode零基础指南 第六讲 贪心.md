## 知识梳理
### 贪心
贪心, 是一种算法思路. 总体来说就是在当下做出对现在最好的选择. 使用贪心算法, 我们得到是一个系统的局部最优解.

具体的贪心的实现手段非常灵活, 需要根据题不断变化. 因此我们配合后面的刷题内容进行了解.

## 解题报告
### [1913. 两个数对之间的最大乘积差](https://leetcode-cn.com/problems/maximum-product-difference-between-two-pairs/)
	两个数对 (a, b) 和 (c, d) 之间的 乘积差 定义为 (a * b) - (c * d) 。
	
	例如，(5, 6) 和 (2, 7) 之间的乘积差是 (5 * 6) - (2 * 7) = 16 。
	给你一个整数数组 nums ，选出四个 不同的 下标 w、x、y 和 z ，使数对 (nums[w], nums[x]) 和 (nums[y], nums[z]) 之间的 乘积差 取到 最大值 。
	
	返回以这种方式取得的乘积差中的 最大值 。

#### 通过截图
![](pics/Pasted%20image%2020220402170147.png)

#### 思路解析
我们使用贪心的思想对这题进行思考, 在当下情况中最大的乘积差是怎么得到的呢? 显然我们要获得尽可能大的数和尽可能小的一个数, 那么对于期待的 `w, x, y, z` 四个数, 我们的期待就应该是最大和第二大, 最小和第二小的数.

因此我们对这个数组进行排序, 然后返回最大两元素-最小两元素即可.

#### 代码
```Python
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        rank = sorted(nums)
        return rank[-1] * rank[-2] - rank[0] * rank[1]
```

### [976. 三角形的最大周长](https://leetcode-cn.com/problems/largest-perimeter-triangle/)
	题目描述

#### 通过截图
![](pics/Pasted%20image%2020220402170309.png)

#### 思路解析
同样应用贪心的思想, 我们只要从大到小排序数组, 然后取满足三角形两边之和大于第三边要求的最大的数组即可.

#### 代码
```Python
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        rank = sorted(nums, reverse = True)
        for i in range(len(rank)-2):
            if rank[i+1] + rank[i+2] > rank[i]:
                return rank[i+1] + rank[i+2] + rank[i]
        return 0
```

### [561. 数组拆分 I](https://leetcode-cn.com/problems/array-partition-i/)
	给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到 n 的 min(ai, bi) 总和最大。
	
	返回该 最大总和 。

#### 通过截图
![](pics/Pasted%20image%2020220402171039.png)

#### 思路解析
想要将这 2n 个数分布为 n 对, 并使其中最小值的总和最大. 

我们用贪心的思想进行考虑, 那么在每一次分配数对的时候, 我们应该期待能分到一个数组中有尽可能大的 min(ai, bi), 因此我决定进行降序排序, 然后最大和第二大组成一个数组, 以此类推, 来让我们能够得到尽可能大的最小值总和.

#### 代码
```Python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        rank = sorted(nums)
        ret = 0
        for i in range(len(nums)//2):
            ret += rank[2*i]
        return ret
```

### [881. 救生艇](https://leetcode-cn.com/problems/boats-to-save-people/)
	给定数组 people 。people[i]表示第 i 个人的体重 ，船的数量不限，每艘船可以承载的最大重量为 limit。
	
	每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。
	
	返回 承载所有人所需的最小船数 。

#### 通过截图
![](pics/Pasted%20image%2020220402173538.png)

#### 思路解析
因为一艘船可能载的人数为 1, 2 ( 0 不考虑因为如果有 0 的情况的话就不可能救下所有人). 我的贪心思路是, 找到当下小于但是最接近 limit 的数对, 所以我准备设立两个指针, 然后从降序排序后的数组两侧出发, 进行两数之和与 limit 的越界判定.

在越界的情况下: 左指针右移一格, 乘船计数+1, 右指针不动继续进行判断.
不越界的情况下: 左右指针一起移动, 乘船计数+1

直到左右指针相遇.

#### 代码
```Python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left = 0
        right = len(people)-1
        cnt = 0
        rank = sorted(people, reverse = True)
        while left <= right:
            if rank[left] + rank[right] <= limit:
                left += 1
                right -= 1
                cnt += 1
            else:
                left += 1
                cnt += 1
        return cnt
```

### [324. 摆动排序 II](https://leetcode-cn.com/problems/wiggle-sort-ii/)
	给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。
	
	你可以假设所有输入数组都可以得到满足题目要求的结果。

#### 通过截图
![](pics/Pasted%20image%2020220402182913.png)

#### 思路解析
本题考虑, 观察这个排序可以发现, 奇数索引位置上的元素都比周围的数要高, 所以我们可以贪心从最大的元素里调进这个位置.

直接先对数组进行排序, 然后在数组中开始遍历, 对该元素的索引的奇偶性进行判断, 然后分别给出 > 和 < 的判断, 只要满足判断就继续, 不满足判断就交换位置即可.

#### 代码
```Python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rank = sorted(nums)
        cnt = len(nums)-1
        i = 1
        while i < len(nums):
            nums[i] = rank[cnt]
            i += 2
            cnt -= 1
        i = 0
        while i < len(nums):
            nums[i] = rank[cnt]
            i += 2
            cnt -= 1
```

### [455. 分发饼干](https://leetcode-cn.com/problems/assign-cookies/)
	假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
	
	对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

#### 通过截图
![](pics/Pasted%20image%2020220402185232.png)

#### 思路解析
这道题在我看来, 思路有一点像救生艇问题, 可以同样通过使用指针来做贪心.

1. 将两个数组都进行排序, 然后设立两个指针分别指向 `g[i]` 和 `s[i]` 的尾端.
2. 进行判断, 当饼干能满足孩子的胃口时, 两个指针分别向前移动, 计数+1
3. 如果不能满足, 就说明无论如何都无法满足这个孩子的胃口, 那么就胃口指针前移, 寻找下一个胃口能够满足的孩子

*这道题还算是比较简单的情况, 不过如果孩子可以吃多个饼干来满足自己的胃口, 那么算法的设计应该怎么改动呢, 这个问题作者暂时也没有思路.*

#### 代码
```Python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        idx1 = len(g)-1
        idx2 = len(s)-1
        cnt = 0
        while idx1 >= 0 and idx2 >= 0:
            if g[idx1] <= s[idx2]:
                idx1 -= 1
                idx2 -= 1
                cnt += 1
            else:
                idx1 -= 1
        return cnt
```

### [1827. 最少操作使数组递增](https://leetcode-cn.com/problems/minimum-operations-to-make-the-array-increasing/)
	给你一个整数数组 nums （下标从 0 开始）。每一次操作中，你可以选择数组中一个元素，并将它增加 1 。
	
	比方说，如果 nums = [1,2,3] ，你可以选择增加 nums[1] 得到 nums = [1,3,3] 。
	请你返回使 nums 严格递增 的 最少 操作次数。
	
	我们称数组 nums 是 严格递增的 ，当它满足对于所有的 0 <= i < nums.length - 1 都有 nums[i] < nums[i+1] 。一个长度为 1 的数组是严格递增的一种特殊情况。

#### 通过截图
![](pics/Pasted%20image%2020220402190503.png)

#### 思路解析
这题的贪心思路比较清晰, 因为数组本身的顺序不能改变, 所以只要对比相邻元素的大小, 然后一直调整使得 ```nums[i+1] > nums[i]``` 即可.

注意分开讨论长度只有 1 的情况

#### 代码
```Python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        if len(nums) == 1:
            return cnt
        else:
            for i in range(len(nums)-1):
                if nums[i] >= nums[i+1]:
                    cnt += nums[i] + 1 - nums[i+1]
                    nums[i+1] = nums[i] + 1
            return cnt
```

### [945. 使数组唯一的最小增量](https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique/)
	给你一个整数数组 nums 。每次 move 操作将会选择任意一个满足 0 <= i < nums.length 的下标 i，并将 nums[i] 递增 1。
	
	返回使 nums 中的每个值都变成唯一的所需要的最少操作次数。

#### 通过截图
![](pics/Pasted%20image%2020220402193155.png)

#### 思路解析
这题思路和前一题也比较相似. 我们可以先排序, 然后在数组中遍历, 当 ```nums[i] == nums[i+1]``` 时, 就 ```nums[i+1] += 1```.

#### 代码
```Python
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                cnt += nums[i]-nums[i+1]+1
                nums[i+1] = nums[i]+1
        return cnt
```

### [611. 有效三角形的个数](https://leetcode-cn.com/problems/valid-triangle-number/)
	给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数

#### 通过截图
![](pics/Pasted%20image%2020220402195222.png)

#### 思路解析
这题继续使用指针实现贪心算法.

1. 进行排序
2. 建立三个指针指向三角形的三个边
3. 写一个嵌套循环,  不断遍历 `i, j, k` , 然后进行三角形存在性的判断
4. 这里有一个关键来节省时间, 不然会超时: 那就是 k 的值在第一次确定完 i 和 j 之后就可以在 j 之后的遍历中不再遍历了, 因为能满足之前的三角形存在性的 k 值肯定能满足现在的三角形.

#### 代码
```Python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        i,j,k = 0,0,0
        cnt = 0
        nums.sort()
        while i < len(nums):
            j = i+1
            # 这一步是降低复杂度的关键, 因为这样就不用再重新遍历k了, 因为之前能构成三角形的k值现在肯定也能构成三角形, 直接返回 k-j+ 就行
            k = j+1
            while j < len(nums):
                while k < len(nums):
                    if nums[i] + nums[j] <= nums[k]:
                        break
                    k += 1
                cnt += k-j-1
                j += 1
                if j == k:
                    k = j+1
            i += 1
        return cnt
```