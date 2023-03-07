from typing import List
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        value_dict ={}
        for i in nums:
            if i not in value_dict:
                value_dict[i] = i
            else:
                return i
        return 'null'



if __name__=="__main__":
    solution = Solution()
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(solution.findRepeatNumber(nums))

