# find the kth factor of n
# a factor means n % i == 0

def isFactor(n,i):
    if n % i == 0:
        return True
    return False

print("isFactor : ", isFactor(4,2))
print("isFactor : ", isFactor(4,3))
print("isFactor : ", isFactor(4,5))
print("isFactor : ", isFactor(4,8))

def getFactors(n):
    factors = []
    for i in range(1, n + 1):
        if isFactor(n, i):
            factors.append(i)
    return factors

def getKthFactor(n, k):
    factors = getFactors(n)
    if k <= len(factors):
        return factors[k - 1]
    else:
        return None

n = 25*2*3*4
j = 5
factors = getFactors(25*2*3*4)
print(factors)
k = 5
kthFactor = getKthFactor(n,k)
print("kth factor : ", kthFactor)