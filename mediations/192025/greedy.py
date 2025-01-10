def coinChange(coins, amount):
    # Sort coins in descending order for greedy choice
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if amount == 0:
            break
        # Use as many coins of this denomination as possible
        count += amount // coin
        amount %= coin

    # If amount becomes 0, we have found the minimum number of coins
    return count if amount == 0 else -1  # -1 if it's not possible to make the amount


# Example usage
coins = [1, 5, 10, 25]
amount = 30
print(coinChange(coins, amount))  # Output: 2 (1 coin of 25, 1 coin of 5)
