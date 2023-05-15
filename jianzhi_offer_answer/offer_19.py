class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp代表是否匹配
        dp =[[False for _ in range(len(p)+1)]for _ in range(len(s)+1)]
        # 空正则项

        # 空串和空正则项
        dp[0][0] = True
        if len(p) != 0:
            # 非空正则项
            for i in range(0, len(s)+1):
                for j in range(1, len(p)+1):
                    
                    # 正则串当前位置是‘*’
                    if p[j-1] == '*':
                        # 看
                        if i >=1 and j >=2 and (s[i-1] == p[j-2] or p[j-2] == '.'):
                            dp[i][j] |= dp[i-1][j]
                        # 不看
                        else:
                            if j >=2:
                                dp[i][j] |= dp[i][j-2]
                                            
                    else:
                    # 正则串当前位置不是‘*’
                        if i > 0 and (p[j-1] == '.' or p[j-1] == s[i-1]):
                            dp[i][j] = dp[i-1][j-1]
                    print(i, j, dp[i][j])
        return dp[len(s)][len(p)]
