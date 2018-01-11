from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def merge_sort(a_list):
    """Merge sort."""
    print('Binary split: {}'.format(a_list))
    
    if len(a_list) > 1:
        # Merge sort by recursion.
        mid = len(a_list) // 2
        left_list = a_list[:mid]
        right_list = a_list[mid:]
        merge_sort(left_list)
        merge_sort(right_list)

        # Merge two small sorted lists.
        i = 0
        j = 0
        k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                a_list[k] = left_list[i]
                i += 1
            else:
                a_list[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            a_list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            a_list[k] = right_list[j]
            j += 1
            k += 1

    print('Merge {}'.format(a_list))


def main():
    import time

    start_time = time.time()
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('a_list: \n{}'.format(a_list))
    print('By merge sort:')
    merge_sort(a_list)
    print('Run time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
