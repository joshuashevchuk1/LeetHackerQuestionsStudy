
def slidingWindowLoop(nums):
    fast = 1
    slow = 0
    l = len(nums)
    while fast != l:
        print(nums[slow])
        print(nums[fast])
        fast += 1
        slow += 1


nums = [2,3,4,5]

slidingWindowLoop(nums)


def slidingWindow(nums, k):
    n = len(nums)
    if n < k:
        return None  # Handle edge case if window size is larger than the array

    max_sum = 0
    current_sum = sum(nums[:k])  # Initialize the window sum with the first k elements
    max_sum = current_sum

    # Slide the window
    for i in range(k, n):
        current_sum += nums[i] - nums[i - k]  # Add the next element, remove the leftmost element
        max_sum = max(max_sum, current_sum)  # Update the maximum sum if needed

    return max_sum


def slidingWindowOfK(nums, k):
    n = len(nums)
    if n < k:
        return None

    for i in range(n - k + 1):
        print(nums[i:i + k]) # actual i to k sliding

# Example call
nums = [1, 2, 3, 4, 5]
slidingWindowOfK(nums, 2)
