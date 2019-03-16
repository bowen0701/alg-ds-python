"""Factorial series:

1!, 2!, 3!, ...

- Factorial(1) = 1! = 1
- Factorial(2) = 2! = 2
- Factorial(n) = n! = n * (n - 1)! = n * Factorial(n - 1)
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def factorial_recur(n):
    """Get the nth number of factorial series by recursion.

    - Time complexity: O(n)
    - Space complexity: O(n).
    """
    if n <= 1:
        return 1
    else:
        return n * factorial_recur(n - 1)


def factorial_memo(n):
    """Get the nth number of factorial series by memorization.
    
    - Time complexity: O(n).
    - Space complexity: O(n).
    """
    F = [None for _ in range(n + 1)]
    F[0] = 1
    F[1] = 1

    for k in range(2, n + 1):
        F[k] = k * F[k - 1]

    return F[n]


def factorial_dp(n):
    """Get the nth number of factorial series by dynamic programming.

    - Time complexity: O(n).
    - Space complexity: O(1).
    """
    fn = 1
    for i in range(2, n + 1):
        fn *= i 
    return fn


def main():
    import time
    n = 10
    
    print('{}th number of factorial series:'.format(n))

    start_time = time.time()
    print('By recursion: {}'.format(factorial_recur(n)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By memorization: {}'.format(factorial_memo(n)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By dynamic programming: {}'.format(factorial_dp(n)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
