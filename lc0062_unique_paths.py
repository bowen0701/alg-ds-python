"""Leetcode 62. Unique Paths.
Medium

URL: https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid 
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid
(marked 'Finish' in the diagram below).

How many possible unique paths are there?

Input: m = 3, n = 2
Output: 3
"""

from typing import List

class SolutionRecur(object):
    """Unique paths by Recursion.

    Time complexity: O(2^(m*n)).
    Space complexity: O(m*n).
    """
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        # Recursively trace paths from up and left.
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


class SolutionMemo(object):
    """Unique paths by top-down dynamic programming w/ memoization.

    Time complexity: O(m*n).
    Space complexity: O(m*n).
    """  
    def _uniquePathsRecur(self, m: int, n: int, T: List[List[int]]):
        # Base cases: set the 1st row/col to 1.
        if m == 0 or n == 0:
            return 1

        if T[m][n]:
            return T[m][n]

        # For other rows/cols, backtrack from up and left.
        T[m][n] = (self._uniquePathsRecur(m - 1, n, T) + 
                   self._uniquePathsRecur(m, n - 1, T))
        return T[m][n]

    def uniquePaths(self, m: int, n: int) -> int:
        # Use T for memoization.
        T = [[0] * n for _ in range(m)]
        return self._uniquePathsRecur(m - 1, n - 1, T)


class SolutionDP(object):
    """Unique paths by bottom-up dynamic programming.

    Time complexity: O(m*n).
    Space complexity: O(m*n).
    """
    def uniquePaths(self, m: int, n: int) -> int:
        # Use T for memoization.
        T = [[0] * n for _ in range(m)]

        # Set the 1st row/col to 1.
        for c in range(n):
            T[0][c] = 1
        for r in range(m):
            T[r][0] = 1

        # For other rows/cols, trace from up and lefts.
        for r in range(1, m):
            for c in range(1, n):
                T[r][c] = T[r - 1][c] + T[r][c - 1]

        return T[-1][-1]


class SolutionDP2(object):
    """Unique paths by dynamic programming w/ optimized space."

    Time complexity: O(m*n).
    Space complexity: O(n).
    """
    def uniquePaths(self, m: int, n: int) -> int:
        # Scan row by row to get unique paths.
        T = [1] * n
        for r in range(1, m):
            for c in range(1, n):
                T[c] += T[c - 1]
        return T[-1]


def main():
    import time

    # Output: 3.
    m, n = 3, 2

    start_time = time.time()
    print('By Recur:', SolutionRecur().uniquePaths(m, n))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By Memo:', SolutionMemo().uniquePaths(m, n))
    print('Time: {}'.format(time.time() - start_time))
    
    start_time = time.time()
    print('By DP:', SolutionDP().uniquePaths(m, n))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP2:', SolutionDP2().uniquePaths(m, n))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
