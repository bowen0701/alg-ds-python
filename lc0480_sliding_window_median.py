"""Leetcode 480. Sliding Window Median
Hard

URL: https://leetcode.com/problems/sliding-window-median/

Median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value. 
So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from 
the very left of the array to the very right. 
You can only see the k numbers in the window. 
Each time the sliding window moves right by one position. 
Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6

Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note: 
You may assume k is always valid, ie: 
k is always smaller than input array's size for non-empty array.
"""

import random


class SolutionSelection(object):
    def _select_mth_smallest(self, sub_nums, m):
        # Randomly select a num in sub array as pivot.
        pivot_idx = random.choice(range(len(sub_nums)))
        pivot = sub_nums[pivot_idx]

        # Collect idx with num smaller than, equal to, and larger than pivot.
        small_idx = [idx for idx, n in enumerate(sub_nums) if n < pivot]
        mid_idx = [idx for idx, n in enumerate(sub_nums) if n == pivot]
        large_idx = [idx for idx, n in enumerate(sub_nums) if n > pivot]

        n_small = len(small_idx)
        n_mid = len(mid_idx)

        if m <= n_small:
            # Select the m from small nums.
            small_nums = [sub_nums[idx] for idx in small_idx]
            return self._select_mth_smallest(small_nums, m)
        elif n_small < m <= n_small + n_mid:
            # Select pivot as the m.
            return pivot
        elif m > n_small + n_mid:
            # Select the m from large nums.
            large_nums = [sub_nums[idx] for idx in large_idx]
            return self._select_mth_smallest(large_nums, m - n_small - n_mid)

    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]

        Time complexity: O(n*k), where n is the length of nums.
        Space complexity: O(n).
        """
        n = len(nums)
        medians = []

        for i in range(n - k + 1):
            # Create a sub nums.
            sub_nums = nums[i:(i + k)]

            if k % 2 == 1:
                # If k is odd, select the (k // 2 + 1)th as median.
                med = self._select_mth_smallest(sub_nums, k // 2 + 1)
            elif k % 2 == 0:
                # If k is even, select the (k // 2)th and (k // 2 + 1)th nums,
                # and take mean of them as median.
                med1 = self._select_mth_smallest(sub_nums, k // 2)
                med2 = self._select_mth_smallest(sub_nums, k // 2 + 1)
                med = (med1 + med2) / 2.0

            medians.append(med)

        return medians


class SolutionSortAndBinarySearch(object):
    def _binary_search(self, window, k, element):
        # Apply binary search to
        # - remove old element from sorted window.
        # - insert new element into sorted window.
        left = 0
        right = k - 1

        while left < right:
            mid = left + (right - left) // 2

            if window[mid] == element:
                return mid
            elif window[mid] < element:
                left = mid + 1
            else:
                # Note: not right = mid - 1.
                right = mid

        return left

    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]

        Time complexity: O(k*logk + n*(logk+k)) = O(n*k).
        Space complexity: O(k).
        """
        medians = []

        # Keep the window as sorted list.
        window = sorted(nums[:k])

        # Apply two pointers method with to-be-removed & to-be-added elements.
        # The last zippped pair is to add the last median only.
        for old, new in zip(nums, nums[k:] + [None]):
            medians.append((window[k // 2] + window[~(k // 2)]) / 2.0)

            # Apply binary search to remove old element from sorted window.
            old_pos = self._binary_search(window, k, old)
            window.pop(old_pos)
            
            # Apply binary search to add new element to sorted window.
            left_pos = self._binary_search(window, k, new)
            window.insert(left_pos, new)

        return medians


def main():
    import time

    # Output: [1, -1, -1, 3, 5, 6].
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    start_time = time.time()
    print 'By kth smallest selection method:'
    print SolutionSelection().medianSlidingWindow(nums, k)
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By sorted window with binary search:'
    print SolutionSortAndBinarySearch().medianSlidingWindow(nums, k)
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
