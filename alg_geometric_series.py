from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""Geometric series: 1 + r + r^2 + ... + r^(n+1)."""

def geometric_series_recur(n, r):
    """Geometric series by recursion.

    Time complexity: O(n).
    Space complexity: O(n)
    """
    # a_list = [pow(2, x) for x in range(n + 1)]
    # return _geometric_series_recur(a_list)
    if n == 0:
        return 1
    return pow(r, n) +  geometric_series_recur(n - 1, r)


def geometric_series_memo(n, r):
    """Geometric series by recursion.

    Time complexity: O(n).
    Space complexity: O(n)
    """
    # TODO: Implement geometric_series_memo().
    if n == 0:
        return 1
    return pow(r, n) +  geometric_series_recur(n - 1, r)


def geometric_series_dp(n, r):
    """Geometric series by bottom-up dynamic programming 
    w/ optimized space.

    Time complexity: O(n).
    Space complexity: O(1)
    """
    a_list = [pow(r, x) for x in range(n + 1)]
    s = 0
    for x in a_list:
        s += x
    return s


def geometric_series(n, r):
    """Geometric series by Gauss sum formula.

    Time complexity: O(1).
    Space complexity: O(1)
    """
    return 1 * (pow(r, n + 1) - 1) / (r - 1)


def main():
    import time

    start_time = time.time()
    print('By recursion: {}'.format(geometric_series_recur(63)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By optimized DP: {}'.format(geometric_series_dp(63)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By closed form: {}'.format(geometric_series(63)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
