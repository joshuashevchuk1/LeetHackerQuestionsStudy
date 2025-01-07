from collections import deque


def maxSubarray(arr):
    if not arr:
        return []

    cs = 0  # Current sum
    max_sum = float('-inf')  # To store the maximum sum found
    max_array = deque()  # Deque to track the current window elements
    current_window = deque()  # To track the current subarray of maximum sum

    for num in arr:
        cs += num
        current_window.append(num)

        # Check if current sum is greater than previous max sum
        if cs > max_sum:
            max_sum = cs
            max_array = deque(current_window)  # Update the result with the new window

        # If the sum of the current window becomes negative, reset the window
        if cs < 0:
            cs = 0
            current_window.clear()

    return list(max_array)  # Return the subarray corresponding to the max sum
