# not num, use i derp
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

class Solution:
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

# use a queue for a better result. The queue is faster!
class SolutionQ:
    def minimualSubarraySumQ(self, arr, k):
        current_sum = sum(arr[:k])  # Initial sum of the first window
        ms = current_sum

        # Use a sliding window approach
        for i in range(k, len(arr)):  # Start sliding the window from index k onwards
            # Update the sum by removing the element that's left out and adding the new one
            current_sum = current_sum - arr[i - k] + arr[i]
            ms = max(ms, current_sum)

        return ms


# can be optimized using a prefix sum

class Solution:
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