from fiona.crs import defaultdict


# example

def mapPatterns(pattern,s):
    map = defaultdict()
    sl = s.split(" ")

    for string in sl:
        for char in pattern:
            if string not in map.values() and char not in map.keys():
                map[char] = string
            elif map[char] is not string:
                return False
    return True

def mapPatterns(pattern, s):
    mapping = {}
    words = s.split()

    if len(pattern) != len(words):
        return False

    for char, word in zip(pattern, words):
        if char in mapping:
            if mapping[char] != word:
                return False
        else:
            if word in mapping.values():
                return False
            mapping[char] = word

    return True


print(mapPatterns(pattern="aba",s="ate bat ate"))