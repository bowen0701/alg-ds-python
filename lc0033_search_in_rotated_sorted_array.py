"""Leetcode 33. Search in Rotated Sorted Array
Medium

URL: https://leetcode.com/problems/search-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot unknown 
to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, 
otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

class SolutionTwoPointers(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        Time complexity: O(logn), where n is the lenght of nums.
        Space complexity: O(1).
        """
        if not nums:
            return -1

        # Fixed pivot is nums[0].
        pivot = nums[0]

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # Check if target & middle are bigger than pivot (not splitted).
            if (target >= pivot) == (nums[mid] >= pivot):
                is_split = False
            else:
                is_split = True

            if not is_split:
                # If not splitted, apply normal binary search w.r.t. mid.
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # If splitted, apply "reversed" binary search w.r.t. pivot.
                if nums[mid] > target:
                    left = mid + 1
                else:
                    right = mid - 1

        if nums[left] == target:
            return left
        else:
            return -1


def main():
    # Ans: 4
    nums = [4,5,6,7,0,1,2]
    target = 0
    print SolutionTwoPointers().search(nums, target)

    # Ans: -1
    nums = [4,5,6,7,0,1,2]
    target = 3
    print SolutionTwoPointers().search(nums, target)

    # Ans: 1
    nums = [1,3]
    target = 3
    print SolutionTwoPointers().search(nums, target)


if __name__ == '__main__':
    main()
