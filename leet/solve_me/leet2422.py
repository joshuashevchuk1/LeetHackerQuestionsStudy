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
# Initialize two pointers:
#
# left starting from the beginning (0).
# right starting from the end (n - 1).
# Iterate while left < right:
#
# Case 1: If nums[left] == nums[right], these elements are already palindromic. Move the pointers inward:
#
# Increment left.
# Decrement right.
# Case 2: If nums[left] != nums[right], perform the following:
#
# If nums[left] < nums[right]:
# Merge nums[left] with nums[left + 1] by summing them.
# Replace nums[left] and move left inward.
# If nums[right] < nums[left]:
# Merge nums[right] with nums[right - 1] by summing them.
# Replace nums[right] and move right inward.
# Stop the process when the pointers meet or cross (left >= right):
#
# At this point, the array is guaranteed to be a palindrome if all conditions are followed.
# Edge case: If the array cannot be transformed into a palindrome (though this is not possible under valid constraints), return 0. However, since merging always reduces the array size, it should always converge to a palindrome eventually.
#
# Return the count of operations performed during the process.
