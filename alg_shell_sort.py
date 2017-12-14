from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while (position >= gap) and (a_list[position - gap] > current_value):
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def shell_sort(a_list):
    """Shell Sort algortihm."""
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_pos in range(sublist_count):
            _gap_insertion_sort(a_list, start_pos, sublist_count)
        
        print('After increments of size {0}, a_list is \n{1}'
              .format(sublist_count, a_list))

        sublist_count = sublist_count // 2


def main():
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('a_list: \n{}'.format(a_list))
    print('By Shell Sort: ')
    shell_sort(a_list)


if __name__ == '__main__':
    main()
