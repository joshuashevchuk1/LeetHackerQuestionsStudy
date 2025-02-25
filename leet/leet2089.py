from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l, r = 0, len(nums) - 1
        idxs = set()

        def binarySearch(l, r, target):
            while l <= r:
                middle = (l + r) // 2
                if nums[middle] == target and middle not in idxs:
                    idxs.add(middle)
                    left, right = middle - 1, middle + 1
                    while left >= l and nums[left] == target:
                        idxs.add(left)
                        left -= 1
                    while right <= r and nums[right] == target:
                        idxs.add(right)
                        right += 1
                    return
                elif nums[middle] < target:
                    l = middle + 1
                else:
                    r = middle - 1

        binarySearch(l, r, target)
        return sorted(list(idxs))
