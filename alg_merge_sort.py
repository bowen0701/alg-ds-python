from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _merge_sorted_lists_recur(sorted_nums1, sorted_nums2):
    """Helper method for merge_sort_recur().

    Merge two sorted lists by recusion.
    """
    if not sorted_nums1 or not sorted_nums2:
        return sorted_nums1 or sorted_nums2

    # Merge two lists one by one element.
    if sorted_nums1[0] <= sorted_nums2[0]:
        return ([sorted_nums1[0]] + 
                _merge_sorted_lists_recur(sorted_nums1[1:], sorted_nums2))
    else:
        return ([sorted_nums2[0]] + 
                _merge_sorted_lists_recur(sorted_nums1, sorted_nums2[1:]))


def merge_sort_recur(nums):
    """Merge sort algorithm by divide and conquer.

    Merge sorted list by recursion.

    Time complexity: O(n*logn).
    Space complexity: O(n).
    """
    if len(nums) <= 1:
        return nums
    
    # Sort the 1st & 2nd halves respectively and merge them.
    mid = len(nums) // 2
    sorted_nums1 = merge_sort_recur(nums[:mid])
    sorted_nums2 = merge_sort_recur(nums[mid:])
    return _merge_sorted_lists_recur(sorted_nums1, sorted_nums2)


def _merge_sorted_lists_iter(sorted_nums1, sorted_nums2):
    """Helper method for merge_sort_iter().

    Merge two sorted lists by iteration.
    """
    # Apply two pointer method.
    i, j = 0, 0
    result = []

    for _ in range(len(sorted_nums1) + len(sorted_nums2)):
        if i < len(sorted_nums1) and j < len(sorted_nums2):
            if sorted_nums1[i] <= sorted_nums2[j]:
                result.append(sorted_nums1[i])
                i += 1
            else:
                result.append(sorted_nums2[j])
                j += 1      
        elif i < len(sorted_nums1) and j >= len(sorted_nums2):
            result.extend(sorted_nums1[i:])
            break
        elif i >= len(sorted_nums1) and j < len(sorted_nums2):
            result.extend(sorted_nums2[j:])
            break

    return result


def merge_sort_iter(nums):
    """Merge sort algorithm by divide and conquer.

    Merge sorted list by iteration with two pointers.

    Time complexity: O(n*logn).
    Space complexity: O(n).
    """
    if len(nums) <= 1:
        return nums
    
    # Sort the 1st & 2nd halves respectively and merge them.
    mid = len(nums) // 2
    sorted_nums1 = merge_sort_iter(nums[:mid])
    sorted_nums2 = merge_sort_iter(nums[mid:])
    return _merge_sorted_lists_iter(sorted_nums1, sorted_nums2)


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
