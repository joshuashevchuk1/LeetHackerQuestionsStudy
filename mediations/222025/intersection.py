
def intersection(nums1,nums2):
    s1 = set(nums1)
    s2 = set(nums2)
    return list(s1 & s2)


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