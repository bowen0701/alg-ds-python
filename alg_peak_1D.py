from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""
Find a peak in 1D array.

Support a is an array of length n.
If a is an array of length 1, a[0] is a peak.
In general, a[k] is a peak iff a[k] > a[k - 1] and a[k] > a[k + 1].
If a[0] > a[1], then a[0] is a peak.
If a[n - 1] > a[n - 2], then a[n - 1] is a peak.  
"""

def peak_1d_iter(arr):
    """Find peak by naive iteration.

    Time complexity: O(n).
    Space complexity: O(1).
    """
    for i in range(len(arr)):
        if ((i == 0 or arr[i - 1] < arr[i]) and 
            (i == len(arr) - 1 or arr[i] > arr[i + 1])):
            return arr[i]


def peak_1d_binary_search_iter(arr):
    """Find peak by iterative binary search algorithm.

    Time complexity: O(logn).
    Space complexity: O(1).
    """
    first, last = 0, len(arr) - 1

    while first < last:
        mid = first + (last - first) // 2

        if arr[mid - 1] > arr[mid]:
            last = mid - 1
        elif arr[mid] < arr[mid + 1]:
            first = mid + 1
        else:
            return arr[mid]

    return arr[first]


def _binary_search_recur_helper(arr, start, end):
    """Helper function for peak_1d_binary_search_recur()."""
    if end - start == 0:
        return arr[start]
    else:
        mid = start + (end - start) // 2
        if arr[mid - 1] > arr[mid]:
            return _binary_search_recur_helper(arr, start, mid - 1)
        elif arr[mid] < arr[mid + 1]:
            return _binary_search_recur(arr, mid + 1, end)
        else:
            return arr[mid]


def peak_1d_binary_search_recur(arr):
    """Find peak by recursive binary search algorithm.

    Time complexity: O(logn).
    Space complexity: O(1).
    """
    return _binary_search_recur_helper(arr, 0, len(arr) - 1)


def main():
    import time
    import numpy as np

    # Array of length 5 with peak 4.
    arr = [0, 1, 4, 3, 2]
    
    start_time = time.time()
    print('By peak_1d_iter(): {}'.format(peak_1d_iter(arr)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By peak_1d_binary_search_iter(): {}'
          .format(peak_1d_binary_search_iter(arr)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By peak_1d_binary_search_recur(): {}'
          .format(peak_1d_binary_search_recur(arr)))
    print('Time: {}'.format(time.time() - start_time))

    np.random.seed(71)
    arr = np.random.permutation(1000000)

    start_time = time.time()
    print('By peak_1d_iter(): {}'.format(peak_1d_iter(arr)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By peak_1d_binary_search_iter(): {}'
          .format(peak_1d_binary_search_iter(arr)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By peak_1d_binary_search_recur(): {}'
          .format(peak_1d_binary_search_recur(arr)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
