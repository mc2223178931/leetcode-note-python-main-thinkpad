from typing import List
from collections import deque
# 最大子数组和
# 暴力遍历 O（n^2）
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = -100000
        for i in range(n):
            queue = deque()
            length = i + 1
            for j in range(length):
                queue.append(nums[j])                
            
            if sum(queue) > res:               
                res = sum(queue)
            index = length
            while index < n:
                queue.popleft()
                # queue.popleft()
                queue.append(nums[index])
                if sum(queue) > res:
                    res = sum(queue)                    
                index += 1

        return res
# 分治法 O(nlogn)
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        def maxsumfunc(nums, start, end):
            if end == start:
                return nums[start]
            mid = int((end + start)/2)
            mid_num = nums[mid]
            left_tmp = [0]
            left_sum = 0
            for i in range(mid-1, start-1, -1):              
                left_tmp.append(left_sum + nums[i])
                left_sum += nums[i]
            right_tmp = [0]
            right_sum = 0
            for j in range(mid+1, end+1, 1):
                right_tmp.append(right_sum + nums[j])
                right_sum += nums[j]
            
            cross_max = max(left_tmp) + mid_num + max(right_tmp)
            
            if start < mid:
                left = maxsumfunc(nums, start, mid-1)

                cross_max = max(left, cross_max)
            if mid < end:
                right = maxsumfunc(nums, mid+1, end)

                cross_max = max(right, cross_max)
            return cross_max
            
       
        n = len(nums)
        return maxsumfunc(nums, 0, n-1)
# 动态规划 Q（i）表示以索引i结尾的最大子序列和，Q(i) = max(Q(i-1) , 0) + nums[i] O(n)
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum_end_index = ['inf' for _ in range(n)]
        max_sum_end_index[0] = max_sum = nums[0]
        for i in range(1, n):
            max_sum_end_index[i] = max(max_sum_end_index[i-1], 0) + nums[i]
            max_sum = max(max_sum, max_sum_end_index[i])
        return max_sum
    def maxSubArray_op(self, nums: List[int]) -> int:
        n = len(nums)
        # max_sum_end_index = ['inf' for _ in range(n)]
        max_sum_end_index = max_sum = nums[0]
        for i in range(1, n):
            max_sum_end_index = max(max_sum_end_index+ nums[i], nums[i])
            max_sum = max(max_sum, max_sum_end_index)
        return max_sum
# 最大前缀和差 O（n）
class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        min_sum = sum = 0
        max_sum = nums[0]
        for i in range(n):
            sum += nums[i]
            max_sum = max(sum-min_sum, max_sum)
            min_sum = min(sum, min_sum)
        return max_sum


if __name__ == "__main__":
    solution = Solution3()
    nums = [5,4,-1,7,8]
    # nums = [-2,-3,-1]
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = solution.maxSubArray(nums)
    print(res)