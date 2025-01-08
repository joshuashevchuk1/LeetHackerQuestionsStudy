class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        print('n is ', n)

        if needle not in haystack:
            return -1

        for i in range(h):
            print(i)
            print(haystack[i:i + len(needle)])
            if haystack[i:len(needle)] == needle:
                return i