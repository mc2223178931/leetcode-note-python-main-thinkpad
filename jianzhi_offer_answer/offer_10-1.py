class Solution:
    def fib(self, n: int) -> int:
        def cal_fib(n):
            if n ==0 or n==1:
                return n            
            if n not in hashmap:                         
                hashmap[n] = int((cal_fib(n-1)+cal_fib(n-2))%(1e9+7))
            return hashmap[n]
        hashmap = {}
        return cal_fib(n)