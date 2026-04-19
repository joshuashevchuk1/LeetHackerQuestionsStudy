
def getBytes(x):
    return bin(x)

print(getBytes(11))

print(str(getBytes(16)))

def getHamminWeight(x):
    x_bytes = bin(x)
    return str(bin(x).count("1"))

print(getHamminWeight(11))

class Solution:
    def hammingWeight(self, n: int) -> int:
        return int(str(bin(n).count("1")))
