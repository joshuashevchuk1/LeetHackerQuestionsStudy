class Solution:
    def twoSumLessThanK(self, nums: list[int], k: int) -> int:
        ms = -1
        nums.sort()  # Sort the list first

        left, right = 0, len(nums) - 1  # Two pointers

        def newMax(cs, ms, k):
            if cs < k and cs > ms:
                ms = cs
            return ms

        while left < right:
            cs = nums[left] + nums[right]
            ms = newMax(cs, ms, k)  # Check and update max sum

            if cs < k:
                left += 1  # If sum is less than k, move left pointer to increase sum
            else:
                right -= 1  # If sum is >= k, move right pointer to decrease sum

        return ms
