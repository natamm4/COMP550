# Problem 2. Suppose there are an unlimited number of dimes (10 cents each), nickels (5 cents), and
# pennies (1 cent). The input is a positive integer t, and we want to select the fewest number of coins such
# that their total value is t cents. The greedy algorithm is to pick as many dimes as possible (i.e., without
# exceeding t), then as many nickels as possible, then as many pennies as possible.
# Describe an O(1)-time implementation of the greedy algorithm, explain why the greedy algorithm is
# correct, and analyze the running time of your implementation. The algorithm should return a tuple (a, b, c),
# where a is the number of dimes, b is the number of nickels, and c is the number of pennies chosen by the
# greedy algorithm.
# Hint: For the correctness explanation, start by using an exchange argument to prove that ALG and
# OPT pick the same number of dimes. Bonus (0 points): Explain why your proof is not correct if the coins
# had values (4, 3, 1) instead of (10, 5, 1).

def coins(t):
    dimes = t // 10
    t = t - dimes * 10
    nickels = t // 5
    t = t - nickels * 5
    pennies = t
    return (dimes, nickels, pennies)

print(coins(1002))