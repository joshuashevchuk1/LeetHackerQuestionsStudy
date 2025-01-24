class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n == 1:
            return True

        i = 1
        while i <= n:
            if i == n:
                return True
            i = i * 4
        return False
