# this file is to contain the conceptual understanding of kadanes algorithim (in 1d)

def ksum(nums):
    cs = ms = nums[0]
    for num in nums[1:]:
        cs = max(num, cs + num)
        ms = max(ms,cs)
    return ms

nums = [[1,2,3,4],[1,2,4,3]]
print(ksum([[1, 2, 3, 4], [1, 2, 4, 3]]))
print(max(nums))

nums2 = [2,-8,3,-2,4,-10]
print(ksum(nums2))


# also a problem in cracking the coding interview
def ksum(nums):
    cs = ms = nums[0] # the current max sum and current sum are both just negative infinity (none)
    for num in nums[1:]: # iterate over the array
        cs = max(num, cs + num) # find the current sum , add the cs + num and decide which is larger
        if cs > ms: # if current sum is greater than the max sum pointer, increase the max sum
            ms = cs
    return ms

# what about in 2 dimensions?

def k2d(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    ms = float('-inf')  # Initialize the maximum sum as negative infinity

    # Iterate over all pairs of rows (top, bottom)
    for top in range(rows):
        # Temporary 1D array to store column sums
        temp = [0] * cols # store a temp dp

        for bottom in range(top, rows):
            # Update column sums for the current row range
            for col in range(cols):
                temp[col] += grid[bottom][col]

            # Find the maximum sum subarray in the current column sums
            ms = max(ms, ksum(temp))  # Update the overall max sum

    return ms

grid = [[1,2,3],[1,2,3]]



print(ksum(nums))
print(ksum(nums2))
print(k2d(grid))