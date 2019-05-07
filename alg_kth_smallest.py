from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random


def kth_smallest(ls, k):
	"""Kth smallest element selection.

    Just select the kth element, without caring about the 
    relative ordering of the rest of them.

    Time complexity: O(n).
    Space complexity: O(n).
	"""
	pivot = random.choice(ls)

	pos_eq = [pos for pos, e in enumerate(ls) if e == pivot]
	pos_le = [pos for pos, e in enumerate(ls) if e < pivot]
	pos_gr = [pos for pos, e in enumerate(ls) if e > pivot]

	n_le = len(pos_le)
	n_eq = len(pos_eq)

	if k <= n_le:
		le_ls = [ls[pos] for pos in pos_le]
		return kth_smallest(le_ls, k)
	elif n_le < k <= n_le + n_eq:
		return pivot
	elif k > n_le + n_eq:
		gr_ls = [ls[pos] for pos in pos_gr]
		return kth_smallest(gr_ls, k - n_le - n_eq)


def main():
	n = 100
	ls = list(range(1, n))
	random.shuffle(ls)

	print('Median: {}'.format(kth_smallest(ls, n // 2)))
	print('Min: {}'.format(kth_smallest(ls, 1)))
	print('Max: {}'.format(kth_smallest(ls, len(ls))))


if __name__ == '__main__':
	main()
