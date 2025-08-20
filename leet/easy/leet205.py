class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if len(set(s)) != len(set(t)):
            return False

        map_a = list(dict.fromkeys(s))
        map_b = list(dict.fromkeys(t))

        mapping = dict(zip(map_a, map_b))

        for c1,c2 in zip(s,t):
            if mapping[c1] != c2:
                return False
        return True