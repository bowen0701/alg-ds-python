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
    """Get nth number of Fibonacci series by recursion."""
    if n <= 1:
        return n
    else:
        return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)


def main():
    import time
    n = 13
    
    start_time = time.time()
    print('{}th number of Fibonacci series by recursion: {}'
          .format(n, fibonacci_recur(n)))
    print('Time: {}'.format(time.time() - start_time))

if __name__ == '__main__':
    main()
