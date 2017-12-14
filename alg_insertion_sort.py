from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def insertion_sort(a_list):
    """Insertion Sort algortihm."""
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position -= 1

        a_list[position] = current_value


def main():
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('a_list: \n{}'.format(a_list))
    print('By insertion sort: ')
    insertion_sort(a_list)
    print(a_list)


if __name__ == '__main__':
    main()
