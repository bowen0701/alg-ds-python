from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def quicksort_lc(nums):
    """Quick sort algortihm by recursion with list comprehension.

    Procedure:
      - Pick a pivot which ideally is a median pf the list.
      - Arrange half elements which are smaller than pivot to left,
        and the other half ones that are bigger than pivot to right.
      - Then to each half, recursively apply quick sort.

    Time complexity: O(n*logn).
    Space complexity: O(n).
    """
    # Base case.
    if len(nums) <= 1:
        return nums

    # Use middle num as pivot to collect small, middle & large numbers.
    pivot = nums[len(nums) // 2]
    smalls = [x for x in nums if x < pivot]
    middles = [x for x in nums if x == pivot]
    larges = [x for x in nums if x > pivot]

    # Concat small, middle & large numbers.
    return quicksort_lc(smalls) + middles + quicksort_lc(larges)


def _partition(nums, left, right):
    """Util for quicksort() to rearrange nums in place."""
    # Use right number as pivot.
    right_num = nums[right]

    # Rearrange numbers w.r.t. pivot: 
    # - For left <= k <= i: nums[k] <= pivot,
    # - For i+1 <= k <= j-1: nums[k] > pivot,
    # - For k = right: nums[k] = pivot.
    i = left - 1
    for j in range(left, right):
        if nums[j] <= right_num:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    # Swap num[i+1] and pivot, to rearrange to correct order.
    nums[i + 1], nums[right] = nums[right], nums[i + 1]
    return i + 1


def _quicksort_recur(nums, left, right):
    """Util for quicksort() by recursion."""
    if left < right:
        mid = _partition(nums, left, right)
        _quicksort_recur(nums, left, mid - 1)
        _quicksort_recur(nums, mid + 1, right)


def quicksort_ip(nums):
    """Quick sort algortihm with recursion.

    Time complexity: O(n*logn).
    Space complexity: O(1).
    """
    # Base case.
    if len(nums) <= 1:
        return nums

    _quicksort_recur(nums, 0, len(nums) - 1)
    return nums


def main():
    import time
    import random

    nums = range(100)
    random.shuffle(nums)
    start_time = time.time()
    print(quicksort_lc(nums))
    print('Time for quick sort by list comprehension: {}'
          .format(time.time() - start_time))

    nums = range(100)
    random.shuffle(nums)
    start_time = time.time()
    print(quicksort_ip(nums))
    print('Time for quick sort in place: {}'
          .format(time.time() - start_time))


if __name__ == '__main__':
    main()
