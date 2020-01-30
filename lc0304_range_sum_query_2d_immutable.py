"""Leetcode 304. Range Sum Query 2D - Immutable
Medium

URL: https://leetcode.com/problems/range-sum-query-2d-immutable/

Given a 2D matrix matrix, find the sum of the elements inside the rectangle
defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by
(row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:
- You may assume that the matrix does not change.
- There are many calls to sumRegion function.
- You may assume that row1 <= row2 and col1 <= col2.

Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(row1,col1,row2,col2)
"""

class NumMatrixBruteForce(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int

        Time complexity: O((row2-row1+1)*(col2-col1+1)).
        Space complexity: O(1).
        """
        if not self.matrix or not self.matrix[0]:
            return 0

        sum_region = 0

        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                sum_region += self.matrix[r][c]

        return sum_region


class NumMatrixDP(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]

        Time complexity: O(m*n), where
          - m: number of rows.
          - n: number of columns.
        Space complexity: O(m*n).
        """
        self.matrix = matrix

        nrows = len(matrix)
        if nrows > 0:
            ncols = len(matrix[0])
        else:
            ncols = 0

        # Create T for memoization of region sum from (0, 0) to (r, c).
        T = [[0] * (ncols + 1) for _ in range(nrows + 1)]

        # Compute top-left range sum: left + up + entry - overlap.
        for r in range(1, nrows + 1):
            for c in range(1, ncols + 1):
                T[r][c] = (T[r - 1][c] + T[r][c - 1]
                           + matrix[r - 1][c - 1]
                           - T[r - 1][c - 1])

        self.T = T

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int

        Time complexity: O(1).
        Space complexity: O(m*n).
        """
        if not self.matrix or not self.matrix[0]:
            return 0

        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        # Compute sum region based on top-left range sum. 
        return (self.T[row2][col2]
                - self.T[row1 - 1][col2] - self.T[row2][col1 - 1]
                + self.T[row1 - 1][col1 - 1])


def main():
    import time

    # Edge cases.
    # matrix = []
    # matrix = [[]]

    matrix = [
               [3, 0, 1, 4, 2],
               [5, 6, 3, 2, 1],
               [1, 2, 0, 1, 5],
               [4, 1, 0, 1, 7],
               [1, 0, 3, 0, 5]
             ]

    print 'By naive:'
    start_time = time.time()
    num_matrix = NumMatrixBruteForce(matrix)

    # sumRegion(2, 1, 4, 3) -> 8
    print num_matrix.sumRegion(2, 1, 4, 3)

    # sumRegion(1, 1, 2, 2) -> 11
    print num_matrix.sumRegion(1, 1, 2, 2)

    # sumRegion(1, 2, 2, 4) -> 12
    print num_matrix.sumRegion(1, 2, 2, 4)
    print 'Time:', time.time() - start_time

    print 'By DP:'
    start_time = time.time()
    num_matrix = NumMatrixDP(matrix)

    # sumRegion(2, 1, 4, 3) -> 8
    print num_matrix.sumRegion(2, 1, 4, 3)

    # sumRegion(1, 1, 2, 2) -> 11
    print num_matrix.sumRegion(1, 1, 2, 2)

    # sumRegion(1, 2, 2, 4) -> 12
    print num_matrix.sumRegion(1, 2, 2, 4)
    print 'Time:', time.time() - start_time


if __name__ == '__main__':
    main()
