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
# nested loops lead to an order of O(n * m)
# use a sliding window for O(n)

#
#  create a window of len(target),
#  slide across the iterable
#
#







