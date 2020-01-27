"""Leetcode 34. Find left and right Position of Element in Sorted Array
Medium

URL: https://leetcode.com/problems/find-left-and-right-position-of-element-in-sorted-array

Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

class SolutionBinarySearchTwice(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Time complexity: O(logn), where n is the length of nums.
        Space complexity: O(1).
        """
        # Apply to 2 binary searches to update result [-1, -1].
        res = [-1, -1]

        if not nums:
            return res

        # Apply the 1st binary search to search target's left position.
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        # If left pos is not target, return not found.
        if nums[left] != target:
            return res
        else:
            res[0] = left

        # Apply the 2nd binary search to search target's right position.
        right = len(nums) - 1

        while left < right:
            # Make mid biased to the right.
            mid = left + (right - left) // 2 + 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        res[1] = right
        return res


def main():
    # Ans: [3,4]
    nums = [5,7,7,8,8,10]
    target = 8
    print SolutionBinarySearchTwice().searchRange(nums, target)

    # Ans: [-1,-1]
    nums = [5,7,7,8,8,10]
    target = 6
    print SolutionBinarySearchTwice().searchRange(nums, target)


if __name__ == '__main__':
    main()
