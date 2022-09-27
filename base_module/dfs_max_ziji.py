# 找到全部子集
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        # 从空集开始搜索，每次将nums的节点加入空集中
        result = []
        tmp = []

        if nums is None:
            return None

        nums.sort()

        startIndex = 0
        self.dfsHelper(nums, startIndex, tmp, result)

        return result

    def dfsHelper(self, nums, startIndex, tmp, result):
        # dfs出口
        tmp_copy = tmp.copy()  # 拷贝一份
        result.append(tmp_copy)

        if startIndex == len(nums):
            return

        for i in range(startIndex, len(nums)):
            tmp.append(nums[i])
            self.dfsHelper(nums, i + 1, tmp, result)
            tmp.pop()
        return

if __name__ == "__main__":
    test = Solution()
    nums = [1,2,3,4,5]
    subset_list = test.subsets(nums)
    print(subset_list)
