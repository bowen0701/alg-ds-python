from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def insertion_sort(nums):
    """Insertion Sort algortihm.

    Time complexity: O(n^2).
    Space complexity: O(1).

    Although its complexity is bigger than the ones with O(n*logn), 
    one advantage is the sorting happens in place.
    """
    gen = ((i, val) for i, val in enumerate(nums) if i > 0)
    for (i, val) in gen:
        j = i
        while j > 0 and nums[j - 1] > val:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = val


def main():
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(nums)
    print(nums)


if __name__ == '__main__':
    main()
