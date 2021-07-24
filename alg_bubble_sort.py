from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def bubble_sort(nums):
    """Bubble sort algortihm.

    The list is sorted in place.

    Time complexity: O(n^2).
    Space complexity: O(1).
    """
    # Swap pairs, if not sorted, to put max numbers at pos n-1,...,1.
    for i in reversed(range(1, len(nums))):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def bubble_sort_early_stop(nums):
    """Bubble Sort algorithm with early stop.

    The list is sorted in place.

    Time complexity: O(n^2).
    Space complexity: O(1).
    """
    # Use is_sorted for early stop.
    is_sorted = False

    # Next max position.
    i_max = len(nums) - 1
    
    while not is_sorted and i_max > 0:
        is_sorted = True

        # Scan nums before next max pos, swap num pair if order is not correct.
        for i in range(i_max):
            if nums[i] > nums[i + 1]:
                is_sorted = False
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        # Decrement to get next max position.
        i_max -= 1


def main():
    import time
    import random

    nums = range(10)
    random.shuffle(nums)

    start_time = time.time()
    print('By bubble sort: ')
    bubble_sort(nums)
    print(nums)
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By bubble sort with early stop: ')
    bubble_sort_early_stop(nums)
    print(nums)
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
