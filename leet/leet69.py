import numpy as np


def find_all_subsets(paramArray):
    subsets = []
    # There are 2^len(paramArray) subsets for a given list
    num_subsets = 2 ** len(paramArray)

    for i in range(num_subsets):
        # Generate each subset using bit manipulation or combination logic
        subset = []
        for j in range(len(paramArray)):
            # If the j-th bit in i is 1, include paramArray[j] in the subset
            if (i & (1 << j)) > 0:
                subset.append(paramArray[j])
        subsets.append(subset)

    return subsets


paramArray = [1, 2, 3]

subsets = find_all_subsets(paramArray)
print(subsets)
