class Solution:
    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    def findMaxConsecutiveOnes(self, nums) -> int:
        if nums is [] or len(nums) == 0:
            return 0
        max_count = 0
        count = 0
        for i, value in enumerate(nums):
            if value > 0:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        # max_count = max(max_count, count)
        return max(max_count, count)




if __name__ == "__main__":

    test = Solution()
    nums = [1,1,0,1,1,1,0,1,1,1,1]
    count = test.findMaxConsecutiveOnes(nums)
    print(count)
