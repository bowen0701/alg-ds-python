"""Climbing Stairs.

How many paths up a stair of say 100 steps if the child jumps 1, 2 or 3 steps?

F(n) = F(n - 1) + F(n - 2) + F(n - 3)
- F(0) = 1  # Stay put.
- F(1) = 1  # Take 1-step leap.
- F(2) = 2  # Take 2 1-step leaps or 1 2-step leap.

Remark: This is just like a variant of Fibonacci series.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def climbing_stairs_three_recur(steps):
    """Staircase by top-down recursion.

    Time complexity: O(3^n).
    Space complexity: O(n).
    """
    if steps < 0:
        return 0

    if steps == 0:
        return 1

    return (climbing_stairs_three_recur(steps - 1) + 
            climbing_stairs_three_recur(steps - 2) + 
            climbing_stairs_three_recur(steps - 3))


def _climbing_stairs_three_memo(steps, T):
    if steps < 0:
        return 0

    if steps == 0:
        return 1

    if T[steps]:
        return T[steps]

    T[steps] = (_climbing_stairs_three_memo(steps - 1, T) +
                _climbing_stairs_three_memo(steps - 2, T) + 
                _climbing_stairs_three_memo(steps - 3, T))
    return T[steps]


def climbing_stairs_three_memo(steps):
    """Staircase by top-down memoization.

    Time complexity: O(n).
    Space complexity: O(n).
    """
    T = [0] * (steps + 1)
    return _climbing_stairs_three_memo(steps, T)


def climbing_stairs_three_dp(steps):
    """Staircase by bottom-up dynamic programming.

    Time complexity: O(n).
    Space complexity: O(n).
    """
    T = [0] * (steps + 1)
    T[0] = 1
    T[1] = 1
    T[2] = 2
    
    for s in range(3, steps + 1):
        M[s] = M[s - 1] + M[s - 2] + M[s - 3]
    return M[steps]


def climbing_stairs_three_iter(steps):
    """Staircase by bottom-up iteration w/ optimized space.

    Time complexity: O(n).
    Space complexity: O(1).
    """
    if steps <= 1:
        return 1
    if steps == 2:
        return 2

    # Track the last three staircase results.
    a, b, c = 1, 1, 2

    # Iterate through the remaining steps 3 ~ end.
    for s in range(3, steps + 1):
        # Add three numbers and then shift position by one.
        a, b, c = b, c, a + b + c
    return c


def main():
    import time

    steps = 20

    start_time = time.time()
    print('Recur: {}'.format(climbing_stairs_three_recur(steps)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('Memo: {}'.format(climbing_stairs_three_memo(steps)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('DP: {}'.format(climbing_stairs_three_dp(steps)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('Iter: {}'.format(climbing_stairs_three_iter(steps)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
