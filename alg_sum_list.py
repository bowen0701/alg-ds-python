from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def sum_list_recur(a_list):
    """Sum list by recursion.

    Time complexity: O(n), where n is the list length.
    Space complexity: O(n).
    """
    if len(a_list) == 1:
        return a_list[0]
    else:
        return a_list[0] + sum_list_recur(a_list[1:])


def sum_list_dp(a_list):
    """Sum list by bottom-up dynamic programming.

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

    start_time = time.time()
    print('By recursion: {}'.format(sum_list_recur(a_list)))
    print('Time: {}'.format(time.time() - start_time))

    
    start_time = time.time()
    print('By DP: {}'.format(sum_list_dp(a_list)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
