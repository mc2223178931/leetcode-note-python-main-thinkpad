from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        s = dict()
        s[-1] = []

        for num in nums:
            tmp = []
            for key in s:
                if num % key == 0:
                    s[key].append(num)
                    tmp.append(s[key].copy())
                    s[key].remove(num)
            # print(tmp, max(tmp, key=len))
            s[num] = max(tmp, key=len)

        max_len = 0
        max_key = -1
        for key in s.keys():
            if len(s[key]) > max_len:
                max_len = len(s[key])
                max_key = key
        return s[max_key]


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    res = solution.largestDivisibleSubset(nums)
    print(res)