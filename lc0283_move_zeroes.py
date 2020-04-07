"""Leetcode 283. Move Zeroes
Easy

Given an array nums, write a function to move all 0's to the right of it 
while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class SolutionPopAppend(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Time complexity: O(n).
        Space complexity: O(n).
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] == 0:
                nums.append(nums.pop(left))
                right -= 1
            else:
                left += 1


class SolutionUpdate(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        nonzero_idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonzero_idx] = nums[i]
                nonzero_idx += 1

        for i in range(nonzero_idx, len(nums)):
            nums[i] = 0


def main():
    nums1 = [0, 1, 0, 3, 12]
    SolutionPopAppend().moveZeroes(nums1)
    print nums1
    nums1 = [0, 1, 0, 3, 12]
    SolutionUpdate().moveZeroes(nums1)
    print nums1

    nums2 = [0, 0, 3, 12, 1, 0, 5]
    SolutionPopAppend().moveZeroes(nums2)
    print nums2
    nums2 = [0, 0, 3, 12, 1, 0, 5]
    SolutionUpdate().moveZeroes(nums2)
    print nums2


if __name__ == '__main__':
    main()
