# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#将传入的数组转化为链表
def create_linked_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head
#传入链表头节点，以数组形式返回
def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

class Solution:
    def removeElements(self, head: ListNode, val: int):
        dummy = ListNode(0)
        dummy.next = head
        previous = dummy
        while (head != None):
            if head.next != None:
                if head.val == val:
                    previous.next = head.next
                    head = head.next
                else:
                    previous = head
                    head = head.next
            else:
                if head.val == val:
                    previous.next = None
                    head = None
                else:
                    head = None
        return dummy.next
if __name__ == "__main__":

    test = Solution()
    head = [1, 2, 6, 3, 4, 5, 6]
    head = create_linked_list(head)
    val = 6
    list_ans = test.removeElements(head, val)
    print(print_linked_list(list_ans))

