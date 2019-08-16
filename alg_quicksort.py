from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def quicksort(nums):
    """Quick sort algortihm by recursion with list comprehension.

    Procedure:
      - Pick a pivot which ideally is a median pf the list.
      - Arrange half elements which are smaller than pivot to left,
        and the other half ones that are bigger than pivot to right.
      - Then to each half, revursively apply quicksort().
    
    Time complexity: O(n*logn).
    Space complexity: O(n).
    """
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]

    small_nums = [x for x in nums if x < pivot]
    mid_nums = [x for x in nums if x == pivot]
    large_nums = [x for x in nums if x > pivot]

    return quicksort(small_nums) + mid_nums + quicksort(large_nums)


def _partition(nums, left, right, mid):
    """Helper function for quicksort_raw() to get partition point."""
    pivot = nums[mid]

    while left <= right:
        while nums[left] < pivot:
            # Find left element which is bigger than pivot.
            left += 1

        while nums[right] > pivot:
            # Find right element which is smaller than pivot.
            right -= 1

        if left <= right:
            # If "bigger" left element is on left side of "smaller" right,
            # swap the two elements, and then keep moving.
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
            right -= 1

    return left


def _quicksort_recur(nums, left, right):
    """Helper function for quicksort_raw() by recursion."""
    if left < right:
        mid = left + (right - left) // 2
        partition = _partition(nums, left, right, mid)
        _quicksort_recur(nums, left, partition - 1)
        _quicksort_recur(nums, partition + 1, right)


def quicksort_raw(nums):
    """Raw quick sort algortihm with recursion.

    Time complexity: O(n*logn).
    Space complexity: O(n).
    """
    _quicksort_recur(nums, 0, len(nums) - 1)
    return nums


def main():
    import time
    import random

    # nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    nums = range(100)
    random.shuffle(nums)

    start_time = time.time()
    print(quicksort(nums))
    print('Time for quick sort by recursion: {}'
          .format(time.time() - start_time))

    start_time = time.time()
    print(quicksort_raw(nums))
    print('Time for quick sort by "raw" recursion: {}'
          .format(time.time() - start_time))


if __name__ == '__main__':
    main()
