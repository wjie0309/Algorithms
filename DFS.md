# DFS(深度优先搜索)
从任意一个结点开始, 一直遍历到最深后返回上一层继续遍历其他路径\
使用递归实现

## 复杂度
时间复杂度为指数级, 但是可以通过减少边界等明显不可用的遍历次数来加快速度

## 应用:
- 一次遍历
- 迷宫路径问题

## 代码实现
以黄金矿工为例
```
def dfs(x:int,y:int,tmp:int)->None:
	# 先进行路径的记录/需求数值累加
	tmp += grid[x][y]
	nonlocal ans
	ans = max(ans,tmp)
	# 标记已经走过的路径,这里因为矿工中值为0即不进入,故直接标记为0即可
	rec = grid[x][y]
	grid[x][y] = 0

	# 进行递归
	for nx,ny in ((x,y+1),(x,y-1),(x+1,y),(x-1,y)):
		if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 0: # m,n分别为迷宫的长和宽
			dfs(nx,ny,tmp)

	# 循环完成了要回溯了, 将标记的区域值返回
	grid[x][y] = rec
```
