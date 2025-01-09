
# subarray of size k with sum = 3

def sliding_window(arr,k):
    # window = arr[:k]
    window_sum = sum(arr[:k])
    max_sum = window_sum
    idx = 1
    n = len(arr)
    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        if window_sum > max_sum:
            max_sum = window_sum
            idx = i + 1

    return arr[idx:idx + k],max_sum


arr, sum_2 = sliding_window([1, 3, 4, 5, 6, 7], 3)
print(arr)
print(sum_2)


# not num, use i derp
from leet.leet2461 import SolutionQ


class Solution:
    def minimualSubarraySum(self, arr, k):
        ms = 0
        # Use a sliding window approach
        for i in range(len(arr) - k + 1):  # We only need to go to len(arr) - k
            cs = sum(arr[i:i+k])  # sum of the subarray from i to i+k
            ms = max(ms, cs)  # Update max sum
        return ms

arr = [1,2,3,4,3,5]

solution = Solution()
print(solution.minimualSubarraySum(arr,2))

# for 2d arrays

class Solution2D:
    def minimualSubarraySum(self, arr, k):
        ms = 0
        rows = len(arr)
        cols = len(arr[0])

        # Iterate over each row and apply sliding window for columns
        for i in range(rows):
            for j in range(cols - k + 1):  # For each row, slide horizontally
                cs = sum(arr[i][j:j+k])  # Sum the subarray of length k horizontally
                ms = max(ms, cs)  # Track the maximum sum
        return ms

# use a queue
from collections import deque


class SolutionQ:
    def minimualSubarraySumQ(self, arr, k):
        current_sum = sum(arr[:k])  # Initialize sum with first k elements
        ms = current_sum

        window = deque(arr[:k])  # Initialize the deque with the first k elements

        for i in range(k, len(arr)):  # Start sliding the window
            # Update the sum by removing the leftmost element and adding the new element
            current_sum -= window.popleft()  # Pop the leftmost element (the one leaving the window)
            current_sum += arr[i]  # Add the new element to the window
            window.append(arr[i])  # Add the new element to the deque

            ms = max(ms, current_sum)  # Track the max sum

        return ms


# can be optimized using a prefix sum
class SolutionP:
    def minimualSubarraySum(self, arr, k):
        ms = 0
        current_sum = sum(arr[:k])  # Initial sum of the first window
        ms = current_sum

        for i in range(1, len(arr) - k + 1):
            current_sum = current_sum - arr[i - 1] + arr[i + k - 1]
            ms = max(ms, current_sum)

        return ms

arr = [1,2,3,4,3,5]
sq = SolutionQ()
print(sq.minimualSubarraySumQ(arr,2))