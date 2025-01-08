
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


arr, sum = sliding_window([1,3,4,5,6,7],3)
print(arr)
print(sum)
