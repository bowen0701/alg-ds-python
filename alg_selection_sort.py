from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def selection_sort(nums):
    """Selection Sort algortihm.

    Time complexity: O(n^2).
    Space complexity: O(1).
    """
    # Start from the last num, iteratively select next max num to swap them.  
    for i in reversed(range(len(nums))):
        max_i = 0
        for j in range(1, i + 1):
            # Update max pos max_i to get max num in loop i.
            if nums[j] > nums[max_i]:
                max_i = j

        nums[max_i], nums[i] = nums[i], nums[max_i]


def main():
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('By selection sort: ')
    selection_sort(nums)
    print(nums)


if __name__ == '__main__':
    main()
