"""Leetcode 1. Two Sum
Easy

URL: https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that 
they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

from typing import List


class SolutionNumPosDictIter(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        num_idx_d = dict()
        for i, num in enumerate(nums):
            if target - num in num_idx_d:
                return [num_idx_d[target - num], i]
            num_idx_d[num] = i


def main():
    # Output: [0, 1].
    print(SolutionNumPosDictIter().twoSum([2, 7, 11, 15], 9))


if __name__ == '__main__':
    main()
