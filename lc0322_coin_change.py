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

class SolutionRecur(object):
    def coinChange(self, coins, amount):
        """Change fewest #coins by recursion.

        Time complexity: O(c^a), where c is number of coins, and a is amount.
        Space complexity: O(c).
        """
        # Base cases.
        if amount < 0:
            return -1
        if amount == 0:
            return 0

        min_coins = float('inf')

        for c in coins:
            # Not changeable.
            if amount < c:
                continue

            extra_coins = self.coinChange(coins, amount - c)
            if extra_coins < 0:
                continue
            min_coins = min(min_coins, 1 + extra_coins)

        if min_coins != float('inf'):
            return min_coins
        else:
            return -1


class SolutionMemo(object):
    def _coin_change_memo(self, coins, amount, T):
        """Helper function for coin_change_memo()."""
        # Base cases.
        if amount < 0:
            return -1
        if amount == 0:
            return 0

        # Apply memoization.
        if T[amount] > 0:
            return T[amount]

        # Get fewest num with iterating coins by recursion.
        min_coins = float('inf')

        for c in coins:
            # Not changeable.
            if amount < c:
                continue

            extra_coins = self._coin_change_memo(coins, amount - c, T)
            if extra_coins < 0:
                continue
            min_coins = min(min_coins, 1 + extra_coins)

        if min_coins != float('inf'):
            T[amount] = min_coins
        else:
            T[amount] = -1

        return T[amount]


    def coinChange(self, coins, amount):
        """Change fewest #coins by top-down dynamic programming:
        recursion + memoization.

        Time complexity: O(a*n), where a is amount, and n is number of coins.
        Space complexity: O(a).
        """
        T = [0] * (amount + 1)
        return self._coin_change_memo(coins, amount, T)


class SolutionDp(object):
    def coinChange(self, coins, amount):
        """Change fewest #coins by bottom-up dynamic programming.

        Time complexity: O(a*n), where a is amount, and n is number of coins.
        Space complexity: O(a*n).
        """
        n_coins = len(coins)
        T = [[float('inf')] * (amount + 1) for _ in range(n_coins)]

        # For amount 0, set num equal 0.
        for i in range(n_coins):
            T[i][0] = 0

        for a in range(1, amount + 1):
            for i in range(n_coins):
                if coins[i] == a:
                    # Directly use coin i to change total amount.
                    T[i][a] = 1
                elif coins[i] < a:
                    # If coin i can be included, decide which uses less coins:
                    # 1. #coins without coin i to make a
                    # 2. 1 + #coins with coin i to make a - coins[i]
                    T[i][a] = min(T[i - 1][a], 1 + T[i][a - coins[i]])
                else:
                    # If coin i cannot be included, use previous #coins.
                    T[i][a] = T[i - 1][a]

        if T[-1][-1] != float('inf'):
            return T[-1][-1]
        else:
            return -1


class SolutionDp2(object):
    def coinChange(self, coins, amount):
        """Change fewest #coins by bottom-up dynamic programming.

        Time complexity: O(a*n), where a is amount, and n is number of coins.
        Space complexity: O(a).
        """
        # Sort coins for early stopping.
        coins = sorted(coins)

        T = [float('inf')] * (amount + 1)

        # For amount 0, set num of coints to 0.
        T[0] = 0

        for a in range(1, amount + 1):
            for i in range(len(coins)):
                if coins[i] <= a:
                    # If coin i can be included:
                    # 1. #coins without coin i to make a
                    # 2. 1 + #coins with coin i to make a - coins[i]
                    T[a] = min(T[a], 1 + T[a - coins[i]])
                else:
                    # Early stop.
                    break

        if T[-1] != float('inf'):
            return T[-1]
        else:
            return -1


def main():
    import time

    # Ans: 3.
    coins = [1, 2, 5]
    amount = 11

    start_time = time.time()
    print 'By recur: {}'.format(SolutionRecur().coinChange(coins, amount))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By memo: {}'.format(SolutionMemo().coinChange(coins, amount))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By DP: {}'.format(SolutionDp().coinChange(coins, amount))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By DP2: {}'.format(SolutionDp2().coinChange(coins, amount))
    print 'Time: {}'.format(time.time() - start_time)

    # Ans: -1.
    coins = [2]
    amount = 3

    start_time = time.time()
    print 'By recur: {}'.format(SolutionRecur().coinChange(coins, amount))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By memo: {}'.format(SolutionMemo().coinChange(coins, amount))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By DP: {}'.format(SolutionDp().coinChange(coins, amount))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By DP2: {}'.format(SolutionDp2().coinChange(coins, amount))
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
