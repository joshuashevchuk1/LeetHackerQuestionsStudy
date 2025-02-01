
def iterateTwoPointersForBackAndForth(nums):
    l = 0
    r = len(nums)
    while l < r:
        if l != r:
            return False
        l +=1
        r +=1
    return True

nums = [0,1,2,3,4,5]

boolval = iterateTwoPointersForBackAndForth(nums)
print(boolval)

nums = [1,2,3,4,5]

def iterateTwoPointersToFindTheMiddle(nums):
    slow = 0
    fast = 0
    while fast < len(nums) and fast + 1 < len(nums):
        fast +=2
        slow +=1

    return nums[slow]


middle = iterateTwoPointersToFindTheMiddle(nums)

print(middle)