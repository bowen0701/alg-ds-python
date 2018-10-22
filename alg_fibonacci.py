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
    """Get the nth number of Fibonacci series, Fn, by recursion.

    - Time complexity: 2Fn - 1 = O(Fn); too fast.
    - Space complexity: O(n).
    """
    if n <= 1:
        return n
    else:
        return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)


def fibonacci_memo(n):
    """Get the nth number of Fibonacci series, Fn, by memoization.

    - Time complexity: O(n).
    - Space complexity: O(n).
    """
    fn_d = {}
    fn_d[0] = 0
    fn_d[1] = 1
    for n in range(2, n + 1):
        fn_d[n] = fn_d[n - 1] + fn_d[n - 2]
    return fn_d[n]


def fibonacci_dp(n):
    """Get the nth number of Fibonacci series by dynamic programming.

    - Time complexity is still O(n), like fibonacci_memo().
    - Space complexity is O(1), improving a lot.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = a + b, a
    return a


def fibonacci_gen(n):
    """Get the nth number of Fibonacci series by generator."""
    a, b = 0, 1
    for _ in range(n):
        a, b = a + b, a
        yield a


def main():
    import time
    n = 30
    
    print('{}th number of Fibonacci series:'.format(n))

    start_time = time.time()
    print('By recursion: {}'.format(fibonacci_recur(n)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By memorization: {}'.format(fibonacci_memo(n)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By dynamic programming: {}'.format(fibonacci_dp(n)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By generator: {}'.format(list(fibonacci_gen(n))[-1]))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
