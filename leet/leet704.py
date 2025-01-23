# recursive solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def recurse(nums, target, start=0):
            if not nums:
                return -1
            m = (len(nums) - 1) // 2
            left = nums[:m]
            right = nums[m + 1:]
            mid_value = nums[m]
            if mid_value == target:
                return start + m
            if target in left:
                return recurse(left, target, start)
            if target in right:
                return recurse(right, target, start + m + 1)
            return -1

        return recurse(nums, target)

# two pointer solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)

        if nums[l] == target:
            return l

        while l < r:
            if nums[l] == target:
                return l
            else:
                r -= 1
            if nums[r] == target:
                return r
            else:
                l += 1

        return -1
