class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        start = 0
        end = len(str_x) - 1
        while start < end:
            if str_x[start] != str_x[end]:
                return False
            start += 1
            end -= 1

        return True
