# this file is to contain the conceptual understanding of kadanes algorithim (in 1d)

def ksum(nums):
    cs = ms = nums[0]
    for num in nums[1:]:
        cs = max(num, cs + num)
        ms = max(ms,cs)
    return ms

nums = [[1,2,3,4],[1,2,4,3]]
print(ksum([[1, 2, 3, 4], [1, 2, 4, 3]]))
print(max(nums))
