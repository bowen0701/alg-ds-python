from __future__ import print_function

def binary_search(a_list, item):
    """Binary search."""
    pass


def main():
    import time
    a_list = [54, 26, 93, 17,77, 31, 44, 55, 20, 65]
    print('a_list: {}'.format(a_list))

    start_time = time.time()
    item = None
    print('Search item {0}: {1}'
          .format(item, binary_search(a_list, item)))


if __name__ == '__main__':
    main()
