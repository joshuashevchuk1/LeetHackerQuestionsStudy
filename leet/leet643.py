class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)

        if n == 1 and k == 1:
            return nums[0]

        if n < k:
            return None

        def slide(nums,k):
            ca = 0
            ma = 0
            for i in range(n - k + 1):
                num = nums[i:i + k]
                ca = sum(num)/len(num)
                if ca > ma:
                    ma = ca
            return ma

        return slide(nums,k)

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n == k:
            return sum(nums) / k

        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, n):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k

# optimial solution
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        if n == k == 1:
            return nums[0]

        def slide(nums,k):
            cs = sum(nums[:k])
            ms = cs

            for i in range(k, n):
                cs += nums[i] - nums[i - k]
                ms = max(ms,cs)
            return ms

        return slide(nums,k)/k
