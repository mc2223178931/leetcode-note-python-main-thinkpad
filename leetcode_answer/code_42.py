# 接雨水 
from typing import List
class Solution:
    # 按列 每一列分别找到左边最大和右边最大 取较小的和当前列对比 O（n^2）
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            max_left = 0
            for j in range(i):
                max_left = max(max_left, height[j])
            max_right = 0
            for k in range(i+1, len(height)):
                max_right = max(max_right, height[k])
            min_num = min(max_left, max_right)
            if min_num > height[i]:
                res+=min_num-height[i]
        return res
    # 优化 用两个数组 存储左边最大和右边最大的列
    def trap(self, height: List[int]) -> int:
        res = 0
        max_left = [0]
        for i in range(1, len(height)):
            max_left.append(max(max_left[i-1], height[i-1]))
        max_right = [0]*len(max_left)
        for i in range(len(height)-2, 0, -1):
            max_right[i] = max(max_right[i+1], height[i+1])
        for i in range(len(height)):
            min_num = min(max_left[i], max_right[i])
            if min_num > height[i]:
                res+=min_num-height[i]
        return res

if __name__ == "__main__":
    solution = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    res = solution.trap(height)
    print(res)