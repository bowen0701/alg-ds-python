from __future__ import print_function
import time


def change_coin_recur(change, coin_val_ls):
    """Change coin by 'naive' recursion."""
    min_coins = change
    if change in coin_val_ls:
        return 1
    else:
        for m in [c for c in coin_val_ls if c <= change]:
            num_coins = (
                1 + change_coin_recur(change - m, coin_val_ls))
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


def change_coin_recur_cache(change, coin_val_ls, known_results_ls):
    """Change coin by recursion with caching."""
    min_coins = change
    if change in coin_val_ls:
        known_results_ls[change - 1] = 1
        return 1
    elif known_results_ls[change - 1] > 0:
        return known_results_ls[change - 1]
    else:
        for m in [c for c in coin_val_ls if c <= change]:
            num_coins = (
                1 + change_coin_recur_cache(
                    change - m, coin_val_ls, known_results_ls))
            if num_coins < min_coins:
                min_coins = num_coins
                known_results_ls[change - 1] = min_coins
    return min_coins


def change_coin_dp(change, coin_val_ls, min_coins, used_coins):
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1
        for m in [c for c in coin_val_ls if c <= cents]:
            if min_coins[cents - m] + 1 < coin_count:
                coin_count = min_coins[cents - m] + 1
                new_coin = m
        min_coins[cents] = coin_count
        used_coins[cents] = new_coin
    return min_coins[change]

def print_coins(change, used_coins):
    coin = change
    while coin > 0:
        this_coin = used_coins[coin]
        print('this_coin: {}'.format(this_coin))
        coin = coin - this_coin


def main():
    # start_time = time.time()
    # min_coins = change_coin_recur(63, [1, 5, 10, 25])
    # print('min_coins: {}'.format(min_coins))
    # print('Time for change_coin_recur(): {}'
    #       .format(time.time() - start_time))

    start_time = time.time()
    min_coins = change_coin_recur_cache(63, [1, 5, 10, 25], [0]*63)
    print('min_coins: {}'.format(min_coins))
    print('Time for change_coin_recur_cache(): {}'
          .format(time.time() - start_time))

    start_time = time.time()
    change = 63
    coint_count = [0] * (change + 1)
    used_coins = [0] * (change + 1)
    min_coins = change_coin_dp(
        change, [1, 5, 10, 21, 25], 
        coint_count, used_coins)
    print('min_coins: {}'.format(min_coins))
    print('Time for change_coin_recur_cache(): {}'
          .format(time.time() - start_time))
    print('used_coins: {}'.format(used_coins))
    print_coins(change, used_coins)


if __name__ == '__main__':
    main()
