"""Leetcode 283. Move Zeroes
Easy

Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] == 0:
                nums.append(nums.pop(start))
                end -= 1
            else:
                start += 1


def main():
    nums1 = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums1)
    print nums1

    nums2 = [0, 0, 3, 12, 1, 0, 5]
    Solution().moveZeroes(nums2)
    print nums2


if __name__ == '__main__':
    main()
