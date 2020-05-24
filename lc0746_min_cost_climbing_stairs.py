"""Leetcode 746. Min Cost Climbing Stairs
Easy

URL: https://leetcode.com/problems/min-cost-climbing-stairs/

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum
cost to reach the top of the floor, and you can either start from the step with 
index 0, or the step with index 1.

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

class SolutionRecur(object):
    def _climb_stairs(self, cost, n):
        if n <= 1:
            return 0
        return min(self._climb_stairs(cost, n - 1) + cost[n - 1],
                   self._climb_stairs(cost, n - 2) + cost[n - 2])

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int

        Note: Time limit exceeded.

        Time complexity: O(2^n).
        Space complexity: O(n).
        """
        n = len(cost)
        return self._climb_stairs(cost, n)


class SolutionMemo(object):
    def _climb_stairs(self, cost, n, T):
        if n <= 1:
            return 0

        if T[n]:
            return T[n]

        T[n] = min(self._climb_stairs(cost, n - 1, T) + cost[n - 1],
                   self._climb_stairs(cost, n - 2, T) + cost[n - 2])
        return T[n]

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int

        Note: Time limit exceeded.

        Time complexity: O(n).
        Space complexity: O(n).
        """
        n = len(cost)
        T = [0] * (n + 1)
        return self._climb_stairs(cost, n, T)


def main():
    # Output: 15
    cost = [10, 15, 20]
    print SolutionRecur().minCostClimbingStairs(cost)
    print SolutionMemo().minCostClimbingStairs(cost)

    # Output: 6
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print SolutionRecur().minCostClimbingStairs(cost)
    print SolutionMemo().minCostClimbingStairs(cost)


if __name__ == '__main__':
    main()
