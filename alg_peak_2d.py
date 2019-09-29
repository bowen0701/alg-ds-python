from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools

"""
Find a peak in 2D array.

Support a is an array of length (m, n).
If a is an array of length (1, 1), a[0][0] is a peak.
In general, a[i][j] is a peak iff 
  a[i][j] >= a[i][j - 1] and a[i][j] >= a[i][j + 1] and
  a[i][j] >= a[i + 1][j] and a[i][j] >= a[i - 1][j] 
Similarly for corner cases, a[i][j], i = 0 or m - 1, or j = 0 or n -1.
"""

def peak_2d_iter(arr):
    """Find peak in 2D array (nxm) by iterative algorithm.

    Time complexity: O(n*m).
    Space complexity: O(1).
    """
    nrow, ncol = len(arr), len(arr[0])

    for (i, j) in itertools.product(range(nrow), range(ncol)):
        if (i, j) == (0, 0):
            # Upper left.
            if (arr[i][j] >= arr[i][j + 1] and 
                arr[i][j] >= arr[i + 1][j]):
                return arr[i][j]
        elif (i, j) == (0, ncol - 1):
            # Upper right.
            if (arr[i][j] >= arr[i][j - 1] and 
                arr[i][j] >= arr[i + 1][j]):
                return arr[i][j]
        elif (i, j) == (nrow - 1, 0):
            # Lower left.
            if (arr[i][j] >= arr[i][j + 1] and 
                arr[i][j] >= arr[i - 1][j]):
                return arr[i][j]
        elif (i, j) == (nrow - 1, ncol - 1):
            # Lower right.
            if (arr[i][j] >= arr[i][j - 1] and 
                arr[i][j] >= arr[i - 1][j]):
                return arr[i][j]
        elif i == 0 and 0 < j < ncol - 1:
            # On the 0th row.
            if (arr[i][j] >= arr[i][j - 1] and 
                arr[i][j] >= arr[i][j + 1] and
                arr[i][j] >= arr[i + 1][j]):
                return arr[i][j]
        elif i == nrow - 1 and 0 < j < ncol - 1:
            # On the last row.
            if (arr[i][j] >= arr[i][j - 1] and 
                arr[i][j] >= arr[i][j + 1] and
                arr[i][j] >= arr[i - 1][j]):
                return arr[i][j]
        elif 0 < i < nrow - 1 and j == 0:
            # On the 0th col.
            if (arr[i][j] >= arr[i][j + 1] and
                arr[i][j] >= arr[i - 1][j] and
                arr[i][j] >= arr[i + 1][j]):
                return arr[i][j]
        elif 0 < i < nrow - 1 and j == ncol - 1:
            # On the last col.
            if (arr[i][j] >= arr[i][j - 1] and 
                arr[i][j] >= arr[i - 1][j] and
                arr[i][j] >= arr[i + 1][j]):
                return arr[i][j]
        else:
            # Other center entries.
            if (arr[i][j] >= arr[i][j - 1] and 
                arr[i][j] >= arr[i][j + 1] and
                arr[i][j] >= arr[i - 1][j] and
                arr[i][j] >= arr[i + 1][j]):
                return arr[i][j]


def _max_1d(arr):
    """Find max in 1D array.

    Time complexity: O(m).
    Space complexity: O(1).
    """
    max_id = 0
    max_item = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_item:
            max_id = i
            max_item = arr[i]
    return max_id, max_item


def peak_2d(arr, start_row, end_row):
    """Find peak in 2D array (nxm) by divide & conquer algorithm.

    Procedure:
    - Find max element in mid row to get max column.
    - Find peak in max column.

    Time complexity: O(m*log(n)).
    Space complexity: O(1).
    """
    if end_row - start_row == 0:
        _, max_item = _max_1d(arr)
        return max_item
    else:
        mid_row = start_row + (end_row - start_row) // 2
        max_col, _ = _max_1d(arr[mid_row])
        if arr[mid_row][max_col] < arr[mid_row - 1][max_col]:
            return peak_2d(arr, start_row, mid_row - 1)
        elif arr[mid_row][max_col] < arr[mid_row + 1][max_col]:
            return peak_2d(arr, mid_row + 1, end_row)
        else:
            return arr[mid_row][max_col]


def main():
    import time

    # 2D array with peak 21.
    arr = [[10, 8, 10, 10, 7], 
           [14, 13, 12, 11, 9], 
           [15, 9, 11, 21, 22], 
           [16, 17, 19, 20, 18]]

    start_time = time.time()
    print('Peak: {}'.format(peak_2d_iter(arr)))
    print('Time for peak_2D_iter(): {}'.format(time.time() - start_time))

    start_time = time.time()
    start_row, end_row = 0, len(arr) - 1
    print('Peak: {}'.format(peak_2d(arr, start_row, end_row)))
    print('Time for peak_2D(): {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
