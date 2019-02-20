from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def gcd(m, n):
    """Greatest Common Divisor (GCD) by Euclid's Algorithm.

    Time complexity: O(m%n).
    """
    while n != 0:
        m, n = n, m % n
    return m


def main():
    print('gcd(4, 2): {}'.format(gcd(4, 2)))
    print('gcd(2, 4): {}'.format(gcd(2, 4)))

    print('gcd(10, 4): {}'.format(gcd(10, 4)))
    print('gcd(4, 10): {}'.format(gcd(4, 10)))

    print('gcd(3, 4): {}'.format(gcd(3, 4)))
    print('gcd(4, 3): {}'.format(gcd(4, 3)))


if __name__ == '__main__':
    main()
