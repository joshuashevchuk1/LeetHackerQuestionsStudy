def allSubsets(nums):
    subsets = [[]]  # Start with the empty subset
    for num in nums:
        # For each element in the nums list, add it to all existing subsets
        subsets += [subset + [num] for subset in subsets]
    return subsets

nums = [1,1,1]

print(allSubsets(nums))


def allSubRecursive(nums):
    subsets = []

    def recur(index, current):
        if current in subsets:
            return
        # Append the current subset to the subsets list
        subsets.append(current[:])  # Make a copy of current to avoid reference issues

        for i in range(index, len(nums)):
            # Include the current number and recurse
            current.append(nums[i])
            recur(i + 1, current)
            current.pop()  # Backtrack

    recur(0, [])
    return subsets

print(allSubRecursive(nums))
