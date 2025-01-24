# o log(n)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        i = 1
        while i <= n:
            if i == n:
                return True
            i = i * 2
        return False