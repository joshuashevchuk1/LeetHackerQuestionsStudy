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

# #You apply a dynamic programming (DP) table when you have a problem that exhibits the following key characteristics:
#
# 1. Overlapping Subproblems:
# The problem can be broken down into smaller subproblems, and these subproblems are solved repeatedly.
# Instead of solving the same subproblem multiple times (which would be inefficient), we solve each subproblem once and store the results to reuse later.
# Example: In the Longest Common Subsequence (LCS) problem, the subproblems involve calculating the LCS for progressively smaller prefixes of both strings.
# The same subproblems may be encountered multiple times during recursion.
# A DP table helps store the results of these subproblems and avoids redundant calculations.
#
# 2. Optimal Substructure:
# The optimal solution to the problem can be constructed efficiently from the optimal solutions to its subproblems.
# DP relies on the fact that solving smaller subproblems optimally will allow you to solve larger problems optimally.