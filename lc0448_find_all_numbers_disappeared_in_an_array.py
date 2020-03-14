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

class SolutionDistinctNumsSet(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        if not nums:
            return []

        # Use set to collect distinct numbers.
        distinct_nums = set()
        for num in nums:
            distinct_nums.add(num)

        # Iterate through nums to collect disappeared numbers.
        disappeared_nums = []
        for i in range(1, len(nums) + 1):
            if i not in distinct_nums:
                disappeared_nums.append(i)
        return disappeared_nums


class SolutionMarkIdxNumNeg(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if not nums:
            return []

        # Use idx=num-1 to mark appeared by updating num[idx]=-num[idx].
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])

        # Return disappeared numbers which are idx's with positive values. 
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


def main():
    # Output: [5,6]
    nums = [4,3,2,7,8,2,3,1]
    print SolutionDistinctNumsSet().findDisappearedNumbers(nums)
    print SolutionMarkIdxNumNeg().findDisappearedNumbers(nums)


if __name__ == '__main__':
    main()
