from typing import List
# 暴力
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res = 0

        for l in range(len(hours)):
            if l + res >= len(hours):
                break
            flag = 0
            for r in range(l, len(hours)):
                # print(l, r,  hours[l:r+1])
                if hours[r] > 8:
                    flag += 1
                else:
                    flag -= 1
                if flag > 0:
                    res = max(r-l+1, res)

        return res
#   优化
class Solution1:
    def longestWPI(self, hours: List[int]) -> int:
        res = 0
        scores = []
        for i in hours:
            if i > 8:
                scores.append(1)
            else:
                scores.append(-1)
        sum = 0
        prefixSum = [0]  # 前缀和数组
        for j in range(len(scores)):
            sum += scores[j]
            prefixSum.append(sum)
        print(prefixSum)
        num = len(prefixSum)
        suk = []
        for i in range(num):
            if len(suk) == 0 or prefixSum[suk[-1]] > prefixSum[i]:
                suk.append(i)
                for j in range(num-1, i, -1):
                    # 检查每一对下标看是否符合条件
                    if prefixSum[i] < prefixSum[j]:
                        res = max(j - i, res)
                        break
        return res









if __name__ == "__main__":
    solution = Solution1()
    hours = [9, 9, 6, 0, 6, 6, 9]
    # hours = [6, 6, 9]
    res = solution.longestWPI(hours)
    print(res)
