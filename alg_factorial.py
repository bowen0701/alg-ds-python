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
    """Nth number of factorial series by recursion.

    - Time complexity: O(n)
    - Space complexity: O(n).
    """
    # Base case.
    if n <= 1:
        return 1

    return n * factorial_recur(n - 1)


def _factorial_memo(n, T):
    # Base case.
    if n <= 1:
        return 1

    if T[n]:
        return T[n]

    T[n] = n * _factorial_memo(n - 1, T)
    return T[n]


def factorial_memo(n):
    """Nth number of factorial series by top-down DP w/ recursion + memo.

    - Time complexity: O(n)
    - Space complexity: O(n).
    """
    T = [0 for _ in range(n + 1)]
    return _factorial_memo(n, T)


def factorial_dp(n):
    """Nth number of factorial series by bottom-up DP.
    
    - Time complexity: O(n).
    - Space complexity: O(n).
    """
    T = [0 for _ in range(n + 1)]
    T[0] = 1
    T[1] = 1
    for k in range(2, n + 1):
        T[k] = k * T[k - 1]

    return T[n]


def factorial_iter(n):
    """Nth number of factorial series by bottom-up DP w/ optimized space.

    - Time complexity: O(n).
    - Space complexity: O(1).
    """
    f = 1
    for k in range(2, n + 1):
        f *= k 
    return f


def main():
    import time
    n = 10
    
    print('{}th number of factorial series:'.format(n))

    start_time = time.time()
    print('Recur: {}'.format(factorial_recur(n)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('Memo: {}'.format(factorial_memo(n)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('DP: {}'.format(factorial_dp(n)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('Iter: {}'.format(factorial_iter(n)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
