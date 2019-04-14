from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def count_subset_sum_recur(arr, total, n):
    """Count subsets given sum by recusrion.

    Time complexity: O(2^n), where n is length of array.
    Space complexity: O(1).
    """
    if total < 0:
        return 0
    if total == 0:
        return 1

    if n < 0:
        return 0

    if total < arr[n]:
        return count_subsets_total_recur(arr, total, n - 1)
    else:
        n_subsets_in = count_subsets_total_recur(arr, total - arr[n], n - 1)
        n_subsets_out = count_subsets_total_recur(arr, total, n - 1)
        return n_subsets_in + n_subsets_out


def _count_subset_sum_memo(arr, total, T, n):
    """Helper function for count_subsets_total_memo()."""
    if total < 0:
        return 0
    if total == 0:
        return 1

    if n < 0:
        return 0

    if T[n][total]:
        return T[n][total]

    if total < arr[n]:
        n_subsets = count_subsets_total_recur(arr, total, n - 1)
    else:
        n_subsets_in = count_subsets_total_recur(arr, total - arr[n], n - 1)
        n_subsets_out = count_subsets_total_recur(arr, total, n - 1)
        n_subsets = n_subsets_in + n_subsets_out

    T[n][total] = n_subsets
    return n_subsets


def count_subset_sum_memo(arr, total):
    """Count subsets given sum by top-down memoization.

    Time complexity: O(nm), where n is length of array, and m is total.
    Space complexity: O(nm).
    """
    n = len(arr) - 1

    T = [[0] * (total + 1) for _ in range(n + 1)]

    for a in range(n):
        T[a][0] = 1

    return _count_subsets_memo(arr, total, T, n)


def count_subset_sum_dp(arr, total):
    """Count subsets given sum by bottom-up dynamic programming.

    Time complexity: O(nm).
    Space complexity: O(nm).
    """
    n = len(arr) - 1
    T = [[0] * (total + 1) for _ in range(n + 1)]

    for a in range(n + 1):
        T[a][0] = 1

    for a in range(n):
        for t in range(1, total + 1):
            if t < arr[a]:
                T[a][t] = T[a - 1][t]
            else:
                n_subsets_in = T[a - 1][t - arr[a]]
                n_subsets_out = T[a - 1][t]
                n_subsets = n_subsets_in + n_subsets_out
                T[a][t] = n_subsets

    return T[-1][-1]


def main():
    import time

    arr = [2, 4, 6, 10]
    total = 16
    n = len(arr) - 1

    start_time = time.time()
    n_subsets = count_subset_sum_recur(arr, total, n)
    print('Recursion: {}'.format(n_subsets))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    n_subsets = count_subset_sum_memo(arr, total)
    print('Memo: {}'.format(n_subsets))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    n_subsets = count_subset_sum_dp(arr, total)
    print('Memo: {}'.format(n_subsets))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
