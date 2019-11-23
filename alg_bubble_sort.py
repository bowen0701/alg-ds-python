from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def bubble_sort(nums):
    """Bubble Sort algortihm.

    The list is sorted in place.

    Time complexity: O(n^2).
    Space complexity: O(1).
    """
    for end in reversed(range(len(nums))):
        # Scan nums[0]~nums[end-1], if nums[i] > nums[i+1], swap them.
        for i in range(end):
            if nums[i] > nums[i + 1]:
                nums[i + 1], nums[i] = nums[i], nums[i + 1] 


def bubble_sort_early_stop(nums):
    """Bubble Sort algorithm with early stop.

    The list is sorted in place.

    Time complexity: O(n^2).
    Space complexity: O(1).
    """
    # Use is_sorted for early stop.
    is_sorted = False
    end = len(nums) - 1
    
    while not is_sorted and end > 0:
        is_sorted = True

        # Scan nums[0]~nums[end-1], if nums[i] > nums[i+1], swap them.
        for i in range(end):
            if nums[i] > nums[i + 1]:
                is_sorted = False
                nums[i + 1], nums[i] = nums[i], nums[i + 1]
        end -= 1


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
