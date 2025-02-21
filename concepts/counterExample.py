from collections import Counter


def anagram(s, t):
    return Counter(s)==Counter(t)

s="racecarererer"
t="carraceererre"

print(anagram(s, t))