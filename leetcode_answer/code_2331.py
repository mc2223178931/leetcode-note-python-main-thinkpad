# compute bool two split tree value
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def compute_bool(root: Optional[TreeNode]):
            if root.left == None and root.right == None:
                return root.val
            left_val = compute_bool(root.left)
            right_val = compute_bool(root.right)
            if root.val == 2:
                return left_val | right_val
            elif root.val == 3:
                return left_val & right_val

        return True if compute_bool(root) == 1 else False

def makeTree(l:List) -> TreeNode:
    """ 由输入列表生成树，返回根节点 """
    q = []
    if not l:
        return
    root = TreeNode(val=l.pop(0))
    q.append(root)
    while q:
        t = q.pop(0)
        if l:
            if l[0] != 'null':
                t.left = TreeNode(val=l.pop(0))
                q.append(t.left)
            else:
                l.pop(0)
        if l:
            if l[0] != 'null':
                t.right = TreeNode(val=l.pop(0))
                q.append(t.right)
            else:
                l.pop(0)
    return root


if __name__ == "__main__":
    solution = Solution()
    # null = None
    root = [2, 1, 3, 'null', 'null', 0, 1]
    root = makeTree(root)
    res = solution.evaluateTree(root)
    print(res)
