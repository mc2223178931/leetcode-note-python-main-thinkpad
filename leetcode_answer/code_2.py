# Definition for singly-linked list.
#定义节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 将传入的数组转化为链表
def create_linked_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head

# 传入链表头节点，以数组形式返回
def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

class Solution:
    def addTwoNumbers(self, l1, l2) :
        head = ListNode(0)
        cur = head
        res_next = 0
        for i in range(101):
            l1_num = l1.val if l1 else 0
            l2_num = l2.val if l2 else 0
            res = l1_num + l2_num + res_next
            # if res == 0:
            #     cur.next = None
            #     break
            res_next = res // 10
            cur.next = ListNode(res % 10)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if not l1 and not l2 and not res_next:
                # print(l1)
                # print(l2)
                cur.next = None
                break
        return head.next
            # result.next




if __name__ == "__main__":
    solution1 = Solution()



    l1 = [1, 6, 0, 3, 3, 6, 7, 2, 0, 1]
    l2 =  [6, 3, 0, 8, 9, 6, 6, 9, 6, 1]
    l1_listnode = create_linked_list(l1)
    l2_listnode = create_linked_list(l2)
    res_listnode = solution1.addTwoNumbers(l1_listnode, l2_listnode)
    # print(res_list)
    res_array = print_linked_list(res_listnode)
    #
    print(res_array)
