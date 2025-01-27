def get_all_substrings(s):
    n = len(s)
    substrings = []
    for i in range(n):
        substrings.append(s[i])
        for j in range(i + 1, n):
            substrings.append(s[i:j + 1])
    return substrings


s = "asddab"

subs = get_all_substrings(s)

print(subs)


