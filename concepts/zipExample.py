
a = "aac"
b = "bbd"

def isoCheck(s,t):
        if len(s) != len(t):
            return False

        if len(set(s)) != len(set(t)):
            return False

        map_a = list(dict.fromkeys(s))
        map_b = list(dict.fromkeys(t))

        mapping = dict(zip(map_a, map_b))

        for c1, c2 in zip(s, t):
            if mapping[c1] != c2:
                return False
        return True


print(isoCheck(a,b))