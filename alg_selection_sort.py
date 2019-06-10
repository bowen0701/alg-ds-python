from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def selection_sort(ls):
    """Selection Sort algortihm.

    Time complexity: O(n^2).
    Space complexity: O(1).
    """
    # Start from the last position reversely: len(ls) - 1, ..., 0.
    for i in reversed(range(len(ls))):
        # Select next max element, and swap it and element at position i.
        s = 0
        for j in range(1, i + 1):
            if ls[j] > ls[s]:
                s = j
        ls[s], ls[i] = ls[i], ls[s]


def main():
    ls = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('List: {}'.format(ls))
    print('By selection sort: ')
    selection_sort(ls)
    print(ls)


if __name__ == '__main__':
    main()
