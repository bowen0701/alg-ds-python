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


def _max_1d(nums):
    """Find max in 1D array."""
    max_col = 0
    max_num = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max_num:
            max_col = i
            max_num = nums[i]
    return max_col, max_num


def _peak_2d_recur(nums, start_row, end_row):
    """Recursively find a peak in 2D array."""
    if end_row - start_row == 0:
        # For last one row, find the max item.
        max_col, max_num = _max_1d(nums)
        return max_num

    mid_row = start_row + (end_row - start_row) // 2

    max_col, max_num = _max_1d(nums[mid_row])

    if nums[mid_row][max_col] < nums[mid_row + 1][max_col]:
        # Binary search in bottom half.
        return _peak_2d_recur(nums, mid_row + 1, end_row)
    elif nums[mid_row][max_col] < nums[mid_row - 1][max_col]:
        # Binary search in upper half.
        return _peak_2d_recur(nums, start_row, mid_row - 1)
    else:
        # Found a 2D peak.
        return nums[mid_row][max_col]


def peak_2d(nums):
    """Find peak in 2D array (nxm) by divide & conquer algorithm.

    Procedure:
    - In mid row, find its max num and the corresponding column.
    - If max num < its bottom, find a peak in bottom subarray,
      if max num < its up, find a peak in upper subarray,
      else, found a peak.

    Time complexity: O(n*log(m)), where
      m: number of rows
      n: number of columns
    Space complexity: O(1).
    """
    start_row, end_row = 0, len(nums) - 1
    return _peak_2d_recur(nums, start_row, end_row)


def main():
    # 2D array with peak 21 at pos (2, 3).
    nums = [[10, 8, 10, 10, 7], 
            [14, 13, 12, 11, 9], 
            [15, 9, 11, 21, 20], 
            [16, 17, 19, 20, 18]]
    print(peak_2d(nums))


if __name__ == '__main__':
    main()
