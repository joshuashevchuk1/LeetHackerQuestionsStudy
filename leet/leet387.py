from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters_map = defaultdict(list)
        firstCharIndex = float('inf')
        for index, char in enumerate(s):
            letters_map[char].append(index)
        for key,value in letters_map.items():
            if len(value) == 1:  # Unique character
                firstCharIndex = min(firstCharIndex, value[0])
        return firstCharIndex if firstCharIndex != float('inf') else -1

s1 = "eeleetcode"
s2 = "leetcode"
solution = Solution()
print(solution.firstUniqChar(s1))
print(solution.firstUniqChar(s2))