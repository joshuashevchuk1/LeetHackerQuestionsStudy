class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        bigC = max(candies)
        kids = []
        for candy in candies:
            if candy + extraCandies >= bigC:
                kids.append(True)
            else:
                 kids.append(False)
        return kids
