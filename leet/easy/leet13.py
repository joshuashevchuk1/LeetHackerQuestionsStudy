class Solution:
    def romanToInt(self, s: str) -> int:
        map_roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = 0
        for i in range(len(s)):
            value = map_roman[s[i]]
            if i +1 < len(s) and map_roman[s[i]] < map_roman[s[i+1]]:
                total -= value
            else:
                total += value
        return total