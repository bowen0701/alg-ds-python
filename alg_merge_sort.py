from __future__ import print_function
from __future__ import division


def merge_sort_naive(a_list):
    """Merge sort."""
    print('Binary split: {}'.format(a_list))
    
    if len(a_list) > 1:
        # Merge sort by recursion.
        mid = len(a_list) // 2
        left_list = a_list[:mid]
        right_list = a_list[mid:]
        merge_sort_naive(left_list)
        merge_sort_naive(right_list)

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
    """Merge two sorted lists by iteration."""
    z_list = []
    x_pos = 0
    y_pos = 0
    for z_pos in range(len(x_list) + len(y_list)):
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

def merge_sort(a_list, merge_ft=merge_iter):
    """Merge sort by divide and conquer algorithm with
    two methods for sorted sub-lists; see merge_ft.

    Args:
      a_list: A list. List to sort.
      merge_ft: A function. Default: merge_iter.
        - if merge_ft = merge_recur: 
          Merge two sorted lists by recursion.
        - if merge_ft = merge_iter: 
          Merge two sorted lists by iteration.
    """
    if len(a_list) > 1:
        mid = len(a_list) // 2
        return merge_ft(merge_sort(a_list[:mid], merge_ft), 
                        merge_sort(a_list[mid:], merge_ft))
    else:
        return a_list


def main():
    import time

    start_time = time.time()
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('a_list: \n{}'.format(a_list))
    print('By merge sort:')
    merge_sort_naive(a_list)
    print('Run time: {}'.format(time.time() - start_time))

    start_time = time.time()
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('a_list: \n{}'.format(a_list))
    print('By merge sort with divide and conquer algortihm:')
    print(merge_sort(a_list, merge_ft=merge_recur))
    print('Run time: {}'.format(time.time() - start_time))

    start_time = time.time()
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('a_list: \n{}'.format(a_list))
    print('By merge sort with iterative algortihm:')
    print(merge_sort(a_list, merge_ft=merge_iter))
    print('Run time: {}'.format(time.time() - start_time))

if __name__ == '__main__':
    main()
