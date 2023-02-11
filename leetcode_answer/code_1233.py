from typing import List
class Trie:
    def __init__(self):
        self.child = dict()
        self.ref = -1

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Trie()
        for path in folder:
            cur = root
            path_split_list = path.split('/')
            for subpath in path_split_list[1:]:
                if subpath not in cur.child:
                    cur.child[subpath] = Trie()
                cur = cur.child[subpath]
            cur.ref = 1
        # DFS
        res = []
        path = []
        def dfs(root, path, res):
            # if root.ref > 0:
            #     res.append('/'.join(path.copy()))
            #     return
            for i in root.child:
                cur_trie = root.child[i]
                path.append(i)
                # print(i, path, cur_trie.ref)
                if cur_trie.ref < 0:
                    dfs(cur_trie, path, res)
                else:
                    res.append('/'+'/'.join(path.copy()))
                path.pop()

        dfs(root, path, res)
        return res




if __name__ == "__main__":
    solution1 = Solution()
    folder = ["/aa/ab", "/ah"]
    RES = solution1.removeSubfolders(folder)
    print(RES)
