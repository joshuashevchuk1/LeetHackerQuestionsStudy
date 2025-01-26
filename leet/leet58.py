class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        slist = s.split(" ")
        sl = len(slist) - 1
        last_word = [slist[sl]]
        return len(last_word[0])
