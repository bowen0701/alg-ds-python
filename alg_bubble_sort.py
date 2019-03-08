from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def bubble_sort_naive(a_list):
    """Bubble Sort algortihm.

    The list is sorted in place.

    Time complexity: O(n^2).
    Space complexity: O(1).
    """
    for pass_num in reversed(range(len(a_list))):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                a_list[i + 1], a_list[i] = a_list[i], a_list[i + 1] 


def bubble_sort(a_list):
    """Bubble Sort algorithm with early stop.

    The list is sorted in place.

    Time complexity: O(n^2).
    Space complexity: O(1).
    """
    is_sorted = False
    end = len(a_list) - 1
    
    while not is_sorted and end > 0:
        is_sorted = True
        for i in range(end):
            if a_list[i] > a_list[i + 1]:
                is_sorted = False
                a_list[i + 1], a_list[i] = a_list[i], a_list[i + 1]
        end -= 1


def main():
    import time
    import random

    a_list = range(100)
    random.shuffle(a_list)

    start_time = time.time()
    print('By naive bubble sort: ')
    bubble_sort_naive(a_list)
    print(a_list)
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By bubble sort: ')
    bubble_sort(a_list)
    print(a_list)
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
