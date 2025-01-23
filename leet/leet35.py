class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        def search(nums,target):
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
                elif nums[mid] > target:
                    r = mid - 1

            return l

        return search(nums,target)