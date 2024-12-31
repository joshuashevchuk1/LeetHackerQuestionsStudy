#
# concept to help out with default lists
#
from fiona.crs import defaultdict


#
#
#

def createDictIn3s(nums):
    weights = defaultdict()
    weights[1] = nums[:2]
    weights[2] = nums[3:5]
    weights[3] = nums[6:len(nums)]
    return weights


nums = [1,2,3,4,5,6,7,8,9]

