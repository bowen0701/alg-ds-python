from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


"""Arithmetic series: 1 + 2 + 3 + ... + n."""

def arithmetic_series_recur(n):
    """Arithmetic series by recursion.

    Time complexity: O(n).
    Space complexity: O(n)
    """
    # Base case.
    if n <= 1:
        return n
    return n + arithmetic_series_recur(n - 1)


def _arithmetic_series_memo(n, s):
    # Base case.
    if n <= 1:
        return n

    if s[n]:
        return s[n]

    s[n] = n + _arithmetic_series_memo(n - 1, s)
    return s[n]


def arithmetic_series_memo(n):
    """Arithmetic series by recursion.

    Time complexity: O(n).
    Space complexity: O(n)
    """
    s = [0 for _ in range(n + 1)]
    return _arithmetic_series_memo(n, s)


def arithmetic_series_dp(n):
    """Arithmetic series by bottom-up DP.

    Time complexity: O(n).
    Space complexity: O(n)
    """
    s = [0 for _ in range(n + 1)]
    s[0] = 0
    s[1] = 1
    for k in range(2, n + 1):
        s[k] = k + s[k - 1]
    return s[n]


def arithmetic_series_dp2(n):
    """Arithmetic series by bottom-up DP w/ optimized space.

    Time complexity: O(n).
    Space complexity: O(1)
    """
    s = 0
    for x in range(1, n + 1):
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
    print('By memo: {}'.format(arithmetic_series_memo(100)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP: {}'.format(arithmetic_series_dp(100)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By optimized DP: {}'.format(arithmetic_series_dp2(100)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By Gauss sum: {}'.format(arithmetic_series(100)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()