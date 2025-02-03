class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 2
        right = num/2

        if not isinstance(num,int):
            return False

        if num == 1:
            return True

        while left <= right:
            mid = (left + right)//2
            guess_squared = mid * mid
            if guess_squared == num:
                return True
            if guess_squared > num:
                right = mid - 1
            else:
                left = mid + 1
        return False