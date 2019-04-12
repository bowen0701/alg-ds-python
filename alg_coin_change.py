from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

"""Coin Change.

Compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the 
coins, return -1.

Assume that you have an infinite number of each kind of coin.
"""


def coin_change_recur(amount, coins):
    """Change minimum coins by naive recursion.

    Time complexity: O(c^a), where c is number of coins, and a is amount.
    Space complexity: O(1).
    """
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


def _coin_change_memo(amount, coins, T):
    """Helper function for coin_change_memo()."""
    if amount < 0:
        return -1
    if amount == 0:
        return 0

    if T[amount] > 0:
        return T[amount]

    min_coins = float('inf')

    for c in coins:
        extra_coins = _coin_change_memo(amount - c, coins, T)
        if extra_coins >= 0 and extra_coins < min_coins:
            min_coins = 1 + extra_coins

    if min_coins != float('inf'):
        T[amount] = min_coins
    else:
        T[amount] = -1

    return T[amount]


def coin_change_memo(amount, coins):
    """Change minimum coins by top-down dynamic programming: 
    recursion + memoization.

    Time complexity: O(c * a), where c is number of coins, and a is amount.
    Space complexity: O(a).
    """
    T = [0] * (amount + 1)
    return _coin_change_memo(amount, coins, T)


def coin_change_dp(amount, coins):
    """Change minimum coins by bottom-up dynamic programming.

    Time complexity: O(c * a), where c is number of coins, and a is amount.
    Space complexity: O(c * a).
    """
    # Why sorted coin list? Since we want to start from smaller coins.
    coins = sorted(coins)

    n_coins = len(coins)
    M = [[float('inf')]*(amount + 1) for c in range(n_coins)]

    # Base case for amount 0.
    for c in range(n_coins):
        M[c][0] = 0

    # Start from smallest coin to change from amount 0 to total amount.
    for c in range(n_coins):
        for a in range(1, amount + 1):
            if coins[c] == a:
                # Directly use coin c to change total amount.
                M[c][a] = 1
            elif a - coins[c] > 0:
                # If coin c can be included, decide which uses less coins:
                # 1. previous coins without coin c to make a.
                # 2. previous coins without coin c to make a - coins[c]
                #    plus this 1 extra coin c.
                M[c][a] = min(M[c - 1][a], 1 + M[c][a - coins[c]])
            else:
                # If coin c cannot be included, use previous coins.
                M[c][a] = M[c - 1][a]

    min_coins = M[-1][-1]
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
