class Solution:
    def myAtoi(self, s: str) -> intc:
        isNeg = False
        s = s.replace(" ", "")
        s = s.lstrip("0")
        if "-" in s:
            s = s.lstrip("-")
            isNeg = True

        for i in range(len(s)):
            if not s[i].isnumeric():
                s = s.split(s[i])[0]
                break

        if isNeg is False:
            return int(s)
        if isNeg is True:
            return int(s) * -1


class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        result = 0

        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Convert digits
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        # 4. Clamp to 32-bit signed int
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result