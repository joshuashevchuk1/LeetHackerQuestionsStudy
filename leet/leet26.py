class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums.sort()

        u = set()
        for i in range(len(nums) - 1, -1, -1):  # O(n)
            if nums[i] in u:
                nums.pop(i)  # O(n)
            if nums[i] not in u:
                u.add(nums[i])

# O(n^2)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        new_nums = []
        u = set()
        for num in nums:  # O(n)
            if num not in u:
                u.add(num)
                new_nums.append(num) #O(1)
        nums[:] = new_nums

# O(n)