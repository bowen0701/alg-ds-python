"""Knapsack Problem
Given weights and values of n "splittable" items, put these items in a 
knapsack of capacity to get the maximum total value in the knapsack. 
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def knapsack(val, wt, wt_cap):
    """Knapsack Problem by greedy algorithm w/ max val per wt.

    Time complexity: O(n*logn), where n is the number of items. 
    Space complexity: O(n).
    """
    # Add highest value per weight first.
    vals_per_wts = [(v / w, v, w) for (v, w) in zip(val, wt)]
    sorted_vals_per_wts = sorted(vals_per_wts, reverse=True)

    max_val = 0
    total_wt = 0

    for vw, v, w in sorted_vals_per_wts:
        if total_wt + w <= wt_cap:
            total_wt += w
            max_val += v
        else:
            wt_remain = (wt_cap - total_wt)
            max_val += vw * wt_remain
            break
    return max_val


def main():
    # Output: 70.5.
    val = [3, 8, 18, 6, 8, 20, 5, 6, 7, 15]
    wt = [4, 2, 9, 5, 5, 8, 5, 4, 5, 5]
    wt_cap = 30
    print('Max value: {}'.format(knapsack(val, wt, wt_cap)))


if __name__ == '__main__':
    main()
