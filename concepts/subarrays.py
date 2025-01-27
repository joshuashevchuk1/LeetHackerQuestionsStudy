def allSubarrays(nums):
    subarrays = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subarrays.append(nums[i:j+1])  # Slice from i to j
    return subarrays

def subarraySum(nums, k):
    window_sum = 0
    for i in range(len(nums)):
        window_sum += nums[i]
        if i >= k:
            window_sum -= nums[i - k]  # Remove the element that's sliding out of the window
        if i >= k - 1:
            print(f"Subarray sum from {i-k+1} to {i}: {window_sum}")