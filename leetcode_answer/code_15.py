from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i, num in enumerate(nums):         
            if i > n-3:
                continue
            if i > 0 and num == nums[i-1]:
                continue
            target = 0 - num
            l = i + 1
            r = n - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    # if [num, nums[l], nums[r]] not in res:             
                    res.append([num, nums[l], nums[r]])
                    while (l < r and nums[l] == nums[l + 1]):
                        l += 1
                    while (l < r and nums[r] == nums[r - 1]):
                        r -= 1
                    l += 1    
                    r -= 1    
        return res



if __name__ == "__main__":
    solution = Solution()
    nums = [-1,0,1,2,-1,-4]
    res = solution.threeSum(nums)
    print(res)
