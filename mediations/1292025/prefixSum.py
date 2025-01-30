
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
