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


class SolutionSelect(object):
    def _select_mth_smallest_sub_nums(self, sub_nums, mth):
        # Randomly select a num in sub array as pivot.
        pivot_idx = random.choice(range(len(sub_nums)))
        pivot = sub_nums[pivot_idx]

        # Collect idx with num smaller than, equal to, and larger than pivot.
        small_idx = [idx for idx, n in enumerate(sub_nums) if n < pivot]
        mid_idx = [idx for idx, n in enumerate(sub_nums) if n == pivot]
        large_idx = [idx for idx, n in enumerate(sub_nums) if n > pivot]

        n_small = len(small_idx)
        n_mid = len(mid_idx)

        if mth <= n_small:
            # Select the mth from small nums.
            small_nums = [sub_nums[idx] for idx in small_idx]
            return self._select_mth_smallest_sub_nums(small_nums, mth)
        elif n_small < mth <= n_small + n_mid:
            # Select pivot as the mth.
            return pivot
        elif mth > n_small + n_mid:
            # Select the mth from large nums.
            large_nums = [sub_nums[idx] for idx in large_idx]
            return self._select_mth_smallest_sub_nums(
                large_nums, mth - n_small - n_mid)

    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]

        Time complexity: O((n - k)*k), where n is the length of nums.
        Space complexity: O(k).
        """
        n = len(nums)
        med_nums = []

        for i in range(n - k + 1):
            # Create a sub nums.
            sub_nums = nums[i:(i + k)]

            if k % 2 == 1:
                # If k is odd, select the (k // 2 + 1)th as median.
                m = k // 2 + 1
                med = self._select_mth_smallest_sub_nums(sub_nums, m)
            elif k % 2 == 0:
                # If k is even, select the (k // 2)th and (k // 2 + 1)th nums,
                # and take mean of them as median.
                m1 = k // 2
                m2 = k // 2 + 1
                med1 = self._select_mth_smallest_sub_nums(sub_nums, m1)
                med2 = self._select_mth_smallest_sub_nums(sub_nums, m2)
                med = (med1 + med2) / 2.0
            med_nums.append(med)

        return med_nums


class SolutionSortAndBinarySearch(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        pass


def main():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print 'For {0} with k = {1}, the median is:'.format(nums, k)
    print SolutionSelect().medianSlidingWindow(nums, k)


if __name__ == '__main__':
    main()
