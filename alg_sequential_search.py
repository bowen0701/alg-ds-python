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
    pass


def main():
    a_list = [54, 26, 93, 17,77, 31, 44, 55, 20, 65]
    print('a_list: {}'.format(a_list))
    item = 65
    print('Search item {0}: {1}'
          .format(item, sequential_search(a_list, item)))
    item = 100
    print('Search item {0}: {1}'
          .format(item, sequential_search(a_list, item)))


if __name__ == '__main__':
    main()
