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

