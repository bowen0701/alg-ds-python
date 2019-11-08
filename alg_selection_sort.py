from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def selection_sort(nums):
    """Selection Sort algortihm.

    Time complexity: O(n^2).
    Space complexity: O(1).
    """
    # Start from the last position reversely: len(nums) - 1, ..., 0.
    for i in reversed(range(len(nums))):
        # Select "next" max element, and swap it and ith element.
        m = 0
        for j in range(1, i + 1):
            if nums[j] > nums[m]:
                m = j
        nums[m], nums[i] = nums[i], nums[m]


def main():
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('List: {}'.format(nums))
    print('By selection sort: ')
    selection_sort(nums)
    print(nums)


if __name__ == '__main__':
    main()
