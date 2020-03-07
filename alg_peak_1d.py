"""
Find a peak position in 1D array.

Support nums is an array of length n.
In general, nums[k] is a peak iff 
nums[k] > nums[k - 1] and nums[k] > nums[k + 1].
If nums[0] > nums[1], then nums[0] is a peak.
If nums[n - 2] < nums[n - 1], then nums[n - 1] is a peak.  
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def peak_1d_brute_force(nums):
    """Find peak by naive iteration.

    Time complexity: O(n).
    Space complexity: O(1).
    """
    # Iterate to check element is greater than its neighbors.
    for i in range(len(nums)):
        if ((i == 0 or nums[i] >= nums[i - 1]) and 
            (i == len(nums) - 1 or nums[i] >= nums[i + 1])):
            return i


def _binary_search_recur(nums, left, right):
    """Helper function for peak_1d_binary_search_recur()."""
    if left == right:
        return left
        
    mid = left + (right - left) // 2

    if nums[mid] < nums[mid + 1]:
        # If mid < its right, search right part.
        return _binary_search_recur(nums, mid + 1, right)
    elif nums[mid] < nums[mid - 1]:
        # If mid < its left, search left part.
        return _binary_search_recur(nums, left, mid - 1)
    else:
        # Else, found peak.
        return mid


def peak_1d_binary_search_recur(nums):
    """Find peak by recursive binary search algorithm.

    Time complexity: O(logn).
    Space complexity: O(1).
    """
    return _binary_search_recur(nums, 0, len(nums) - 1)


def peak_1d_binary_search_iter(nums):
    """Find peak by iterative binary search algorithm.

    Time complexity: O(logn).
    Space complexity: O(1).
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            # If mid < its right, search right part.
            left = mid + 1
        elif nums[mid] < nums[mid - 1]:
            # If mid < its left, search left part.
            right = mid - 1
        else:
            # Else, found peak.
            return mid

    # For left = right.
    return left


def main():
    import time
    import numpy as np

    # nums of length 5 with peak 4 at 3.
    nums = [0, 1, 2, 4, 3]
    print('nums', nums)
    
    start_time = time.time()
    print('By brute force: {}'.format(peak_1d_brute_force(nums)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By recur binary search: {}'
          .format(peak_1d_binary_search_recur(nums)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By iter binary search: {}'
          .format(peak_1d_binary_search_iter(nums)))
    print('Time: {}'.format(time.time() - start_time))

    np.random.seed(71)
    nums = np.random.permutation(10)
    print('nums', nums)

    start_time = time.time()
    print('By brute force: {}'.format(peak_1d_brute_force(nums)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By recur binary search: {}'
          .format(peak_1d_binary_search_recur(nums)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By iter binary search: {}'
          .format(peak_1d_binary_search_iter(nums)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
