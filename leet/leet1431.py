class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bigC = max(candies)
        kids = []
        for candy in candies:
            if candy + extraCandies >= bigC:
                kids.append(True)
            else:
                 kids.append(False)
        return kids
