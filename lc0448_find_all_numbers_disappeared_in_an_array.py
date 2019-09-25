"""Leetcode 448. Find All Numbers Disappeared in an Array
Easy

URL: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Given an array of integers where 1 <= a[i] <= n (n = size of array),
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space.

Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[5,6]
"""

class SolutionSetDiff(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        if not nums:
            return []

        # Create the complete set of 1 to n.
        size = len(nums)
        complete_set = set([i for i in range(1, size + 1)])

        # Use a set to collect distinct elements in nums.
        distinct_set = set()
        for n in nums:
            distinct_set.add(n)

        # Return difference between the complete list and distinct one.
        diff_set = complete_set - distinct_set
        return list(diff_set)


def main():
    # Output: [5,6]
    nums = [4,3,2,7,8,2,3,1]
    print SolutionSetDiff().findDisappearedNumbers(nums)


if __name__ == '__main__':
    main()
