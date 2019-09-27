from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def kth_smallest_maxheap(nums, k):
    """Kth smallest element by MaxHeap.

    Time complexity: O(n*logk).
    Space complexity: O(k).
    """
    import heapq

    # Since we want maxheap with heapq, create negative nums.
    neg_nums = [-n for n in nums]
    maxheap = []

    # Push the first k nums into maxheap.
    for i in range(k):
        heapq.heappush(maxheap, neg_nums[i])

    # Push the remaining nums into maxheap if > maxheap's root.
    # Then keep maxheap with k elements.
    for j in range(k + 1, len(neg_nums)):
        if neg_nums[j] > maxheap[0]:
            heapq.heappop(maxheap)
            heapq.heappush(maxheap, neg_nums[j])

    return -maxheap[0]


def kth_smallest_select(nums, k):
    """Kth smallest element by selection.

    Time complexity: O(n).
    Space complexity: O(n).
    """
    # Just select the kth element, without caring about the 
    # relative ordering of the rest of them.
    pivot = nums[len(nums) // 2]

    mid_pos = [pos for pos, x in enumerate(nums) if x == pivot]
    small_pos = [pos for pos, x in enumerate(nums) if x < pivot]
    large_pos = [pos for pos, x in enumerate(nums) if x > pivot]

    n_small = len(small_pos)
    n_mid = len(mid_pos)

    if k <= n_small:
        small_nums = [nums[pos] for pos in small_pos]
        return kth_smallest_select(small_nums, k)
    elif n_small < k <= n_small + n_mid:
        return pivot
    elif k > n_small + n_mid:
        large_nums = [nums[pos] for pos in large_pos]
        return kth_smallest_select(large_nums, k - n_small - n_mid)


def main():
    import time
    import random

    n = 100
    nums = list(range(1, n))
    random.shuffle(nums)

    start_time = time.time()
    print('By maxheap:')
    print('- Median: {}'.format(kth_smallest_maxheap(nums, n // 2)))
    print('- Min: {}'.format(kth_smallest_maxheap(nums, 1)))
    print('- Max: {}'.format(kth_smallest_maxheap(nums, len(nums))))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By selection:')
    print('- Median: {}'.format(kth_smallest_select(nums, n // 2)))
    print('- Min: {}'.format(kth_smallest_select(nums, 1)))
    print('- Max: {}'.format(kth_smallest_select(nums, len(nums))))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
