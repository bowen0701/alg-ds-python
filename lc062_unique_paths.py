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
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


class SolutionDp(object):
    """Unique paths by Dynamic Programming."

    Time complexity: O(mn).
    Space complexity: O(mn).
    """
    def uniquePaths(self, m, n):
        path = [[0] * n for _ in range(m)]

        for j in range(n):
            path[0][j] = 1

        for i in range(m):
            path[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                path[i][j] = path[i - 1][j] + path[i][j - 1]

        return path[-1][-1]


class SolutionDp2(object):
    """Unique paths by extended Dynamic Programming."

    Time complexity: O(mn).
    Space complexity: O(m).
    """
    def uniquePaths(self, m, n):
        path = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                path[j] += path[j - 1]

        return path[-1]


def main():
    import time

    start_time = time.time()
    print SolutionRecur().uniquePaths(3, 2)
    print 'Recursion: {}'.format(time.time() - start_time)
    
    start_time = time.time()
    print SolutionDp().uniquePaths(3, 2)
    print 'By DP: {}'.format(time.time() - start_time)

    start_time = time.time()
    print SolutionDp2().uniquePaths(3, 2)
    print 'By DP 2: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
