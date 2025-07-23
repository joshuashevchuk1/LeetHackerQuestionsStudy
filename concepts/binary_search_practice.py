def binary_search_practice(nums, target):
    l , r = 0, len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l += 1
        else:
            r -=1
    return -1

nums = [1, 3, 5, 7, 9, 11, 20, 6, 8, 9,7]
nums.sort()
target = 7
print(binary_search_practice(nums, target))