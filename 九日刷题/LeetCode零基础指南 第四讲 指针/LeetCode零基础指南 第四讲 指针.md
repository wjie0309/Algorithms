## 知识梳理
### 指针的定义
指针即是地址, 表达了在内存中字节的编号, 可以用来指向储存在这个内存里的值.

在C语言中, 指针定义的方法为:
```C
DataType *dataName
```

### 指针的读取
我们可以通过 `&` 把对应元素的地址获取到.
```C
char x = 'o';
char *p = &x;
```

对于数组来说, 获得的地址是数组第一个元素的地址.

### 返回一个数组的范式
```C
/**
 * Note: The returned array must be malloced, assume caller calls free().  // (1)
 */
 int *func(int *nums, int numsSize, int *returnSize) {                     // (2)
     int *ret = (int *)malloc( sizeof(int) * xxx );                        // (3)
     // TODO                                                               // (4)
     *returnSize = xxx;                                                    // (5)
     return ret;                                                           // (6)
 }
```

### Python中的"指针"
因为Python其实没有指针的概念, 所以我们在Python中一般通过直接定义一个变量来充当指针, 当需要指针的 `index.next` 等功能的时候, 我们只需要先进行一下简单的对变量属性的定义即可.

## 解题报告
### [1470. 重新排列数组](https://leetcode-cn.com/problems/shuffle-the-array/)
	给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。
	
	请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

#### 通过截图
![](pics/Pasted%20image%2020220331070312.png)

#### 思路解析
只需要分别添加两个地址的值即可.

可以通过n次循环, 每次添加指定的值, 也可以先指定好每一个指针对应的值的格式, 然后2n循环添加.

#### 代码
```Python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n+i])
        return res
 ```

```Python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(2*n):
            if i & 1:
                res.append(nums[n+i//2])
            else:
                res.append(nums[(i+1)//2])
        return res
```

### [1929. 数组串联](https://leetcode-cn.com/problems/concatenation-of-array/)
	给你一个长度为 n 的整数数组 nums 。请你构建一个长度为 2n 的答案数组 ans ，数组下标 从 0 开始计数 ，对于所有 0 <= i < n 的 i ，满足下述所有要求：
	
	ans[i] == nums[i]
	ans[i + n] == nums[i]
	具体而言，ans 由两个 nums 数组 串联 形成。
	
	返回数组 ans 。

#### 通过截图
![](pics/Pasted%20image%2020220331085014.png)

#### 思路解析
这道题用Python做确实有点无聊...

#### 代码
```Python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums*2
        return ans
```

### [1920. 基于排列构建数组](https://leetcode-cn.com/problems/build-array-from-permutation/)
	给你一个 从 0 开始的排列 nums（下标也从 0 开始）。请你构建一个 同样长度 的数组 ans ，其中，对于每个 i（0 <= i < nums.length），都满足 ans[i] = nums[nums[i]] 。返回构建好的数组 ans 。
	
	从 0 开始的排列 nums 是一个由 0 到 nums.length - 1（0 和 nums.length - 1 也包含在内）的不同整数组成的数组。

#### 通过截图
![](pics/Pasted%20image%2020220331201236.png)

#### 思路解析
这道题的逻辑还是非常清晰, 只要进行遍历对ans进行赋值就好了.

不过在用Python定义ans数组时我发现了一件事情, 为了方便我一开始直接用```ans = nums```来进行了赋值, 但是这种赋值方式在Python中是有很严重的问题的, 在Python中这种语法不是给 ans 赋值了 nums 的值, 而是赋予了 ans 一个指向 nums 的**指针**, 因此我们这么写的话, nums 的值是会在 ans 变化的时候发生变化的.

那么我们这个时候该怎么进行赋值呢? 我们可以用列表生成式把 nums 中的每一个元素赋值给 ans .
```ans = [i for i in nums]```

#### 代码
```Python
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [i for i in nums]
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans
```

### [1480. 一维数组的动态和](https://leetcode-cn.com/problems/running-sum-of-1d-array/)
	给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
	
	请返回 nums 的动态和。

#### 通过截图
![](pics/Pasted%20image%2020220331204645.png)

#### 思路解析
看到动态的公式就开始启动脑筋! 我们可以分析动态和的公式:
$$runningSum[i] = runningSum[i-1] + nums[i]$$

在这之后, 我们只需在循环中不断给第i个runningSum进行这个公式的计算, 这样可以省下大量重复计算已经算过的累加和的时间.

#### 代码
```Python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSums = [nums[0]]
        for i in range(1,len(nums)):
            runningSums.append(runningSums[i-1] + nums[i])
        return runningSums
```

### [剑指 Offer 58 - II. 左旋转字符串](https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/)
	字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

#### 通过截图
![](pics/Pasted%20image%2020220331214431.png)

#### 思路解析
这道题的解题过程中有几个地方值得学习:
1. 取模操作, 我们可以通过取模操作轻松实现类似这道题的列表循环移动.
2. Python的输出字符串的方式, Python的字符串可以当作 list 访问, 但是在储存为 list 后要输出为字符串要注意使用 join 函数: ```str = ''.join(list)```

#### 代码
```Python
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        ret = []
        for i in range(len(s)):
            ret.append(s[(i+n) % len(s)])
        return ''.join(ret)
```

### [1108. IP 地址无效化](https://leetcode-cn.com/problems/defanging-an-ip-address/)
	给你一个有效的 [IPv4](https://baike.baidu.com/item/IPv4) 地址 `address`，返回这个 IP 地址的无效化版本。
	
	所谓无效化 IP 地址，其实就是用 `"[.]"` 代替了每个 `"."`。

#### 通过截图
![](pics/Pasted%20image%2020220331220733.png)

#### 思路解析
这道题只需要在遍历的时候进行判断, 遇见目标字符进行一个额外的添加流程即可.

#### 代码
```Python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        ret = []
        for i in address:
            if i =='.' :
                ret.append('[')
                ret.append('.')
                ret.append(']')
            else:
                ret.append(i)
        return ''.join(ret)
```

### [剑指 Offer 05. 替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/)
	请实现一个函数，把字符串 `s` 中的每个空格替换成"%20"。

#### 通过截图
![](pics/Pasted%20image%2020220331221427.png)

#### 思路解析
这道题思路与上一道题是一样的, 进行一点简单的调整就可以了. 

#### 代码
```Python
class Solution:
    def replaceSpace(self, s: str) -> str:
        ret = []
        for i in s:
            if i ==' ' :
                ret.append('%20')

            else:
                ret.append(i)
        return ''.join(ret)
```

### [1365. 有多少小于当前数字的数字](https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/)
	给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
	
	换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
	
	以数组形式返回答案。

#### 通过截图
![](pics/Pasted%20image%2020220331224339.png)

#### 思路解析
1. 通过给数组排序的方式在查找小于自己的数量时减小查找时间
2. 对数组进行遍历
3. 在循环中嵌套一个循环来查询排序后的数组里的大小关系, 然后在遇见比自己大的数或者一样大的数的时候返回当时的索引即可

#### 代码
```Python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ret = []
        rank = sorted(nums)
        length = len(nums)
        for i in range(length):
            for j in range(length):
                if rank[j] >= nums[i]:
                    ret.append(j)
                    break
        return ret
```

### [剑指 Offer 17. 打印从1到最大的n位数](https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/)
	输入数字 n ，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

#### 通过截图
![](pics/Pasted%20image%2020220331225434.png)

#### 思路解析
首先我们要获得我们列表的元素总数, 那就是n位数的数字总量, 显而易见是 $10^n -1$ 个元素. 在这之后, 我们就只需遍历这些元素即可.

#### 代码
```Python
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        num = 1
        ret = []
        for i in range(n):
            num *= 10
        for j in range(1, num):
            ret.append(j)
        return ret
```

### [1389. 按既定顺序创建目标数组](https://leetcode-cn.com/problems/create-target-array-in-the-given-order/)
	给你两个整数数组 nums 和 index。你需要按照以下规则创建目标数组：
	
	目标数组 target 最初为空。
	按从左到右的顺序依次读取 nums[i] 和 index[i]，在 target 数组中的下标 index[i] 处插入值 nums[i] 。
	重复上一步，直到在 nums 和 index 中都没有要读取的元素。
	请你返回目标数组。
	
	题目保证数字插入位置总是存在。

#### 通过截图
![](pics/Pasted%20image%2020220331230535.png)

#### 思路解析
这道题的关键是, 需要按照顺序每次对当时的数组进行对应的索引处插入操作.

因此我们首先进行遍历, 然后每次循环中使用更新中的目标数组.

#### 代码
```Python
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target
 ```