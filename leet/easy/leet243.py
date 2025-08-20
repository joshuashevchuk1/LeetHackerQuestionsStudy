class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        i1,i2=-1,-1
        min_distance = float("inf")
        for index, word in enumerate(wordsDict):
            if word == word1:
               i1=index
            if word == word2:
               i2=index
            if i1 != -1 and i2 != -1:
                min_distance = min(min_distance, abs(i1 - i2))
        return min_distance