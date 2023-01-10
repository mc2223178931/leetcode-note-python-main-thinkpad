# 两数之和
# 暴力枚举 O(N^2)
class Solution:
    def twoSum(self, nums, target: int):
        # result_list = []
        length = len(nums)
        for i, num in enumerate(nums):
            # if num > target:
            #     return []

            for j in range(i + 1, length):
                if num + nums[j] == target:
                    return [i, j]
        return []
# 哈希表
# 遍历一遍数组，创建哈希表，然后查找哈希表中是否存在(target-x)元素 O(N)
class Solution1:
    def twoSum(self, nums, target: int):
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
        return []

if __name__ == "__main__":
    solution1 = Solution1()
    nums = [2, 7, 11, 15]
    target = 9
    result_list = solution1.twoSum(nums, target)
    print(result_list)
