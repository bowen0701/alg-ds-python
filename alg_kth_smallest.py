from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random


def kth_smallest(nums, k):
	"""Kth smallest element selection.

    Just select the kth element, without caring about the 
    relative ordering of the rest of them.

    Time complexity: O(n).
    Space complexity: O(n).
	"""
	pivot = random.choice(nums)

	pos_eq = [pos for pos, x in enumerate(nums) if x == pivot]
	pos_le = [pos for pos, x in enumerate(nums) if x < pivot]
	pos_gr = [pos for pos, x in enumerate(nums) if x > pivot]

	n_le = len(pos_le)
	n_eq = len(pos_eq)

	if k <= n_le:
		nums_le = [nums[pos] for pos in pos_le]
		return kth_smallest(nums_le, k)
	elif n_le < k <= n_le + n_eq:
		return pivot
	elif k > n_le + n_eq:
		nums_gr = [nums[pos] for pos in pos_gr]
		return kth_smallest(nums_gr, k - n_le - n_eq)


def main():
	n = 100
	nums = list(range(1, n))
	random.shuffle(nums)

	print('Median: {}'.format(kth_smallest(nums, n // 2)))
	print('Min: {}'.format(kth_smallest(nums, 1)))
	print('Max: {}'.format(kth_smallest(nums, len(ls))))


if __name__ == '__main__':
	main()
