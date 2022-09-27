class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        双指针，1：当前索引 2：后面第一个不为零的索引，当前数为0时两者交换，直到指针2超出数组长度范围
        """
        next_nonzero_index = 1
        index = 0
        # for i in range(0, len(nums)):
        while next_nonzero_index < len(nums):
            if nums[index] != 0:
                index += 1
                next_nonzero_index += 1
            else:
                # next_nonzero_index = i+1
                while nums[next_nonzero_index] == 0:
                    if next_nonzero_index == len(nums)-1:
                        return nums
                    next_nonzero_index += 1
                swap_num = nums[index]
                nums[index] = nums[next_nonzero_index]
                nums[next_nonzero_index] = swap_num
                index += 1
                next_nonzero_index += 1
        return nums
    def moveZeroes_2(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        双指针，1：当前索引 2：后面第一个不为零的索引，当前数为0时用2指针覆盖1，直到指针2超出数组长度范围
        """
        next_nonzero_index = 1
        index = 0
        # for i in range(0, len(nums)):
        while next_nonzero_index < len(nums):
            if nums[index] != 0:
                index += 1
                next_nonzero_index += 1
            else:
                # next_nonzero_index = i+1
                while nums[next_nonzero_index] == 0:
                    if next_nonzero_index == len(nums)-1:
                        return nums
                    next_nonzero_index += 1
                # swap_num = nums[index]
                nums[index] = nums[next_nonzero_index]
                nums[next_nonzero_index] = 0
                index += 1
                next_nonzero_index += 1
        return nums


if __name__ == "__main__":

    test = Solution()
    nums = [1,0,0,1,0,3,0,0,12,0]
    print(nums)
    nums = test.moveZeroes(nums)
    print(nums)
