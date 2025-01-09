
class Solution:
    def isPalindrome(self, s: str) -> bool: # O(n^2)
        s = ''.join(char.lower() for char in s if char.isalnum())
        rstr = ''.join(reversed(s))
        for char in range(len(s)):
            if s[char] != rstr[char]:
                return False
        return True

# Better solution
class Solution2: # O(n)
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        return s == s[::-1]

#two pointer solution, waaaay better and simpler
class Solution2p:
    def isPalindrome(self, s: str) -> bool:
        sl = len(s)
        start = 0
        end = sl - 1  # Corrected to sl - 1
        while start < end:  # Changed to start < end
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True  # if loop is not broken

solution = Solution2p()
print(solution.isPalindrome("aba"))
print(solution.isPalindrome("abad"))
print(solution.isPalindrome("abba"))
print(solution.isPalindrome("ababa"))
print(solution.isPalindrome("abcba"))
print(solution.isPalindrome("abcdaba"))
