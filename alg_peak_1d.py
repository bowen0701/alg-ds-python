"""
Find a peak position in 1D array.

Support a is an array of length n.
If a is an array of length 1, a[0] is a peak.
In general, a[k] is a peak iff a[k] > a[k - 1] and a[k] > a[k + 1].
If a[0] > a[1], then a[0] is a peak.
If a[n - 1] > a[n - 2], then a[n - 1] is a peak.  
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def peak_1d_iter(arr):
    """Find peak by naive iteration.

    Time complexity: O(n).
    Space complexity: O(1).
    """
    # Iterate to check element is greater than its left & right neighbors.
    for i in range(len(arr)):
        if ((i == 0 or arr[i - 1] <= arr[i]) and 
            (i == len(arr) - 1 or arr[i] >= arr[i + 1])):
            return i


def _binary_search_recur_helper(arr, left, right):
    """Helper function for peak_1d_binary_search_recur()."""
    if right - left == 0:
        return left
    else:
        mid = (left + right + 1) // 2

        if arr[mid - 1] > arr[mid]:
            # If mid's left > mid, search left part.
            return _binary_search_recur_helper(arr, left, mid - 1)
        else:
            # Otherwise, search right part.
            return _binary_search_recur_helper(arr, mid, right)


def peak_1d_binary_search_recur(arr):
    """Find peak by recursive binary search algorithm.

    Time complexity: O(logn).
    Space complexity: O(1).
    """
    return _binary_search_recur_helper(arr, 0, len(arr) - 1)


def peak_1d_binary_search_iter(arr):
    """Find peak by iterative binary search algorithm.

    Time complexity: O(logn).
    Space complexity: O(1).
    """
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right + 1) // 2

        if arr[mid - 1] > arr[mid]:
            # If mid's left > mid, search left part.
            right = mid - 1
        else:
            # Otherwise, search right part.
            left = mid

    # For left = right.
    return left


def main():
    import time
    import numpy as np

    # Array of length 5 with peak at 3.
    arr = [0, 1, 2, 4, 3]
    print('arr', arr)
    
    start_time = time.time()
    print('By peak_1d_iter(): {}'.format(peak_1d_iter(arr)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By peak_1d_binary_search_recur(): {}'
          .format(peak_1d_binary_search_recur(arr)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By peak_1d_binary_search_iter(): {}'
          .format(peak_1d_binary_search_iter(arr)))
    print('Time: {}'.format(time.time() - start_time))

    np.random.seed(71)
    arr = np.random.permutation(10)
    print('arr', arr)

    start_time = time.time()
    print('By peak_1d_iter(): {}'.format(peak_1d_iter(arr)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By peak_1d_binary_search_recur(): {}'
          .format(peak_1d_binary_search_recur(arr)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By peak_1d_binary_search_iter(): {}'
          .format(peak_1d_binary_search_iter(arr)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
