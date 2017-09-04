from __future__ import division
from __future__ import print_function


def square_root(n, steps=20):
    """Approximate square root by Newton's Method.
    
    - Initial guess: old_guess = n / 2
    - Iterations: new_guess = 1/2 * (old_guess + n / old_guess)
    """
    sqroot = n / 2
    for k in range(steps):
        sqroot = 1 / 2 * (sqroot + n / sqroot)
        print('Iteration {0}: {1}'.format(k, sqroot))
    return sqroot


def main():
    n = 16
    print('Find squared root of {}'.format(n))
    square_root(16, steps=20)

    n = 17
    print('Find squared root of {}'.format(n))
    square_root(17, steps=20)


if __name__ == '__main__':
    main()
