from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def selection_sort(ls):
    """Selection Sort algortihm.

    Time complexity: O(n^2).
    Space complexity: O(1).
    """
    # Start from the last elemenet reversely: len(ls) - 1, ..., 0.
    for i_max in reversed(range(len(ls))):
        # Select the next max, and interchange it with corresponding element.
        s = 0
        for i in range(1, i_max + 1):
            if ls[i] > ls[s]:
                s = i
        ls[s], ls[i_max] = ls[i_max], ls[s]


def main():
    ls = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('List: {}'.format(ls))
    print('By selection sort: ')
    selection_sort(ls)
    print(ls)


if __name__ == '__main__':
    main()
