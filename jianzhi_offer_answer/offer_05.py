class Solution:
    def replaceSpace(self, s: str) -> str:
        s2 = ''
        for i in s:
            if i != ' ':
                s2+=i
            else:
                s2+='%20'
        return s2


if __name__=="__main__":
    solution = Solution()
    s = "We are happy."
    print(solution.replaceSpace(s))