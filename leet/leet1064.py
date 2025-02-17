
# l        m        r
#[-2,1,0,1,2,5,8,10,11]
#[0,1,2,3,4,5,6,7,8]

class Solution:
    def fixedPoint(self, arr: list[int]) -> int:
        l , r = 0, len(arr) -1

        ans = -1
        while l <= r:
            mid = (l+r)//2
            if arr[mid] == mid:
                ans = mid
                r = mid - 1 # push towards minimum ->l
            elif arr[mid] > mid:
                r = mid - 1  # push towards minimum -> l
            elif arr[mid] < mid:
                l = mid + 1 # push towards maximum -> r
        return ans