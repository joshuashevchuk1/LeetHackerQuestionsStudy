class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # O(n^2) solution
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True

        return False

# efficient solution

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for array in matrix:
            if target >= array[0] and target <= array[-1]:
                l, r = 0, len(array) - 1
                while l <= r:
                    mid = (l + r) // 2

                    if array[mid] == target:
                        return True
                    elif array[mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1

        return False
