from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def coin_change_recur(change, coins_ls):
    """Change minimum coins by naive top-down recursion."""   
    # TODO: Fix bug for unchangeable amount.

    min_coins = change

    if change in coins_ls:
        return 1

    for m in [c for c in coins_ls if c <= change]:
        num_coins = 1 + coin_change_recur(change - m, coins_ls)
        if num_coins < min_coins:
            min_coins = num_coins

    return min_coins


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
    if amount < 1:
        return 0

    min_coins_ls = [0] * (amount + 1)
    min_coins = _coin_change_memo(amount, coins_ls, min_coins_ls)
    return min_coins


def coin_change_dp(change, coins_ls):
    """Change minimum coins by dynamic programming."""
    # TODO: Fix bug for unchangeable amount.

    min_coins_ls = [0] * (change + 1)

    for _change in range(change + 1):
        num_coins = _change
        new_coin = 1

        for m in [c for c in coins_ls if c <= _change]:
            if min_coins_ls[_change - m] + 1 < num_coins:
                num_coins = min_coins_ls[_change - m] + 1
                new_coin = m

        min_coins_ls[_change] = num_coins

    return min_coins_ls[change]


def main():
    import time

    change = 17
    coins_ls = [1, 5, 10, 20, 50]    # Include coin 1.
    # coins_ls = [5, 10, 20, 50]     # Exclude coin 1.

    start_time = time.time()
    min_coins = coin_change_recur(change, coins_ls)
    print('min_coins: {}'.format(min_coins))
    print('Time for coin_change_recur(): {}'
          .format(time.time() - start_time))

    start_time = time.time()
    min_coins = coin_change_memo(change, coins_ls)
    print('min_coins: {}'.format(min_coins))
    print('Time for coin_change_memo(): {}'
          .format(time.time() - start_time))

    start_time = time.time()
    min_coins = coin_change_dp(change, coins_ls)
    print('min_coins: {}'.format(min_coins))
    print('Time for coin_change_dp(): {}'
          .format(time.time() - start_time))


if __name__ == '__main__':
    main()
