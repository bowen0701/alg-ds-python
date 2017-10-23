from __future__ import print_function

def binary_search(a_list, item):
    """Binary search for ordered list."""
    first = 0
    last = len(a_list) - 1
    found_bool = False

    while first <= last and not found_bool:
        mid_point = (first + last) // 2
        if a_list[mid_point] == item:
            found_bool = True
        else:
            if item < a_list[mid_point]:
                last = mid_point - 1
            else:
                first = mid_point + 1

    return found_bool

def binary_search_recur(a_list, item):
    """Binary search for ordered list by recursion."""
    if len(a_list) == 0:
        return False
    else:
        mid_point = len(a_list) // 2
        if a_list[mid_point] == item:
            return True
        else:
            if item < a_list[mid_point]:
                return binary_search_recur(a_list[:mid_point], item)
            else:
                return binary_search_recur(a_list[(mid_point+1):], item)


def main():
    import time

    start_time = time.time()
    a_list = [54, 26, 93, 17,77, 31, 44, 55, 20, 65]
    print('a_list: {}'.format(a_list))
    # Sort the list.
    a_list = sorted(a_list)
    print('Sorted a_list: {}'.format(a_list))
    print('Time for sorted(): {}'
          .format(time.time() - start_time))   

    start_time = time.time()
    item = None
    print('Search item {0}: {1}'
          .format(item, binary_search(a_list, item)))
    item = 93
    print('Search item {0}: {1}'
          .format(item, binary_search(a_list, item)))
    print('Time for binary_search(): {}'
          .format(time.time() - start_time))

    start_time = time.time()
    item = None
    print('Search item {0}: {1}'
          .format(item, binary_search_recur(a_list, item)))
    item = 93
    print('Search item {0}: {1}'
          .format(item, binary_search_recur(a_list, item)))
    print('Time for binary_search_recur(): {}'
          .format(time.time() - start_time))


if __name__ == '__main__':
    main()
