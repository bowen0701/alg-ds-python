"""Leetcode 221. Maximal Square
Medium

URL: https://leetcode.com/problems/maximal-square/

Given a 2D binary matrix filled with 0's and 1's, find the largest
square containing only 1's and return its area.

Example:
Input: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Output: 4
"""


class SolutionDPSquare(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int

        Time complexity: O(m*n), where
          - m: number of rows
          - n: number of cols
        Space complexity: O(m*n).
        """
        # Edge case.
        if not matrix or not matrix[0]:
            return 0

        # Create DP table T[i][j] as maximal square with bottom-right at (i, j).
        nrows, ncols = len(matrix), len(matrix[0])
        T = [[0] * (ncols + 1) for _ in range(nrows + 1)]

        # Update max size.
        size = 0

        for r in range(1, nrows + 1):
            for c in range(1, ncols + 1):
                if matrix[r - 1][c - 1] == '1':
                    # If (r, c) is 1, set as min(left, top-left, left) + 1.
                    T[r][c] = min(T[r - 1][c], T[r - 1][c - 1], T[r][c - 1]) + 1
                    size = max(size, T[r][c])
        return size * size


class SolutionDPTwoRows(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int

        Time complexity: O(m*n), where
          - m: number of rows
          - n: number of cols
        Space complexity: O(n).
        """
        # Edge case.
        if not matrix or not matrix[0]:
            return 0

        # Create DP table T[i][j] as maximal square with bottom-right at (i, j).
        nrows, ncols = len(matrix), len(matrix[0])
        pre_row = [0] * (ncols + 1)
        cur_row = [0] * (ncols + 1)

        # Update max size.
        size = 0

        for r in range(1, nrows + 1):
            for c in range(1, ncols + 1):
                if matrix[r - 1][c - 1] == '1':
                    # If (r, c) is 1, set as min(left, top-left, left) + 1.
                    cur_row[c] = min(pre_row[c], pre_row[c - 1], cur_row[c - 1]) + 1
                    size = max(size, cur_row[c])

            pre_row = cur_row
            cur_row = [0] * (ncols + 1)

        return size * size


def main():
    # Output: 4
    matrix = [
        ['1', '0', '1', '0', '0'],
        ['1', '0', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '0', '0', '1', '0']
    ]
    print SolutionDPSquare().maximalSquare(matrix)
    print SolutionDPTwoRows().maximalSquare(matrix)


if __name__ == '__main__':
    main()
