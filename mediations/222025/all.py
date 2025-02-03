# prefix-sum calc

nums = [1,2,3,4]

def ps(nums):
    prev = 0
    ps = []
    for num in nums:
        prev += num
        ps.append(prev)

def get_max(ps,j,i):
    return ps[j-i]