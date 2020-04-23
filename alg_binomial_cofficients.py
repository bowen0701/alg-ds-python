"""Binomial cofficients

Binomial coefficient of m chooses k:
C(m, k) = m!/[(m - k)! * k!]
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def binomial_cofficient(m, k):
    """Binomial coefficien of m taking k.

    Note there is a recursion relationship for binomial coefficients:
    C(m, k) = C(m - 1, k - 1) + C(m - 1, k)
    which represents C(m, k) is the sum of selecting and not selecting m.

    Apply bottom-up dynamic programming.

    Time complexity: O(m*k).
    Space complexity: O(m*k).
    """
    # Base cases: C(m, k) with m < k.
    if m < k:
        return 0

    # Base cases: C(m, 0) or C(m, m).
    if k == 0 or m == k:
        return 1

    # Apply DP with table T[m+1][m+1] to memoize previous results.
    T = [[0] * (k + 1) for _ in range(m + 1)]

    # Initialize T[i][0] = 1.
    for i in range(m + 1):
        T[i][0] = 1

    # Initialize T[i][i] = 1 for i < k+1, since min(m+1, k+1) = k+1. 
    for i in range(k + 1):
        T[i][i] = 1

    # Compute T[i][j] for i > j >= 1 for selecting and not selecting m.
    for i in range(1, m + 1):
        for j in range(1, min(i, k + 1)):
            T[i][j] = T[i - 1][j - 1] + T[i - 1][j]

    return T[-1][-1]


def main():
    # Output: 0.
    m, k = 5, 0
    print(binomial_cofficient(m, k))

    # Output: 5.
    m, k = 5, 4
    print(binomial_cofficient(m, k))

    # Output: 5.
    m, k = 5, 1
    print(binomial_cofficient(m, k))

    # Output: 10.
    m, k = 5, 2
    print(binomial_cofficient(m, k))

    # Output: 10.
    m, k = 5, 3
    print(binomial_cofficient(m, k))


if __name__ == '__main__':
    main()
