def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index
        if nums[mid] == target:  # Found the target
            return mid
        elif nums[mid] < target:  # Target is on the right half
            left = mid + 1
        else:  # Target is on the left half
            right = mid - 1

    return -1  # Target not found

def binary_search_first(nums, target):
    l, r = 0, len(nums) - 1
    result = -1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            result = m
            r = m - 1  # continue search on left side
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return result

def binary_search_last(nums, target):
    l, r = 0, len(nums) - 1
    result = -1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            result = m
            l = m + 1  # continue search on right side
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return result


# Example usage
nums = [1, 3, 5, 7, 9, 11]
target = 7
print(binary_search(nums, target))  # Output: 3 (index of target 7)
