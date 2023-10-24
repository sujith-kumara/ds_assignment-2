def greedy_coin_change(denominations, target_amount):
    # Sort the denominations in descending order
    denominations.sort(reverse=True)
    
    # Initialize variables to keep track of the number of coins used and the remaining amount
    num_coins = 0
    remaining_amount = target_amount

    # Iterate through the denominations
    for coin in denominations:
        while remaining_amount >= coin:
            # Use as many of the current coin denomination as possible
            num_coins += 1
            remaining_amount -= coin

    return num_coins

# Example usage
coin_denominations = [25, 10, 5, 1]  # Quarters, dimes, nickels, pennies
target_amount = 63  # 63 cents

min_coins = greedy_coin_change(coin_denominations, target_amount)
print(f"Minimum number of coins needed: {min_coins}")
