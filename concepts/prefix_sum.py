def prefixSumArray(nums):
    prev = 0
    ps = []
    for num in nums:
        prev += num
        ps.append(prev)

nums = [1,2,3]
prefixSumArray(nums)