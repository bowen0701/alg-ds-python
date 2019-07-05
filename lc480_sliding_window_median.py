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


class Solution(object):
    def _select_mth_smallest_sub_nums(self, nums, start, end, mth):
        pass

    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        n = len(nums)
        med_nums = []

        for i in range(n - k):
            if k % 2 == 1:
                m = k // 2 + 1
                med = self._select_mth_smallest_sub_nums(nums, i, i + k - 1, m)
            elif k % 2 == 0:
                m1 = k // 2
                m2 = k // 2 + 1
                med1 = self._select_mth_smallest_sub_nums(nums, i, i + k - 1, m1)
                med2 = self._select_mth_smallest_sub_nums(nums, i, i + k - 1, m2)
                med = (med1 + med2) / 2.0
            med_nums.append(med)

        return med_nums


def main():
    pass


if __name__ == '__main__':
    main()
