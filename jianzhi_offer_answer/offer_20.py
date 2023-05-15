class Solution:
    def isNumber(self, s: str) -> bool:
        def iszheng(s) -> bool:
            if len(s) == 0:
                return False
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
            if len(s) == 0:
                return False
            for i in s:
                if '0' <= i <= '9':
                    continue                
                return False
            return True
        def iszzheng(s) -> bool:
            if len(s) == 0:
                return False
            for i in s:
                if '0' <= i <= '9':
                    continue                
                return False
            return True
        def beforepoint(s) -> bool:
            if len(s) == 0:
                return False
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
            for i in s:
                if '0' <= i <= '9':
                    continue                
                return False
            return True
        def isxiao(s) -> bool:            
            if '.' not in s or s == '.':
                return False
            ind = s.index('.')
            return (beforepoint(s[:ind]) and iszzheng(s[ind+1:])) or (iszheng(s[:ind]) and len(s[ind+1:])==0) or (len(s[:ind])==0 and iszzheng(s[ind+1:]))
        if len(s) == 0:
            return False
        a = s[0]
        while a == ' ':
            s = s[1:]
            if len(s) == 0:
                return False 
            a = s[0]
        b = s[-1]
        while b == ' ':
            s = s[:-1]
            b = s[-1]
        if len(s) == 0:
            return False
        if 'e' in s:
            if s == 'e':
                return False
            ind = s.index('e')
            return (iszheng(s[:ind]) or isxiao(s[:ind])) and  iszheng(s[ind+1:])
        elif 'E' in s:
            if s=='E':
                return False
            ind = s.index('E')
            return (iszheng(s[:ind]) or isxiao(s[:ind])) and  iszheng(s[ind+1:])            
        else:
            return iszheng(s) or isxiao(s)

if __name__=="__main__":
    solution = Solution()
    s = '.'
    res = solution.isNumber(s)
    print(res)
            