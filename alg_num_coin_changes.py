from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


"""Number of Coin Changes.

Count how many distinct ways you can make change that amount.
Assume that you have an infinite number of each kind of coin.
"""


def num_coin_changes_recur(amount, coins, n):
    """Number of coin changes by recursion.

    Time complexity: O(2^n), where n is number of coins.
    Space complexity: O(1).
    """
    if amount < 0:
        return 0
    if amount == 0:
        return 1

    # When number of coins is 0 but there is still amount remaining.
    if n < 0 and amount >= 1:
        return 0

    # Sum num of ways with coin n included & excluded.
    n_changes_in = num_coin_changes_recur(amount - coins[n], coins, n)
    n_changes_ex = num_coin_changes_recur(amount, coins, n - 1)
    n_changes = n_changes_in + n_changes_ex
    return n_changes


def _num_coin_changes_memo(amount, coins, T, n):
    """Helper function for num_coin_changes_memo()."""
    if amount == 0:
        return 1
    if amount < 0:
        return 0

    if n < 0 and amount >= 1:
        return 0

    # Apply memoization.
    if T[n][amount]:
        return T[n][amount]

    # Sum num of ways with coin n included & excluded.
    n_changes_in = _num_coin_changes_memo(amount - coins[n], coins, T, n)
    n_changes_ex = _num_coin_changes_memo(amount, coins, T, n - 1)
    T[n][amount] = n_changes_in + n_changes_ex

    return T[n][amount]


def num_coin_changes_memo(amount, coins):
    """Number of coin changes by top-bottom dynamic programming:
    recursion + memoization.

    Time complexity: O(a*n), where a is amount, and n is number of coins.
    Space complexity: O(a*n).
    """
    n = len(coins) - 1
    T = [[0] * (amount + 1) for c in range(n + 1)]

    # For amount 0, set num equal 1.
    for c in range(n + 1):
        T[c][0] = 1

    return _num_coin_changes_memo(amount, coins, T, n)


def num_coin_changes_dp(amount, coins):
    """Number of coin changes by bottom-up dynamic programming.

    Time complexity: O(a*n), where a is amount, and n is number of coins.
    Space complexity: O(a*n).
    """
    n = len(coins) - 1
    T = [[0] * (amount + 1) for c in range(n + 1)]

    # For amount 0, set num equal 1.
    for c in range(n):
        T[c][0] = 1

    for c in range(n + 1):
        for a in range(1, amount + 1):
            if a < coins[c]:
                # Cannot make a change by coin c.
                T[c][a] = T[c - 1][a]
            else:
                # Sum num of ways with coin n included & excluded.
                T[c][a] = T[c][a - coins[c]] + T[c - 1][a]

    return T[-1][-1]


def main():
    import time

    amount = 5
    coins = [1, 2, 3]    # Ans = 5.
    n = len(coins) - 1

    start_time = time.time()
    print('Make change by recursion: {}'
          .format(num_coin_changes_recur(amount, coins, n)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('Make change by memo: {}'
          .format(num_coin_changes_memo(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('Make change by DP: {}'
          .format(num_coin_changes_dp(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
