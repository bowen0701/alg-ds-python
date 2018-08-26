from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def insertion_sort(a_list):
    """Insertion Sort algortihm.

    Time complexity: O(n^2).

    Although its complexity is bigger than the ones with O(n*logn), 
    one advantage is the sorting happens in place.
    """
    gen = ((i, v) for i, v in enumerate(a_list) if i > 0)
    for (i, v) in gen:
        key = i
        while key > 0 and a_list[key - 1] > v:
            a_list[key] = a_list[key - 1]
            key -= 1
        a_list[key] = v


def main():
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(a_list)
    print(a_list)


if __name__ == '__main__':
    main()
