class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:

        def prefixSum(nums):
            ps = [0]
            for num in nums:
                ps.append(ps[-1] + num)
            return ps

        ps = prefixSum(nums)
        min_sum = float('inf')

        for size in range(l, r + 1):
            for start in range(len(nums) - size + 1):
                end = start + size - 1
                subarray_sum = ps[end + 1] - ps[start]
                if subarray_sum > 0:
                    min_sum = min(min_sum, subarray_sum)

        return min_sum if min_sum != float('inf') else -1