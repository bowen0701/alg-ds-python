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
    elif 1 < len(a_ls) < 3:
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
    pass


def main():
    # a_ls = [1, 2, 3, 4, 5, 6, 7, 8]
    a_ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('A list: {}'.format(a_ls))
    print('Find min & max:')

    print('By naive method: {}'
          .format(find_min_max_naive(a_ls)))

    print('By divide and conquer method: {}'
          .format(find_min_max_dc(a_ls)))

if __name__ == '__main__':
    main()
