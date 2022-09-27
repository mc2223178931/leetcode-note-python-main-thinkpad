

class Solution:
    """
        从左向右遍历nums1， 从右向左遍历nums2，nums2比x大的压入栈
    """
    def nextGreaterElement(self, nums1, nums2):
        results_list = []
        for i in nums1:
            stack = []
            for j in range(len(nums2)):
                j_ele = nums2[-1-j]
                if j_ele > i:
                    stack.append(j_ele)
                elif j_ele == i:
                    if len(stack) != 0:
                        results_list.append(stack.pop())
                    else:
                        results_list.append(-1)
        return results_list
    """
        通过Stack、HashMap解决

        先遍历大数组nums2，首先将第一个元素入栈；
        继续遍历，当当前元素小于栈顶元素时，继续将它入栈；当当前元素大于栈顶元素时，栈顶元素出栈，此时应将该出栈的元素与当前元素形成key-value键值对，存入HashMap中；
        当遍历完nums2后，得到nums2中元素所对应的下一个更大元素的hash表；
        遍历nums1的元素在hashMap中去查找‘下一个更大元素’，当找不到时则为-1。
    """

    def nextGreaterElement1(self, nums1, nums2):
        stack, hashmap = [], {}
        for i in nums2:
            while stack and stack[-1] < i:
                hashmap[stack.pop()] = i
            stack.append(i)
        return [hashmap.get(j, -1) for j in nums1]









if __name__ == "__main__":

    test = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    result = test.nextGreaterElement1(nums1, nums2)
    print(result)
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    result = test.nextGreaterElement1(nums1, nums2)
    print(result)
