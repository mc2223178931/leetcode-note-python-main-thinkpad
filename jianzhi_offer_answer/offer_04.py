from typing import List
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        def find_target(array):
            n = len(array)
            if n <= 1:
                return (target in array)
            else:
                if array[n//2] == target:
                    return True
                elif array[n//2] > target:
                    return find_target(array[:n//2])
                else: 
                    return find_target(array[n//2:])

        if matrix == [[]] or matrix == []:
            return False
        # m = len(matrix)
        n = len(matrix[0])
        for li in matrix:
            if li[0] == target or li[-1] == target:
                return True
            elif li[0] > target and li[-1] < target:
                continue
            else:
                if find_target(li[1:n]):
                    return True
        return False

if __name__=="__main__":
    solution = Solution()
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    matrix = []
    target = 5
    print(solution.findNumberIn2DArray(matrix, target))

