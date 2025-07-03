def min_swaps_to_group_ones(arr):
    total_ones = sum(arr)
    if total_ones == 0 or total_ones == len(arr):
        return 0  # Already grouped

    # Sliding window of size total_ones
    max_ones_in_window = 0
    current_ones = 0
    left = 0

    for right in range(len(arr)):
        if arr[right] == 1:
            current_ones += 1

        # If window size exceeds total_ones, slide left pointer
        if right - left + 1 > total_ones:
            if arr[left] == 1:
                current_ones -= 1
            left += 1

        max_ones_in_window = max(max_ones_in_window, current_ones)

    # Minimum swaps needed
    return total_ones - max_ones_in_window

# Example usage:
arr = [1, 0, 1, 0, 1]
print(min_swaps_to_group_ones(arr))  # Output: 1
