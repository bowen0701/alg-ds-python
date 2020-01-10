"""Leetcode 35. Search Insert Position
Easy

URL: https://leetcode.com/problems/search-insert-position/

Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
"""

class SolutionBinarySearch(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if nums[left] >= target:
            return left
        else:
            return left + 1


def main():
    # Output: 2
    nums = [1,3,5,6]
    target = 5
    print SolutionBinarySearch().searchInsert(nums, target)

    # Output: 1
    nums = [1,3,5,6]
    target = 2
    print SolutionBinarySearch().searchInsert(nums, target)

    # Output: 4
    nums = [1,3,5,6]
    target = 7
    print SolutionBinarySearch().searchInsert(nums, target)

    # Output: 0
    nums = [1,3,5,6]
    target = 0
    print SolutionBinarySearch().searchInsert(nums, target)


if __name__ == '__main__':
    main()
