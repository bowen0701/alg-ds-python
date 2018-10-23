from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

def find_min_max_naive(a_ls):
    """Find mix & max in a list by naive algorithm.

    - Time complexity: O(n).
    - Space complexity: O(1).
    """
    _min = a_ls[0]
    _max = a_ls[0]
    for i in range(1, len(a_ls)):
        if a_ls[i] < _min:
            _min = a_ls[i]
        if a_ls[i] > _max:
            _max = a_ls[i]
    return [_min, _max]


def find_min_max_dc(a_ls):
    """Find mix & max in a list by divide and conquer algorithm.

    - Time complexity: O(n).
    - Space complexity: O(1).
    """
    if len(a_ls) == 1:
        return [a_ls[0], a_ls[0]]
    elif len(a_ls) == 2:
        if a_ls[0] < a_ls[1]:
            return [a_ls[0], a_ls[1]]
        else:
            return [a_ls[1], a_ls[0]]
    else:
        len_a = len(a_ls)
        [_min1, _max1] = find_min_max_dc(a_ls[:len_a//2])
        [_min2, _max2] = find_min_max_dc(a_ls[len_a//2:])

        if _min1 < _min2:
            _min = _min1
        else:
            _min = _min2

        if _max1 > _max2:
            _max = _max1
        else:
            _max = _max2

        return [_min, _max]


def find_min_max_seq(a_ls):
    """Find mix & max in a list by sequential algorithm.

    - Time complexity: O(n).
    - Space complexity: O(1).
    """
    if a_ls[0] < a_ls[1]:
        cur_min, cur_max = a_ls[0], a_ls[1]
    else:
        cur_min, cur_max = a_ls[1], a_ls[0]

    for i in range(2, len(a_ls), 2):
        if i + 1 < len(a_ls):
            if a_ls[i] < a_ls[i + 1]:
                _min, _max = a_ls[i], a_ls[i + 1]
            else:
                _min, _max = a_ls[i + 1], a_ls[i]
        else:
            _min, _max = a_ls[i], a_ls[i]

        if _min < cur_min:
            cur_min = _min
        if _max > cur_max:
            cur_max = _max

    return [cur_min, cur_max]


def main():
    import time

    # List with even numbers.
    # a_ls = [0, 1, 2, 3, 4, 5, 6, 7]
    # List with odd numbers.
    # a_ls = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    a_ls = range(int(1e6))
    print('Find min & max for list: {}'.format(a_ls))

    start_time = time.time()
    print('By naive algorithm: {}'
          .format(find_min_max_naive(a_ls)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By divide and conquer algorithm: {}'
          .format(find_min_max_dc(a_ls)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By sequential algorithm: {}'
          .format(find_min_max_seq(a_ls)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
