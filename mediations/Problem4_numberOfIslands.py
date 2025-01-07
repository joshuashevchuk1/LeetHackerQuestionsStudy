
# 1. use the dfs method as below. At location mark visted.
def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid) or grid[i][j] == "0":
        return
    dfs[i][j] = "0" # visited marker

    # iteration steps
    dfs[i+1][j] # right
    dfs[i-1][j] # left
    dfs[i][j-1] # up
    dfs[i][j+1] # down

# 2. check if its a grid
def numIslands(grid):
    if not grid:
        return 0

# 3. pointer for the island
    island_count = 0

# 4 .iterate through the grid.
    for i in range(len(grid)):
        for j in range(len(grid[0])):

# 5. found an island, do a dfs on the islands perimeters
            if grid[i][j] == "1":
                island_count += 1
                dfs(grid, i, j)  # Start DFS from this point

# 6. repeat until the island is visited and return the island count

    return island_count

# this can be increased for performance on the iteration using a que

from collections import deque

def numIslands(grid):
    if not grid:
        return 0

    def bfs(grid, i, j):
        # Initialize a queue for BFS
        queue = deque([(i, j)])
        grid[i][j] = "0"  # Mark as visited
        while queue:
            x, y = queue.popleft()  # Get the current position
            # Explore all 4 directions
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1":
                    grid[nx][ny] = "0"  # Mark as visited
                    queue.append((nx, ny))  # Add to the queue for further exploration

    island_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":  # Found an unvisited land
                island_count += 1
                bfs(grid, i, j)  # Start BFS from this land cell
    return island_count

# BFS is generally safer in terms of memory and avoids issues with deep recursion in DFS.
# It may also be slightly more efficient in terms of handling certain grid shapes.
# DFS might be faster in cases where the island is relatively compact and doesn’t require too deep of recursion.
# In terms of asymptotic time complexity, both BFS and DFS for this problem are O(m * n), so the difference in
# performance would not be due to time complexity but to practical considerations like memory usage,
# recursion depth, and specific grid shapes.