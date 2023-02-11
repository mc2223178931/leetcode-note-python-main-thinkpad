# 1223. 掷骰子模拟 动态规划
from typing import List
# 错误 会存在重复计算情况
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        def delete_count_func(roll_num, n):
            print('all:', roll_num, n)
            delete_count = 0
            for i in range(roll_num+1, n+1):

                if n == i:
                    c = 1
                    delete_count += c
                else:
                    c = (n-i-1) * (5**2) * (6**(n-i-2)) + (2*5*6**(n-i-1))
                    delete_count += c
                print(i, n, c)
            print(delete_count)
            return delete_count
        hashmap = dict()
        count = 6 ** n
        for roll_num in rollMax:
            if roll_num < n:
                if roll_num in hashmap:
                    count -= hashmap[roll_num]
                else:
                    delete_count = delete_count_func(roll_num, n)
                    count -= delete_count
                    hashmap[roll_num] = delete_count
        print(hashmap)
        return int(count % (10**9 + 7))
# 动态规划
class Solution1:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        max_roll = max(rollMax)
        d = [[[0 for _ in range(max_roll + 1)] for _ in range(6)] for _ in range(n+1)]
        for j in range(6):
            d[1][j][1] = 1
        for i in range(2, n+1):
            for j in range(6):
                max_k = rollMax[j]
                for q in range(6):
                    for k in range(1, max_k+1):
                        if q != j:
                            d[i][q][1] += d[i-1][j][k]
                        elif k+1 <= max_k:
                            d[i][q][k+1] += d[i-1][j][k]

        count = 0
        for j in range(6):
            for k in range(1, rollMax[j]+1):
                count += d[n][j][k]
        return (count % (10**9 + 7))

if __name__ == "__main__":
    solution1 = Solution1()
    n = 3
    rollMax = [1,1,1,2,2,3]
    # n = 2
    # rollMax = [1,1,2,2,2,3]
    # n = 4
    # rollMax = [2, 1, 1, 3, 3, 2]
    print(solution1.dieSimulator(n, rollMax))
