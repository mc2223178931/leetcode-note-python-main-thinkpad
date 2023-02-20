class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s, l, r):
            while l<r:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return isPalindrome(s, l+1, r) or isPalindrome(s, l, r-1)
            else:
                l += 1
                r -= 1
        return True



if __name__ == "__main__":
    s = "abca"
    solution = Solution()
    print(solution.validPalindrome(s))
