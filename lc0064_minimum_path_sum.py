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

class SolutionDpUpdate(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        Time complexity: O(m*n),
          - m is the length of rows.
          - n is the lenght of cols.
        Space complexity: O(1).
        """
        # Base case.
        if not grid:
            return 0

        # Apply DP to get min path sum of every entry.
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
    print SolutionDpUpdate().minPathSum(grid)


if __name__ == '__main__':
    main()
