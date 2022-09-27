class UnionFind:
    def __init__(self, tree_list):
        self.root = [i for i in tree_list]

    # 找到x的根节点
    def find(self, x):
        if x == self.root[x]:
            return self.root[x]
        return self.find(self.root[x])

    #将x，y的根节点合并
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_x] = root_y
class UnionFind_quick:
    def __init__(self, tree_list):
        self.root = [i for i in tree_list]
        self.rank = [0 for i in tree_list]
    # 找到x的根节点
    def quick_find(self, x):
        if x == self.root[x]:
            return self.root[x]
        self.root[x] = self.quick_find(self.root[x])
        return self.root[x]

    #将x，y的根节点合并 权重 思想：防止树太高
    def quick_union(self, x, y):
        root_x = self.quick_find(x)
        root_y = self.quick_find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            else:
                self.root[root_y] = root_x
                self.root[root_x] += 1

