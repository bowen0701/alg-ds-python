from __future__ import print_function
from __future__ import division


def _gap_insertion_sort(a_list, start, gap):
    pass


def shell_sort(a_list):
    """Shell Sort algortihm."""
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_pos in range(sublist_count):
            _gap_insertion_sort(a_list, start_pos, sublist_count)
        print('After increments of size {0}, a_list is {1}'
              .format(sublist_count, a_list))


def main():
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('a_list: \n{}'.format(a_list))
    print('By Shell Sort: ')
    shell_sort(a_list)
    print(a_list)


if __name__ == '__main__':
    main()
