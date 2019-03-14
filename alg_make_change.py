from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


"""Make Change.

Compute how many distinct ways you can make change that amount. 
If that amount of money cannot be made up by any combination of the 
coins, return -1.

Assume that you have an infinite number of each kind of coin.
"""


def make_change_recur(amount, coins, n):
    """Make change by recursion."""
    if amount < 0:
        return 0
    if amount == 0:
        return 1
    # When number of coins is 0 but there is still amount remaining.
    if n <= 0 and amount >= 1:
        return 0

    return (make_change_recur(amount - coins[n - 1], coins, n)
            + make_change_recur(amount, coins, n - 1))


def make_change_memo(amount, coins):
    """Make change by top-bottom dynamic programming: 
    recursion + memoization."""
    pass


def make_change_dp(amount, coins):
    """Make change by bottom-up dynamic programming."""
    pass


def main():
    import time

    amount = 5
    coins = [1, 2, 3]    # counter = 5.
    n_coin = len(coins)

    start_time = time.time()
    print('Make change by recursion: {}'
          .format(make_change_recur(amount, coins, n_coin)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
