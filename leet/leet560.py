class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        array_count = 0
        for i in range(len(nums)):
            current_sum = 0  # Reset current_sum for each new starting point
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum == k:
                    array_count += 1
        return array_count



# with hashmap prefix sum

# Sum[i,j] = P[j] - P[i-1]

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # Step 1: Initialize the hashmap with the base case {0: 1}
        # which represents the prefix sum before we start, and a counter for the subarrays
        prefix_sum_count = {0: 1}  # Tracks how many times each prefix sum has occurred.
        current_sum = 0            # Running total (P[j]).
        array_count = 0            # Subarrays found.

        # Step 2: Iterate through each number in the array
        for num in nums:
            current_sum += num  # Update P[j] (current prefix sum)

            # Step 3: Check if current_sum - k exists in the hashmap
            if current_sum - k in prefix_sum_count:
                array_count += prefix_sum_count[current_sum - k]  # Add the number of times that sum occurred

            # Step 4: Update the hashmap with the current prefix sum
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

        # Step 5: Return the total number of subarrays found
        return array_count


