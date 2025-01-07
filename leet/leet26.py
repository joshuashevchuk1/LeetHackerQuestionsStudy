class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()

        u = set()
        for i in range(len(nums) - 1, -1, -1):  # O(n)
            if nums[i] in u:
                nums.pop(i)  # O(n)
            if nums[i] not in u:
                u.add(nums[i])

# O(n^2)
