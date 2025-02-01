class Solution:
    def twoSumLessThanK(self, nums: list[int], k: int) -> int:
        ms = -1
        nums.sort()

        left, right = 0, len(nums) - 1

        def newMax(cs, ms, k):
            if cs < k and cs > ms:
                ms = cs
            return ms

        while left < right:
            cs = nums[left] + nums[right]
            ms = newMax(cs, ms, k)

            if cs < k:
                left += 1
            else:
                right -= 1

        return ms
