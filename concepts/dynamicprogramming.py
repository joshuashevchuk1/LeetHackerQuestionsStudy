# the fibonaci sequence is (n-1)th and (n-2)th

# the lowest number is 1

# via recursion
def getFibN(n): # O(2**n)
        if n <= 1:
            return n
        return getFibN(n-1) + getFibN(n-2)

print(getFibN(5))


# using dp tabulation:

def getFibTabulation(n):
    dp = [0] * (n+1)

    dp[0] = 0
    dp[1] = 1
    print(dp)

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        print(dp)
    return dp[n]

print(getFibTabulation(5))


def LCSTabulation(text1,text2):
    m,n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)] # dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j]= dp[i-1][j-1] + 1
        else:  # Characters don't match
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # dp recursion relation
        print(dp)
    return dp[m][n]

text1="dog"
text2="cad"
print("table: ", LCSTabulation(text1,text2))