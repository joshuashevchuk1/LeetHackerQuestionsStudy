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


def find_all_subsets_without_math(paramArray):
    subsets = [[]]  # Start with the empty set
    for element in paramArray:
        # For each element, create new subsets by adding the element to existing subsets
        new_subset = [subset + [element] for subset in subsets]
        subsets.extend(new_subset)  # Add the new subsets to the list of subsets

    return subsets

paramArray = [1, 2, 3,4, 4]

subsets = find_all_subsets(paramArray)
print(subsets)

subsets = find_all_subsets_without_math(paramArray)
print(subsets)
