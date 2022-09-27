class Solution:
    def containsDuplicate(self, nums) -> bool:
        hashmap = {}
        for i in nums:
            if hashmap.get(i):
                return True
            hashmap[i] = 1
        return False

    def containsDuplicate1(self, nums) -> bool:
        set_1 = set()
        for i in nums:
            set_1.add(i)
        return len(set_1) != len(nums)




if __name__ == "__main__":

    test = Solution()
    nums = [1, 2, 3, 1]
    nums1 = [1,1,1,3,3,4,3,2,4,2]
    res = test.containsDuplicate(nums1)
    print(res)
