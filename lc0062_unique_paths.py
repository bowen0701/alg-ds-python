"""Leetcode 62. Unique Paths.
Medium

URL: https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid 
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Input: m = 3, n = 2
Output: 3
"""

class SolutionRecur(object):
    """Unique paths by Recursion."

    Time complexity: O(2^((m - 1) * (n - 1))).
    Space complexity: O(mn).
    """
    def uniquePaths(self, m, n):
        # Recursively backbrack paths from (m - 1, n) and (m, n - 1). 
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


class SolutionMemo(object):
    """Unique paths by top-down dynamic programming w/ memoization."

    Time complexity: O(mn.
    Space complexity: O(mn).
    """  
    def _uniquePathsHelper(self, m, n, path):
        if path[m][n]:
            return path[m][n]

        if m == 1 or n == 1:
            # Set the 1st row or col to 1.
            path[m][n] = 1
        else:
            # For other rows/cols, backtrack from (m - 1, n) and (m, n - 1).
            path[m][n] = (self._uniquePathsHelper(m - 1, n, path) + 
                          self._uniquePathsHelper(m, n - 1, path))

        return path[m][n]

    def uniquePaths(self, m, n):
        # Use path for memoization.
        path = [[0] * (n + 1) for _ in range(m + 1)]
        return self._uniquePathsHelper(m, n, path)


class SolutionDp(object):
    """Unique paths by Dynamic Programming."

    Time complexity: O(mn).
    Space complexity: O(mn).
    """
    def uniquePaths(self, m, n):
        # Use path for memoization.
        path = [[0] * n for _ in range(m)]

        # Set the 1st row to 1.
        for j in range(n):
            path[0][j] = 1

        # Set the 1st col to 1.
        for i in range(m):
            path[i][0] = 1

        # For other rows/cols, backtrack from (i - 1, j) and (i, j - 1).
        for i in range(1, m):
            for j in range(1, n):
                path[i][j] = path[i - 1][j] + path[i][j - 1]

        return path[-1][-1]


class SolutionDp2(object):
    """Unique paths by extended Dynamic Programming."

    Time complexity: O(mn).
    Space complexity: O(n).
    """
    def uniquePaths(self, m, n):
        path = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                path[j] += path[j - 1]

        return path[-1]


def main():
    import time

    m, n = 3, 2

    start_time = time.time()
    print 'By Recur:', SolutionRecur().uniquePaths(m, n)
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By Memo:', SolutionMemo().uniquePaths(m, n)
    print 'Time: {}'.format(time.time() - start_time)
    
    start_time = time.time()
    print 'By DP:', SolutionDp().uniquePaths(m, n)
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By DP2:', SolutionDp2().uniquePaths(m, n)
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
