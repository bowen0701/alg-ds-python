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

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        num_idx_d = {}
        for i, n in enumerate(nums):
            if target - n in num_idx_d:
                return [num_idx_d[target - n], i]
            num_idx_d[n] = i
        return []


def main():
    print Solution().twoSum([2, 7, 11, 15], 9)


if __name__ == '__main__':
    main()
