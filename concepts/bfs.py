from collections import deque

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