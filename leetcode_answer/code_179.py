from typing import List
import functools
# 最大数 字符串
# 自定义比较器
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comp(a,b):
            if (a+b) > (b+a):
                return 1
            if (a+b) < (b+a):
                return -1
            return 0
        str_list = [str(i) for i in nums]
        str_list.sort(reverse=True, key=functools.cmp_to_key(comp))
        s = str()
        for j in str_list:
            s+=j
        return str(int(s))



if __name__ == "__main__":
    solution = Solution()
    nums = [3,30,34,5,9]
    # nums = [-2,-3,-1]
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = solution.largestNumber(nums)
    print(res)