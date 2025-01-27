def prefixSumArray(nums):
    prev = 0
    ps = []
    for num in nums:
        prev += num
        ps.append(prev)
    return ps

nums = [1,2,3]
ps = prefixSumArray(nums)

def subarraySum(ps, i, j):
    if i == 0:
        return ps[j]
    return ps[j] - ps[i-1]


def subarraySumWindowK(ps, k):
    subarray_sums = []
    for i in range(k-1, len(ps)):
        subarray_sum = subarraySum(ps,i,i-k)
        subarray_sums.append(subarray_sum)
    return subarray_sums

def subarraySumWindowK(ps, k):
    subarray_sums = []
    for i in range(k-1, len(ps)):
        subarray_sum = subarraySum(ps,i,i-k)
        subarray_sums.append(subarray_sum)
    return min(subarray_sums)

i = 0
j = 2
print(ps)
sum = subarraySum(ps,i,j)
print(sum)

