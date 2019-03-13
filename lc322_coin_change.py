"""Leetcode 322. Coin Change
Medium

URL: https://leetcode.com/problems/coin-change/

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

Note:
You may assume that you have an infinite number of each kind of coin.
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = sorted(coins)

        n_coins = len(coins)
        T = [[float('inf')]*(amount + 1) for _ in range(n_coins)]

        for c in range(n_coins):
            T[c][0] = 0

        for c in range(n_coins):
            for a in range(1, amount + 1):
                if a == coins[c]:
                    T[c][a] = 1
                elif a >= coins[c]:
                    T[c][a] = min(T[c - 1][a], 1 + T[c][a - coins[c]])
                else:
                    T[c][a] = T[c - 1][a]

        if T[-1][-1] != float('inf'):
            return T[-1][-1]
        else:
            return -1


def main():
    coins = [1, 2, 5]
    amount = 11
    print Solution().coinChange(coins, amount)

    coins = [2]
    amount = 3
    print Solution().coinChange(coins, amount)


if __name__ == '__main__':
    main()
