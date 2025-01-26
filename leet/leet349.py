class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common = []
        l1 = len(nums1)
        l2 = len(nums2)
        l = l1 if l1 < l2 else l2
        if l == l1:
            for num in nums1:
                if num in nums2 and num not in common:
                    common.append(num)
        if l == l2:
            for num in nums2:
                if num in nums1 and num not in common:
                    common.append(num)

        return common

