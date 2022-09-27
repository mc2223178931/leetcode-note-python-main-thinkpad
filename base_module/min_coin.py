
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if 0 < amount < min(coins):
            return -1
        elif amount == 0:
            return 0
        result = [int("inf") for i in range(amount+1)]
        result[0] = 0
        for j in range(amount+1):
            # tmp_list = []
            for i in coins:
                # tmp_list.append(result[j-i] + 1)
                if i > amount:
                    continue
                result[j] = min(result[j], result[j - i]+1)

        if result[-1] == int("inf"):
            return -1
        else:
            return result[-1]

if __name__ == "__main__":
    count = 2
    coin = [2147483647]
    test = Solution()
    min_num = test.coinChange(coin, count)
    print(min_num)





