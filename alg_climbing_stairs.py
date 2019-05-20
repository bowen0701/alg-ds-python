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


def climbing_stairs_recur(steps):
    """Staircase by top-down recursion.

    Time complexity: O(3^n).
    Space complexity: O(n).
    """
    if steps < 0:
        return 0

    if steps == 0:
        return 1

    return (climbing_stairs_recur(steps - 1) + 
            climbing_stairs_recur(steps - 2) + 
            climbing_stairs_recur(steps - 3))


def _climbing_stairs_memo(steps, M):
    if steps < 0:
        return 0

    if steps == 0:
        return 1

    if M[steps]:
        return M[steps]

    M[steps] = (_climbing_stairs_memo(steps - 1, M) +
                _climbing_stairs_memo(steps - 2, M) + 
                _climbing_stairs_memo(steps - 3, M))
    return M[steps]


def climbing_stairs_memo(steps):
    """Staircase by top-down memoization.

    Time complexity: O(n).
    Space complexity: O(n).
    """
    M = [0] * (steps + 1)
    return _climbing_stairs_memo(steps, M)


def climbing_stairs_dp(steps):
    """Staircase by bottom-up dynamic programming.

    Time complexity: O(n).
    Space complexity: O(n).
    """
    M = [0] * (steps + 1)
    M[0] = 1
    M[1] = 1
    M[2] = 2
    
    for s in range(3, steps + 1):
        M[s] = M[s - 1] + M[s - 2] + M[s - 3]
    return M[steps]


def climbing_stairs_iter(steps):
    """Staircase by bottom-up iteration w/ optimized space.

    Time complexity: O(n).
    Space complexity: O(1).
    """
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
    print('Recur: {}'.format(climbing_stairs_recur(steps)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('Memo: {}'.format(climbing_stairs_memo(steps)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('DP: {}'.format(climbing_stairs_dp(steps)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('Iter: {}'.format(climbing_stairs_iter(steps)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
