"""Leetcode 137. Single Number II
Medium

URL: https://leetcode.com/problems/single-number-ii/

Given a non-empty array of integers, every element appears three times except
for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example 1:
Input: [2,2,3,2]
Output: 3

Example 2:
Input: [0,1,0,1,0,1,99]
Output: 99
"""

class SolutionDict(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        from collections import defaultdict
        num_counts = defaultdict(int)

        for n in nums:
            num_counts[n] += 1

        for n, count in num_counts.items():
            if count == 1:
                return n


class SolutionSumDivide(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        return (sum(set(nums)) * 3 - sum(nums)) / 2


def main():
    # Output: 3.
    nums = [2,2,3,2]
    print SolutionDict().singleNumber(nums)
    print SolutionSumDivide().singleNumber(nums)

    # Output: 99.
    nums = [0,1,0,1,0,1,99]
    print SolutionDict().singleNumber(nums)
    print SolutionSumDivide().singleNumber(nums)


if __name__ == '__main__':
    main()
