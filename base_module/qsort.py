# 递归
def qsort(arr):

    if not len(arr):
        return []
    else:
    # 在这里以第一个元素为基准线
        pivot = arr[0]
        left = qsort([x for x in arr[1:] if x < pivot])
        right = qsort([x for x in arr[1:] if x >= pivot])
    return left+[pivot]+right

arr = [4,3,7,2,1,9,3,0]
arr_sort = qsort(arr)
print(arr_sort)

def quick_sort(arr):
    '''''
    模拟栈操作实现非递归的快速排序
    '''
    if len(arr) < 2:
        return arr
    stack = []
    stack.append(len(arr)-1)
    stack.append(0)
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(arr, l, r)
        if l < index - 1:
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index + 1)


def partition(arr, start, end):
    # 分区操作，返回基准线下标
    pivot = arr[start]
    while start < end:
        while start < end and arr[end] >= pivot:
            end -= 1
        arr[start] = arr[end]
        while start < end and arr[start] <= pivot:
            start += 1
        arr[end] = arr[start]
    # 此时start = end
    arr[start] = pivot
    return start