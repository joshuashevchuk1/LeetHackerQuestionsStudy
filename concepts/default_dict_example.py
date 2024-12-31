#
# concept to help out with default lists
#
from collections import defaultdict
#
#
#

def createDictIn3s(nums):
    weights = defaultdict()
    weights[1] = nums
    if len(nums) > 9:
        weights[1] = nums[:8]
    if len(nums) > 9*2:
         weights[2] = nums[3:5]
    if len (nums) > 9*3:
        weights[3] = nums[6:len(nums)]
    return weights

def getStringArray(string):
    items = list(string)
    items.sort()
    return items

nums = [1,2,3,4,5,6,7,8,9]
string = 'apple'

weights = createDictIn3s(nums)
string_array = getStringArray(string)

print(weights)

string_weights = createDictIn3s(string_array)
print(string_weights)


