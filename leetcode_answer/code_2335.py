class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        if amount[0] + amount[1] <= amount[2]:
            return amount[2]
        elif (amount[0] + amount[1] - amount[2]) % 2 == 0:
            return amount[2] + (amount[0] + amount[1] - amount[2])//2
        else:
            return amount[2] + (amount[0] + amount[1] - amount[2] -1) // 2 + 1
