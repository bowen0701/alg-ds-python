"""Leetcode 518. Coin Change II
Medium

URL: https://leetcode.com/problems/coin-change-ii/

You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount.
If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1

Constraints:
- 1 <= coins.length <= 300
- 1 <= coins[i] <= 5000
- 0 <= amount <= 5000
"""


class SolutionRecur:
    def _change_recur(self, amount, coins, start):
        # Base cases.
        if amount < 0:
            return 0
        if amount == 0:
            return 1

        n_ways = 0

        # Start from 'start' to avoid counting permutations.
        for i in range(start, len(coins)):
            n_ways += self._change_recur(amount - coins[i], coins, i)

        return n_ways

    def change(self, amount, coins):
        """Count #combinations by recursion.

        Time complexity: O(c^a), where
          - c is number of coins
          - a is amount.
        Space complexity: O(a).
        """
        return self._change_recur(amount, coins, 0)


class SolutionMemo:
    def _change_recur(self, amount, coins, start, T):
        # Base cases.
        if amount < 0:
            return 0
        if amount == 0:
            return 1

        if (amount, start) in T:
            return T[(amount, start)]

        n_ways = 0

        for i in range(start, len(coins)):
            n_ways += self._change_recur(amount - coins[i], coins, i, T)

        T[(amount, start)] = n_ways
        return n_ways

    def change(self, amount, coins):
        """Count #combinations by top-down DP: recursion + memoization.

        Time complexity: O(a*n), where a is amount, and n is number of coins.
        Space complexity: O(a*n).
        """
        T = {}
        return self._change_recur(amount, coins, 0, T)


class SolutionDP:
    def change(self, amount, coins):
        """Count #combinations by bottom-up dynamic programming.

        Time complexity: O(a*n), where a is amount, and n is number of coins.
        Space complexity: O(a*n).
        """
        # Apply DP with tabular T: n_coins x (amount + 1).
        n = len(coins)
        T = [[0] * (amount + 1) for _ in range(n)]

        # For amount 0, there is 1 way: use no coins.
        for i in range(n):
            T[i][0] = 1

        for j in range(1, amount + 1):
            for i in range(n):
                if coins[i] <= j:
                    # Use coin i (stay on row i for reuse) + skip coin i.
                    T[i][j] = T[i][j - coins[i]] + T[i - 1][j]
                else:
                    # Coin i doesn't fit, use previous coins only.
                    T[i][j] = T[i - 1][j]

        return T[-1][-1]


class SolutionDP1D:
    def change(self, amount, coins):
        """Count #combinations by bottom-up DP w/ optimized space.

        Time complexity: O(a*n), where a is amount, and n is number of coins.
        Space complexity: O(a).
        """
        T = [0] * (amount + 1)

        # For amount 0, there is 1 way: use no coins.
        T[0] = 1

        # Iterate coins in outer loop to count combinations, not permutations.
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                T[j] += T[j - coins[i]]

        return T[-1]


class SolutionDP1DEarlyStop:
    def change(self, amount, coins):
        """Count #combinations by bottom-up DP w/ optimized space & early stop.

        Time complexity: O(a*n+n*logn), where
          - a is amount, and
          - n is number of coins.
        Space complexity: O(a).
        """
        # Sort coins to enable early stopping.
        coins = sorted(coins)

        T = [0] * (amount + 1)

        # For amount 0, there is 1 way: use no coins.
        T[0] = 1

        # Iterate coins in outer loop to count combinations, not permutations.
        for i in range(len(coins)):
            if coins[i] <= amount:
                for j in range(coins[i], amount + 1):
                    T[j] += T[j - coins[i]]
            else:
                # Early stop: remaining coins all > amount.
                break

        return T[-1]


def main():
    import time

    # Ans: 4.
    amount = 5
    coins = [1, 2, 5]

    start_time = time.time()
    print('By recur: {}'.format(SolutionRecur().change(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By memo: {}'.format(SolutionMemo().change(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP: {}'.format(SolutionDP().change(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP 1D: {}'.format(SolutionDP1D().change(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP 1D w/ early stop: {}'.format(
        SolutionDP1DEarlyStop().change(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    # Ans: 0.
    amount = 3
    coins = [2]

    start_time = time.time()
    print('By recur: {}'.format(SolutionRecur().change(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By memo: {}'.format(SolutionMemo().change(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP: {}'.format(SolutionDP().change(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP 1D: {}'.format(SolutionDP1D().change(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP 1D w/ early stop: {}'.format(
        SolutionDP1DEarlyStop().change(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    # Ans: 1.
    amount = 10
    coins = [10]

    start_time = time.time()
    print('By recur: {}'.format(SolutionRecur().change(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By memo: {}'.format(SolutionMemo().change(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP: {}'.format(SolutionDP().change(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP 1D: {}'.format(SolutionDP1D().change(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP 1D w/ early stop: {}'.format(
        SolutionDP1DEarlyStop().change(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
