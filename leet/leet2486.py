# You are given two strings s and t consisting of only lowercase English letters.
#
# Return the minimum number of characters that need to be appended
# to the end of s so that t becomes a subsequence of s.
#
# A subsequence is a string that can be derived from another string by
# deleting some or no characters without changing the order of the remaining characters.


class Solution:
    # this is wrong because only 1 pointer is used
    def appendCharactersWrong(self, s: str, t: str) -> int:
        value = 0
        for i in range(len(s)):
            if i < len(t) and t[i] == s[i]:
                value += 1
        return abs(value - len(t))

    # Greedy refers to the strategy where you make the locally optimal choice
    # (in this case, trying to match the characters of t in s in order)
    # with the hope that it leads to the globally optimal solution.

    # need to use 2 pointer approach
    # this is correct because
    def appendCharactersCorrect(self, s: str, t: str) -> int:
        t_index = 0  # Pointer for t
        # Iterate through s
        for i in range(len(s)):
            if t_index < len(t) and t[t_index] == s[i]:
                t_index += 1  # Move the pointer in t when there's a match
            if t_index == len(t):  # All characters of t are found in order
                break
        # The number of characters to append is the remainder of t
        return len(t) - t_index

    def appendCharactersBest(self, s: str, t: str) -> int:
        i = 0
        # in this case no breaks need to be defined
        # the additional range(len(s)) comp is not needed.
        for char in s:
            if i < len(t) and char == t[i]:
                i += 1
        return len(t) - i

solution = Solution()
s ="abx"
t ="xba"
print(solution.appendCharactersCorrect(s,t))

