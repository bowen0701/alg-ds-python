from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def sequential_search(a_list, item):
    """Sequential search by iteration."""
    pos = 0
    found_bool = False
    while pos < len(a_list) and not found_bool:
        if a_list[pos] == item:
            found_bool = True
        else:
            pos += 1
    return found_bool


def sequential_search_ordered(a_list, item):
    """Sequential search by ordering first."""
    a_list = sorted(a_list)
    pos = 0
    found_bool = False
    stop_bool = False
    while pos < len(a_list) and not found_bool and not stop_bool:
        if a_list[pos] == item:
            found_bool = True
        else:
            if a_list[pos] > item:
                stop_bool = True
            else:
                pos += 1
    return found_bool


def main():
    import time
    a_list = [54, 26, 93, 17,77, 31, 44, 55, 20, 65]

    start_time = time.time()
    item = 65
    print('Search item {0}: {1}'
          .format(item, sequential_search(a_list, item)))
    item = 100
    print('Search item {0}: {1}'
          .format(item, sequential_search(a_list, item)))
    print('Time for sequential sorts: {}'
          .format(time.time() - start_time))

    start_time = time.time()
    item = 65
    print('Search item {0}: {1}'
          .format(item, sequential_search_ordered(a_list, item)))
    item = 100
    print('Search item {0}: {1}'
          .format(item, sequential_search_ordered(a_list, item)))
    print('Time for sequential sort ordered: {}'
          .format(time.time() - start_time))


if __name__ == '__main__':
    main()
