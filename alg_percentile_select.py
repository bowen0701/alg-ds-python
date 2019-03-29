from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random


def percentile_select(ls, k):
	"""Kth percentile selection algorithm.

    Just select the kth element, without caring about
    the relative ordering of the rest of them.

    The algorithm performs in place without allocating
    new memory for the three sublists using three pointers.

    Time complexity: O(n).
	"""
	v = random.choice(ls)
	idx_eq_v = [i for i, a in enumerate(ls) if a == v]
	idx_le_v = [i for i, a in enumerate(ls) if a < v]
	idx_ge_v = [i for i, a in enumerate(ls) if a > v]
	n_le = len(idx_le_v)
	n_eq = len(idx_eq_v)

	if k <= n_le:
		le_v_ls = [ls[idx] for idx in idx_le_v]
		return percentile_select(le_v_ls, k)
	elif n_le < k <= n_le + n_eq:
		return v
	elif k > n_le + n_eq:
		ge_v_ls = [ls[idx] for idx in idx_ge_v]
		return percentile_select(ge_v_ls, k - n_le - n_eq)


def main():
	n = 100
	ls = range(n)
	random.shuffle(ls)

	print('Get median by selection:')
	print(percentile_select(ls, n // 2))
	print('Get min by selection:')
	print(percentile_select(ls, 1))
	print('Get max by selection:')
	print(percentile_select(ls, n))


if __name__ == '__main__':
	main()
