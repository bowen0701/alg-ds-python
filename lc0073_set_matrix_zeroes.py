"""Leetcode 73. Set Matrix Zeroes
Medium

URL: https://leetcode.com/problems/set-matrix-zeroes/

Given a m x n matrix, if an element is 0, set its entire row and column to 0. 
Do it in-place.

Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:
- A straight forward solution using O(mn) space is probably a bad idea.
- A simple improvement uses O(m + n) space, but still not the best solution.
- Could you devise a constant space solution?
"""

class SolutionCopy(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.

        Time complexity: O(m*n*(m+n))).
        Space complexity: O(m*n).
        """
        m, n = len(matrix), len(matrix[0])

        # Copy matrix to a new matrix.
        copy = [[matrix[i][j] for j in range(n)] for i in range(m)]
        
        # Update its row and col by checking matrix[i][j] == 0.
        for i in range(m):
            for j in range(n):
                if copy[i][j] == 0:
                    for r in range(m):
                        matrix[r][j] = 0
                    for c in range(n):
                        matrix[i][c] = 0


class SolutionZeroRowsCols(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.

        Time complexity: O(m*n).
        Space complexity: O(m+n).
        """
        m, n = len(matrix), len(matrix[0])

        # Use zero_rows and zero_cols to collect 0's positions.
        zero_rows = [0] * m
        zero_cols = [0] * n
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows[i] = 1
                    zero_cols[j] = 1

        # Update matrix rows and cols based on zero_rows and zero_cols.
        for r in range(len(zero_rows)):
            if zero_rows[r] == 1:
                for j in range(n):
                    matrix[r][j] = 0

        for c in range(len(zero_cols)):
            if zero_cols[c] == 1:
                for i in range(m):
                    matrix[i][c] = 0


class SolutionOptimSpace(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.

        Time complexity: O(m*n).
        Space complexity: O(1).
        """
        m, n = len(matrix), len(matrix[0])

        # Record any zeros are in the first row/col. 
        is_zero_row0, is_zero_col0 = False, False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        is_zero_row0 = True
                    if j == 0:
                        is_zero_col0 = True

                    # Use 1st element in the row/col to record zero.
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # For each element which is not in the 1st row/col, 
        # update it to zero by checking its 1st row/col elements. 
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0

        # For 1st row/col, update to zero if needed.
        if is_zero_row0:
            for j in range(n):
                matrix[0][j] = 0
        if is_zero_col0:
            for i in range(m):
                matrix[i][0] = 0


def main():
    matrix = [
               [1,1,1],
               [1,0,1],
               [1,1,1]
             ]
    # SolutionCopy().setZeroes(matrix)
    SolutionZeroRowsCols().setZeroes(matrix)
    # SolutionOptimSpace().setZeroes(matrix)
    print matrix


    matrix = [
               [0,1,2,0],
               [3,4,5,2],
               [1,3,1,5]
             ]
    # SolutionCopy().setZeroes(matrix)
    SolutionZeroRowsCols().setZeroes(matrix)
    # SolutionOptimSpace().setZeroes(matrix)
    print matrix


if __name__ == '__main__':
    main()
