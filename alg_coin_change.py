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


def coin_change_recur(amount, coins_ls):
    """Change minimum coins by naive top-down recursion."""
    if amount < 0:
        return -1
    if amount == 0:
        return 0

    min_coins = float('inf')

    for c in coins_ls:
        extra_coins = coin_change_recur(amount - c, coins_ls)
        if extra_coins >= 0 and extra_coins < min_coins:
            min_coins = 1 + extra_coins

    if min_coins != float('inf'):
        return min_coins
    else:
        return -1


def _coin_change_memo(amount, coins_ls, min_coins_ls):
    """Helper function for coin_change_memo()."""    
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    
    if min_coins_ls[amount] > 0:
        return min_coins_ls[amount]

    min_coins = float('inf')

    for c in coins_ls:
        extra_coins = _coin_change_memo(amount - c, coins_ls, min_coins_ls)
        if extra_coins >= 0 and extra_coins < min_coins:
            min_coins = 1 + extra_coins

    if min_coins != float('inf'):
        min_coins_ls[amount] = min_coins
    else:
        min_coins_ls[amount] = -1

    return min_coins_ls[amount]


def coin_change_memo(amount, coins_ls):
    """Change minimum coins by top-down recursion + memoization."""
    min_coins_ls = [0] * (amount + 1)
    min_coins = _coin_change_memo(amount, coins_ls, min_coins_ls)
    return min_coins


def coin_change_dp(amount, coins_ls):
    """Change minimum coins by dynamic programming by bottom-up."""
    # Why sorted coin list? Since we want to start from smaller coins.
    coins_ls = sorted(coins_ls)

    n_coins = len(coins_ls)
    min_coins_arr = [[float('inf')]*(amount + 1) for c in range(n_coins)]

    # TODO: Apply DP with 2-d array and fix bug for unchangeable amount.
    # Base case for amount 0.
    for c in range(n_coins):
        min_coins_arr[c][0] = 0

    pass


def main():
    import time

    amount = 18
    coins_ls = [1, 5, 10, 20, 50]    # Include coin 1.
    # coins_ls = [5, 10, 20, 50]     # Exclude coin 1.

    start_time = time.time()
    min_coins = coin_change_recur(amount, coins_ls)
    print('min_coins: {}'.format(min_coins))
    print('Time for coin_change_recur(): {}'
          .format(time.time() - start_time))

    start_time = time.time()
    min_coins = coin_change_memo(amount, coins_ls)
    print('min_coins: {}'.format(min_coins))
    print('Time for coin_change_memo(): {}'
          .format(time.time() - start_time))

    start_time = time.time()
    min_coins = coin_change_dp(amount, coins_ls)
    print('min_coins: {}'.format(min_coins))
    print('Time for coin_change_dp(): {}'
          .format(time.time() - start_time))


if __name__ == '__main__':
    main()
