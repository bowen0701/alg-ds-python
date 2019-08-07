"""Leetcode 34. Find First and Last Position of Element in Sorted Array
Medium

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

class Solution(object):
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
        first, last = 0, len(nums) - 1

        while first < last:
            mid = first + (last - first) // 2
            if nums[mid] < target:
                first = mid + 1
            else:
                last = mid

        if nums[first] != target:
            return res
        else:
            res[0] = first

        # Apply the 2nd binary search to search target's right position.
        last = len(nums) - 1
        while first < last:
            # Make mid biased to the right.
            mid = first + (last - first) // 2 + 1
            if nums[mid] > target:
                last = mid - 1
            else:
                first = mid

        res[1] = last
        return res


def main():
    # Ans: [3,4]
    nums = [5,7,7,8,8,10]
    target = 8
    print Solution().searchRange(nums, target)

    # Ans: [-1,-1]
    nums = [5,7,7,8,8,10]
    target = 6
    print Solution().searchRange(nums, target)


if __name__ == '__main__':
    main()
