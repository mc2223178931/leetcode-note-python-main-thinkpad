class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): 
            return ''
        need = collections.defaultdict(int)
        for tt in t:
            need[tt] += 1
        l = 0
        needcnt = len(t)
        res = s
        len_res = len(s)
        flag = False
        for r, ss in enumerate(s):
            # 向右扩张窗口
            if need[ss] > 0:                
                needcnt -= 1
            need[ss]-= 1
            if needcnt == 0:
                # 窗口包含了t所有字符 移动l
                flag = True # s字符串中包含t
                while True:
                    c = s[l]
                    if need[c] == 0:
                        # 遇到必须包含的字符 跳出
                        break
                    need[c] += 1
                    l += 1
                if r-l+1 < len_res:
                    res = s[l:r+1]
                    len_res = r-l+1
                l += 1
                needcnt += 1
                need[c] += 1

        return res if flag else ''