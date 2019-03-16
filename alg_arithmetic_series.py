from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


"""Arithmetic series: 1 + 2 + 3 + ... + 100."""

def _arithmetic_series_recur(a_list):
    """Helper function for geometric_series_recur()."""
    if len(a_list) == 1:
        return a_list[0]
    else:
        return a_list[0] + _arithmetic_series_recur(a_list[1:])


def arithmetic_series_recur(n):
    """Arithmetic series by recursion.

    Time complexity: O(n).
    Space complexity: O(n)
    """
    a_list = range(1, n + 1)
    return _arithmetic_series_recur(a_list)


def arithmetic_series_dp(n):
    """Arithmetic series by bottom-up dynamic programming 
    w/ optimized space.

    Time complexity: O(n).
    Space complexity: O(1)
    """
    a_list = range(1, n + 1)
    s = 0
    for x in a_list:
        s += x
    return s


def arithmetic_series(n):
    """Arithmetic series by Gauss sum formula.

    Time complexity: O(1).
    Space complexity: O(1)
    """
    return (1 + n) * n / 2


def main():
    import time

    start_time = time.time()
    print('By recursion: {}'.format(arithmetic_series_recur(100)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By optimized DP: {}'.format(arithmetic_series_dp(100)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By Gauss sum: {}'.format(arithmetic_series(100)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()