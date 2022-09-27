from collections import deque

class Test:
    def test(self):
        queue = deque()

        queue.append(1)
        queue.append(2)
        queue.append(3)

        print(queue)

        tm1 = queue[0]
        print(tm1)

        tm2 = queue.popleft()
        print(tm2)
        print(queue)

        leng = len(queue)
        print(leng)

        

if __name__ == "__main__":
    test = Test()
    test.test()
