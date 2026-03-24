
def Solution(a):
    return lambda x : x * a


l1 = Solution(2)

print(l1(2))