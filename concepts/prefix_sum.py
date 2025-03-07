# prefix sum is defined as
# sum of the previous element plus the current element at each iteration
#
# n[i] = n[0]...n[i]
# p[i] = [n[-1] + n[0]] + [n[0] + n[1]] ... [n[len(n)-2] + n[-1]]
# sum[i,j] = P[j] - P[i]

def getPrefixSum(nums):
    n = len(nums)
    prefix = [0] * n
    prev = 0
    for i in range(n):
        prefix[i] = prev + nums[i]
        prev = nums[i]
    return prefix


nums = [1,2,3]

print(getPrefixSum(nums))

def subarraySum(ps, i, j):
    if i == 0:
        return ps[j]
    return ps[j] - ps[i-1]

def prefixSumArray(nums):
    prev = 0
    ps = []
    for num in nums:
        prev += num
        ps.append(prev)
    return ps

nums = [1,2,3]
ps = prefixSumArray(nums)

def subarraySumWindowK(ps, k):
    subarray_sums = []
    for i in range(k-1, len(ps)):
        subarray_sum = subarraySum(ps,i,i-k)
        subarray_sums.append(subarray_sum)
    return subarray_sums

i = 0
j = 2
print(ps)
sum = subarraySum(ps,i,j)
print(sum)

