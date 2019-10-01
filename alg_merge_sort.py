from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def merge_sorted_lists_recur(x, y):
    """Merge two sorted lists by recusions."""
    if len(x) == 0:
        return y
    if len(y) == 0:
        return x

    if x[0] <= y[0]:
        return [x[0]] + merge_sorted_lists_recur(x[1:], y)
    else:
        return [y[0]] + merge_sorted_lists_recur(x, y[1:])


def merge_sorted_lists_iter(x, y):
    """Merge two sorted lists by iteration."""
    # Apply two pointer method.
    x_pos, y_pos = 0, 0

    z = []

    for _ in range(len(x) + len(y)):
        if x_pos < len(x) and y_pos < len(y):
            if x[x_pos] <= y[y_pos]:
                z.append(x[x_pos])
                x_pos += 1
            else:
                z.append(y[y_pos])
                y_pos += 1      
        elif x_pos < len(x) and y_pos >= len(y):
            z.extend(x[x_pos:])
            break
        elif x_pos >= len(x) and y_pos < len(y):
            z.extend(y[y_pos:])
            break

    return z


def merge_sort(arr, merge):
    """Merge sort algorithm by divide and conquer with recursion.

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
    print(merge_sort(arr, merge_sorted_lists_recur))
    print('By recusion: {}'.format(time.time() - start_time))

    start_time = time.time()
    print(merge_sort(arr, merge_sorted_lists_iter))
    print('By iteration: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
