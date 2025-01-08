class Solution:
    def isPalindrome(self, s: str) -> bool: # O(n^2)
        s = ''.join(char.lower() for char in s if char.isalnum())
        rstr = ''.join(reversed(s))
        for char in range(len(s)):
            if s[char] != rstr[char]:
                return False
        return True

# Better solution
class Solution: # O(n)
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        return s == s[::-1]
