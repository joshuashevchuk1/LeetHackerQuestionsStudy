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
