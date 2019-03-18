from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


"""Arithmetic series: 1 + 2 + 3 + ... + n."""

def arithmetic_series_recur(n):
    """Arithmetic series by recursion.

    Time complexity: O(n).
    Space complexity: O(n)
    """
    if n <= 1:
        return n
    return n + arithmetic_series_recur(n - 1)


def arithmetic_series_memo(n):
    """Arithmetic series by recursion.

    Time complexity: O(n).
    Space complexity: O(n)
    """
    # Implement arithmetic_series_memo().
    if n <= 1:
        return n
    return n + arithmetic_series_recur(n - 1)


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