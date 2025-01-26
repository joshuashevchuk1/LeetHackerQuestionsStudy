class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0

        grid.sort()
        def isNegative(num):
            return True if num < 0 else False

        for i in range(len(grid)):
            row = grid[i]
            for num in row:
                if isNegative(num):
                    count += 1

        return count


# o log (n) solution which is better because a binary search is implemented
class Solution:
    def findFirstNegative(self,arr):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]<0:
                high=mid-1
            else:
                low=mid+1
        return high+1
    def countNegatives(self, grid: list[list[int]]) -> int:
        c=0
        for arr in grid:
            n=self.findFirstNegative(arr)
            total=len(arr)
            c+=total-n
        return c