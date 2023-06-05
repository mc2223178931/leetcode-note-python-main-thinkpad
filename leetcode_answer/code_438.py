from typing import List
class Solution:
# 暴力 双指针
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        windows = len(p)
        if len(s)<windows:return res
        num_dict = {}
        for pp in p:
            if pp not in num_dict:
                num_dict[pp] = 1
            else:
                num_dict[pp] += 1

        for start in range(len(s)-windows+1):
            num_dict2 = {}
            temp = s[start:start+windows]
            for tt in temp:
                if tt not in num_dict2:
                    num_dict2[tt] = 1
                else:
                    num_dict2[tt] += 1
            if num_dict == num_dict2:
                res.append(start)
 # 滑动窗口 数组存储异位词频率
    def findAnagrams1(self, s: str, p: str) -> List[int]:               
        res = []
        windows = len(p)
        if len(s)<windows:return res
        s_count, p_count = [0]*26, [0]*26
        for i in range(len(p)):
            s_count[ord(s[i])-97] += 1
            p_count[ord(p[i])-97] += 1

        if s_count == p_count: res.append(0)

        for start in range(1, len(s)-windows+1):
            s_count[ord(s[start-1])-97] -= 1
            s_count[ord(s[start+windows-1])-97] += 1
            if s_count == p_count: res.append(start)