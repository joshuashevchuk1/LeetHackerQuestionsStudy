class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        def boundary(i, j):
            return i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0

        def dfs(i, j):
            if boundary(i, j):
                return 0

            grid[i][j] = 0

            area = 1

            area += dfs(i + 1, j)  # Down
            area += dfs(i - 1, j)  # Up
            area += dfs(i, j + 1)  # Right
            area += dfs(i, j - 1)  # Left

            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:  # Found a new island
                    max_area = max(max_area, dfs(i, j))

        return max_area