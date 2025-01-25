class Solution:
    def kthCharacter(self, k: int) -> str:

        s = ["a"]

        def next_letter(char):
            return chr(ord(char) + 1)

        while len(s) < k:
            for i in range(len(s)):
                s.append(next_letter(s[i]))

        return s[k - 1]




