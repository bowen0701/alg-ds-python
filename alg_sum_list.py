from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def sum_list_recur(a_list, n):
    """Sum list by recursion.

    Time complexity: O(n).
    Space complexity: O(n).
    """
    if n == 0:
        return a_list[0]
    else:
        return a_list[n] + sum_list_recur(a_list, n - 1)


def sum_list_dp(a_list, n):
    """Sum list by bottom-up dynamic programming.

    Time complexity: O(n).
    Space complexity: O(n).
    """
    s = [None for _ in range(n + 1)]

    s[0] = a_list[0]

    for i in range(1, n + 1):
        s[i] = a_list[i] + s[i - 1]
    return s[-1]


def sum_list_dp2(a_list):
    """Sum list by bottom-up dynamic programming w/ optimized space.

    Time complexity: O(n).
    Space complexity: O(1).
    """
    s = 0
    for x in a_list:
        s += x
    return s


def main():
    import time
    import random

    a_list = [random.randint(0, 1000) for _ in range(100)]
    n = len(a_list) - 1

    start_time = time.time()
    print('By recursion: {}'.format(sum_list_recur(a_list, n)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP: {}'.format(sum_list_dp(a_list, n)))
    print('Time: {}'.format(time.time() - start_time))
    
    start_time = time.time()
    print('By DP: {}'.format(sum_list_dp2(a_list)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
