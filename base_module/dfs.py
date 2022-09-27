#深度优先遍历 DFS 回溯
# 当前点x, y ,经过的步数为step
map = [[0 for j in range(100)] for i in range(100)]
# print(size(map))
def dfs(x, y, p, q, step):
    min = 999999
    if x == p and y == q:
        if step < min:
            min = step
        return
    # 顺时针试探
    # 右

    # 下

    # 左

    # 上


