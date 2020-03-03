"""
Find a peak in 2D array.

Support a is an array of length (m, n).
If a is an array of length (1, 1), a[0][0] is a peak.
In general, a[i][j] is a peak iff 
  a[i][j] >= a[i][j - 1] and a[i][j] >= a[i][j + 1] and
  a[i][j] >= a[i + 1][j] and a[i][j] >= a[i - 1][j] 
Similarly for corner cases, a[i][j], i = 0 or m - 1, or j = 0 or n -1.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def _max_1d(arr):
    """Find max in 1D array.

    Time complexity: O(m).
    Space complexity: O(1).
    """
    max_col = 0
    max_item = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_item:
            max_col = i
            max_item = arr[i]
    return max_col, max_item


def peak_2d(arr, start_row, end_row):
    """Find peak in 2D array (nxm) by divide & conquer algorithm.

    Procedure:
    - Find max element in mid row to get max column.
    - Find peak in max column.

    Time complexity: O(m*log(n)).
    Space complexity: O(1).
    """
    if end_row - start_row == 0:
        # For last one row, find the max item.
        _, max_item = _max_1d(arr)
        return max_item
    else:
        mid_row = start_row + (end_row - start_row) // 2
        max_col, _ = _max_1d(arr[mid_row])
        if arr[mid_row - 1][max_col] > arr[mid_row][max_col]:
            # Binary search the upper half.
            return peak_2d(arr, start_row, mid_row - 1)
        elif arr[mid_row + 1][max_col] > arr[mid_row][max_col]:
            # Binary search the bottom half.
            return peak_2d(arr, mid_row + 1, end_row)
        else:
            # Find 2D peak.
            return arr[mid_row][max_col]


def main():
    # 2D array with peak 21 at pos (2, 3).
    arr = [[10, 8, 10, 10, 7], 
           [14, 13, 12, 11, 9], 
           [15, 9, 11, 21, 20], 
           [16, 17, 19, 20, 18]]

    start_row, end_row = 0, len(arr) - 1
    print('Peak: {}'.format(peak_2d(arr, start_row, end_row)))


if __name__ == '__main__':
    main()
