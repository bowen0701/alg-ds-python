"""0-1 Knapsack Problem
Given weights and values of n "non-splittable" items, put these items in a 
knapsack of capacity to get the maximum total value in the knapsack. 
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def _knapsack01_recur(val, wt, wt_cap, n):
    """0-1 Knapsack Problem by naive recursion.

    Time complexity: O(2^n), where n is the number of items.
    Space complexity: O(n).
    """
    if n < 0 or wt_cap == 0:
        return 0
    
    if wt[n] > wt_cap:
        # Cannot be added.
        result = _knapsack01_recur(val, wt, wt_cap, n - 1)
    else:
        # Can be added: to add or not to add. 
        val_in = val[n] + _knapsack01_recur(val, wt, wt_cap - wt[n], n - 1)
        val_ex = _knapsack01_recur(val, wt, wt_cap, n - 1)
        result = max(val_in, val_ex)
    return result


def knapsack01_recur(val, wt, wt_cap):
    """0-1 Knapsack Problem by naive recursion.

    Time complexity: O(2^n), where n is the number of items.
    Space complexity: O(n).
    """
    n = len(wt) - 1
    return _knapsack01_recur(val, wt, wt_cap, n)


def _knapsack01_memo(val, wt, wt_cap, T, n):
    if n < 0 or wt_cap == 0:
        return 0

    if T[n][wt_cap]:
        return T[n][wt_cap]

    if wt[n] > wt_cap:
        # Cannot be added.
        result = _knapsack01_memo(val, wt, wt_cap, T, n - 1)
    else:
        # Can be added: to add or not to add. 
        val_in = val[n] + _knapsack01_memo(val, wt, wt_cap - wt[n], T, n - 1)
        val_ex = _knapsack01_memo(val, wt, wt_cap, T, n - 1)
        result = max(val_in, val_ex)

    T[n][wt_cap] = result
    return result


def knapsack01_memo(val, wt, wt_cap):
    """0-1 Knapsack Problem by top-down dynamic programming w/ memoization.

    Time complexity: O(n*c), where 
      - n is the number of items, and 
      - c is the weight capacity.
    Space complexity: O(n*c).
    """
    n = len(wt) - 1

    # Memoization table T of (n+1)*(wt_cap+1).
    T = [[None] * (wt_cap + 1) for i in range(n + 1)]

    # For empty cap, no value can be added.
    for i in range(n + 1):
        T[i][0] = 0

    return _knapsack01_memo(val, wt, wt_cap, T, n)


def knapsack01_dp(val, wt, wt_cap):
    """0-1 Knapsack Problem by bottom-up dynamic programming.

    Time complexity: O(n*c), where 
      - n is the number of items, and 
      - c is the weight capacity.
    Space complexity: O(n*c).
    """
    n = len(wt)

    # Memoization table T of n x (wt_cap+1).
    T = [[None] * (wt_cap + 1) for i in range(n)]
 
    # For empty cap, no value can be added.   
    for i in range(n):
        T[i][0] = 0
    
    # For 1s item only.
    for j in range(1, wt_cap + 1):
        if wt[0] <= j:
            T[0][j] = val[0]
        else:
            T[0][j] = 0

    for i in range(1, n):
        for j in range(1, wt_cap + 1):
            if wt[i] <= j:
                # Can be added: to add or not to add.
                T[i][j] = max(val[i] + T[i - 1][j - wt[i]], T[i - 1][j])
            else:
                # Cannot be added.
                T[i][j] = T[i-1][j]

    return T


def get_items(T, wt, wt_cap):
    n = len(wt)
    items = [0] * n

    w = wt_cap
    for i in range(n - 1, -1, -1):
        if i >= 1 and T[i][w] > T[i - 1][w]:
            # Item i, i >= 1, is added.
            items[i] = 1
            w -= wt[i]
        elif i == 0 and T[i][w] != 0:
            # Item 0 is added.
            items[i] = 1

    return items


def main():
    import time

    val = [6, 3, 5, 4, 6]
    wt = [2, 5, 4, 2, 3]
    wt_cap = 10
    # Output: 17

    start_time = time.time()
    print('By recur: {}'.format(knapsack01_recur(val, wt, wt_cap)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By memo: {}'.format(knapsack01_memo(val, wt, wt_cap)))
    print('Time by memo: {}'.format(time.time() - start_time))

    start_time = time.time()
    T = knapsack01_dp(val, wt, wt_cap)
    print('By DP: {}'.format(T[-1][-1]))
    print('Time: {}'.format(time.time() - start_time))
    print('Items: {}'.format(get_items(T, wt, wt_cap)))


if __name__ == '__main__':
    main()
