class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        def prefixSum(nums):
            ps = []
            prev = 0
            for num in nums:
                prev += num
                ps.append(num+prev)
            return ps

        ps = prefixSum(nums)

        total_sum = ps[-1]

        for i in range(len(nums)):
            left_sum = ps[i - 1] if i > 0 else 0
            right_sum = total_sum - ps[i]

            if left_sum == right_sum:
                return i

        return -1