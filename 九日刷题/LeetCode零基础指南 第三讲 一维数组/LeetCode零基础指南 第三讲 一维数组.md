## 知识梳理
### 数组
#### 顺序储存
顺序储存结构是用一段地址连续的储存单元进行数据的储存.

我们就将通过数组的数据格式来实现顺序储存结构

第一个数据元素会被储存到下标为0的位置中, 然后第二个元素储存到1的位置, 以此类推.

#### 长度和容量
容量指的是数组最大能够储存多少个元素, 在C, C++等语言中需要在定义数组的时候就定义好容量.

长度是数组当前拥有的元素数量.

#### 索引
我们可以通过输入数组的索引来获得储存在该位置的元素 ```a = a[i]```

#### 函数传参
我们可以通过循环的方式来对数组进行赋值和值的调用.

一般来说只要给我们数组, 以及数组的长度, 就可以进行函数传参.

```
int add(int nums[], int numsize){
	int i;
	int s = 0;
	for(i=0; i < numsize; ++i){
		s += nums[i]
		}
		return s;
}
```

## 解题报告
### [33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)
	整数数组 nums 按升序排列，数组中的值 互不相同 。
	
	在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
	
	给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

#### 通过截图
![](pics/Pasted%20image%2020220330223610.png)

#### 思路解析
这道题更加考察的应当是翻转后的序列具有部分单调的性质, 怎么利用这个性质来进一步简化搜索流程. 

我就先使用简单的数组搜索, 直接过辣!

#### 代码
```Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
```

### [81. 搜索旋转排序数组 II](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/)
	已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。

	在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。
	
	给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。
	
	你必须尽可能减少整个操作步骤。


#### 通过截图
![](pics/Pasted%20image%2020220330224035.png)

#### 思路解析
这道题与前面非常类似啦, 最简单的解决思路就是基本的使用循环来查找数组中的值, 只要把返回值改为布尔值就可以了.

#### 代码
```Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return True
        return False
 ```
 
### [153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)
	已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
	若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
	若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
	注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
	
	给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
	
	你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

#### 通过截图
![](pics/Pasted%20image%2020220330225257.png)

#### 思路解析
这道题要求中提到了时间复杂度需要为 ```O(logn)```, 这里就要提到我们的经典算法二分查找了.

二分查找是一种从数组首端和尾端同时向中间进行搜索的算法, 因为这种性质, 可以节省很多的时间, 时间复杂度为 ```O(logn)```. 因此在看见对数形式的时间复杂度的时候我们就可以开始思考二分查找的算法了.

二分查找的实现思路为:
1. 定义一个左指针和右指针, 分别指向数组的头和尾.
2. 对数组进行判断处理.
3. 每次处理完后, 左指针右移, 右指针左移.
4. 每次进行一次判断, 当左指针越过右指针的时候, 循环结束.

#### 代码
```Python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums)-1
        while left <= right:
            tmp = min(nums[left], nums[right])
            if tmp < res:
                res = tmp
            left += 1
            right -= 1
        return res
```

### [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)
	假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
	
	每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

#### 通过截图
![](pics/Pasted%20image%2020220330232412.png)

#### 思路解析
这道题非常的有趣哦, 要知道总共到第n阶的所有方法总数, 重要的是要确定一个数量关系.

那么爬楼梯中有什么数量关系呢, 关键是每次可以爬 1 个或者 2 个台阶, 那么意味着对于任意一个楼梯阶数 n 来说, 到达它的上一步要么是从 n-1 迈一阶, 要么是从 n-2 迈两阶, 也就是说我们可以把第 n 阶的方法总数表示为:
$$f(n) = f(n-1) + f(n-2)$$

知道了这件事, 我们就可以发现这其实就是构建一个斐波那契数列, 使用循环很快得到答案~

这里注意一下, Python初始化数组的方式和其他语言不太一样, Python只有通过numpy库才能定义一个固定容量的数组, 所以在不使用numpy的前提下, 我们通过对数组一直进行添加的方法来进行数组的操作, 而不是直接给出数组索引对应的数.

#### 代码
```Python
class Solution:
    def climbStairs(self, n: int) -> int:
        count = []
        count.append(1)
        count.append(1)
        for i in range(2, n+1):
            count.append(count[i-1] + count[i-2])
        return count[n]
```

### [509. 斐波那契数](https://leetcode-cn.com/problems/fibonacci-number/)
	斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
	
	F(0) = 0，F(1) = 1
	F(n) = F(n - 1) + F(n - 2)，其中 n > 1
	给定 n ，请计算 F(n) 。

#### 通过截图
![](pics/Pasted%20image%2020220330233637.png)

#### 思路解析
这道题的实现方法与上一题一样, 轻松拿下~

#### 代码
```Python
class Solution:
    def fib(self, n: int) -> int:
        count = []
        count.append(0)
        count.append(1)
        for i in range(2, n+1):
            count.append(count[i-1] + count[i-2])
        return count[n]
```

### [1137. 第 N 个泰波那契数](https://leetcode-cn.com/problems/n-th-tribonacci-number/)
	泰波那契序列 Tn 定义如下： 
	
	T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
	
	给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

#### 通过截图
![](pics/Pasted%20image%2020220330232642.png)

#### 思路解析
这道题的实现方法与上一题一样, 只需要调整为3个数的累加就好了, 轻松拿下~

#### 代码
```Python
class Solution:
    def tribonacci(self, n: int) -> int:
        count = []
        count.append(0)
        count.append(1)
        count.append(1)
        for i in range(3, n+1):
            count.append(count[i-1] + count[i-2]+count[i-3])
        return count[n]
```
