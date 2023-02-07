class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def jiecheng(a):
            if a <= 1:
                return 1
            return a * jiecheng(a-1)
        prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        count = 0
        while prime_list[count] <= n:
            count += 1
        print(count, (jiecheng(count) * jiecheng(n-count)))
        return (jiecheng(count) * jiecheng(n-count)) % (10**9 +7)




if __name__ == "__main__":
    solution = Solution()
    n = 2
    res = solution.numPrimeArrangements(n)
    print(res)
