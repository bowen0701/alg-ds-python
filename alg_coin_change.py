from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def change_coin_recur(change, coins_ls):
    """Change coins by naive recursion."""
    min_coins = change
    if change in coins_ls:
        return 1
    else:
        for m in [c for c in coins_ls if c <= change]:
            num_coins = 1 + change_coin_recur(change - m, coins_ls)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


def change_coin_recur_memo(change, coins_ls, min_coins_memo_ls):
    """Change coins by recursion with memoization."""
    min_coins = change
    if change in coins_ls:
        min_coins_memo_ls[change - 1] = 1
        return 1
    elif min_coins_memo_ls[change - 1] > 0:
        return min_coins_memo_ls[change - 1]
    else:
        for m in [c for c in coins_ls if c <= change]:
            num_coins = (
                1 + change_coin_recur_memo(
                    change - m, coins_ls, min_coins_memo_ls))
            if num_coins < min_coins:
                min_coins = num_coins
                min_coins_memo_ls[change - 1] = min_coins
    return min_coins


def change_coin_dp(change, coins_ls, min_coins_ls, used_coins_ls):
    """Change coins by dynamic programming."""
    for cents in range(change + 1):
        num_coins = cents
        new_coin = 1
        for m in [c for c in coins_ls if c <= cents]:
            if min_coins_ls[cents - m] + 1 < num_coins:
                num_coins = min_coins_ls[cents - m] + 1
                new_coin = m
        min_coins_ls[cents] = num_coins
        used_coins_ls[cents] = new_coin
    return min_coins_ls[change]


def print_coins(change, used_coins_ls):
    """Print used coins for change."""
    coin = change
    while coin > 0:
        used_coin = used_coins_ls[coin]
        print('used_coin: {}'.format(used_coin))
        coin = coin - used_coin
    return None


def main():
    import time

    change = 63
    coins_ls = [1, 5, 10, 25]

    start_time = time.time()
    min_coins = change_coin_recur(change, coins_ls)
    print('min_coins: {}'.format(min_coins))
    print('Time for change_coin_recur(): {}'
          .format(time.time() - start_time))

    start_time = time.time()
    min_coins = change_coin_recur_memo(change, coins_ls, [0]*change)
    print('min_coins: {}'.format(min_coins))
    print('Time for change_coin_recur_memo(): {}'
          .format(time.time() - start_time))

    start_time = time.time()
    min_coins_ls = [0] * (change + 1)
    used_coins_ls = [0] * (change + 1)
    min_coins = change_coin_dp(change, coins_ls, min_coins_ls, used_coins_ls)
    print('min_coins: {}'.format(min_coins))
    print('used_coins_ls: {}'.format(used_coins_ls))
    print_coins(change, used_coins_ls)
    print('Time for change_coin_dp(): {}'
          .format(time.time() - start_time))


if __name__ == '__main__':
    main()
