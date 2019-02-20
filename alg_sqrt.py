from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def sqrt_bisect(n, steps=20, epsilon=10**-5):
    """Approximate square root by the bisection method."""
    assert n > 0
    assert epsilon > 0
    low = 0
    high = n
    step = 1
    sqrt = (low + high) / 2
    while abs(sqrt**2 - n) > epsilon and step <= steps:
        if sqrt**2 < n:
            low = sqrt
        else:
            high = sqrt
        sqrt = (low + high) / 2
        step += 1
    return sqrt


def sqrt_newton(n, steps=20):
    """Approximate square root by Newton's Method.
    
    - Initial guess: old_guess = n / 2
    - Iterations: new_guess = 1/2 * (old_guess + n / old_guess)
    """
    sqrt = n / 2
    for step in range(steps):
        sqrt = 1 / 2 * (sqrt + n / sqrt)
    return sqrt


def main():
    import time

    n = 16

    start_time = time.time()
    print('Find square root of {0} by bisection: {1}'
          .format(n, sqrt_bisect(n, steps=20)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('Find square root of {0} by Newton method: {1}'
          .format(n, sqrt_newton(n, steps=20)))
    print('Time: {}'.format(time.time() - start_time))

    n = 1234567890

    start_time = time.time()
    print('Find square root of {0} by bisection: {1}'
          .format(n, sqrt_bisect(n, steps=20)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('Find square root of {0} by Newton method: {1}'
          .format(n, sqrt_newton(n, steps=20)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
