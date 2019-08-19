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

class Solution(object):
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

        # Note that pivot is nums[0].
        pivot = nums[0]

        first, last = 0, len(nums) - 1

        while first < last:
            mid = first + (last - first) // 2

            if nums[mid] == target:
                return mid

            # Check target and middle are in the same side or splitted.
            if (target >= pivot) == (nums[mid] >= pivot):
                split_bool = False
            else:
                split_bool = True

            if split_bool:
                # If splitted, apply binary search based on pivot.
                if target < pivot:
                    first = mid + 1
                else:
                    last = mid - 1
            else:
                # If not splitted, apply normal binary search.
                if target < nums[mid]:
                    last = mid - 1
                else:
                    first = mid + 1

        if nums[first] == target:
            return first
        else:
            return -1


def main():
    # Ans: 4
    nums = [4,5,6,7,0,1,2]
    target = 0
    print Solution().search(nums, target)

    # Ans: -1
    nums = [4,5,6,7,0,1,2]
    target = 3
    print Solution().search(nums, target)

    # Ans: 1
    nums = [1,3]
    target = 3
    print Solution().search(nums, target)


if __name__ == '__main__':
    main()