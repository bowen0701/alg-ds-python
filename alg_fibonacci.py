"""Fibonacci series:

0, 1, 1, 2, 3, 5, 8,... 

- Fib(0) = 0
- Fib(1) = 1
- Fib(n) = Fib(n - 1) + Fib(n - 2)
"""

from __future__ import print_function
import time


def fibonacci(n):
    """Get nth number of Fibonacci series by recursion."""
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    n = 13
    print('{}th number of Fibonacci series: {}'
          .format(n, fibonacci(n)))


if __name__ == '__main__':
    main()
