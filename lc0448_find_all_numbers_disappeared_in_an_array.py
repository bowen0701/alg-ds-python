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
        n = len(nums)
        complete_set = set([i for i in range(1, n + 1)])

        # Use a set to collect distinct numbers in nums.
        nums_set = set()
        for num in nums:
            nums_set.add(num)

        # Compute difference set.
        diff_set = complete_set - nums_set
        return list(diff_set)


class SolutionNegMark(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if not nums:
            return []

        for num in nums:
            # Use idx=num-1 to mark appeared by updating num[idx]=-num[idx].
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])
            print num, idx, nums

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


def main():
    # Output: [5,6]
    nums = [4,3,2,7,8,2,3,1]
    print nums
    print SolutionSetDiff().findDisappearedNumbers(nums)
    print SolutionNegMark().findDisappearedNumbers(nums)


if __name__ == '__main__':
    main()
