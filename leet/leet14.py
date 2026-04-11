# longest common prefix

# def lcp(s):
#     common = set.intersection(*map(set, s))
#     return common

def lcp(s):
    lcp = ""
    s.sort()
    for i in range(len(s) - 1):
        if s[i] in s[i + 1]:
            lcp += s[i]
    return lcp


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs
        s.sort()

        first_word = s[0]
        last_word = s[-1]

        lcp = ""

        for i in range(len(first_word)):
            if i < len(last_word) and first_word[i] == last_word[i]:
                lcp += first_word[i]
            else:
                break

        return lcp

list_of_strings = ["apple", "app", "ape"]

print(lcp(list_of_strings))