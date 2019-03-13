from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

"""Coin Change.

You are given coins of different denominations and a total amount of 
money amount. Write a function to compute the fewest number of coins 
that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the 
coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Note: You may assume that you have an infinite number of each kind of coin.

Ref: Leetcode 322. Coin Change (Medium)
"""


def coin_change_recur(amount, coins):
    """Change minimum coins by naive top-down recursion."""
    if amount < 0:
        return -1
    if amount == 0:
        return 0

    min_coins = float('inf')

    for c in coins:
        extra_coins = coin_change_recur(amount - c, coins)
        if extra_coins >= 0 and extra_coins < min_coins:
            min_coins = 1 + extra_coins

    if min_coins != float('inf'):
        return min_coins
    else:
        return -1


def _coin_change_memo(amount, coins, L):
    """Helper function for coin_change_memo()."""    
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    
    if L[amount] > 0:
        return L[amount]

    min_coins = float('inf')

    for c in coins:
        extra_coins = _coin_change_memo(amount - c, coins, L)
        if extra_coins >= 0 and extra_coins < min_coins:
            min_coins = 1 + extra_coins

    if min_coins != float('inf'):
        L[amount] = min_coins
    else:
        L[amount] = -1

    return L[amount]


def coin_change_memo(amount, coins):
    """Change minimum coins by top-down recursion + memoization."""
    L = [0] * (amount + 1)
    min_coins = _coin_change_memo(amount, coins, L)
    return min_coins


def coin_change_dp(amount, coins):
    """Change minimum coins by dynamic programming by bottom-up."""
    # Why sorted coin list? Since we want to start from smaller coins.
    coins = sorted(coins)

    n_coins = len(coins)
    T = [[float('inf')]*(amount + 1) for c in range(n_coins)]

    # Base case for amount 0.
    for c in range(n_coins):
        T[c][0] = 0

    # Start from smallest coin to change from amount 0 to total amount.
    for c in range(n_coins):
        for a in range(1, amount + 1):
            if coins[c] == a:
                # Directly use coin c to change total amount.
                T[c][a] = 1
            elif a - coins[c] >= 0:
                # If coin c can be included, decide which uses less coins:
                # 1. previous coins without coin c to make a.
                # 2. previous coins without coin c to make a - coins[c]
                #    plus this 1 extra coin c.
                T[c][a] = min(T[c - 1][a], 1 + T[c][a - coins[c]])
            else:
                # If coin c cannot be included, use previous coins.
                T[c][a] = T[c - 1][a]

    min_coins = T[-1][-1]
    if min_coins != float('inf'):
        return min_coins
    else:
        return -1


def main():
    import time

    amount = 19
    coins = [1, 5, 10, 20, 50]    # Include coin 1.
    # coins = [5, 10, 20, 50]     # Exclude coin 1.

    start_time = time.time()
    min_coins = coin_change_recur(amount, coins)
    print('min_coins: {}'.format(min_coins))
    print('Time for coin_change_recur(): {}'
          .format(time.time() - start_time))

    start_time = time.time()
    min_coins = coin_change_memo(amount, coins)
    print('min_coins: {}'.format(min_coins))
    print('Time for coin_change_memo(): {}'
          .format(time.time() - start_time))

    start_time = time.time()
    min_coins = coin_change_dp(amount, coins)
    print('min_coins: {}'.format(min_coins))
    print('Time for coin_change_dp(): {}'
          .format(time.time() - start_time))


if __name__ == '__main__':
    main()
