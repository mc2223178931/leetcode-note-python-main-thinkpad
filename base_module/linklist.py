from collections import deque

class Test:
    def test(self):
        # create a linkedlist
        linklist = deque()

        # add element
        # time complexity: O(1)
        linklist.append(1)
        linklist.append(2)
        linklist.append(3)

        print(linklist)

        # insert element
        # time complexity: O(N)
        linklist.insert(2, 99)
        print(linklist)

        # access element
        # time complexity: O(N)
        element = linklist[2]
        print(element)

        # search element
        # time complexity: O(N)
        index = linklist.index(99)
        print(index)

        # update element
        # time complexity: O(N)
        linklist[2] = 88
        print(linklist)

        # remove element
        linklist.remove(88)
        print(linklist)

        # length
        # time complexity: O(1)
        length = len(linklist)
        print(length)
if __name__ == "__main__":
    test = Test()
    test.test()

