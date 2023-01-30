from typing import List
# 四数之和 II

class Solution:
    # 暴力枚举
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        def nListSum(nums_list, n, length, path, res):
            if n < 1:
                print(path)
                if sum(path) == 0:
                    # print(path)
                    print(0)
                    res.append(path.copy())
                return               
            else:
                index_key = 4-n
                nums = nums_list[index_key]
                for i in range(length):
                    nListSum(nums_list, n-1, length, path + [nums[i]], res)

        l = len(nums1)
        res = []
        nums_list = []
        nums_list.append(nums1)
        nums_list.append(nums2)
        nums_list.append(nums3)
        nums_list.append(nums4)

        nListSum(nums_list, 4, l, [], res)
        return len(res)
    # 两两组合
    def fourSumCount1(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        hashmap = dict()

        for num1 in nums1:
            for num2 in nums2:
                hashmap[num1 + num2] = hashmap.get(num1 + num2, 0) + 1
        for num3 in nums3:
            for num4 in nums4:
                count += hashmap.get(-(num3 + num4), 0)
            
        return count



if __name__ == "__main__":
    solution = Solution()
    # nums1 = [1,2]
    # nums2 = [-2,-1]
    # nums3 = [-1,2]
    # nums4 = [0,2]
    nums1 = [-1,-1]
    nums2 = [-1,1]
    nums3 = [-1,1]
    nums4 = [1,-1]
    res = solution.fourSumCount1(nums1, nums2, nums3, nums4)
    print(res)