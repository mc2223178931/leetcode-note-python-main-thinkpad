class ArrayTest:
    def test(self):
        # create an array
        a = []

        # add  element
        a.append(1)
        # O(1)
        a.append(2)
        a.append(3)
        print(a)
        a.insert(2, 99)
        # O(N)
        print(a)

        # access element
        temp = a[2]
        # O(1)
        print(temp)

        # update element
        a[2] = 88
        print(a)

        # remove element
        a.remove(88)
        print(a)

        a.pop(1)
        print(a)

        a.pop()
        print(a)

        # get array size
        a = [1, 2, 3]
        size = len(a)
        print(size)

        # iterate array O(N)
        # first iterate
        for i in a:
            print(i)
        # second iterate
        for index, element in enumerate(a):
            print("Index at:", index, "is:", element)
        # third iterate
        for index in range(0, len(a)):
            print("Index at:", index, "is:", a[index])

        # find an element O(N)
        index = a.index(2)
        print(index)

        # sort an array O(NlogN)

        a = [3, 1, 2]
        # from small to big
        a.sort()
        print(a)
        # from big to small
        a.sort(reverse=True)
        print(a)

if __name__=="__main__":
    test = ArrayTest()
    test.test()
