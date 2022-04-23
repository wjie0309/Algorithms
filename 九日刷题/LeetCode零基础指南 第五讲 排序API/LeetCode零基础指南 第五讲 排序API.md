## 知识梳理
### 排序简介
排序的基本思路有非常多, 有八大排序:
1.  冒泡排序
2. 选择排序
3. 插入排序
4. 归并排序
5. 快速排序
6. 希尔排序
7. 计数排序
8. 桶排序

在本次基础的笔记中先不介绍这些排序. 本次先对排序的API进行了解, 让我们可以通过简单的调用实现排序.

### Python 中的 sorted 函数
在Python中要进行排序很简单, sorted 的参数有 ```iterable, key, reverse``` 三个, 分别对应排序操作的对象, 进行排序参考的值, 是升序还是降序.

```
target == [2, 3, 8, 5, 1]

rank = sorted(target)

print(rank)
```

这样进行执行就可以得到排序后的目标数组.

## 解题报告
### [912. 排序数组](https://leetcode-cn.com/problems/sort-an-array/)
	给你一个整数数组 `nums`，请你将该数组升序排列。

#### 通过截图
![](pics/Pasted%20image%2020220401221115.png)

#### 思路解析
只需要按照我们说的, 使用 sorted 函数即可.

#### 代码
```Python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)
```

### [169. 多数元素](https://leetcode-cn.com/problems/majority-element/)
	给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
	
	你可以假设数组是非空的，并且给定的数组总是存在多数元素。

#### 通过截图
![](pics/Pasted%20image%2020220401222549.png)

#### 思路解析
1. 进行数组排序, 那之后相同的数就会排列在一起.
2. 进行遍历, 判断它会不会和在它后面 ```n//2``` 的元素进行判断.
3. 这里可以注意, 遍历的次数可以控制在 ```n//2``` 以内.

#### 代码
```Python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        rank = sorted(nums)
        n = len(nums)
        for i in range(n//2+1):
            if rank[i] == rank[i+n//2]:
                return rank[i]
```

### [217. 存在重复元素](https://leetcode-cn.com/problems/contains-duplicate/)
	给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。

#### 通过截图
![](pics/Pasted%20image%2020220401223617.png)

#### 思路解析
1. 进行排序, 得到有序数组.
2. 进行遍历, 如果一个元素与相邻元素相等即可.

#### 代码
```Python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        rank = sorted(nums)
        for i in range(len(nums)-1):
            if rank[i] == rank[i+1]:
                return True
        return False
```

### [164. 最大间距](https://leetcode-cn.com/problems/maximum-gap/)
	给定一个无序的数组 nums，返回 数组在排序之后，相邻元素之间最大的差值 。如果数组元素个数小于 2，则返回 0 。
	
	您必须编写一个在「线性时间」内运行并使用「线性额外空间」的算法。

#### 通过截图
![](pics/Pasted%20image%2020220401230158.png)

#### 思路解析
1. 进行排序
2. 进行长度判定, 小于 2 的直接return.
3. 进行实时判定, 在得到更大的差值时就更新最终的最大差值

#### 代码
```Python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        rank = sorted(nums)
        ret = 0
        if len(nums) < 2:
            return 0
        for i in range(len(nums)-1):
            tmp = rank[i+1] - rank[i]
            if tmp > ret:
                ret = tmp
        return ret
```

### [905. 按奇偶排序数组](https://leetcode-cn.com/problems/sort-array-by-parity/)
	给定一个非负整数数组 `A`，返回一个数组，在该数组中， `A` 的所有偶数元素之后跟着所有奇数元素。
	
	你可以返回满足此条件的任何数组作为答案。

#### 通过截图
![](pics/Pasted%20image%2020220401231327.png)

#### 思路解析
这里可以让我们学会使用参数 ```key``` 的用法, 我们可以通过定义一个函数, 来决定升降排序的对象, 就像这里我们使用 ```x%2``` 来进行判断, 这样就可以实现奇数在后偶数在前的效果了.

#### 代码
```Python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key= lambda x: x%2 )
```

### [976. 三角形的最大周长](https://leetcode-cn.com/problems/largest-perimeter-triangle/)
	给定由一些正数（代表长度）组成的数组 `nums` ，返回 _由其中三个长度组成的、**面积不为零**的三角形的最大周长_ 。如果不能形成任何面积不为零的三角形，返回 `0`。

#### 通过截图
![](pics/Pasted%20image%2020220401232638.png)

#### 思路解析
只要满足三角形两边之和大于第三边的公式即可拉.

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