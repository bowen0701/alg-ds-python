from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _merge_recur(x_list, y_list):
    """Merge two sorted lists by recusions."""
    if len(x_list) == 0:
        return y_list
    if len(y_list) == 0:
        return x_list
    if x_list[0] <= y_list[0]:
        return [x_list[0]] + _merge_recur(x_list[1:], y_list)
    else:
        return [y_list[0]] + _merge_recur(x_list, y_list[1:])


def _merge_iter(x_list, y_list):
    """Merge two sorted lists by iteration."""
    z_list = []
    x_pos = 0
    y_pos = 0
    for z_pos in xrange(len(x_list) + len(y_list)):
        if x_pos < len(x_list) and y_pos < len(y_list):
            if x_list[x_pos] <= y_list[y_pos]:
                z_list.append(x_list[x_pos])
                x_pos += 1
            else:
                z_list.append(y_list[y_pos])
                y_pos += 1      
        elif x_pos < len(x_list) and y_pos >= len(y_list):
            z_list.append(x_list[x_pos])
            x_pos += 1
        elif x_pos >= len(x_list) and y_pos < len(y_list):
            z_list.append(y_list[y_pos])
            y_pos += 1
        else:
            pass
    return z_list


def merge_sort(a_list, merge_ft=_merge_iter):
    """Merge sort by divide and conquer algorithm with
    two methods for sorted sub-lists; see merge_ft.

    Args:
      a_list: A list. List to sort.
      merge_ft: A function. Default: merge_iter.
        - if merge_ft = merge_recur: 
          Merge two sorted lists by recursion: merge_recur().
        - if merge_ft = merge_iter: 
          Merge two sorted lists by iteration: merge_iter().
    """
    if len(a_list) == 1:
        return a_list
    else:
        mid = len(a_list) // 2
        return merge_ft(merge_sort(a_list[:mid], merge_ft), 
                        merge_sort(a_list[mid:], merge_ft))


def main():
    import time

    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('a_list: \n{}'.format(a_list))

    start_time = time.time()
    print('By merge sort with recusions:')
    print(merge_sort(a_list, merge_ft=_merge_recur))
    print('Run time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By merge sort with iterations:')
    print(merge_sort(a_list, merge_ft=_merge_iter))
    print('Run time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
