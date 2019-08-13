"""Leetcode 240. Search a 2D Matrix II

URL: https://leetcode.com/problems/search-a-2d-matrix-ii/

Medium

Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:
- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

Example:
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.
Given target = 20, return false.
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        Time complexity: O(m+n), where 
          - m is the row number, and 
          - n is the column number.
        Space complexity: O(1).
        """
        if not len(matrix) or not len(matrix[0]):
            return False

        # Search starting from the bottom-left, moving to top/right.
        i, j = len(matrix) - 1, 0

        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                # If entry is bigger than target, decrease next entry.
                i -= 1
            elif matrix[i][j] < target:
                # If entry is smaller than target, increase next entry.
                j += 1

        return False


def main():
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    target = 5   # Should be True.
    print Solution().searchMatrix(matrix, target)

    target = 20  # Should be False.
    print Solution().searchMatrix(matrix, target)


if __name__ == '__main__':
    main()
