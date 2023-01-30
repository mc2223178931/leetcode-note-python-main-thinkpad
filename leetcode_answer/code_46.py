from typing import List
# 全排列
# 回溯法 DFS 递归

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path:List[int], used, res):
            if depth == size:
                res.append(path[:])
                return
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth+1, path, used, res)
                    used[i] = False
                    print(i, path, res)
                    path.pop()


        size = len(nums)
        if size == 0:
            return []
        res = []
        depth = 0
        used = [False for _ in range(size)]
        path = []
        dfs(nums, size, depth, path, used, res)
        return res




if __name__ == "__main__":
    solution1 = Solution()
    nums = [1,2,3]
    result_list = solution1.permute(nums)
    print(result_list)