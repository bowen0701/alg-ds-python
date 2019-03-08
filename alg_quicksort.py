from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def quicksort(a_list):
    """Quick sort algortihm by recursion with list comprehension.

    Procedure:
      - Pick a pivot which ideally is a median pf the list.
      - Arrange half elements which are smaller than pivot to left,
        and the other half ones that are bigger than pivot to right.
      - Then to each half, revursively apply quicksort().
    
    Time complexity: O(n*logn).
    Space complexity: O(n).
    """
    if len(a_list) <= 1:
        return a_list
    pivot_value = a_list[len(a_list) // 2]
    left_list = [x for x in a_list if x < pivot_value]
    middle_list = [x for x in a_list if x == pivot_value]
    right_list = [x for x in a_list if x > pivot_value]
    return quicksort(left_list) + middle_list + quicksort(right_list)


def _partition(a_list, left, right, pivot):
    """Get partition point for patition."""
    pivot_value = a_list[pivot]

    while left <= right:
        while a_list[left] < pivot_value:
            # Find left element which is bigger than pivot.
            left += 1

        while a_list[right] > pivot_value:
            # Find right element which is smaller than pivot.
            right -= 1

        if left <= right:
            # If "bigger" left element is on left side of "smaller" right,
            # swap the two elements, and then keep moving.
            a_list[right], a_list[left] = a_list[left], a_list[right]
            left += 1
            right -= 1

    return left


def _quicksort_recur(a_list, left, right):
    if left < right:
        pivot = left + (right - left) // 2
        partition = _partition(a_list, left, right, pivot)
        _quicksort_recur(a_list, left, partition - 1)
        _quicksort_recur(a_list, partition + 1, right)


def quicksort_raw(a_list):
    """Quick sort algortihm with raw recursion.

    Time complexity: O(n*logn).
    Space complexity: O(n).
    """
    _quicksort_recur(a_list, 0, len(a_list) - 1)
    return a_list


def main():
    import time
    import random

    # a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    a_list = range(100)
    random.shuffle(a_list)

    start_time = time.time()
    print(quicksort(a_list))
    print('Time for quick sort by recursion with list comprehension:: {}'
          .format(time.time() - start_time))

    start_time = time.time()
    print(quicksort_raw(a_list))
    print('Time for quick sort by raw recursion:: {}'
          .format(time.time() - start_time))


if __name__ == '__main__':
    main()
