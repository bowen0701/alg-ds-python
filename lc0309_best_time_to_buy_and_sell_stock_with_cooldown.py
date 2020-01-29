"""Leetcode 309. Best Time to Buy and Sell Stock with Cooldown
Medium

URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions
as you like (ie, buy one and sell one share of the stock multiple times) with the
following restrictions:
- You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
- After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:
Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""

class SolutionDp(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        if not prices:
            return 0

        n = len(prices)

        # Before day i, the max profit ending with buy/sell.
        profit_buys = [0] * n
        profit_sells = [0] * n

        profit_buys[0] = -prices[0]

        for i in range(1, n):
            profit_buys[i] = max(profit_sells[i - 2] - prices[i],
                                 profit_buys[i - 1])
            profit_sells[i] = max(profit_buys[i - 1] + prices[i],
                                  profit_sells[i - 1])

        return profit_sells[-1]


class SolutionIter(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if not prices:
            return 0

        profit_buy = -prices[0]
        profit_sell = 0
        profit_buy_prev = 0
        profit_sell_prev = 0

        for i in range(1, len(prices)):
            profit_buy_prev = profit_buy
            profit_buy = max(profit_sell_prev - prices[i], profit_buy_prev)

            profit_sell_prev = profit_sell
            profit_sell = max(profit_buy_prev + prices[i], profit_sell_prev)

        return profit_sell


def main():
    # Output: 3
    prices = [1,2,3,0,2]
    print SolutionDp().maxProfit(prices)
    print SolutionIter().maxProfit(prices)


if __name__ == '__main__':
    main()
