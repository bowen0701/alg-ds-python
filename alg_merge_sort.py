from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def merge_sorted_lists_recur(left, right):
    """Merge two sorted lists by recusions."""
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    if left[0] <= right[0]:
        return [left[0]] + merge_sorted_lists_recur(left[1:], right)
    else:
        return [right[0]] + merge_sorted_lists_recur(left, right[1:])


def merge_sorted_lists_iter(left, right):
    """Merge two sorted lists by iteration."""
    # Apply two pointer method.
    i, j = 0, 0

    merged = []

    for _ in range(len(left) + len(right)):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1      
        elif i < len(left) and j >= len(right):
            merged.extend(left[i:])
            break
        elif i >= len(left) and j < len(right):
            merged.extend(right[j:])
            break

    return merged


def merge_sort(arr, merge):
    """Merge sort algorithm by divide and conquer.

    Time complexity: O(n*logn).
    Space complexity: O(n).
    """
    if len(arr) == 1:
        return arr
    
    # Sort the 1st & 2nd halves respectively and merge them.
    mid = len(arr) // 2

    left = merge_sort(arr[:mid], merge)
    right = merge_sort(arr[mid:], merge)
    return merge(left, right)


def main():
    import time
    import random

    arr = range(100)
    random.shuffle(arr)

    start_time = time.time()
    print('By recur: {}'.format(merge_sort(arr, merge_sorted_lists_recur)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By iter: {}'.format(merge_sort(arr, merge_sorted_lists_iter)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
