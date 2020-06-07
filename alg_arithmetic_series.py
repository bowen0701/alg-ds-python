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


def _arithmetic_series_memo(n, T):
    # Base case.
    if n <= 1:
        return n

    if T[n]:
        return T[n]

    T[n] = n + _arithmetic_series_memo(n - 1, T)
    return T[n]


def arithmetic_series_memo(n):
    """Arithmetic series by recursion.

    Time complexity: O(n).
    Space complexity: O(n)
    """
    T = [0 for _ in range(n + 1)]
    return _arithmetic_series_memo(n, T)


def arithmetic_series_dp(n):
    """Arithmetic series by bottom-up DP.

    Time complexity: O(n).
    Space complexity: O(n)
    """
    T = [0 for _ in range(n + 1)]
    T[0] = 0
    T[1] = 1
    for k in range(2, n + 1):
        T[k] = k + T[k - 1]
    return T[n]


def arithmetic_series_iter(n):
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
    print('By iteration: {}'.format(arithmetic_series_iter(100)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By Gauss sum: {}'.format(arithmetic_series(100)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()