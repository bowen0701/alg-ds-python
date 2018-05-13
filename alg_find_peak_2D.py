from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools


def find_peak_naive(arr):
    """Find peak by naive algorithm.

    Time complexity: O(nm).
    """
    nrow = len(arr)
    ncol = len(arr)

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


def find_peak(arr):
    pass


def main():
    import time

    # 2D array with peak 21.
    arr = [[10, 8, 10, 10], 
           [14, 13, 12, 11], 
           [15, 9, 11, 21], 
           [16, 17, 19, 20]]

    time_start = time.time()
    peak = find_peak_naive(arr)
    time_run = time.time() - time_start
    print('Peak: {}'.format(peak))
    print('Time for naive alg: {}'.format(time_run))


if __name__ == '__main__':
    main()
