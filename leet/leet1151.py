#
# TODO: Solve me
#
# 1151. Minimum Swaps to Group All 1's Together
# Medium
# Topics
# Companies
# Hint
# Given a binary array data, return the minimum number of swaps required to
# group all 1’s present in the array together in any place in the array.

# Input: data = [1,0,1,0,1]
# Output: 1
# Explanation: There are 3 ways to group all 1's together:
# [1,1,1,0,0] using 1 swap.
# [0,1,1,1,0] using 2 swaps.
# [0,0,1,1,1] using 1 swap.
# The minimum is 1.

# Example 2:
#
# Input: data = [0,0,0,1,0]
# Output: 0
# Explanation: Since there is only one 1 in the array, no swaps are needed.

# best solution
# use a sliding window
# 1. pointer count the window.
# 2. slide the window across the array.
# 3. after sliding k-window pointer is the minimum.