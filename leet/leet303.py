class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefix = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.prefix[i] = self.prefix[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
