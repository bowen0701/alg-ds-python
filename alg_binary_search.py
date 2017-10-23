from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def binary_search(a_list, item):
    """Binary search for ordered list."""
    first = 0
    last = len(a_list) - 1
    found_bool = False

    while first <= last and not found_bool:
        mid = (first + last) // 2
        if a_list[mid] == item:
            found_bool = True
        else:
            if item < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found_bool


def binary_search_recur(a_list, item):
    """Binary search for ordered list by recursion."""
    if len(a_list) == 0:
        return False
    else:
        mid = len(a_list) // 2
        if a_list[mid] == item:
            return True
        else:
            if item < a_list[mid]:
                return binary_search_recur(a_list[:mid], item)
            else:
                return binary_search_recur(a_list[(mid + 1):], item)


def binary_search_recur_fast(a_list, item, first, last):
    """Binary search for ordered list by recursion w/o slice.

    This binary_search_recur_fast() performs faster than 
    binary_search_recur().
    """
    if last - first < 2:
        return a_list[first] == item or a_list[last] == item
    else:
        mid = first + (last - first) // 2
        if a_list[mid] == item:
            return True
        else:
            if item < a_list[mid]:
                return binary_search_recur_fast(a_list, item, first, mid - 1)
            else:
                return binary_search_recur_fast(a_list, item, mid + 1, last)


def main():
    import time

    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]
    print('a_list: {}'.format(a_list))

    # Sort the list.
    start_time = time.time()
    a_list = sorted(a_list)
    print('Sorted a_list: {}'.format(a_list))
    print('Time for sorted(): {}'
          .format(time.time() - start_time))   

    # Binary search by binary_search().
    start_time = time.time()
    item = None
    print('Search item {0}: {1}'
          .format(item, binary_search(a_list, item)))
    item = 93
    print('Search item {0}: {1}'
          .format(item, binary_search(a_list, item)))
    print('Time for binary_search(): {}'
          .format(time.time() - start_time))

    # Binary search by binary_search_recur().
    start_time = time.time()
    item = None
    print('Search item {0}: {1}'
          .format(item, binary_search_recur(a_list, item)))
    item = 93
    print('Search item {0}: {1}'
          .format(item, binary_search_recur(a_list, item)))
    print('Time for binary_search_recur(): {}'
          .format(time.time() - start_time))

    # Binary search by binary_search_recur_fast().
    start_time = time.time()
    item = None
    print('Search item {0}: {1}'
          .format(item, binary_search_recur_fast(a_list, item, 0, len(a_list) - 1)))
    item = 93
    print('Search item {0}: {1}'
          .format(item, binary_search_recur_fast(a_list, item, 0, len(a_list) - 1)))
    print('Time for binary_search_recur(): {}'
          .format(time.time() - start_time))

if __name__ == '__main__':
    main()
