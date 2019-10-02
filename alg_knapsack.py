from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""Knapsack Problem
Given weights and values of n "splittable" items, put these items in a knapsack of 
capacity to get the maximum total value in the knapsack. 
"""

def _reverse_quicksort(vals_per_wts):
    """Reverse quick sort by p = v / w."""
    if len(vals_per_wts) <= 1:
        return vals_per_wts

    pivot = vals_per_wts[len(vals_per_wts) // 2]

    left_ls = [(i, v, w, p) for (i, v, w, p) in vals_per_wts if p <  pivot[3]]
    middle_ls = [(i, v, w, p) for (i, v, w, p) in vals_per_wts if p == pivot[3]]
    right_ls = [(i, v, w, p) for (i, v, w, p) in vals_per_wts if p > pivot[3]]

    return _reverse_quicksort(right_ls) + middle_ls + _reverse_quicksort(left_ls)


def knapsack(val, wt, wt_cap):
    """Knapsack Problem by greedy algorithm w/ max val per wt.

    Time complexity: O(n*logn), where n is the number of items. 
    Space complexity: O(n).
    """
    vals_per_wts = [(i, v, w, v / w) for i, (v, w) in enumerate(zip(val, wt))]
    sorted_vals_per_wts = _reverse_quicksort(vals_per_wts)

    max_val = 0
    total_wt = 0

    for _, v, w, p in sorted_vals_per_wts:
        if total_wt + w <= wt_cap:
            total_wt += w
            max_val += v
        else:
            wt_remain = (wt_cap - total_wt)
            max_val += p * wt_remain
            break
    return max_val


def main():
    val = [3, 8, 18, 6, 8, 20, 5, 6, 7, 15]
    wt = [4, 2, 9, 5, 5, 8, 5, 4, 5, 5]
    wt_cap = 30
    # Output: 70.5.
    print('Max value: {}'.format(knapsack(val, wt, wt_cap)))


if __name__ == '__main__':
    main()
