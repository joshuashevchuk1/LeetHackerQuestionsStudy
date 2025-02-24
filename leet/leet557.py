class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        reversedString = ""
        for word in words:
            if reversedString is not "":
                reversedString = reversedString + " " + word[::-1]
            else:
                reversedString = word[::-1]

        return reversedString

class SolutionBetter:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        reversed_words = [word[::-1] for word in words]  # List comprehension
        return " ".join(reversed_words)  # Join the reversed words
