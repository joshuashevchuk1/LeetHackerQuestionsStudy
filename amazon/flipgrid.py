# TODO: find an efficient/more optimized solution

import numpy as np

def flip_by_90(grid):
    flipped = []
    for i in range(len(grid[0])):
        new_row = [grid[j][i] for j in range(len(grid)-1,-1,-1)]
        flipped.append(new_row)

    print("flipped : " + str(flipped))

def flip_by_90_better(grid):
    n = len(grid)
    # In-place operation to rotate the grid by 90 degrees
    for i in range(n // 2):  # Only iterate until half the length
        for j in range(i, n - i - 1):
            # Perform 4-way swap in place
            temp = grid[i][j]
            grid[i][j] = grid[n - j - 1][i]
            grid[n - j - 1][i] = grid[n - i - 1][n - j - 1]
            grid[n - i - 1][n - j - 1] = grid[j][n - i - 1]
            grid[j][n - i - 1] = temp

    print("flipped : " + str(grid))


def flip_by_90_in_place(grid):
    # Step 1: Transpose the matrix in place
    n = len(grid)  # Assuming the grid is square (n x n)
    for i in range(n):
        for j in range(i + 1, n):  # Only swap the upper triangle
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]

    # Step 2: Reverse each row
    for row in grid:
        row.reverse()

    print("flipped in place : " + str(grid))

def flip_by_90_with_numpy(grid):
    a = np.array(grid, dtype='int32')  # Convert the input grid to a numpy array
    a = a.transpose()
    a = a.tolist()
    for row in a:
        row.reverse()
    return print("flipped with numpy : "  + str(a))

# [1.2.3]            [7,4,1]
# [4,5,6] --> 90 --> [8,5,2]
# [7,8,9]            [9,6,3]

grid =  [[1,2,3],[4,5,6],[7,8,9]]
flip_by_90(grid)
grid =  [[1,2,3],[4,5,6],[7,8,9]]
flip_by_90_in_place(grid)
grid =  [[1,2,3],[4,5,6],[7,8,9]]
flip_by_90_with_numpy(grid)