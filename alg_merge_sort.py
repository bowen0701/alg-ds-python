from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _merge_sorted_lists_recur(nums1, nums2):
    """Merge two sorted lists by recusion."""
    if not nums1 or not nums2:
        return nums1 or nums2

    # Merge two lists one element by one element.
    if nums1[0] <= nums2[0]:
        return [nums1[0]] + _merge_sorted_lists_recur(nums1[1:], nums2)
    else:
        return [nums2[0]] + _merge_sorted_lists_recur(nums1, nums2[1:])


def merge_sort_recur(nums):
    """Merge sort algorithm by divide and conquer.

    Merge sorted list by recursion.

    Time complexity: O(n*logn).
    Space complexity: O(n).
    """
    if len(nums) == 1:
        return nums
    
    # Sort the 1st & 2nd halves respectively and merge them.
    mid = len(nums) // 2
    nums1 = merge_sort_recur(nums[:mid])
    nums2 = merge_sort_recur(nums[mid:])
    return _merge_sorted_lists_recur(nums1, nums2)


def _merge_sorted_lists_iter(nums1, nums2):
    """Merge two sorted lists by iteration."""
    # Apply two pointer method.
    i, j = 0, 0
    result = []

    for _ in range(len(nums1) + len(nums2)):
        if i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1      
        elif i < len(nums1) and j >= len(nums2):
            result.extend(nums1[i:])
            break
        elif i >= len(nums1) and j < len(nums2):
            result.extend(nums2[j:])
            break

    return result


def merge_sort_iter(nums):
    """Merge sort algorithm by divide and conquer.

    Merge sorted list by iteration with two pointers.

    Time complexity: O(n*logn).
    Space complexity: O(n).
    """
    if len(nums) == 1:
        return nums
    
    # Sort the 1st & 2nd halves respectively and merge them.
    mid = len(nums) // 2
    nums1 = merge_sort_iter(nums[:mid])
    nums2 = merge_sort_iter(nums[mid:])
    return _merge_sorted_lists_iter(nums1, nums2)


def main():
    import time
    import random

    nums = range(100)
    random.shuffle(nums)

    start_time = time.time()
    print('By recur: {}'.format(merge_sort_recur(nums)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By iter: {}'.format(merge_sort_iter(nums)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
