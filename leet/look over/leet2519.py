# leet 2519 this is a complicated heapq problem. That is the best way to solve it.

# You are given a 0-indexed integer array nums and a positive integer k.

# We call an index i k-big if the following conditions are satisfied:
#
# There exist at least k different indices idx1 such that idx1 < i and nums[idx1] < nums[i].
# There exist at least k different indices idx2 such that idx2 > i and nums[idx2] < nums[i].
# Return the number of k-big indices.