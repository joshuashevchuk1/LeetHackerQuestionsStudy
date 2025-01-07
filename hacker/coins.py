
def getWays(n, c):
    # Initialize the DP array
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: 1 way to make amount 0

    # Update the DP array for each coin
    for coin in c:
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]

    return dp[n]

def maxCoins(n, c):
    # Initialize the DP array with "-infinity" (to find maximums)
    dp = [-float('inf')] * (n + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Iterate over each coin
    for coin in c:
        for amount in range(coin, n + 1):
            dp[amount] = max(dp[amount], dp[amount - coin] + 1)

    # If dp[n] is still -inf, return -1 (not possible to make the amount)
    return dp[n] if dp[n] != -float('inf') else -1

def minCoins(n, c):
    # Initialize the DP array with "infinity" (a large value)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Iterate over each coin
    for coin in c:
        for amount in range(coin, n + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[n] is still infinity, return -1 (not possible to make the amount)
    return dp[n] if dp[n] != float('inf') else -1