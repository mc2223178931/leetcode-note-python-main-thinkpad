
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap = {}
        for i in s:
            if hashmap.get(i):
                hashmap[i] = hashmap.get(i) + 1
            else:
                hashmap[i] = 1
        for j in t:
            if hashmap.get(j):
                if hashmap[j] == 0:
                    return j
                else:
                    hashmap[j] = hashmap[j] - 1
            else:
                return j
    """
        s和t拼接后遍历，统计其个数，若为奇数则输出
    """
    def findTheDifference1(self, s: str, t: str) -> str:
        m=s+t
        for i in m:
            if m.count(i)%2==1:
                return i

if __name__ == "__main__":
    test = Solution()
    s = "abcd"
    t = "abcda"
    result = test.findTheDifference(s, t)
    print(result)