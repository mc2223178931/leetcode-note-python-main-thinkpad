from collections import deque
# 队列 + 哈希表
class Solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
        if len(s) == 0:
            return 0
        hash_table = dict()
        queue = deque()
        max_len = 0
        for i in s:
            if i in hash_table:
                max_len = max(max_len, len(queue))
                val = queue.popleft()
                while i != val:
                    hash_table.pop(val)
                    val = queue.popleft()
                queue.append(i)

            else:
                hash_table[i] = 1
                queue.append(i)
        # max_len =
        return max(max_len, len(queue))
# 滑动窗口 左右指针分别对应窗口的左右边界
class Solution1:
    def lengthOfLongestSubstring(self,s: str) -> int:
        lengh = len(s)
        if len(s) == 0:
            return 0
        max_len = 0
        rk = 0
        for i, symbol in enumerate(s):
            hash_table = dict()

            while s[rk] not in hash_table:
                if rk == lengh-1:
                    break
                hash_table[s[rk]] = 1
                rk += 1
            max_len = max(max_len, rk - i)
        return max_len







if __name__ == "__main__":
    solution1 = Solution1()
    s = "abcabcbb"
    max_len = solution1.lengthOfLongestSubstring(s)
    print(max_len)
