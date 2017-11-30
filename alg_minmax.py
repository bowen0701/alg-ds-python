from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

def find_min_max_naive(a_ls):
    """Find mix & max in a list by naive algorithm."""
    _min = a_ls[0]
    _max = a_ls[0]
    for i in range(1, len(a_ls)):
        _min = min(_min, a_ls[i])
        _max = max(_max, a_ls[i])
    return [_min, _max]


def find_min_max_dc(a_ls):
    """Find mix & max in a list by divide and conquer algorithm."""
    if len(a_ls) == 1:
        return [a_ls[0], a_ls[0]]
    elif len(a_ls) == 2:
        if a_ls[0] < a_ls[1]:
            return [a_ls[0], a_ls[1]]
        else:
            return [a_ls[1], a_ls[0]]
    else:
        [_min1, _max1] = find_min_max_dc(a_ls[:len(a_ls)//2])
        [_min2, _max2] = find_min_max_dc(a_ls[len(a_ls)//2:])
        return [min(_min1, _min2), max(_max1, _max2)]


def find_min_max_seq(a_ls):
    """Find mix & max in a list by sequential algorithm."""
    cur_min = min(a_ls[0], a_ls[1])
    cur_max = max(a_ls[0], a_ls[1])

    for i in range(2, len(a_ls), 2):
        if i + 1 < len(a_ls): 
            _min = min(a_ls[i], a_ls[i + 1])
            _max = max(a_ls[i], a_ls[i + 1])
        else:
            _min = min(a_ls[i], a_ls[i])
            _max = max(a_ls[i], a_ls[i])

        if _min < cur_min:
            cur_min = _min
        if _max > cur_max:
            cur_max = _max
    return [cur_min, cur_max]


def main():
    # List with even numbers.
    # a_ls = [0, 1, 2, 3, 4, 5, 6, 7]
    # List with odd numbers.
    a_ls = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print('A list: {}'.format(a_ls))
    print('Find min & max:')

    print('By naive algorithm: {}'
          .format(find_min_max_naive(a_ls)))

    print('By divide and conquer algorithm: {}'
          .format(find_min_max_dc(a_ls)))

    print('By sequential algorithm: {}'
          .format(find_min_max_seq(a_ls)))

if __name__ == '__main__':
    main()
