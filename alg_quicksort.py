from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def quicksort(a_list):
    """Quick sort algortihm with list comprehension recursion.
    
    Time complexity: O(n*logn).
    """
    if len(a_list) <= 1:
        return a_list
    pivot_value = a_list[len(a_list) // 2]
    left_list = [x for x in a_list if x < pivot_value]
    middle_list = [x for x in a_list if x == pivot_value]
    right_list = [x for x in a_list if x > pivot_value]
    return quicksort(left_list) + middle_list + quicksort(right_list)


def _partition(a_list, first, last):
    """Get split point for patition."""
    pivot_value = a_list[first]
    
    left = first + 1
    right = last
    done_bool = False

    while not done_bool:
        while a_list[left] <= pivot_value and left <= right:
            left += 1

        while a_list[right] >= pivot_value and right >= left:
            right -= 1

        if right < left:
            done_bool = True
        else:
            a_list[right], a_list[left] = a_list[left], a_list[right]

    a_list[right], a_list[first] = a_list[first], a_list[right]

    return right


def _quicksort_recur(a_list, first, last):
    if first < last:
        split_point = _partition(a_list, first, last)
        _quicksort_recur(a_list, first, split_point - 1)
        _quicksort_recur(a_list, split_point + 1, last)


def quicksort_raw(a_list):
    """(Raw) Quick Sort algortihm with recursion."""
    _quicksort_recur(a_list, 0, len(a_list) - 1)
    return a_list


def main():
    import time

    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    start_time = time.time()
    print(quicksort(a_list))
    print('Run time of Quick Sort with list comprehension:: {}'
          .format(time.time() - start_time))

    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    start_time = time.time()
    print(quicksort_raw(a_list))
    print('Run time of Quick Sort with recursion:: {}'
          .format(time.time() - start_time))


if __name__ == '__main__':
    main()
