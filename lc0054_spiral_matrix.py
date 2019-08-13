"""Leetcode 54. Spiral Matrix
Medium

URL: https://leetcode.com/problems/spiral-matrix/

Given a matrix of m x n elements (m rows, n columns), 
return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        Time complexity: O(m*n), where m is n_rows and n is n_cols.
        Space complexity: O(m*n).
        """
        if not matrix or not matrix[0]:
            return []

        spiral = []
        n_rows, n_cols = len(matrix), len(matrix[0])
        up, down, left, right = 0, n_rows - 1, 0, n_cols - 1

        while left < right and up < down:
            # Add elements from top's left to right.
            spiral.extend([matrix[up][j] for j in range(left, right)])
            # Add elements from right's up to down.
            spiral.extend([matrix[i][right] for i in range(up, down)])
            # Add elements from down's right to left.
            spiral.extend([matrix[down][j] for j in range(right, left, -1)])
            # Add elements from left's down to up.
            spiral.extend([matrix[i][left] for i in range(down, up, -1)])

            # Decrement up, down, left and down.
            up, down, left, right = up + 1, down - 1, left + 1, right - 1


        if left == right:
            # When n_rows > n_cols, left = right.
            spiral.extend([matrix[i][right] for i in range(up, down + 1)])
        elif up == down:
            # When n_rows < n_cols, up = down.
            spiral.extend([matrix[down][j] for j in range(left, right + 1)])

        return spiral


def main():
    # Should be: [1,2,3,6,9,8,7,4,5].
    matrix = [
      [ 1, 2, 3 ],
      [ 4, 5, 6 ],
      [ 7, 8, 9 ]
    ]
    print Solution().spiralOrder(matrix)

    # Should be: [1,2,3,4,8,12,11,10,9,5,6,7].
    matrix = [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]
    print Solution().spiralOrder(matrix)


if __name__ == '__main__':
    main()
