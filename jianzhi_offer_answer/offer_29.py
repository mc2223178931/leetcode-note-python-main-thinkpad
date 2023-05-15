from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        l, r, t, b, res = 0, len(matrix[0]), 0, len(matrix), []
        # count = 0
        # all_nums = r * b
        while len(res) < len(matrix[0])*len(matrix):
            # print(l, r)
            # 从左向右
            if l < r and t < b:
                for i in range(l, r):
                    res.append(matrix[t][i])
                    # count+=1
            t += 1
            # 从上到下
            # print(t, b)
            if t < b and l < r:
                for i in range(t, b):
                     res.append(matrix[i][r-1])
                    #  count+=1
            r -= 1
            # 从右到左
            # print(l, r)
            if r > l and t < b:
                for i in range(r-1, l-1, -1):
                    res.append(matrix[b-1][i])
                    # count+=1
            b -= 1
            # 从下到上
            if b > t and l < r:
                for i in range(b-1, t-1, -1):
                    res.append(matrix[i][l])
                    # count+=1
            l += 1
        return res
            
