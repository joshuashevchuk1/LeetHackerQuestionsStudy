def subsets(nums):
    def backtrack(start, path):
        result.append(path[:])  # Add the current subset (path) to the result
        for i in range(start, len(nums)):
            path.append(nums[i])  # Include the current element
            backtrack(i + 1, path)  # Recur to include the next element
            path.pop()  # Backtrack, remove the last element

    result = []
    backtrack(0, [])  # Start from the first element with an empty subset
    return result