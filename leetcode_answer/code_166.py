# 分数到小数
# 余数重复则有循环节 
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator//denominator)
        else:
            s = []
            start = 2
            if numerator//denominator < 0:
                s.append('-')
                start += 1

            numerator = abs(numerator)
            denominator = abs(denominator)
            yushu_list = []
            zhengshu = numerator//denominator

            s.append(str(zhengshu))
            s.append('.')
            yushu = numerator % denominator
            while (yushu not in yushu_list) and yushu:
                yushu_list.append(yushu)
                numerator = yushu * 10
                yushu = numerator % denominator
                chushu = numerator // denominator
                s.append(str(chushu))
                # print(chushu, yushu, s)
            if yushu != 0:
                ind = yushu_list.index(yushu)
                s.insert(ind+start, '(')
                s.append(')')

            return ''.join(s)






if __name__ == "__main__":
    solution = Solution()
    numerator = 7
    denominator = -12
    res = solution.fractionToDecimal(numerator, denominator)
    print(res)
