class Solution:
    def cuttingRope(self, n: int) -> int: 
        if n <= 3:
            return n-1
        a = n//3
        b = n%3
        if b == 0:
            return 3**a
        elif b == 1:
            return 3**(a-1)*4
        elif b == 2:
            return 3**a * 2
    def cuttingRope_dp(self, n: int) -> int: 
        dp = []
        for i in range(n+1):
            dp.append(0)
        # dp[0] = dp[1] = 0
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]
    def cuttingRope_yu(self, n: int) -> int: 
        if n <= 3:
            return n-1
        a = n//3-1
        b = n%3
        p = 1000000007
        x = 3
        rem = 1
        while a > 0:
            if a % 2: rem = (rem * x)%p
            x = x**2%p
            a//=2
        if b == 0:
            return int((rem*3)%p)
        elif b == 1:
            return int((rem*4)%p)
        elif b == 2:
            return int((rem*6)%p)
    




if __name__=="__main__":
    solution = Solution()
    n = 36
    res = solution.cuttingRope_dp(n)
    print(res)