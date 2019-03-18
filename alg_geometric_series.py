from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""Geometric series: 1 + r + r^2 + ... + r^(n+1)."""

def geometric_series_recur(n, r):
    """Geometric series by recursion.

    Time complexity: O(n).
    Space complexity: O(n)
    """
    if n == 0:
        return 1
    return pow(r, n) + geometric_series_recur(n - 1, r)


def _geometric_series_memo(n, r, s):
    if s[n]:
        return s[n]

    if n == 0:
        s[n] = 1
    else:
        s[n] = pow(r, n) + _geometric_series_memo(n - 1, r, s)
    return s[n]


def geometric_series_memo(n, r):
    """Geometric series by recursion+memoization.

    Time complexity: O(n).
    Space complexity: O(n)
    """
    s = [None for _ in range(n + 1)]
    return _geometric_series_memo(n, r, s)


def geometric_series_dp(n, r):
    """Geometric series by bottom-up DP.

    Time complexity: O(n).
    Space complexity: O(n)
    """
    s = [None for x in range(n + 1)]
    s[0] = 1
    for k in range(1, n + 1):
        s[k] = pow(r, k) + s[k - 1]
    return s[n]


def geometric_series_dp2(n, r):
    """Geometric series by bottom-up DP w/ optimized space.

    Time complexity: O(n).
    Space complexity: O(1)
    """
    s = 0
    for k in range(1, n + 1):
        s += pow(r, k)
    return s


def geometric_series(n, r):
    """Geometric series by Gauss sum formula.

    Time complexity: O(1).
    Space complexity: O(1)
    """
    return (pow(r, n + 1) - 1) / (r - 1)


def main():
    import time

    start_time = time.time()
    print('By recursion: {}'.format(geometric_series_recur(63, 2)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By memo: {}'.format(geometric_series_memo(63, 2)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP: {}'.format(geometric_series_dp(63, 2)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By optimized DP: {}'.format(geometric_series_dp2(63, 2)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By closed form: {}'.format(geometric_series(63, 2)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
