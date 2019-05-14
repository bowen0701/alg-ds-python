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

class SolutionMemo(object):
    def _coin_change_memo(self, coins, amount, T):
        """Helper function for coin_change_memo()."""
        if amount < 0:
            return -1
        if amount == 0:
            return 0

        if T[amount] > 0:
            return T[amount]

        min_coins = float('inf')

        for c in coins:
            extra_coins = self._coin_change_memo(coins, amount - c, T)
            if extra_coins >= 0 and extra_coins < min_coins:
                min_coins = 1 + extra_coins

        if min_coins != float('inf'):
            T[amount] = min_coins
        else:
            T[amount] = -1

        return T[amount]


    def coinChange(self, coins, amount):
        """Change minimum coins by top-down dynamic programming: 
        recursion + memoization.

        Time complexity: O(c * a), where c is number of coins, and a is amount.
        Space complexity: O(a).
        """
        T = [0] * (amount + 1)
        return self._coin_change_memo(coins, amount, T)


class SolutionDp(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        Time complexity: O(c * a), where c is number of coins, and a is amount.
        Space complexity: O(c * a).
        """
        # Why sorted coin list? Since we want to start from smaller coins.
        coins = sorted(coins)

        n_coins = len(coins)
        T = [[float('inf')]*(amount + 1) for _ in range(n_coins)]

        # Base case for amount 0.
        for c in range(n_coins):
            T[c][0] = 0

        # Start from smallest coin to change from amount 0 to total amount.
        for c in range(n_coins):
            for a in range(1, amount + 1):
                if a == coins[c]:
                    # Directly use coin c to change total amount.
                    T[c][a] = 1
                elif a >= coins[c]:
                    # If coin c can be included, decide which uses less coins:
                    # 1. previous coins without coin c to make a.
                    # 2. previous coins without coin c to make a - coins[c]
                    #    plus this 1 extra coin c.
                    T[c][a] = min(T[c - 1][a], 1 + T[c][a - coins[c]])
                else:
                    # If coin c cannot be included, use previous coins.
                    T[c][a] = T[c - 1][a]

        if T[-1][-1] != float('inf'):
            return T[-1][-1]
        else:
            return -1


def main():
    coins = [1, 2, 5]
    amount = 11
    print SolutionMemo().coinChange(coins, amount)
    print SolutionDp().coinChange(coins, amount)

    coins = [2]
    amount = 3
    print SolutionMemo().coinChange(coins, amount)
    print SolutionDp().coinChange(coins, amount)


if __name__ == '__main__':
    main()
