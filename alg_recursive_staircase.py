"""Recursive Staircase.

How many paths up a stair of say 100 steps if the child jumps 1, 2 or 3 steps?

F(n) = F(n - 1) + F(n - 2) + F(n - 3)
- F(0) = 1  # Stay put.
- F(1) = 1  # Take 1-step leap.
- F(2) = 2  # Take 2 1-step leaps or 1 2-step leap.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def staircase_recur(steps):
    """Staircase by top-down recursion.

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


def _staircase_memo(steps, M):
    if steps < 0:
        return 0

    if steps == 0:
        return 1

    if M[steps]:
        return M[steps]

    M[steps] = (_staircase_memo(steps - 1, M) +
                _staircase_memo(steps - 2, M) + 
                _staircase_memo(steps - 3, M))
    return M[steps]


def staircase_memo(steps):
    """Staircase by top-down memoization.

    Time complexity: O(n).
    Space complexity: O(n).
    """
    M = [0] * (steps + 1)
    return _staircase_memo(steps, M)


def main():
    import time

    steps = 20

    start_time = time.time()
    print('Recursion: {}'.format(staircase_recur(steps)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('Memo: {}'.format(staircase_memo(steps)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
