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

class SolutionRowSearch(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        Time complexity: O(mn), where m is the row number, and n is column number.
        Space complexity: O(1).
        """
        if not matrix or not matrix[0]:
            return False

        n_rows, n_cols = len(matrix), len(matrix[0])

        # Search the last number of each row j, j = 0, 1,...
        for r in range(n_rows):
            if target == matrix[r][-1]:
                return True
            elif target < matrix[r][-1]:
                # If target is smaller than the last number of the jth row,
                # search numbers in the jth row, which is the only possible place.
                for c in range(n_cols - 2, -1, -1):
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
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        Time complexity: O(log(mn)).
        Space complexity: O(1).
        """
        if not matrix or not matrix[0]:
            return False

        # Perform binary search in 2D matrix.
        n_rows, n_cols = len(matrix), len(matrix[0])
        first, last = 0, n_rows * n_cols - 1
        found_bool = False

        while first <= last and not found_bool:
            mid = first + (last - first) // 2
            i, j = mid // n_cols, mid % n_cols
            if matrix[i][j] == target:
                found_bool = True
            elif matrix[i][j] < target:
                first = mid + 1
            elif matrix[i][j] > target:
                last = mid - 1

        return found_bool


def main():
    import time

    # Input:
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3
    # Output: true

    start_time = time.time()
    print SolutionRowSearch().searchMatrix(matrix, target)
    print 'Time for row search:', time.time() - start_time

    start_time = time.time()
    print SolutionBinarySearch().searchMatrix(matrix, target)
    print 'Time for binary search:', time.time() - start_time


    # Input:
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 13
    # Output: false

    start_time = time.time()
    print SolutionRowSearch().searchMatrix(matrix, target)
    print 'Time for row search:', time.time() - start_time

    start_time = time.time()
    print SolutionBinarySearch().searchMatrix(matrix, target)
    print 'Time for binary search:', time.time() - start_time


if __name__ == '__main__':
    main()
