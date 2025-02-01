
def slide(nums,k):
    sums = []
    n = len(nums)
    for i in range(n-k):
        sums.append(sum(nums[i:k]))
    return sums


k =0
nums = [0,2,3,4,5]
print(slide(nums,k))

def windowSumCall(nums,k):
    n = len(nums)
    window = nums[:k]
    ws = sum(window)
    idx = 1
    ms = 0
    for i in range(n-k):
        ws = ws - nums[i] + nums[i + k]
        if ws > ms:
            ms = ws
            idx = i + 1

    return nums[idx:idx+k]


print(windowSumCall(nums,4))