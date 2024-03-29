"""Leetcode 746. Min Cost Climbing Stairs
Easy

URL: https://leetcode.com/problems/min-cost-climbing-stairs/

On a staircase, the i-th step has some non-negative cost cost[i] assigned
(0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to
find minimum cost to reach the top of the floor, and you can either start
from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:
- cost will have a length in the range [2, 1000].
- Every cost[i] will be an integer in the range [0, 999].
"""

from typing import List


class SolutionRecur(object):
    def _climb_stairs(self, cost: List[int], n: int) -> int:
        # Base cases: no cost.
        if n <= 1:
            return 0

        return min(self._climb_stairs(cost, n - 1) + cost[n - 1],
                   self._climb_stairs(cost, n - 2) + cost[n - 2])

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Note: Time limit exceeded.

        Time complexity: O(2^n).
        Space complexity: O(n).
        """
        # Apply top-down DP by recursion.
        n = len(cost)
        return self._climb_stairs(cost, n)


class SolutionMemo(object):
    def _climb_stairs(self, cost: List[int], n: int, T: List[int]) -> int:
        # Base cases: no cost.
        if n <= 1:
            return 0

        # Check memo table.
        if T[n]:
            return T[n]

        T[n] = min(self._climb_stairs(cost, n - 1, T) + cost[n - 1],
                   self._climb_stairs(cost, n - 2, T) + cost[n - 2])
        return T[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Apply top-down DP by recursion with memoization.
        n = len(cost)
        T = [0] * (n + 1)
        return self._climb_stairs(cost, n, T)


class SolutionDP(object):
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Apply bottom-up DP.
        n = len(cost)

        # Use DP table with zero cost at indices 0 & 1.
        T = [0] * (n + 1)
        for i in range(2, n + 1):
            T[i] = min(T[i - 1] + cost[i - 1], 
                       T[i - 2] + cost[i - 2])
        return T[-1]


class SolutionIter(object):
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Apply bottom-up iteration.
        n = len(cost)
        a, b = 0, 0
        for i in range(2, n + 1):
            a, b = b, min(b + cost[i - 1], a + cost[i - 2])
        return b


def main():
    # Output: 15
    cost = [10, 15, 20]
    print(SolutionRecur().minCostClimbingStairs(cost))
    print(SolutionMemo().minCostClimbingStairs(cost))
    print(SolutionDP().minCostClimbingStairs(cost))
    print(SolutionIter().minCostClimbingStairs(cost))

    # Output: 6
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(SolutionRecur().minCostClimbingStairs(cost))
    print(SolutionMemo().minCostClimbingStairs(cost))
    print(SolutionDP().minCostClimbingStairs(cost))
    print(SolutionIter().minCostClimbingStairs(cost))


if __name__ == '__main__':
    main()
