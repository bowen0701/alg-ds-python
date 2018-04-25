from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def bubble_sort(a_list):
    """Bubble Sort algortihm.

    Time complexity: O(n^2). 
    """
    for pass_num in reversed(range(len(a_list))):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                a_list[i + 1], a_list[i] = a_list[i], a_list[i + 1] 


def bubble_sort_short(a_list):
    """Bubble Short algorithm with early stop."""
    exchange_bool = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchange_bool:
        exchange_bool = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchange_bool = True
                a_list[i + 1], a_list[i] = a_list[i], a_list[i + 1]
        pass_num -= 1


def main():
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('a_list: {}'.format(a_list))
    
    print('By bubble sort: ')
    bubble_sort(a_list)
    print(a_list)

    print('By short_bubble sort: ')
    bubble_sort_short(a_list)
    print(a_list)


if __name__ == '__main__':
    main()
