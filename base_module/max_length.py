class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return max(dp)

