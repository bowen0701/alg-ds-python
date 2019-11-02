"""Leetcode 188. Best Time to Buy and Sell Stock IV
Hard

URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Say you have an array for which the i-th element is the price of a given stock on
day i.

Design an algorithm to find the maximum profit. You may complete at most k
transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell
the stock before you buy again).

Example 1:
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), 
             profit = 4-2 = 2.

Example 2:
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), 
             profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3),
             profit = 3-0 = 3.
"""

class SolutionDp(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int

        Let T[i, j] be the max profit up until prices[j] using at most i transactions.
        T[i, j] = max(T[i, j-1], prices[j] - prices[j'] + T[i-1, j']), for j' in [0, j-1]
                = max(T[i, j-1], prices[j] + max(T[i-1, j'] - prices[j']))
        Note prices[j] - prices[j'] means profit with buying at j' and selling at j.

        Time complexity: O(k*n), where n is the number of prices.
        Space complexity: O(k*n).
        """
        if not prices:
            return 0

        n = len(prices)

        # If k >= half number of dates, we can make max transactions.
        if k >= (n >> 1):
            max_profit = 0
            for i in range(1, n):
                max_profit += max(prices[i] - prices[i - 1], 0)
            return max_profit

        # Let T[i, j] be max profit up until prices[j] using at most i transactions.
        T = [[0] * n for _ in range(k + 1)]

        for i in range(1, k + 1):
            local_max = -float('inf')

            for j in range(n):
                local_max = max(T[i - 1][j] - prices[j], local_max)
                T[i][j] = max(T[i][j - 1], local_max + prices[j])

        return T[-1][-1]


def main():
    # Output: 2
    prices = [2,4,1]
    k = 2
    print SolutionDp().maxProfit(k, prices)

    # Output: 7
    prices = [3,2,6,5,0,3]
    k = 2
    print SolutionDp().maxProfit(k, prices)


if __name__ == '__main__':
    main()
