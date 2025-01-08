# general doc for guidelines on when to use which method

#============================================================================
#
# 1. Prefix sum
#
#
# commonly used when you need to query the sum of elements in a subarray
#

#
# Make a prefix sum array where P[i] = A[0] + A[1] + ... A[i]
#
# Sum[i,j] = P[j] - P[i-1]
#

#
# LC: 303, 525, 560
#

#============================================================================

#
# 2. Two pointers
#

#
# initialize two pointers, p1,p2 and move them in an array closer or further away from each other.
#

#
# useful for palindromes, you can iterate over a string from the start and end to determine if the palindrome
# is actually a palindrome
#
# can reduce problems from O(n^2) to O(n)
#

#
# LC: 167, 15, 11
#

#============================================================================

#
# 3. Sliding window
#

#
# common problems for these would be subarrays
#
# nested loops lead to an order of O(n * m)
# use a sliding window for O(n)
#
# Sliding window is ideal for problems like:
#
# Finding the maximum sum of a subarray of length k.
# Longest substring with at most k distinct characters.
# Contiguous subarrays that meet certain conditions (e.g., sum, product).
#

#
#  create a window of len(target),
#  sum/min etc on the window
#  keep track of the max_sum
#  keep track of the index position
#  slide across the iterable
#  a. subtract the ith element from the window sum
#  b. add the ith + k element to the window sum
#  return array position or sum/min etc
#

#
# LC: 643,3,76
#

#============================================================================

#
# 11. dfs
#

#
# dfs is used to explore ALL paths or branches from graphs or tres. So its mostly used for graph and tree problems
#
# its used for the following common problems
# a. finding a path between two nodes
# b. checking if a graph contains a cycle
# c. finding a topological order in a directed acyclic graph (DAG)
# d. counting the number of connected components in a graph
#

#
# LC: 133, 113, 210
#


#
# 15. dp
#

#
# commonly used for overlapping problems
#
