from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def binary_search_recur(sorted_nums, target):
    """Binary search for sorted list by recursion.

    Time complexity: O(logn).
    Space complexity: O(max(n, logn))=O(n).
    """
    if len(sorted_nums) == 0:
        return False
    else:
        mid = len(sorted_nums) // 2

        if sorted_nums[mid] == target:
            return True
        elif sorted_nums[mid] < target:
            return binary_search_recur(sorted_nums[(mid + 1):], target)
        else:
            return binary_search_recur(sorted_nums[:mid], target)


def binary_search_two_pointers_recur(sorted_nums, target, left, right):
    """Binary search for sorted list by recursion w/ two pointer method.

    Note: It performs faster than binary_search_recur().
    
    Time complexity: O(logn).
    Space complexity: O(logn).
    """
    if left > right:
        return False

    mid = left + (right - left) // 2

    if sorted_nums[mid] == target:
        return True
    elif sorted_nums[mid] < target:
        return binary_search_two_pointers_recur(
            sorted_nums, target, mid + 1, right)
    else:
        return binary_search_two_pointers_recur(
            sorted_nums, target, left, mid - 1)


def binary_search_iter(sorted_nums, target):
    """Binary search for sorted list by iteration.

    Time complexity: O(logn).
    Space complexity: O(1).
    """
    left, right = 0, len(sorted_nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if sorted_nums[mid] == target:
            return True
        elif sorted_nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Final check for left = right.
    if sorted_nums[left] == target:
        return True
    else:
        return False


def main():
    import time

    sorted_nums = range(10000)

    # Ans: True
    target = 9999

    start_time = time.time()
    start_time = time.time()
    print('By recursion: {}'.format(binary_search_recur(sorted_nums, target)))
    print('Time: {}'.format(time.time() - start_time))
    start_time = time.time()
    print('By fast recursion: {}'.format(
          binary_search_two_pointers_recur(sorted_nums, target, 0, len(sorted_nums) - 1)))
    print('Time: {}'.format(time.time() - start_time))
    print('By iteration: {}'.format(binary_search_iter(sorted_nums, target)))
    print('Time: {}'.format(time.time() - start_time))

    # Ans: False
    target = -1

    start_time = time.time()
    print('By recursion: {}'.format(binary_search_recur(sorted_nums, target)))
    print('Time: {}'.format(time.time() - start_time))
    start_time = time.time()
    print('By fast recursion: {}'.format(
          binary_search_two_pointers_recur(sorted_nums, target, 0, len(sorted_nums) - 1)))
    print('Time: {}'.format(time.time() - start_time))
    print('By iteration: {}'.format(binary_search_iter(sorted_nums, target)))
    print('Time: {}'.format(time.time() - start_time))
    start_time = time.time()


if __name__ == '__main__':
    main()
