"""Fibonacci series:

0, 1, 1, 2, 3, 5, 8,... 

- Fib(0) = 0
- Fib(1) = 1
- Fib(n) = Fib(n - 1) + Fib(n - 2)
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def fibonacci_recur(n):
    """Fibonacci series by recursion.

    - Time complexity: O(2^n)
    - Space complexity: O(n).
    """
    if n <= 1:
        return n
    else:
        return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)


def _fibonacci_memo(n, f):
    """Fibonacci series by top-down memoization.

    Time complexity: O(n).
    Space complexity: O(n).
    """
    if f[n]:
        return f[n]

    if n <= 1:
        f[n] = n
    else:
        f[n] = _fibonacci_memo(n - 1, f) + _fibonacci_memo(n - 2, f)
    return f[n]


def fibonacci_memo(n):
    f = [None for _ in range(n + 1)]
    return _fibonacci_memo(n, f)


def fibonacci_dp(n):
    """Fibonacci series by bottom-up dynamic programming.

    - Time complexity: O(n).
    - Space complexity: O(n).
    """
    f = [None for _ in range(n + 1)]
    f[0] = 0
    f[1] = 1
    for n in range(2, n + 1):
        f[n] = f[n - 1] + f[n - 2]
    return f[n]


def fibonacci_iter(n):
    """Fibonacci series by bottom-up dynamic programming with optimized space.

    - Time complexity: O(n).
    - Space complexity: O(1).
    """
    a, b = 0, 1
    for _ in range(n):
        # Add two numbers and then shift position by one.
        a, b = b, a + b
    return a


def main():
    import time
    n = 20
    
    print('{}th number of Fibonacci series:'.format(n))

    start_time = time.time()
    print('By recursion: {}'.format(fibonacci_recur(n)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By memoization: {}'.format(fibonacci_memo(n)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By dynamic programming: {}'.format(fibonacci_dp(n)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By iteration: {}'.format(fibonacci_dp(n)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
