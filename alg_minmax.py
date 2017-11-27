from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

def find_min_max_naive(a_ls):
    """Find mix & max in a list by naive method."""
    _min = a_ls[0]
    _max = a_ls[0]
    for i in range(1, len(a_ls)):
        _min = min(_min, a_ls[i])
        _max = max(_max, a_ls[i])
    return [_min, _max]


def main():
    # a_ls = [1, 2, 3, 4, 5, 6, 7, 8]
    a_ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('A list: {}'.format(a_ls))
    print('Find min & max:')

    print('By naive method: {}'
          .format(find_min_max_naive(a_ls)))

if __name__ == '__main__':
    main()
