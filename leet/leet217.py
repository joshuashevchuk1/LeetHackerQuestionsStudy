class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        common = set()
        for num in nums:
            if num not in common:
                common.add(num)
            elif num in common:
                return True
        return False