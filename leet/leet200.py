# Given an m x n 2D binary grid grid which
# represents a map of '1's (land) and '0's (water),
# return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent
# lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# this is a dfs problem
#
# 1. create the boundary points for the dfs grid,
# 2. the boundaries are i=0,i=len(grid), j=0, j = len(grid[0]) and the visited grid[i][j]
# 3. iterate across the grid
# 4. at the iteration if 1 is found, up a pointer (count, num etc)
# 5. remove all the 1s next to it in the zone.
# 6. restart the iteration from you left off
#
