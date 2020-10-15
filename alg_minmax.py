from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def minmax_naive(a):
    """Find mix & max in a list by naive algorithm.

    - Time complexity: O(n).
    - Space complexity: O(1).
    """
    _min = a[0]
    _max = a[0]
    for i in range(1, len(a)):
        if a[i] < _min:
            _min = a[i]
        if a[i] > _max:
            _max = a[i]
    return [_min, _max]


def minmax_dc(a):
    """Find mix & max in a list by divide and conquer algorithm.

    - Time complexity: O(n).
    - Space complexity: O(1).
    """
    if len(a) == 1:
        return [a[0], a[0]]
    elif len(a) == 2:
        if a[0] < a[1]:
            return [a[0], a[1]]
        else:
            return [a[1], a[0]]
    else:
        len_a = len(a)
        [_min1, _max1] = minmax_dc(a[:(len_a // 2)])
        [_min2, _max2] = minmax_dc(a[(len_a // 2):])

        if _min1 < _min2:
            _min = _min1
        else:
            _min = _min2

        if _max1 > _max2:
            _max = _max1
        else:
            _max = _max2

        return [_min, _max]


def minmax_seq(a):
    """Find mix & max in a list by sequential algorithm.

    - Time complexity: O(n).
    - Space complexity: O(1).
    """
    if a[0] < a[1]:
        cur_min, cur_max = a[0], a[1]
    else:
        cur_min, cur_max = a[1], a[0]

    for i in range(2, len(a), 2):
        if i + 1 < len(a):
            if a[i] < a[i + 1]:
                _min, _max = a[i], a[i + 1]
            else:
                _min, _max = a[i + 1], a[i]
        else:
            _min, _max = a[i], a[i]

        if _min < cur_min:
            cur_min = _min
        if _max > cur_max:
            cur_max = _max

    return [cur_min, cur_max]


def main():
    import time

    a = range(int(1e6))

    start_time = time.time()
    print('By naive algorithm: {}'
          .format(minmax_naive(a)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By divide and conquer algorithm: {}'
          .format(minmax_dc(a)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By sequential algorithm: {}'
          .format(minmax_seq(a)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
