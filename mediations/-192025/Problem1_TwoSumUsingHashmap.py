#Problem 1: Two-Sum using Hashmaps
# Prompt:
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to the target.
# Assume there is exactly one solution, and you may not use the same element twice.

#Use a Hashmap for Fast Lookup:

# Instead of iterating over the array again for each number, maintain a hashmap (num_map) that stores numbers and their indices as you iterate.
# Single Pass:

# For each number, calculate the complement (target - num).
# Check if the complement exists in the hashmap. If it does, you’ve found your pair.
# Return Result:

# If you find the pair, return their indices.
# If no pair is found (although the problem guarantees one), continue iterating.

def two_sum(nums, target):
    num_map = {}  # hashmap to store number and its index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]  # return indices of complement and current number
        num_map[num] = i  # store the current number with its index
    return []  # in case no solution exists (shouldn't happen in this problem)