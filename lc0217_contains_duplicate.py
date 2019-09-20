"""Leetcode 217. Contains Duplicate
Easy

URL: https://leetcode.com/problems/contains-duplicate/

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

class SolutionDict(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_counts = {}

        for n in nums:
            if n in num_counts:
                return True
            else:
                num_counts[n] = 1

        return False


def main():
    # Output: True
    nums = [1,2,3,1]
    print SolutionDict().containsDuplicate(nums)

    # Output: False
    nums = [1,2,3,4]
    print SolutionDict().containsDuplicate(nums)

    # Output: True
    nums = [1,1,1,3,3,4,3,2,4,2]
    print SolutionDict().containsDuplicate(nums)


if __name__ == '__main__':
    main()
