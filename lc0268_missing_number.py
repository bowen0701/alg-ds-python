"""Leetcode 268. Missing Number
Easy

URL: https://leetcode.com/problems/missing-number/

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
"""

class SolutionGauss(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # By Gauss formula: 0+1+...+n = 1+...+n = (1+n)*n/2.
        n = len(nums)
        complete_sum = (1 + n) * n / 2
        return complete_sum - sum(nums)


def main():
    import time

    start_time = time.time()

    # Output: 2.
    nums = [3,0,1]
    print SolutionGauss().missingNumber(nums)

    # Output: 8.
    nums = [9,6,4,2,3,5,7,0,1]
    print SolutionGauss().missingNumber(nums)

    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
