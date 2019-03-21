from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


"""0-1 Knapsack Problem
Given weights and values of n items, put these items in a knapsack of 
capacity to get the maximum total value in the knapsack. 
"""

def knapsack01_recur(val, wt, wt_cap):
    """0-1 Knapsack Problem by naive recursion.

    Time complexity: O(2^n), where n is the number of items.
    Space complexity: O(n).
    """
    if len(wt) == 0 or wt_cap == 0:
        return 0
    elif wt[-1] > wt_cap:
        return knapsack01_recur(val[:-1], wt[:-1], wt_cap)
    else:
        last_excluded = knapsack01_recur(val[:-1], wt[:-1], wt_cap)
        last_included = (
            val[-1] + knapsack01_recur(val[:-1], wt[:-1], wt_cap - wt[-1]))
        return max(last_excluded, last_included)


def _knapsack01_memo(val, wt, wt_cap, M):
    if M[len(wt) - 1][wt_cap]:
        return M[len(wt)][wt_cap]

    if len(wt) == 0 or wt_cap == 0:
        return 0
    elif wt[-1] > wt_cap:
        memo = knapsack01_recur(val[:-1], wt[:-1], wt_cap)
    else:
        last_excluded = knapsack01_recur(val[:-1], wt[:-1], wt_cap)
        last_included = (
            val[-1] + knapsack01_recur(val[:-1], wt[:-1], wt_cap - wt[-1]))
        memo = max(last_excluded, last_included)
    M[len(wt) - 1][wt_cap] = memo
    return memo


def knapsack01_memo(val, wt, wt_cap):
    """0-1 Knapsack Problem by top-down dynamic programming w/ memoization.

    Time complexity: O(nC), where 
      - n is the number of items, and 
      - C is the weight capacity.
    Space complexity: O(nC).
    """
    M = [[None for j in range(wt_cap + 1)] for i in range(len(wt))]
    for i in range(len(wt)):
        M[i][0] = 0

    return _knapsack01_memo(val, wt, wt_cap, M)


def knapsack_dp(val, wt, wt_cap):
    """0-1 Knapsack Problem by bottom-up dynamic programming.

    Time complexity: O(nC), where 
      - n is the number of items, and 
      - C is the weight capacity.
    Space complexity: O(nC).
    """
    M = [[None for j in range(wt_cap + 1)] for i in range(len(wt))]
    
    for i in range(len(wt)):
        M[i][0] = 0
    
    for j in range(1, wt_cap + 1):
        if wt[0] > j:
            M[0][j] = 0
        else:
            M[0][j] = val[0]

    for i in range(1, len(wt)):
        for j in range(1, wt_cap + 1):
            if wt[i] > j:
                M[i][j] = M[i - 1][j]
            else:
                M[i][j] = max(M[i - 1][j], val[i] + M[i - 1][j - wt[i]])

    return M[-1][-1], M


def item_list(M, wt, wt_cap):
    items = [0 for _ in range(len(wt))]

    j = wt_cap
    for i in range(len(wt) - 1, -1, -1):
        if i >= 1 and M[i][j] > M[i - 1][j]:
            items[i] = 1
            j -= wt[i]
        elif i == 0 and M[i][j] != 0:
            items[i] = 1

    return items


def main():
    import time

    val = [6, 3, 5, 4, 6]
    wt = [2, 5, 4, 2, 3]
    wt_cap = 10
    # Ans: 17

    start_time = time.time()
    print(knapsack01_recur(val, wt, wt_cap))
    print('Time by recursion: {}'.format(time.time() - start_time))

    start_time = time.time()
    print(knapsack01_memo(val, wt, wt_cap))
    print('Time by memo: {}'.format(time.time() - start_time))

    start_time = time.time()
    max_val, M = knapsack_dp(val, wt, wt_cap)
    print(max_val)
    print('Time by DP: {}'.format(time.time() - start_time))
    print('Items: {}'.format(item_list(M, wt, wt_cap)))


if __name__ == '__main__':
    main()
