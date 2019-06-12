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

	mid_pos = [pos for pos, x in enumerate(nums) if x == pivot]
	small_pos = [pos for pos, x in enumerate(nums) if x < pivot]
	large_pos = [pos for pos, x in enumerate(nums) if x > pivot]

	n_small = len(small_pos)
	n_mid = len(mid_pos)

	if k <= n_small:
		small_nums = [nums[pos] for pos in small_pos]
		return kth_smallest(small_nums, k)
	elif n_small < k <= n_small + n_mid:
		return pivot
	elif k > n_small + n_mid:
		large_nums = [nums[pos] for pos in large_pos]
		return kth_smallest(large_nums, k - n_small - n_mid)


def main():
	n = 100
	nums = list(range(1, n))
	random.shuffle(nums)

	print('Median: {}'.format(kth_smallest(nums, n // 2)))
	print('Min: {}'.format(kth_smallest(nums, 1)))
	print('Max: {}'.format(kth_smallest(nums, len(nums))))


if __name__ == '__main__':
	main()
