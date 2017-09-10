from __future__ import division
from __future__ import print_function


def square_root_bisection(n, steps=20, epsilon=10**-5):
    """Approximate square root by the bisection method."""
    assert n > 0
    assert epsilon > 0
    low = 0
    high = n
    step = 1
    sqroot = (low + high) / 2
    while abs(sqroot ** 2 - n) > epsilon and step <= steps:
        if sqroot ** 2 < n:
            low = sqroot
        else:
            high = sqroot
        sqroot = (low + high) / 2
        print('Iteration {0}: {1}'.format(step, sqroot))
        step += 1
    return sqroot


def square_root(n, steps=20, epsilon=10**-5):
    """Approximate square root by Newton's Method.
    
    - Initial guess: old_guess = n / 2
    - Iterations: new_guess = 1/2 * (old_guess + n / old_guess)
    """
    sqroot = n / 2
    for step in range(steps):
        sqroot = 1 / 2 * (sqroot + n / sqroot)
        print('Iteration {0}: {1}'.format(step, sqroot))
    return sqroot


def main():
    n = 16
    print('Find squared root of {} by bisection'.format(n))
    square_root_bisection(n, steps=20)
    print('Find squared root of {} by Newton method'.format(n))
    square_root(n, steps=20)

    n = 17
    print('Find squared root of {} by bisection'.format(n))
    square_root_bisection(n, steps=20)
    print('Find squared root of {} by Newton method'.format(n))
    square_root(n, steps=20)


if __name__ == '__main__':
    main()
