## 知识梳理
### 循环
循环的结构一般有两种: for循环以及while循环. 这里我们用for循环进行循环编写逻辑的解释

```
for(循环初始化表达式; 循环条件表达式; 循环执行表达式){
    循环体
}
```

1. 首先执行循环初始化表达式, 如: ```i=0```
2. 给出条件表达式, 这是表征循环继续进行的条件, 每一次循环开始前都会进行一次判断, 只有符合条件才会继续进行循环. 如: ```i<=n```
3. 循环执行表达式一般是一个迭代语句, 来保证程序的推进, 也是避免循环进入死循环的关键, 如: ```i++```
4. 在进行完判断后, 就可以进入循环主体进行语句执行.

不同语言的表达方式在循环上同样是存在差别的, 比如Python的for循环就一般会使用迭代列表的方式进行循环, 并没有齐全的循环条件表达式以及执行表达式的结构:

```Python
for i in range(n):
	循环体
```

这种表达方式在简单的使用循环时更加简单, 但是要实现进一步的功能就还是需要借助while循环进行和for循环相似的循环逻辑的编写.

```Python
while 循环条件表达式:
	循环体
	循环执行表达式
```

这里同样也可以注意, Python作为一个轻量化的脚本语言就没有更正规的语言那么规范, 一般进行循环的循环初始化表达式也是在循环外外置定义的.

## 解题报告
### [剑指 Offer 64. 求1+2+…+n](https://leetcode-cn.com/problems/qiu-12n-lcof/)
	求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

#### 通过截图
![](pics/Pasted%20image%2020220329112111.png)

#### 思路解析
这道题跟昨天的好多题都一样, 当然不是考察循环, 但是相应今天的循环主题我还是用循环做吧~ 正常的做法应该是使用位运算.

#### 代码
```Python
class Solution:
	
	def sumNums(self, n: int) -> int:
	
		res = 0
	
		for i in range(n) :
	
			res += i+1
	
		return res
```

### [231. 2 的幂](https://leetcode-cn.com/problems/power-of-two/)
	给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
	
	如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。

#### 通过截图
![](pics/Pasted%20image%2020220329115824.png)

#### 思路解析
本题只需要使用循环来遍历2的n次方, 然后判断是否与2相等即可. 要注意在算之前先对n的值进行判断, 把不可能的值(负数)去掉, 可以提高很多效率.

#### 代码
```Python
class Solution:

	 def isPowerOfTwo(self, n: int) -> bool:
	
		 if n <= 0:		
		 
			 return False
		
		 else:
		
			 k = 1
		
		 for i in range(31):
		
			 if n == k:
		
				 return True
		
			 k *= 2
		
		 return False
```

### [326. 3 的幂](https://leetcode-cn.com/problems/power-of-three/)
	给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。
	
	整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x

#### 通过截图
![](pics/Pasted%20image%2020220329120747.png)

#### 解题思路
这道题, 可以使用和2的幂同样的方法, 只需要调整一下每次乘的数字以及降低一点循环次数即可. 但是我现在使用另一种做法, 毕竟要多尝试嘛.

我们可以考虑这个数n反过来循环, 一直使用它除以3, 一旦不能整除(也就是取余部不为0), 那么就可以说明这个数不是3的因数.

在Python中实现这种比较复杂的循环判断就使用while会更好.

#### 代码
```Python
class Solution:

	def isPowerOfThree(self, n: int) -> bool:

		while n%3 == 0 and n:

			n //= 3

		return n == 1
```

### [342. 4的幂](https://leetcode-cn.com/problems/power-of-four/)
	给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。
	
	整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x

#### 通过截图
![](pics/Pasted%20image%2020220329122521.png)

#### 思路解析
这题其实还是可以用上面的两种方法做, 但我们再换一种!

本题求的是4的幂的判断, 4和2的幂与3的幂还有那么一丢丢不一样, 因为计算机是2进制记录数据的, 对于2的幂来说(没错, 前面第一题也可以这样做), 在二进制的储存形式一定是 `100...000` 这种形式的, 因为可以直接表达为 $2^n$ 的形式.

那么我们就可以考虑一下另一个数, 那就是 `n-1` , 很容易可以想到, 那这个时候二进制的储存就会是 `011...111` , 至于为什么我觉得有蛮多有意思的解释的. 

首先最直观地看, 二进制在做减法的时候就一直借位, 从第1位借到第n位, 然后自然而然就是 `0111..111` 了.

而还有一个有意思的角度来看, 我们知道等比数列的求和公式:
$$1+2+2^2+2^3+...+2^{n-1} = 2^n -1$$
发现了嘛, 我们就用2进制来表示就可以写成 ```011...111 = 100...000 + 1```

好了扯远了, 那么我们就可以发现2的幂n和n-1的二进制上每一位的数都不同, 因此我们用与运算来判断一个数是否是2的幂: ```n&(n-1) == 0 ? True:False```

然后怎么判断这个数是不是4的幂呢? 首先他得是2的幂对吧~ 然后在是2的幂前提下, 4的幂还有一个性质, 那就是对3取模一定为1, 证明如下:

$$4^n = (3+1)^n = \sum_{i=1} ^{n} C_n^i 3^i + 1$$

通过这个式子我们可以看出, 4的幂可以拆分为一个3的倍数和1的和, 因此对3取模一定为1.

最后我们就得到了答案.

#### 代码
```Python
class Solution:

	def isPowerOfFour(self, n: int) -> bool:

		return n&(n-1) == 0 and n != 0 and n%3 == 1
```

### [1492. n 的第 k 个因子](https://leetcode-cn.com/problems/the-kth-factor-of-n/)
	给你两个正整数 n 和 k 。
	
	如果正整数 i 满足 n % i == 0 ，那么我们就说正整数 i 是整数 n 的因子。
	
	考虑整数 n 的所有因子，将它们 升序排列 。请你返回第 k 个因子。如果 n 的因子数少于 k ，请你返回 -1 。

#### 通过截图
![](pics/Pasted%20image%2020220329124152.png)

#### 思路解析
这道题思路很清晰, 在1到n进行遍历, 判断是否是因数, 并添加一个计数器来计算因数个数, 然后就可以在遇见第k个的时候即可返回因数. 最后记得要进行返回 `-1` 的特殊情况的编写.

#### 代码
```Python
class Solution:

	def kthFactor(self, n: int, k: int) -> int:
		
		count = 0
		
		for i in range(1,n+1):
		
			if n%i == 0:
		
				count += 1
		
					if count == k:
		
						return i
		
		return -1
```

### [367. 有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square/)
	给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
	
	进阶：不要 使用任何内置的库函数，如  sqrt 。

#### 通过截图
![](pics/Pasted%20image%2020220329130212.png)

#### 解题思路
可以写一个死循环, 一直到达到目标数num了再退出循环, 然后一直判断平方数跟num的大小即可.

这种写法时间复杂度为O(n).

#### 代码
```Python
class Solution:

	def isPerfectSquare(self, num: int) -> bool:
		
		i = 0
		
		while True:
		
			p = i*i
		
			if num == p:
		
				return True
		
			elif num < p:
		
				return False
		
			i += 1
		
		return False
```