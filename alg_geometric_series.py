from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""Geometric series: 1 + 2 + 2^2 + ... + 2^63."""

def _geometric_series_recur(a_list):
    """Helper function for geometric_series_recur()."""
    if len(a_list) == 1:
        return a_list[0]
    else:
        return a_list[0] + _geometric_series_recur(a_list[1:])


def geometric_series_recur(n):
    """Geometric series by recursion.

    Time complexity: O(n).
    Space complexity: O(n)
    """
    a_list = [pow(2, x) for x in range(n + 1)]
    return _geometric_series_recur(a_list)


def geometric_series_dp(n):
    """Geometric series by bottom-up dynamic programming 
    w/ optimized space.

    Time complexity: O(n).
    Space complexity: O(1)
    """
    a_list = [pow(2, x) for x in range(n + 1)]
    s = 0
    for x in a_list:
        s += x
    return s


def geometric_series(n):
    """Geometric series by Gauss sum formula.

    Time complexity: O(1).
    Space complexity: O(1)
    """
    return 1 * (pow(2, n + 1) - 1) / (2 - 1)


def main():
    import time

    start_time = time.time()
    print('By recursion: {}'.format(geometric_series_recur(63)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By optimized DP: {}'.format(geometric_series_dp(63)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By equation: {}'.format(geometric_series(63)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
