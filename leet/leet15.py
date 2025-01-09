class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        solutions = set()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            two_sum_result = self.twoSum(nums[i + 1:], target)
            for pair in two_sum_result:
                solutions.add((nums[i], pair[0], pair[1]))

        return [list(triplet) for triplet in solutions]

    def twoSum(self, nums: list[int], target: int) -> list[list[int]]:
        num_map = {}
        result = []
        for num in nums:
            complement = target - num
            if complement in num_map:
                result.append([complement, num])
            num_map[num] = 1
        return result

# two pointer
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Sort the array first
        solutions = []

        for i in range(len(nums) - 2):
            # Skip duplicate elements to avoid repeating triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]  # We are looking for two numbers that sum to -nums[i]
            left, right = i + 1, len(nums) - 1  # Two pointers

            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    solutions.append([nums[i], nums[left], nums[right]])
                    # Move pointers to skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1  # We need a larger sum, so move left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, so move right pointer to the left

        return solutions
