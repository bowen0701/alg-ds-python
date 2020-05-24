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
            if c > amount:
                continue

            extra_coins = self.coinChange(coins, amount - c)
            if extra_coins < 0:
                continue
            min_coins = min(1 + extra_coins, min_coins)

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
            if c > amount:
                continue

            extra_coins = self._coin_change_memo(coins, amount - c, T)
            if extra_coins < 0:
                continue
            min_coins = min(1 + extra_coins, min_coins)

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


class SolutionDP(object):
    def coinChange(self, coins, amount):
        """Change fewest #coins by bottom-up dynamic programming.

        Time complexity: O(a*n), where a is amount, and n is number of coins.
        Space complexity: O(a*n).
        """
        # Apply DP with tabular T: n_coints x (amount + 1).
        n = len(coins)
        T = [[float('inf')] * (amount + 1) for _ in range(n)]

        # For amount 0, set T[i][0] equal 0.
        for i in range(n):
            T[i][0] = 0

        for a in range(1, amount + 1):
            for i in range(n):
                if coins[i] <= a:
                    # If coin i is included: to change or not to change.
                    T[i][a] = min(1 + T[i][a - coins[i]], T[i - 1][a])
                else:
                    # If coin i is not included, use previous #coins.
                    T[i][a] = T[i - 1][a]

        if T[-1][-1] != float('inf'):
            return T[-1][-1]
        else:
            return -1


class SolutionDpEarlyStop(object):
    def coinChange(self, coins, amount):
        """Change fewest #coins by bottom-up dynamic programming.

        Time complexity: O(a*n+n*logn), where 
          - a is amount, and 
          - n is number of coins.
        Space complexity: O(a).
        """
        # Apply DP with tabular T with early stopping by sorting.
        coins = sorted(coins)

        T = [float('inf')] * (amount + 1)

        # For amount 0, set num of coints to 0.
        T[0] = 0

        for a in range(1, amount + 1):
            for i in range(len(coins)):
                if coins[i] <= a:
                    # If coin i is included: to change or not to change.
                    T[a] = min(1 + T[a - coins[i]], T[a])
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
    print 'By DP: {}'.format(SolutionDP().coinChange(coins, amount))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By DP w/ early stop: {}'.format(
        SolutionDpEarlyStop().coinChange(coins, amount))
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
    print 'By DP: {}'.format(SolutionDP().coinChange(coins, amount))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By DP w/ early stop: {}'.format(
        SolutionDpEarlyStop().coinChange(coins, amount))
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
