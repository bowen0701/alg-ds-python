from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def lonely_integer_naive(a_list):
    """Lonely integer by naive dictionary.

    Time complexity: O(n).
    Space complexity: O(n).
    """
    integer_count_d = {}
    
    for x in a_list:
        if x in integer_count_d:
            integer_count_d[x] += 1
        else:
            integer_count_d[x] = 1

    for integer, count in integer_count_d.items():
        if count == 1:
            return integer


def lonely_integer(a_list):
    """Lonely integer by bit operation.

    Time complexity: O(n).
    Space complexity: O(1).
    """
    integer = 0
    for x in a_list:
        integer ^= x
    return integer


def main():
    import time

    a_list = [9, 1, 2, 3, 2, 9, 1, 7, 7]
 
    start_time = time.time()
    print('Find lonely integer by naive dictionary: {}'
          .format(lonely_integer_naive(a_list)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('Find lonely integer by bit operation: {}'
          .format(lonely_integer(a_list)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
