from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def sum_list(num_ls):
    """Sum number list by recursion."""
    if len(num_ls) == 1:
    	return num_ls[0]
    else:
    	return num_ls[0] + sum_list(num_ls[1:])


def main():
	num_ls = [0, 1, 2, 3, 4, 5]
	print('Sum of {}: {}'.format(num_ls, sum_list(num_ls)))


if __name__ == '__main__':
	main()
