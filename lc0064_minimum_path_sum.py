"""Leetcode 64. Minimum Path Sum
Medium

URL: https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1->3->1->1->1 minimizes the sum.
"""

class SolutionRecur(object):
    def _pathSum(self, grid, r, c):
        # Check if top-left entry.
        if r == 0 and c == 0:
            return grid[r][c]

        # Check if the 1st row or 1st col.
        if r == 0:
            return grid[r][c] + self._pathSum(grid, r, c - 1)
        if c == 0:
            return grid[r][c] + self._pathSum(grid, r - 1, c)

        # Return entry + min(up, left).
        return grid[r][c] + min(self._pathSum(grid, r - 1, c), 
                                self._pathSum(grid, r, c - 1))

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        Time complexity: O(2^(m+n)).
          - m is the length of rows.
          - n is the lenght of cols.
        Space complexity: O(m*n).
        """
        # Apply top-down DP by recursion.
        r, c = len(grid) - 1, len(grid[0]) - 1
        return self._pathSum(grid, r, c)


class SolutionMemo(object):
    def _pathSum(self, grid, r, c, T):
        # Check if top-left entry.
        if r == 0 and c == 0:
            return grid[r][c]

        if T[r][c]:
            return T[r][c]

        if r == 0:
            # Check if the 1st row.
            T[r][c] = grid[r][c] + self._pathSum(grid, r, c - 1, T)
        elif c == 0:
            # Check if the 1st col.
            T[r][c] = grid[r][c] + self._pathSum(grid, r - 1, c, T)
        else:
            # Return entry + min(up, left).
            T[r][c] = grid[r][c] + min(self._pathSum(grid, r - 1, c, T), 
                                       self._pathSum(grid, r, c - 1, T))
        return T[r][c]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        Time complexity: O(m*n).
          - m is the number of rows.
          - n is the number of cols.
        Space complexity: O(m*n).
        """
        # Apply top-down DP by recursion with memoization.
        n_rows, n_cols = len(grid), len(grid[0])
        T = [[0] * n_cols for _ in range(n_rows)]
        return self._pathSum(grid, n_rows - 1, n_cols - 1, T)


class SolutionDP(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        Time complexity: O(m*n),
          - m is the number of rows.
          - n is the number of cols.
        Space complexity: O(m*n).
        """
        # Apply bottom-up DP.
        if not grid or not grid[0]:
            return 0

        # Use table T to memorize intermediate results.
        n_rows, n_cols = len(grid), len(grid[0])
        T = [[0] * n_cols for _ in range(n_rows)]

        # Update T's top-left and 1st row & col entries.
        T[0][0] = grid[0][0]
        for r in range(1, n_rows):
            T[r][0] = grid[r][0] + T[r - 1][0]
        for c in range(1, n_cols):
            T[0][c] = grid[0][c] + T[0][c - 1]

        # Update T's middle entries by grid + min(up, left).
        for r in range(1, n_rows):
            for c in range(1, n_cols):
                    T[r][c] += grid[r][c] + min(T[r][c - 1], T[r - 1][c])

        return T[-1][-1]


class SolutionDPUpdate(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        Time complexity: O(m*n),
          - m is the number of rows.
          - n is the number of cols.
        Space complexity: O(1).
        """
        # Apply bottom-up DP.
        if not grid or not grid[0]:
            return 0

        n_rows, n_cols = len(grid), len(grid[0])
        for r in range(n_rows):
            for c in range(n_cols):
                # Update grid entry by itself + min(up, left).
                if r == 0 and c == 0:
                    continue
                elif r == 0 and c > 0:
                    grid[r][c] += grid[r][c - 1]
                elif r > 0 and c == 0:
                    grid[r][c] += grid[r - 1][c]
                else:
                    grid[r][c] += min(grid[r][c - 1], grid[r - 1][c])

        return grid[-1][-1]


def main():
    # Output: 7
    grid = [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    print SolutionRecur().minPathSum(grid)
    print SolutionMemo().minPathSum(grid)
    print SolutionDP().minPathSum(grid)
    print SolutionDPUpdate().minPathSum(grid)


if __name__ == '__main__':
    main()
