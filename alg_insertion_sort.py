from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def insertion_sort(nums):
    """Insertion sort algortihm.

    It's an in-place sorting, without extra space needed.

    Time complexity: O(n^2).
    Space complexity: O(1).
    """
    # Starting from i>=1, 
    # swap (num[j-1], num[j]) if not sorted, for j=i,...,1.
    for i in range(1, len(nums)):
        for j in range(i, -1, -1):
            if j > 0 and nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
            else:
                break


def main():
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(nums)
    print(nums)


if __name__ == '__main__':
    main()
