
def two_sum(nums, target):
    num_map = {}
    for index,num in enumerate(nums):
        print(num)
        diff = target - num
        if diff in num_map:
            return [num_map[diff],index]
        num_map[num] = index

nums = [3,4,5,6]
two_sum(nums, 7)