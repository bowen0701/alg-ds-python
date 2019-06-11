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

	pos_middle = [pos for pos, x in enumerate(nums) if x == pivot]
	pos_smaller = [pos for pos, x in enumerate(nums) if x < pivot]
	pos_bigger = [pos for pos, x in enumerate(nums) if x > pivot]

	n_smaller = len(pos_smaller)
	n_middle = len(pos_middle)

	if k <= n_smaller:
		nums_smaller = [nums[pos] for pos in pos_smaller]
		return kth_smallest(nums_smaller, k)
	elif n_smaller < k <= n_smaller + n_middle:
		return pivot
	elif k > n_smaller + n_middle:
		nums_bigger = [nums[pos] for pos in pos_bigger]
		return kth_smallest(nums_bigger, k - n_smaller - n_middle)


def main():
	n = 100
	nums = list(range(1, n))
	random.shuffle(nums)

	print('Median: {}'.format(kth_smallest(nums, n // 2)))
	print('Min: {}'.format(kth_smallest(nums, 1)))
	print('Max: {}'.format(kth_smallest(nums, len(nums))))


if __name__ == '__main__':
	main()
