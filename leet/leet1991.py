class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        def prefixSum(nums):
            ps = []
            prev = 0
            for num in nums:
                prev += num
                ps.append(prev)
            return ps

        ps = prefixSum(nums)

        def getMiddle(ps,nums):
            n = len(nums)
            for i in range(n):
                left = ps[i-1] if i > 0 else 0
                right = ps[-1] - ps[i]
                if left == right:
                    return i
            return -1

        return getMiddle(ps,nums)