class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = [word for word in s.split(" ") if word]
        answer = " ".join(words[::-1])
        return answer
