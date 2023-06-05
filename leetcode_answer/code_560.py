from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和 哈希表存次数
        res = 0
        hashmap = {0:1}
        presum = 0
        for i in range(len(nums)):
            presum += nums[i]
            if presum-k in hashmap: res += hashmap[presum-k]
            if presum in hashmap:
                hashmap[presum] += 1
            else:
                hashmap[presum] = 1
        return res