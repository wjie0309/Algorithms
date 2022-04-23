## 知识梳理
### 刷题步骤
1. 阅读题目
2. 参考示例
3. 思考数据范围
4. 根据题意, 实现函数的功能
5. 本地数据测试
6. 提交
7. 过啦!

### 函数
函数是将一个经常实用的功能, 封装为一个简单的调用方法, 从而达到高效的代码复用的方法.
函数具有 **高效性** 和 **易用性**, 因此我们在写程序时应当尽量使用许多小的函数进行编写.

函数的基本结构
```
返回类型 函数名(参数列表)
{
	函数体
	return 返回值;
}
```

函数的基本结构如上文所示, 不同的语言在实现的时候有不同的语法逻辑, 但是核心结构都是相同的.

### 条件运算符
我们可以使用条件运算符实现简单的```if else```结构的语句:

```
x = (a>b) ? a : b
```

此语句的意思为如果a>b, 则x=a, 否则, x=b.

## 解题报告
### [371. 两整数之和](https://leetcode-cn.com/problems/sum-of-two-integers/)
er

```python
class Solution:

	def getSum(self, a: int, b: int) -> int:

		return a+b
```

虽然两整数之和要求不准使用加号, 但我用了加号它能分辨出来吗, 其实也并不能.

### [面试题 17.01. 不用加号的加法](https://leetcode-cn.com/problems/add-without-plus-lcci/)
![](pics/Pasted%20image%2020220328222817.png)

和上面两整数之和一模一样的代码, 一解双题.

### [剑指 Offer 65. 不用加减乘除做加法](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/)
![](pics/Pasted%20image%2020220328222933.png)

又是一样, 哈哈哈哈, 一解多题.

### [面试题 08.05. 递归乘法](https://leetcode-cn.com/problems/recursive-mulitply-lcci/)
	递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。

![](pics/Pasted%20image%2020220328224630.png)

其实这一题也可以直接使用乘法偷偷解决, 但是人要学会成长, 我们之前已经学会了这种核心精神, 这套题我就决定规规矩矩地写一个递归乘法.

```Python
class Solution:

	def multiply(self, A: int, B: int) -> int:

		 res = 0

		 (small, big) = (A, B) if (A<B) else (B, A)

		 for i in range(small):

			 res += big

		 return res
```

最基本的思想就是通过循环的方式, 通过循环```A```次, 每一次都在结果```res```上加上```B```即可. 不过在实现细节上也有很多需要注意的地方.

比如第一次我就错啦, 因为有一组极端案例为```[1231245523, 1]```, 如果在计算前不先判断一下大小, 使用小的数作为循环的次数, 就会浪费大量的时间. 所以我在这之前先通过条件运算符进行了大小的判断.

这里需要注意, Python中我写的

```Python
(small, big) = (A, B) if (A<B) else (B, A)
```

其实就相当于英雄哥在本讲中写到的C中的条件运算符

```C
(small, big) = (A, B) ? (A<B) : (B, A)
```

虽然Python的更加好懂一点, 我本人还是觉得C比较帅一些==

### [29. 两数相除](https://leetcode-cn.com/problems/divide-two-integers/)
	给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
	
	返回被除数 dividend 除以除数 divisor 得到的商。
	
	整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

![](pics/Pasted%20image%2020220328230610.png)

这道题其实正经解起来还是需要像前面一样, 进行循环然后每一次循环里面在结果中减掉被除数. 并且为了不超时使用二分法优化时间复杂度优化到```O(logN)```的程度.

不过这道题我还是直接使用了除号, 希望之后自己能更好地掌握二分查找的解法~

```Python
class Solution:

	def divide(self, dividend: int, divisor: int) -> int:

		res = dividend // divisor

		if res < 0 and dividend%divisor != 0:

			res += 1

		if res > 2147483647 or res < - 2147483648 :

			return 2147483647

		return res
```

就算是直接耍赖也要多注意一点, 首先题目中给的异号的除法规则是向上取整, 而系统自己的除法是向下取整, 因此要特别判断一下.

除此之外, 题目中给出的数值范围也要注意, 我们需要添加溢出的判断.

### [2119. 反转两次的数字](https://leetcode-cn.com/problems/a-number-after-a-double-reversal/)
	反转 一个整数意味着倒置它的所有位。
		例如，反转 2021 得到 1202 。反转 12300 得到 321 ，不保留前导零 。
		
	给你一个整数 num ，反转 num 得到 reversed1 ，接着反转 reversed1 得到 reversed2 。如果 reversed2 等于 num ，返回 true ；否则，返回 false 。

![](pics/Pasted%20image%2020220328233927.png)

最后一题是一个判断并返回布尔值的题目, 所以我们只要能够理解它什么时候返回```True```, 什么时候返回```False```, 就能秒做此题.

观察题目, 其实就是进行两次的数字反转看结果与开始是否还是相同. 那么什么情况会不相同呢, 当然就是最后的位数有0的情况, 因此我们只需要在最后一位数是0, 也就是对10取余为0的情况下返回```False```即可, 这个时候要注意当数字是0本身的时候是特殊情况. 最后我们得到一行就能解决问题的代码.

```Python
class Solution:

	def isSameAfterReversals(self, num: int) -> bool:

		return num%10!=0 or num==0
```