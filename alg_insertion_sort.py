from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def insertion_sort(nums):
    """Insertion sort algortihm.

    Time complexity: O(n^2).
    Space complexity: O(1).
    """
    # Starting at pos i >= 1, swap (num[j-1], num[j]), for j=i,i-1,...,1,
    # if order is not correct. 
    for i in range(1, len(nums)):
        for j in range(i, -1, -1):
            if j > 0 and nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]


def main():
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(nums)
    print(nums)


if __name__ == '__main__':
    main()
