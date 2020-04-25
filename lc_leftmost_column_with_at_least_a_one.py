"""Leetcode: Leftmost Column with at Least a One

URL: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3306/

(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of
the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index
(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix
using a BinaryMatrix interface:
- BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col)
  (0-indexed).
- BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which
  means the matrix is rows * cols.

Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong
Answer. Also, any solutions that attempt to circumvent the judge will result in
disqualification.

For custom testing purposes you're given the binary matrix mat as input in the
following four examples. You will not have access the binary matrix directly.

Example 1:
Input: mat = [[0,0],[1,1]]
Output: 0

Example 2:
Input: mat = [[0,0],[0,1]]
Output: 1

Example 3:
Input: mat = [[0,0],[0,0]]
Output: -1

Example 4:
Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
 
Constraints:
- rows == mat.length
- cols == mat[i].length
- 1 <= rows, cols <= 100
- mat[i][j] is either 0 or 1.
- mat[i] is sorted in a non-decreasing way.
"""


# BinaryMatrix's API interface.
class BinaryMatrix(object):
    def __init__(self, mat):
        self.mat = mat
        self.shape = [len(self.mat), len(self.mat[0])]

    def get(self, row, col):
        """
        :type row : int, col : int
        :rtype int
        """
        return self.mat[row][col]

    def dimensions(self):
        """
        :rtype list[]
        """
        return self.shape


class SolutionBinarySearchRows(object):
    def _binarySearchRow(self, row, binaryMatrix):
        nrows, ncols = binaryMatrix.dimensions()
        left_col, right_col = 0, ncols - 1
        while left_col < right_col:
            mid_col = left_col + (right_col - left_col) // 2
            mid_num = binaryMatrix.get(row, mid_col)
            if mid_num == 0:
                left_col = mid_col + 1
            else:
                right_col = mid_col

        if binaryMatrix.get(row, left_col) == 1:
            return left_col
        else:
            return float('inf')

    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int

        Time complexity: O(m*logn), where
          - m is the number of rows
          - n is the number of columns
        """
        # Edge case.
        nrows, ncols = binaryMatrix.dimensions()
        if binaryMatrix.dimensions == [1, 1]:
            if binaryMatrix.get(0, 0) == 1:
                return 0
            else:
                return -1

        # Apply binary search in row to update min col index.
        min_col = float('inf')
        for r in range(nrows):
            left_col_idx = self._binarySearchRow(r, binaryMatrix)
            min_col = min(min_col, left_col_idx)

        if min_col == float('inf'):
            return -1
        else:
            return min_col


def main():
    # Output: 0
    mat = [[0,0],[1,1]]
    binaryMatrix = BinaryMatrix(mat)
    print SolutionBinarySearchRows().leftMostColumnWithOne(binaryMatrix)

    # Output: 1
    mat = [[0,0],[0,1]]
    binaryMatrix = BinaryMatrix(mat)
    print SolutionBinarySearchRows().leftMostColumnWithOne(binaryMatrix)

    # Output: -1
    mat = [[0,0],[0,0]]
    binaryMatrix = BinaryMatrix(mat)
    print SolutionBinarySearchRows().leftMostColumnWithOne(binaryMatrix)

    # Output: 1
    mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
    binaryMatrix = BinaryMatrix(mat)
    print SolutionBinarySearchRows().leftMostColumnWithOne(binaryMatrix)

    # Output: 2
    mat = [[0,0,0,1],[0,0,1,1],[0,0,1,1]]
    binaryMatrix = BinaryMatrix(mat)
    print SolutionBinarySearchRows().leftMostColumnWithOne(binaryMatrix)


if __name__ == '__main__':
    main()
