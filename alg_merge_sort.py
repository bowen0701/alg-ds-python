from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _merge_sorted_lists_recur(arr1, arr2):
    """Merge two sorted lists by recusion."""
    if not arr1 or not arr2:
        return arr1 or arr2

    # Merge two lists one element by one element.
    if arr1[0] <= arr2[0]:
        return [arr1[0]] + _merge_sorted_lists_recur(arr1[1:], arr2)
    else:
        return [arr2[0]] + _merge_sorted_lists_recur(arr1, arr2[1:])


def _merge_sorted_lists_iter(arr1, arr2):
    """Merge two sorted lists by iteration."""
    # Apply two pointer method.
    i, j = 0, 0

    merged = []

    for _ in range(len(arr1) + len(arr2)):
        if i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1      
        elif i < len(arr1) and j >= len(arr2):
            merged.extend(arr1[i:])
            break
        elif i >= len(arr1) and j < len(arr2):
            merged.extend(arr2[j:])
            break

    return merged


def merge_sort(arr, merge):
    """Merge sort algorithm by divide and conquer.

    Two merge sorted list methods:
    - Merge by recursion.
    - Merge by iteration with two pointers.

    Time complexity: O(n*logn).
    Space complexity: O(n).
    """
    if len(arr) == 1:
        return arr
    
    # Sort the 1st & 2nd halves respectively and merge them.
    mid = len(arr) // 2

    arr1 = merge_sort(arr[:mid], merge)
    arr2 = merge_sort(arr[mid:], merge)
    return merge(arr1, arr2)


def main():
    import time
    import random

    arr = range(100)
    random.shuffle(arr)

    start_time = time.time()
    print('By recur: {}'.format(merge_sort(arr, _merge_sorted_lists_recur)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By iter: {}'.format(merge_sort(arr, _merge_sorted_lists_iter)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
