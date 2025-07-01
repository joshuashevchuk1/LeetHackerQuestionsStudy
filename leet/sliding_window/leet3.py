
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        max_len = 0

        for end, char in enumerate(s):
            while char in seen:
                seen.remove(s[start])
                start += 1
            seen.add(char)
            max_len = max(max_len, end - start + 1)
        return max_len


stringA = "ccb"

solution = Solution()

print('longest is : ' , solution.lengthOfLongestSubstring(stringA))