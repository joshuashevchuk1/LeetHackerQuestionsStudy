# old

class Solution:
    def longestPalindrome(self, s: str) -> str:
        sl = len(s)

        if sl <= 1:
            return s

        def getPalin(left, right, s):
            while left >= 0 and right < sl and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the substring that forms the palindrome
            return s[left + 1:right]

        current_longest = ""

        for i in range(sl):
            # Check for odd-length palindromes
            current_palin_odd = getPalin(i, i, s)
            # Check for even-length palindromes
            current_palin_even = getPalin(i, i + 1, s)

            # Update longest palindrome if needed
            if len(current_palin_odd) > len(current_longest):
                current_longest = current_palin_odd
            if len(current_palin_even) > len(current_longest):
                current_longest = current_palin_even

        return current_longest
