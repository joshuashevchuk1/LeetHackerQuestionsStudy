from collections import Counter
from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        count = Counter(num % value for num in nums)
        i = 0
        while True:
            mod = i % value
            if count[mod] == 0:
                return i
            count[mod] -= 1
            i += 1