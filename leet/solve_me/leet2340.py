#
# TODO: Solve me
#
# 2340. Minimum Adjacent Swaps to Make a Valid Array
#
# You are given a 0-indexed integer array nums.
#
# Swaps of adjacent elements are able to be performed on nums.
#
# A valid array meets the following conditions:
#
# The largest element (any of the largest elements if there are multiple) is at the rightmost position in the array.
# The smallest element (any of the smallest elements if there are multiple) is at the leftmost position in the array.
# Return the minimum swaps required to make nums a valid array.

# Input: nums = [3,4,5,5,3,1]
# Output: 6
# Explanation: Perform the following swaps:
# - Swap 1: Swap the 3rd and 4th elements, nums is then [3,4,5,3,5,1].
# - Swap 2: Swap the 4th and 5th elements, nums is then [3,4,5,3,1,5].
# - Swap 3: Swap the 3rd and 4th elements, nums is then [3,4,5,1,3,5].
# - Swap 4: Swap the 2nd and 3rd elements, nums is then [3,4,1,5,3,5].
# - Swap 5: Swap the 1st and 2nd elements, nums is then [3,1,4,5,3,5].
# - Swap 6: Swap the 0th and 1st elements, nums is then [1,3,4,5,3,5].
# It can be shown that 6 swaps is the minimum swaps required to make a valid array.

# Input: nums = [9]
# Output: 0
# Explanation: The array is already valid, so we return 0.

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
#
# Conceptual plan
#
# Find all occurrences:
#
# You will need to find all positions of the minimum element and all positions of the maximum element in the array.
# Determine the closest pair:
#
# After finding all the indices of the smallest and largest elements, you want to find the pair where the smallest element is as close as possible to the largest element.
# The idea is to minimize the total number of moves to bring the smallest element to the front (index 0) and the largest element to the back (index len(nums) - 1).
#
# Evaluate the swaps:
#
# For each combination of a minimum element and a maximum element, calculate the number of swaps:
# Move the minimum element to the leftmost position (index 0).
# Move the maximum element to the rightmost position (index len(nums) - 1).
# If the minimum element is to the right of the maximum element, the swap calculation will need to account for their positions crossing.
#
# Choose the best pair:
#
# After evaluating the possible swap scenarios for all pairs of minimum and maximum element positions, select the one that results in the fewest total swaps.
#
# positions = [i for i, x in enumerate(array) if x == number] <-- gets positions of the numbers. This is required.