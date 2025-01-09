from collections import deque


class SolutionG:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        def ksum(nums):
            current_sum = max_sum = 0
            window = deque()  # Sliding window to maintain order
            seen = set()  # HashSet to track distinct elements

            for num in nums:
                # Remove duplicates from the window
                while num in seen:
                    removed = window.popleft()
                    seen.remove(removed)
                    current_sum -= removed

                # Add the current number to the window
                window.append(num)
                seen.add(num)
                current_sum += num

                # If the window exceeds size k, remove the oldest element
                if len(window) > k:
                    removed = window.popleft()
                    seen.remove(removed)
                    current_sum -= removed

                # Update max_sum only if the window size is exactly k
                if len(window) == k:
                    max_sum = max(max_sum, current_sum)

            return max_sum

        return ksum(nums)

class Solution:
    def minimualSubarraySum(self, arr, k):
        ms = 0
        for num in arr:
            cs = sum(arr[num:num + k])
            ms = max(ms, cs)
        return ms

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