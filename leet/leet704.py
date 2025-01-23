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
    def search(self, nums: list[int], target: int) -> int:

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

# proper solution non recursive

class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l = 0
        r = len(nums)

        if nums[l] == target:
            return l

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
