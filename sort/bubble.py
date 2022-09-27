def bubbleSort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [6,8,3,2,9,1]


print(bubbleSort(nums))

def selectSort(list):
    for i in range(len(list)-1):
        min = i
        for j in range(i+1, len(list)):
            if list[j]<list[min]:
                min = j
                list[min],list[i] = list[i], list[min]
    return list

print(selectSort([1,3,2,8,6,3]))

def insertSort(list):
    for i in range(1,len(list)):
        j = i-1
        key = list[i]
        while j >= 0:
            if list[j] > key:
                list[j+1] = list[j]
                list[j] = key
            j -= 1
    return list
print(insertSort([1,3,2,8,6,3]))