from __future__ import print_function


def change_coin_recur(money, coin_val_ls):
    """Dynamic programming: Change coin by recursion."""
    min_coins = money
    if money in coin_val_ls:
    	return 1
    else:
    	for m in [c for c in coin_val_ls if c <= money]:
    		num_coins = (
    			1 + change_coin_recur(money - m, coin_val_ls))
    		if num_coins < min_coins:
    			min_coins = num_coins
    return min_coins

def main():
	print(change_coin_recur(26, [1, 5, 10, 25]))


if __name__ == '__main__':
	main()
