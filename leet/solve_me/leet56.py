# TODO: Solve me

# Merge intervals

# intervals.sort(key=lambda x: x[0])

# 1. sort the double array by the 1st merged element
# 2. iterate of the array with the two pointer approach
#    merged = []
#    c = nums[i][0]
# 3. update this current as you slide across the array.
#    this condition is if c[start] > nums[i][end] start = 0, end = 1 (inner arrays have len 2)
# 4. if true merge to c.
# 5. else append c to merged and c is now nums[i]
# 6. repeat until i, make sure the len i + 1 is considered so the out of bounds is not hit.