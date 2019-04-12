from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def count_subsets_total_recur(arr, total, n):
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


def count_subsets_total_memo():
    pass


def count_subsets_total_dp():
    pass


def main():
    import time

    arr = [2, 4, 6, 10]
    total = 16
    n = len(arr) - 1

    start_time = time.time()
    n_subsets = count_subsets_total_recur(arr, total, n)
    print('Recursion: {}'.format(n_subsets))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
