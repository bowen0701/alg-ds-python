"""Leetcode 714. Best Time to Buy and Sell Stock with Transaction Fee
Medium

URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

Your are given an array of integers prices, for which the i-th element is the price of
a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction
fee for each transaction. You may not buy more than 1 share of a stock at a time
(ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Note:
- 0 < prices.length <= 50000.
- 0 < prices[i] < 50000.
- 0 <= fee < 50000.
"""

class SolutionDp(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
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
            profit_buys[i] = max(profit_sells[i - 1] - prices[i], 
                                 profit_buys[i - 1])

            # Pay transaction fee when sell.
            profit_sells[i] = max(profit_buys[i - 1] + prices[i] - fee, 
                                  profit_sells[i - 1])

        return profit_sells[-1]


def main():
    # Output: 8
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print SolutionDp().maxProfit(prices, fee)


if __name__ == '__main__':
    main()
