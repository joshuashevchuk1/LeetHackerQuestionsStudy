#
# TODO: solve me
#
# You are given an array nums consisting of positive integers.
#
# You can perform the following operation on the array any number of times:
#
# Choose any two adjacent elements and replace them with their sum.
# For example, if nums = [1,2,3,1], you can apply one operation to make it [1,5,1].
# Return the minimum number of operations needed to turn the array into a palindrome.
#
# Conceptual plan:
#
# 1. iterate the left and right side of the array
# 2. if palondromic no need to sum
# 3. if not palondromic, try to sum and make palondromic
# 4. if cannot be palondromic. return zero.
# 5. otherwise two pointer approach
#
