from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def merge_recur(x_list, y_list):
    """Merge two sorted lists by recusions."""
    if len(x_list) == 0:
        return y_list
    if len(y_list) == 0:
        return x_list
    if x_list[0] <= y_list[0]:
        return [x_list[0]] + merge_recur(x_list[1:], y_list)
    else:
        return [y_list[0]] + merge_recur(x_list, y_list[1:])


def merge_iter(x_list, y_list):
    """Merge two sorted lists by iteration (i.e. two fingers method)."""
    z_list = []
    x_pos = 0
    y_pos = 0
    for _ in range(len(x_list) + len(y_list)):
        if x_pos < len(x_list) and y_pos < len(y_list):
            if x_list[x_pos] <= y_list[y_pos]:
                z_list.append(x_list[x_pos])
                x_pos += 1
            else:
                z_list.append(y_list[y_pos])
                y_pos += 1      
        elif x_pos < len(x_list) and y_pos >= len(y_list):
            z_list.extend(x_list[x_pos:])
            break
        elif x_pos >= len(x_list) and y_pos < len(y_list):
            z_list.extend(y_list[y_pos:])
            break
        else:
            pass
    return z_list


def merge_sort(a_list, merge):
    """Merge sort algorithm by divide and conquer method with recursion.

    Time complexity: O(n*logn).
    Space complexity: O(n).
    """
    if len(a_list) == 1:
        return a_list
    else:
        middle = len(a_list) // 2
        return merge(merge_sort(a_list[:middle], merge), 
                     merge_sort(a_list[middle:], merge))


def main():
    import time
    import random

    a_list = range(100)
    random.shuffle(a_list)

    start_time = time.time()
    print(merge_sort(a_list, merge_recur))
    print('Run time of merge sort with recusions: {}'
          .format(time.time() - start_time))

    start_time = time.time()
    print(merge_sort(a_list, merge_iter))
    print('Run time of merge sort with iterations: {}'
          .format(time.time() - start_time))


if __name__ == '__main__':
    main()
