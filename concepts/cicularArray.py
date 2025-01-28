
nums = [1,2,3]

def loopAroundAnArray(nums):
    n = len(nums)

    for i in range(2 * n):
        print(nums[i % n])

loopAroundAnArray(nums)