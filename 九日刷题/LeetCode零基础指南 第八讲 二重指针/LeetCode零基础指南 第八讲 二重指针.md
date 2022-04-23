## 知识梳理
### 二级指针
如果一个指针指向另外一个指针, 那么就可以被称为二级指针.

因为 Python 中所有的数据类型都可以看作对象, 所以二级指针的实现只要通过二次的变量赋值就好了.

```Python
x = 1
p1 = x
p2 = p1
```

## 解题报告
### [832. 翻转图像](https://leetcode-cn.com/problems/flipping-an-image/)
	给定一个 n x n 的二进制矩阵 image ，先 水平 翻转图像，然后 反转 图像并返回 结果 。
	
	水平翻转图片就是将图片的每一行都进行翻转，即逆序。
	
	例如，水平翻转 [1,1,0] 的结果是 [0,1,1]。
	反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。
	
	例如，反转 [0,1,1] 的结果是 [1,0,0]。

#### 通过截图
![](pics/Pasted%20image%2020220404213816.png)

#### 思路解析
1. 定义一个二维数组
2. 遍历原二维数组, 将值按要求进行操作


#### 代码
```Python
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                if image[i][left] == image[i][right]:
                    image[i][left] ^= 1
                    image[i][right] ^= 1
                left += 1
                right -= 1
            if left == right:
                image[i][left] ^= 1
        return image
```

### [867. 转置矩阵](https://leetcode-cn.com/problems/transpose-matrix/)
	给你一个二维整数数组 `matrix`， 返回 `matrix` 的 **转置矩阵** 。
	
	矩阵的 **转置** 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

#### 通过截图
![](pics/Pasted%20image%2020220404214350.png)

#### 思路解析
进行转置需要判断每个遍历状态下的翻转是否越界, 除此之外进行遍历就好了.

需要注意构造返回的转置矩阵的时候要把长宽对调.

#### 代码
```Python
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        trans = [[0]*r for _ in range(c)]
        for i in range(r):
            for j in range(c):
                trans[j][i] = matrix[i][j]
        return trans
```

### [566. 重塑矩阵](https://leetcode-cn.com/problems/reshape-the-matrix/)
	在 MATLAB 中，有一个非常有用的函数 reshape ，它可以将一个 m x n 矩阵重塑为另一个大小不同（r x c）的新矩阵，但保留其原始数据。
	
	给你一个由二维数组 mat 表示的 m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。
	
	重构后的矩阵需要将原始矩阵的所有元素以相同的 行遍历顺序 填充。
	
	如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

#### 通过截图
![](pics/Pasted%20image%2020220404215513.png)

#### 思路解析
1. 进行 reshape 合理性判断: $m \times n = r \times c$
2. 用一个一维数组储存原矩阵的元素, 然后再输入到重构后的矩阵中

#### 代码
```Python
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat
        tmp = []
        for row in mat:
            for item in row:
                tmp.append(item)
        ret = [[0]*c for _ in range(r)]
        cnt = 0
        for i in range(r):
            for j in range(c):
                ret[i][j] = tmp[cnt]
                cnt += 1
        return ret
```

### [2022. 将一维数组转变成二维数组](https://leetcode-cn.com/problems/convert-1d-array-into-2d-array/)
	给你一个下标从 0 开始的一维整数数组 original 和两个整数 m 和  n 。你需要使用 original 中 所有 元素创建一个 m 行 n 列的二维数组。
	
	original 中下标从 0 到 n - 1 （都 包含 ）的元素构成二维数组的第一行，下标从 n 到 2 * n - 1 （都 包含 ）的元素构成二维数组的第二行，依此类推。
	
	请你根据上述过程返回一个 m x n 的二维数组。如果无法构成这样的二维数组，请你返回一个空的二维数组。

#### 通过截图
![](pics/Pasted%20image%2020220404220229.png)

#### 思路解析
1.  进行可行性判断, 如果元素数量不等于要求的元素数量, 则无法构成二维数组
2. 仿照上一题进行遍历即可

#### 代码
```Python
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        ret = [[0]*n for _ in range(m)]
        cnt = 0
        for i in range(m):
            for j in range(n):
                ret[i][j] = original[cnt]
                cnt += 1
        return ret

```