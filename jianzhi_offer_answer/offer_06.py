from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head == None:
            return []
        return self.reversePrint(head.next)+[head.val]




if __name__=="__main__":
    solution = Solution()
    head = [1,3,2]
    print(solution.reversePrint())