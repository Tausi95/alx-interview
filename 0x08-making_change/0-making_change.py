#!/usr/bin/python3

def makeChange(coins, total):
    """Return the fewest number of coins needed to meet the total."""
    
    # If total is 0 or less, no coins are needed
    if total <= 0:
        return 0
    
    # Initialize the DP array with infinity
    dp = [float('inf')] * (total + 1)
    
    # Base case: 0 coins are needed to make the total of 0
    dp[0] = 0
    
    # Iterate over each coin
    for coin in coins:
        # Update the DP array for each amount from the coin value to total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still infinity, return -1 (total cannot be met)
    return dp[total] if dp[total] != float('inf') else -1
