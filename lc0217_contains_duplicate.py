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

class SolutionSet(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(n).
        """
        num_set = set()

        for n in nums:
            if n in num_set:
                return True
            else:
                num_set.add(n)

        return False


def main():
    import time

    start_time = time.time()
    print 'By set:'
    # Output: True
    nums = [1,2,3,1]
    print SolutionSet().containsDuplicate(nums)

    # Output: False
    nums = [1,2,3,4]
    print SolutionSet().containsDuplicate(nums)

    # Output: True
    nums = [1,1,1,3,3,4,3,2,4,2]
    print SolutionSet().containsDuplicate(nums)
    print 'Time:', time.time() - start_time


if __name__ == '__main__':
    main()
