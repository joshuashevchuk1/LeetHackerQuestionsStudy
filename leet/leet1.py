#
# for this problem we want to use a dictonary to store the indexs
#

#
# the meat of the problem is how we iterate using the hashmap
#

#
# we want iterate over nums
# the complement is the difference between the target and the num
# if the complement is not found store the num an index in the hashmap
# else if you find the complement as a key in num_map, return the i and i of the num_map[complement]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Dictionary to store number and its index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]  # Return indices of the two numbers
            num_map[num] = i  # Store the number and its index
