from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def sum_list_iter(num_ls):
    """Sum number list by for loop."""
    _sum = 0
    for num in num_ls:
        _sum += num
    return _sum


def sum_list_recur(num_ls):
    """Sum number list by recursion."""
    if len(num_ls) == 1:
        return num_ls[0]
    else:
        return num_ls[0] + sum_list_recur(num_ls[1:])


def main():
    import time

    num_ls = range(100)
    
    start_time = time.time()
    print('By iteration: {}'.format(sum_list_iter(num_ls)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By recursion: {}'.format(sum_list_recur(num_ls)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
