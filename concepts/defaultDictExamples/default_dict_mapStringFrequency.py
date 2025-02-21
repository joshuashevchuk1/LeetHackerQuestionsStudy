from collections import defaultdict

def anagram(s, t):
    smap = defaultdict(int)
    tmap = defaultdict(int)
    for char in s:
        smap[char] += 1

    for char in t:
        tmap[char] += 1

    return smap==tmap

s="racecarererer"
t="carraceererre"

print(anagram(s, t))