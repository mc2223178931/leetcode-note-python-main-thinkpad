from collections import deque
class RecentCounter:

    def __init__(self):
        # self.count = 0
        self.queue = deque()
    def ping(self, t: int) -> int:
        self.queue.append(t)
        while len(self.queue) > 1 and (t-self.queue[0]) > 3000:
            self.queue.popleft()

        return len(self.queue)




# Your RecentCounter object will be instantiated and called as such:


if __name__ == "__main__":
    obj = RecentCounter()
    # requests = [1, 100, 3001, 3002]

    requests = [642, 1849, 4921, 5936, 5957]
    output = []
    for t in requests:
        param_1 = obj.ping(t)
        output.append(param_1)
    print(output)