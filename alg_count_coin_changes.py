from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


"""Count Coin Changes.

Count how many distinct ways you can make change that amount.
Assume that you have an infinite number of each kind of coin.
"""


def count_coin_changes_recur(amount, coins, n):
    """Count changes by recursion.

    Time complexity: O(2^n).
    Space complexity: O(1).
    """
    if amount < 0:
        return 0
    if amount == 0:
        return 1

    # When number of coins is 0 but there is still amount remaining.
    if n < 0 and amount >= 1:
        return 0

    # Compute ways with coin n included plus that with coin excluded.
    n_changes_in = count_coin_changes_recur(amount - coins[n], coins, n)
    n_changes_out = count_coin_changes_recur(amount, coins, n - 1)
    n_changes = n_changes_in + n_changes_out
    return n_changes


def _count_coin_changes_memo(amount, coins, T, n):
    """Helper function for count_changes_memo()."""
    if amount == 0:
        return 1
    if amount < 0:
        return 0

    if n < 0 and amount >= 1:
        return 0

    if T[n][amount]:
        return T[n][amount]

    n_changes_in = _count_coin_changes_memo(amount - coins[n - 1], coins, T, n)
    n_changes_out = _count_coin_changes_memo(amount, coins, T, n - 1)
    T[n][amount] = n_changes_in + n_changes_out

    return T[n][amount]


def count_coin_changes_memo(amount, coins):
    """Count changes by top-bottom dynamic programming: 
    recursion + memoization.

    Time complexity: O(a * c), where a is amount, and c is number of coins.
    Space complexity: O(a * c).
    """
    n = len(coins) - 1
    T = [[0] * (amount + 1) for c in range(n + 1)]

    for c in range(n + 1):
        T[c][0] = 1

    return _count_coin_changes_memo(amount, coins, T, n)


def count_coin_changes_dp(amount, coins):
    """Count changes by bottom-up dynamic programming.

    Time complexity: O(a * c), where a is amount, and c is number of coins.
    Space complexity: O(a * c).
    """
    n = len(coins) - 1
    T = [[0] * (amount + 1) for c in range(n + 1)]

    for c in range(n):
        T[c][0] = 1

    for c in range(n + 1):
        for a in range(1, amount + 1):
            if a < coins[c]:
                T[c][a] = T[c - 1][a]
            else:
                T[c][a] = T[c - 1][a] + T[c][a - coins[c]]

    return T[-1][-1]


def main():
    import time

    amount = 5
    coins = [1, 2, 3]    # Ans = 5.
    n = len(coins) - 1

    start_time = time.time()
    print('Make change by recursion: {}'
          .format(count_coin_changes_recur(amount, coins, n)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('Make change by memo: {}'
          .format(count_coin_changes_memo(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('Make change by DP: {}'
          .format(count_coin_changes_dp(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
