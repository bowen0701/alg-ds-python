from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

def row_product(arr):
	nrow, ncol = len(arr), len(arr[0])
	rprod = [1 for _ in range(ncol)]

	for j in range(ncol):
		for i in range(nrow):
			rprod[j] *= arr[i][j]

	return rprod


def main():
	arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

	print('Row product: {}'.format(row_product(arr)))


if __name__ == '__main__':
	main()
