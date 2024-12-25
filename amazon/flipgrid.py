# TODO: find an efficient/more optimized solution

def flip_by_90(grid):
    flipped = []
    for i in range(len(grid[0])):
        new_row = [grid[j][i] for j in range(len(grid))]
        flipped.append(new_row)
    print("flipped : " + str(flipped))

grid =  [[1,2,3],[4,5,6],[7,8,9]]
grid2 = [[1,2],[3,4],[5,6]]

# [1.2.3]            [1,4,7]
# [4,5,6] --> 90 --> [2,5,8]
# [7,8,9]            [3,6,9]

# [1,2]             [1,3,5]
# [3,4] --> 90 -->  [2,4,6]
# [5,6]

flip_by_90(grid)
flip_by_90(grid2)