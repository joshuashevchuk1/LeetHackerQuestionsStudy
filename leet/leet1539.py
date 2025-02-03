class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        i = 0
        current = 1
        missing = 0

        while k > 0:
            if i < len(arr) and arr[i] == current:
                i += 1
            else:
                k -= 1
                missing = current
            current += 1

        return missing
