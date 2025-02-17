# [Newman-Conway sequence] is the one which generates the following integer sequence.
# 1 1 2 2 3 4 4 4 5 6 7 7….. and follows below recursive formula.


def solve_newman_conway(n):
    dp = [0] * (n+1)

    dp[1] = 1
    dp[2] = 1

    for i in range(3,n+1):
        dp[i] = dp[dp[i-1]] + dp[i-dp[i-1]]

    return dp

dp = solve_newman_conway(10)

print(dp)

