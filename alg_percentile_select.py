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
	v = random.sample(ls, 1)[0]
	idx_eq_v = [i for i, a in enumerate(ls) if a == v]
	idx_le_v = [i for i, a in enumerate(ls) if a < v]
	idx_ge_v = [i for i, a in enumerate(ls) if a > v]

	if k <= len(idx_le_v):
		le_v_ls = [ls[idx] for idx in idx_le_v]
		return percentile_select(le_v_ls, k)
	elif len(idx_le_v) < k <= len(idx_le_v) + len(idx_eq_v):
		return v
	elif k > len(idx_le_v) + len(idx_eq_v):
		ge_v_ls = [ls[idx] for idx in idx_ge_v]
		return percentile_select(ge_v_ls, k - len(idx_le_v) - len(idx_eq_v))


def main():
	n = 100
	ls = range(n)
	random.shuffle(ls)
	print('List: {}'.format(ls))
	print('Get median by selection:')
	print(percentile_select(ls, n // 2))
	print('Get min by selection:')
	print(percentile_select(ls, 1))
	print('Get max by selection:')
	print(percentile_select(ls, n))


if __name__ == '__main__':
	main()
