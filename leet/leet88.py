class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int):
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        return nums1,nums2



a = [1,2,3]
m = 1
b = [2,3,4]
n = 2
solution = Solution()
print(solution.merge(a,m,b,n))
