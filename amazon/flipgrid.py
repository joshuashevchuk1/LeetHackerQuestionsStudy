# TODO: find an efficient/more optimized solution

import numpy as np

def flip_by_90(grid):
    flipped = []
    for i in range(len(grid[0])):
        new_row = [grid[j][i] for j in range(len(grid)-1,-1,-1)]
        flipped.append(new_row)

    print("flipped : " + str(flipped))

grid =  [[1,2,3],[4,5,6],[7,8,9]]
grid2 = [[1,2],[3,4],[5,6]]

# [1.2.3]            [7,4,1]
# [4,5,6] --> 90 --> [8,5,2]
# [7,8,9]            [9,6,3]

# [1,2]             [1,3,5]
# [3,4] --> 90 -->  [2,4,6]
# [5,6]

flip_by_90(grid)
flip_by_90(grid2)