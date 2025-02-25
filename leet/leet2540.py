class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        common_min = float('inf')

        def binary_search(num, nums2):
            l, r = 0, len(nums2) - 1
            while l <= r:
                middle = (l + r) // 2
                if nums2[middle] == num:
                    return num
                elif nums2[middle] > num:
                    r = middle - 1
                else:
                    l = middle + 1
            return float('inf')

        for num in nums1:
            common_min = min(common_min, binary_search(num, nums2))

        return common_min if common_min != float('inf') else -1

# better solution

class BetterSolution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        i = j = 0
        m, n = len(nums1), len(nums2)
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1