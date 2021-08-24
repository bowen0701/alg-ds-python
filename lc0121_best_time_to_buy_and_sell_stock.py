"""Leetcode 121. Best Time to Buy and Sell Stock
Easy

URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), 
design an algorithm to find the maximum max_profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), max_profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max max_profit = 0.
"""

from typing import List


class SolutionBruteForce(object):
    def maxProfit(self, prices: List[int]) -> int:
        """
        Note: Time limit exceeded.

        Time complexity: O(n^2), where n is the number of prices.
        Space complexity: O(1).
        """
        # Edge case.
        if not prices:
            return 0

        n = len(prices)

        # Iterate through price pairs (i, j), i < j, to update max profit.
        result = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                if prices[j] - prices[i] > result:
                    result = prices[j] - prices[i]

        return result


class SolutionBinarySearch(object):
    def _binarySearch(self, prices: List[int], left: int, right: int) -> int:
        # Edge case: only one date.
        if left == right:
            return 0

        # Compute profits in left and right subarrays.
        mid = left + (right - left) // 2

        left_profit = self._binarySearch(prices, left, mid)
        right_profit = self._binarySearch(prices, mid + 1, right)

        # Compute cross profit for buying in left and selling in right.
        left_min = min(prices[left:(mid+1)])
        right_max = max(prices[(mid+1):(right+1)])
        cross_profit = max(0, right_max - left_min)

        return max(left_profit, right_profit, cross_profit)

    def maxProfit(self, prices: List[int]) -> int:
        """
        Time complexity: O(n*logn), where n is the number of prices.
        Space complexity: O(1).
        """
        # Edge case.
        if not prices:
            return 0

        # Binary search.
        left, right = 0, len(prices) - 1
        return self._binarySearch(prices, left, right)


class SolutionIter(object):
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time complexity: O(n), where n is the number of prices.
        Space complexity: O(1).
        """
        if not prices:
            return 0
    
        # Continue tracking min price and max profit.
        min_price = float('inf')
        max_profit = 0

        for i, p in enumerate(prices):
            if p < min_price:
                min_price = p
            else:
                max_profit = max(p - min_price, max_profit)

        return max_profit


def main():
    import time

    # Ans: 5
    prices = [7,1,5,3,6,4]

    start_time = time.time()
    print('By brute force:', SolutionBruteForce().maxProfit(prices))
    print('Time:', time.time() - start_time)

    start_time = time.time()
    print('By binary search:', SolutionBinarySearch().maxProfit(prices))
    print('Time:', time.time() - start_time)

    start_time = time.time()
    print('By iter:', SolutionIter().maxProfit(prices))
    print('Time:', time.time() - start_time)

    # Ans: 6
    prices = [6,1,3,2,4,7]

    start_time = time.time()
    print('By brute force:', SolutionBruteForce().maxProfit(prices))
    print('Time:', time.time() - start_time)

    start_time = time.time()
    print('By binary search:', SolutionBinarySearch().maxProfit(prices))
    print('Time:', time.time() - start_time)

    start_time = time.time()
    print('By iter:', SolutionIter().maxProfit(prices))
    print('Time:', time.time() - start_time)


if __name__ == '__main__':
    main()
