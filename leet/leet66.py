class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        t = len(digits) - 1

        def addAtTail(digits, t):
            if t < 0:
                digits = [0] * (len(digits) + 1)
                digits[0] = 1
                return digits
            if digits[t] < 9:
                digits[t] += 1
                return digits
            if digits[t] == 9:
                digits[t] = 0
                t -= 1
                return addAtTail(digits, t)

        return addAtTail(digits, t)

# slighty better solution, O(1) space complexity

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        t = len(digits) - 1

        while t >= 0:
            if digits[t] < 9:
                digits[t] += 1
                return digits
            digits[t] = 0
            t -= 1

        # Handle carry beyond the most significant digit
        return [1] + digits
