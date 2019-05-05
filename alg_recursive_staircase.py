"""Recursive Staircase.

How many paths up a stair of say 100 steps if the child jumps 1, 2 or 3 steps?

F(n) = F(n - 1) + F(n - 2) + F(n -3)
- F(0) = 1  # Stay put.
- F(1) = 1  # Take 1-step leap.
- F(2) = 2  # Take 2 1-step leaps or 1 2-step leap.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def staircase_recur(steps):
    """Staircase by recursion.

    Time complexity: O(3^n).
    Space complexity: O(n).
    """
    if steps < 0:
        return 0

    if steps == 0:
        return 1

    return (staircase_recur(steps - 1) + 
            staircase_recur(steps - 2) + 
            staircase_recur(steps - 3))


def main():
    import time

    steps = 10

    start_time = time.time()
    print('Recursion: {}'.format(staircase_recur(steps)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
