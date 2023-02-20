class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        limit_num = n/4
        cnt = {}
        cnt['Q'] = cnt['W'] = cnt['E'] = cnt['R'] = 0
        for i in s:
            cnt[i] += 1
        if cnt['Q'] == cnt['W'] == cnt['E'] == cnt['R'] == limit_num:
            return 0
        else:
            min_len = n
            r = 0
            for l in range(n):
                cnt_copy = cnt.copy()
                max_count = max(cnt_copy['Q'], cnt_copy['W'], cnt_copy['E'], cnt_copy['R'])
                while (max_count > limit_num and r < n):
                    cnt_copy[s[r]] -= 1
                    max_count = max(cnt_copy['Q'], cnt_copy['W'], cnt_copy['E'], cnt_copy['R'])
                    print(l, r, s[r], cnt_copy['Q'], cnt_copy['W'], cnt_copy['E'], cnt_copy['R'])
                    r += 1

                if max_count <= limit_num:
                    min_len = min(min_len, r-l)
                    print(min_len)
            return min_len




if __name__ == "__main__":
    # s = "QQQQ"
    s = "WQWRQQQW"
    solution = Solution()
    res = solution.balancedString(s)
    print(res)
