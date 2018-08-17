from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""Find a peak in 1D array."""

def find_peak_naive(arr):
    """Find peak by naive iteration.

    Time complexity: O(n).
    """
    for i in range(len(arr)):
        if i == 0:
            if arr[i] >= arr[i + 1]:
                return arr[i]
        elif i == (len(arr) - 1):
            if arr[i] >= arr[i - 1]:
                return arr[i]
        else:
            if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
                return arr[i]


def find_peak(arr):
    """Find peak by divide-end-conquer algorithm.

    Time complexity: O(logn).
    """
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        if arr[mid] <= arr[mid - 1]:
            return find_peak(arr[:mid-1])
        elif arr[mid] <= arr[mid + 1]:
            return find_peak(arr[mid+1:])
        else:
            return arr[mid]


def main():
    import time

    # Array with peak 4.
    arr = [0, 1, 4, 3, 2]
    print('Array: {}'.format(arr))
    
    # Find peak by naive version.
    time_start = time.time()
    peak = find_peak_naive(arr)
    time_run = time.time() - time_start
    print('Peak: {}'.format(peak))
    print('Time for find_peak_naive(): {}'.format(time_run))

    # Find peak by divide-end-conquer algorithm.
    time_start = time.time()
    peak = find_peak(arr)
    time_run = time.time() - time_start
    print('Peak: {}'.format(peak))
    print('Time for find_peak_naive(): {}'.format(time_run))


if __name__ == '__main__':
    main()
