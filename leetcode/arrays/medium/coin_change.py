# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    # print('dp', dp)

    for amt in range(1, amount + 1):
        # print('amt', amt)
        for coin in coins:
            if amt - coin >= 0:
                dp[amt] = min(dp[amt], 1 + dp[amt - coin])

    return dp[amount] if dp[amount] != amount + 1 else -1


coinChange([1, 2, 5], 11)
