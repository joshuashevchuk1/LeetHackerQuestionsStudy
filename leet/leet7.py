class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
        strx = str(abs(x))
        ri = strx[::-1]
        if negative:
            rii = int(ri) * -1
        else:
            rii = int(ri)
        if rii > -2**31 and rii < (2**31)-1:
            return rii
        return 0
