from typing import List
# 四数之和
# 暴力回溯法枚举，判断是否符合条件，并用哈希表去重，超时
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(res, nums, n, path: List[int], depth, start, hashmap):
            if depth == 4:
                if sum(path) == target and str(path) not in hashmap:
                    res.append(path.copy())
                    hashmap[str(path)] = True
                return
            
            for i in range(n):
                if i < start:
                    continue
                path.append(nums[i])
                
                depth += 1
                backtrack(res, nums, n, path, depth, i+1, hashmap)
                
                depth -= 1
                path.pop()

        n = len(nums)
        if n < 4:
            return []
        res = []
        nums.sort()
        start = 0
        depth = 0
        path = []
        hashmap = dict()
        backtrack(res, nums, n, path, depth, start, hashmap)
        return res
# 分治法 将N数和拆解为多个两数和
class Solution1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNsum(nums, remain, N, path, res):
            if len(nums) < N or N < 2:
                return
            if N == 2:
                l = 0
                r = len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == remain:
                        res.append(path + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
                        while nums[r] == nums[r+1] and r > l:
                            r -= 1
                    elif nums[l] + nums[r] > remain:
                        r -= 1
                    elif nums[l] + nums[r] < remain:
                        l += 1 
            else:
                for i in range(len(nums)):
                    if i == 0 or i > 0 and nums[i] != nums[i-1]:
                        findNsum(nums[i+1:], remain - nums[i], N-1, path+[nums[i]], res)


        n = len(nums)
        res = []
        nums.sort()
        remain = target
        N= 4
        path = []
        findNsum(nums, remain, N, path, res)
        return res



if __name__ == "__main__":
    solution = Solution1()
    nums = [1,0,-1,0,-2,2]
    # nums = [2,2,2,2,2]
    target = 0
    res = solution.fourSum(nums, target)
    print(res)
