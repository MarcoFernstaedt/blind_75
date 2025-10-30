def max_profit(prices):
    min_so_far = float("inf")
    max_profit = 0
    for p in prices:
        if p - min_so_far > max_profit:
            max_profit = p - min_so_far
        if p < min_so_far:
            min_so_far = p
    return max_profit


# Profitable
prices = [7, 1, 5, 3, 6, 4]  # expect 5
[2, 4, 1]  # expect 2
[3, 2, 6, 5, 0, 3]  # expect 4

# No profit
[7, 6, 4, 3, 1]  # expect 0
[5]  # expect 0
[2, 2, 2]  # expect 0

# Larger pattern
[1, 2, 3, 4, 5]  # expect 4
[5, 1, 2, 10, 1, 0, 12]  # expect 11
print(max_profit(prices))
