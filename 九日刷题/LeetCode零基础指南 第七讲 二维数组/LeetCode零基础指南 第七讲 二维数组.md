## 知识梳理
### 二维数组
二维数组, 就是储存为 ```[[a, b],[c, d]]``` 的数据结构.

### 二维数组的索引
可以通过 ```a[i][j]``` 的索引方式来获取二维数组元素.

## 解题报告
### [1351. 统计有序矩阵中的负数](https://leetcode-cn.com/problems/count-negative-numbers-in-a-sorted-matrix/)
	给你一个 `m * n` 的矩阵 `grid`，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 请你统计并返回 `grid` 中 **负数** 的数目。

#### 通过截图
![](pics/Pasted%20image%2020220403204345.png)

#### 思路解析
1. 获取二维数组的大小: 行和列的大小.
2. 进行遍历, 查询元素的值获取结果.

#### 代码
```Python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        for i in grid:
            for j in i:
                if j < 0:
                    cnt += 1
        return cnt
```

### [1572. 矩阵对角线元素的和](https://leetcode-cn.com/problems/matrix-diagonal-sum/)
	给你一个正方形矩阵 `mat`，请你返回矩阵对角线元素的和。
	
	请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。

#### 通过截图
![](pics/Pasted%20image%2020220403205040.png)

#### 思路解析
进行二维数组的遍历, 给出清晰的限制条件即可.

#### 代码
```Python
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        r = len(mat)
        for i in range(r):
            ans += mat[i][i]
            if i == r-1-i:
                continue
            ans += mat[i][r-i-1]
        return ans
```

### [1672. 最富有客户的资产总量](https://leetcode-cn.com/problems/richest-customer-wealth/)
	给你一个 m x n 的整数网格 accounts ，其中 accounts[i][j] 是第 i 位客户在第 j 家银行托管的资产数量。返回最富有客户所拥有的 资产总量 。
	
	客户的 资产总量 就是他们在各家银行托管的资产数量之和。最富有客户就是 资产总量 最大的客户。

#### 通过截图
![](pics/Pasted%20image%2020220403205757.png)

#### 思路解析
找到最富有客户只需求得每一行的元素和.

#### 代码
```Python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for item in accounts:
            tmp = sum(item)
            if tmp > ans:
                ans = tmp
        return ans
```

### [766. 托普利茨矩阵](https://leetcode-cn.com/problems/toeplitz-matrix/)
	给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。
	
	如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。

#### 通过截图
![](pics/Pasted%20image%2020220403214805.png)

#### 思路解析
1.  给出一个判断托普利兹矩阵的函数, 顺便判断边界, 防止越界.
2. 在数组中遍历, 分别遍历行和列上的顶点, 再进行判断.

#### 代码
```Python
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def check(sr, sc, mr, mc):
            step = 0
            while 1:
                if sr + step >= mr:
                    break
                if sc + step >= mc:
                    break
                if matrix[sr][sc] != matrix[sr+step][sc+step]:
                    return False
                step += 1
            return True
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            if not check(i,0,r,c):
                return False
        for j in range(c):
            if not check(0,j,r,c):
                return False
        return True

```

### [1380. 矩阵中的幸运数](https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix/)
	给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。
	
	幸运数 是指矩阵中满足同时下列两个条件的元素：
	
	在同一行的所有元素中最小
	在同一列的所有元素中最大

#### 通过截图
![](pics/Pasted%20image%2020220403220023.png)

#### 思路解析
1. 遍历找到每一行中的最小值
2. 遍历找到每一列中的最大值
3. 进行比较, 有相同元素说明这个元素就是幸运数

#### 代码
```Python
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rmin = []
        cmax = []
        ans = []
        for item in matrix:
            rmin.append(min(item))
        for j in range(len(matrix[0])):
            tmax = 0
            for item in matrix:
                if item[j] > tmax:
                    tmax = item[j]
            cmax.append(tmax)
        for x in rmin:
            for y in cmax:
                if x == y:
                    ans.append(x)
        return ans
```

### [1582. 二进制矩阵中的特殊位置](https://leetcode-cn.com/problems/special-positions-in-a-binary-matrix/)
	给你一个大小为 rows x cols 的矩阵 mat，其中 mat[i][j] 是 0 或 1，请返回 矩阵 mat 中特殊位置的数目 。
	
	特殊位置 定义：如果 mat[i][j] == 1 并且第 i 行和第 j 列中的所有其他元素均为 0（行和列的下标均 从 0 开始 ），则位置 (i, j) 被称为特殊位置。

#### 通过截图
![](pics/Pasted%20image%2020220403222530.png)

#### 思路解析
跟之前的题目相似, 先写一个判断函数, 然后遍历判断每一个数.

#### 代码
```Python
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cnt = 0
        def check(mr, mc, r, c):
            if not mat[r][c]:
                return 0
            for i in range(mr):
                if i != r and mat[i][c] :
                    return 0
            for i in range(mc):
                if i != c and mat[r][i] :
                    return 0
            return 1
        
        r = len(mat)
        c = len(mat[0])
        for i in range(r):
            for j in range(c):
                cnt += check(r, c, i, j)
        return cnt
```