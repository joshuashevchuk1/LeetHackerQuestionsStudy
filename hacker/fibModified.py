def fibonacciModified(t1, t2, n):
    dp = [0] * (n + 1)
    dp[0] = t1
    dp[1] = t2
    for i in range(n - 1):
        dp[i + 2] = dp[i] + (dp[i + 1]) ** 2

    return dp[n - 1]
