from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def gcd_recur(a, b):
    """Greatest Common Divisor (GCD) by Euclid's Algorithm.

    Time complexity: O(log(max(a, b))).
    Space complexity: O(log(max(a, b))).
    """
    if b == 0:
        return a
    return gcd_recur(b, a % b)


def gcd_iter(m, n):
    """Greatest Common Divisor (GCD) by Euclid's Algorithm.

    Time complexity: O(log(max(a, b))).
    Space complexity: O(1).
    """
    while b != 0:
        a, b = b, a % b
    return a


def main():
    import time

    start_time = time.time()
    print('gcd_recur(4, 2): {}'.format(gcd_recur(4, 2)))
    print('gcd_recur(2, 4): {}'.format(gcd_recur(2, 4)))
    print('gcd_recur(10, 4): {}'.format(gcd_recur(10, 4)))
    print('gcd_recur(4, 10): {}'.format(gcd_recur(4, 10)))
    print('gcd_recur(3, 4): {}'.format(gcd_recur(3, 4)))
    print('gcd_recur(4, 3): {}'.format(gcd_recur(4, 3)))
    print('Time:', time.time() - start_time)

    start_time = time.time()
    print('gcd_iter(4, 2): {}'.format(gcd_iter(4, 2)))
    print('gcd_iter(2, 4): {}'.format(gcd_iter(2, 4)))
    print('gcd_iter(10, 4): {}'.format(gcd_iter(10, 4)))
    print('gcd_iter(4, 10): {}'.format(gcd_iter(4, 10)))
    print('gcd_iter(3, 4): {}'.format(gcd_iter(3, 4)))
    print('gcd_iter(4, 3): {}'.format(gcd_iter(4, 3)))
    print('Time:', time.time() - start_time)


if __name__ == '__main__':
    main()
