
def getNewSet():
    return set()

set = getNewSet()

set.add(1)
set.pop()


# this solution is nearly as fast as the & operator in python but is customizable to include duplicates
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        common = set()
        l1 = len(nums1)
        l2 = len(nums2)
        s1 = set(nums1)
        s2 = set(nums2) # sets are faster than lists in python
        l = l1 if l1 < l2 else l2 # ternary for which l to iterate over
        if l == l1: # choose this length if smaller
            for num in s1:
                if num in s2 and num not in common:
                    common.add(num)
        if l == l2: # choose this length if smaller
            for num in s2:
                if num in s1 and num not in common:
                    common.add(num)

        return list(common)

# super compact solution

# this solution always its faster due to how sets work in python
# note it would always revoke duplicates
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1=set(nums1)
        set2=set(nums2)

        return list(set2 & set1)

# you can also find dup based sets

from collections import Counter

def duppedBased():
    set1 = [1, 2, 2, 3]
    set2 = [2, 2, 3, 4]

    # Using Counter to preserve counts
    counter1 = Counter(set1)
    counter2 = Counter(set2)

    # Find the intersection with preserved duplicates
    intersection = counter1 & counter2
    print(list(intersection.elements()))  # Output: [2, 2, 3]
