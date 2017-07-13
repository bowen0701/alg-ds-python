from __future__ import print_function

def sequential_search(a_list, item):
    """Sequential search."""
    pos = 0
    found_flag = False
    while pos < len(a_list) and not found_flag:
        if a_list[pos] == item:
            found_flag = True
        else:
            pos += 1
    return found_flag


def ordered_sequential_search(a_list, item):
    """Ordered sequential search."""
    a_list = sorted(a_list)
    pos = 0
    found_flag = False
    stop_flag = False
    while pos < len(a_list) and not found_flag and not stop_flag:
        if a_list[pos] == item:
            found_flag = True
        else:
            if a_list[pos] > item:
                stop_flag = True
            else:
                pos += 1
    return found_flag


def main():
    import time
    a_list = [54, 26, 93, 17,77, 31, 44, 55, 20, 65]
    print('a_list: {}'.format(a_list))

    start_time = time.time()
    item = 65
    print('Search item {0}: {1}'
          .format(item, sequential_search(a_list, item)))
    item = 100
    print('Search item {0}: {1}'
          .format(item, sequential_search(a_list, item)))
    print('Time for 2 sequential sorts: {}'
          .format(time.time() - start_time))

    start_time = time.time()
    item = 65
    print('Search item {0}: {1}'
          .format(item, ordered_sequential_search(a_list, item)))
    item = 100
    print('Search item {0}: {1}'
          .format(item, ordered_sequential_search(a_list, item)))
    print('Time for 2 sequential sorts: {}'
          .format(time.time() - start_time))

if __name__ == '__main__':
    main()
