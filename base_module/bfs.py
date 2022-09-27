# 宽度优先搜索BFS 搜索最短路径
# 由边构造图，字典key为节点，value为与节点有连接的节点
def graph_init(n, edges):
    graph_dict = {}
    for i in range(n):
        graph_dict[i] = []
    for j in range(len(edges)):
        u = edges[j][0]
        v = edges[j][1]
        graph_dict[u].append(v)
        graph_dict[v].append(u)
    return graph_dict
"""
# 队列的两种导入方法
# 1.使用queue
from queue import Queue
q = Queue() # 定义，为什么是这样涉及python的设计，不是很懂
q.put(node) # 放入
q.get() # 出队
# 2.使用deque
import collections
q = collections.deque() # 双向队列
q.append() # 入队
q.popleft() # 出队
"""
# from collections import deque
from queue import Queue
q = Queue()
n = 5
edges = [[0, 1], [0, 2], [1, 4], [2, 3], [2, 4]]
graph_dict = graph_init(n, edges)

def bfs(start_node, end_node):
    if start_node == end_node:
        return 0
    step = 0
    # 防止回溯
    hash_set = set()
    hash_set.add(start_node)
    # 入队
    q.put(start_node)
    while not q.empty():
        size = q.qsize()
        step += 1
        for iter in range(size):
            curr_node = q.get()   # 当前节点
            for neighbor_node in graph_dict[curr_node]:
                if neighbor_node == end_node:
                    return step
                elif neighbor_node in hash_set:
                    continue
                else:
                    hash_set.add(neighbor_node)
                    q.put(neighbor_node)
    return -1
min_step = bfs(0,4)
print(min_step)








