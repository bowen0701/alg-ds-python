"""Leetcode 74. Search a 2D Matrix.
Medium

URL: https://leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""

from typing import List


class SolutionRowSearch(object):
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Time complexity: O(mn), where m is the row number, and n is column number.
        Space complexity: O(1).
        """
        if not matrix or not matrix[0]:
            return False

        n_rows, n_cols = len(matrix), len(matrix[0])

        # Search the last number of each row j, j = 0, 1,...
        for r in range(n_rows):
            if target <= matrix[r][-1]:
                # Search numbers in the jth row, which is the only possible place.
                for c in range(n_cols - 1, -1, -1):
                    if target == matrix[r][c]:
                        return True
                    elif target > matrix[r][c]:
                        # If target is bigger than the element, early stop.
                        return False
                return False
            else:
                continue

        return False


class SolutionBinarySearch(object):
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Time complexity: O(log(mn)).
        Space complexity: O(1).
        """
        if not matrix or not matrix[0]:
            return False

        # Perform binary search in 2D matrix.
        n_rows, n_cols = len(matrix), len(matrix[0])
        left, right = 0, n_rows * n_cols - 1

        while left < right:
            mid = left + (right - left) // 2
            i, j = mid // n_cols, mid % n_cols

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid + 1
            elif matrix[i][j] > target:
                right = mid - 1

        # Finally check left = right case.
        i, j = left // n_cols, left % n_cols
        if matrix[i][j] == target:
            return True
        else:
            return False


def main():
    import time

    # Output: true
    # Input:
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3

    start_time = time.time()
    print(SolutionRowSearch().searchMatrix(matrix, target))
    print('Time for row search:', time.time() - start_time)

    start_time = time.time()
    print(SolutionBinarySearch().searchMatrix(matrix, target))
    print('Time for binary search:', time.time() - start_time)


    # Output: false
    # Input:
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 13

    start_time = time.time()
    print(SolutionRowSearch().searchMatrix(matrix, target))
    print('Time for row search:', time.time() - start_time)

    start_time = time.time()
    print(SolutionBinarySearch().searchMatrix(matrix, target))
    print('Time for binary search:', time.time() - start_time)


if __name__ == '__main__':
    main()
