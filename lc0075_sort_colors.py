"""Leetcode 75. Sort Colors
Medium

URL: https://leetcode.com/problems/sort-colors/

Given an array with n objects colored red, white or blue, sort them in-place 
so that objects of the same color are adjacent, 
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, 
and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:
- A rather straight forward solution is a two-pass algorithm using counting sort.
- First, iterate the array counting number of 0's, 1's, and 2's, 
  then overwrite array with total number of 0's, then 1's and followed by 2's.
- Could you come up with a one-pass algorithm using only constant space?
"""

class SolutionCount(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Time complexity: O(n), where n is the number of nums.
        Space complexity: O(n).
        """
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        if 0 not in d:
            d[0] = 0
        if 1 not in d:
            d[1] = 0
        if 2 not in d:
            d[2] = 0

        for i, _ in enumerate(nums):
            if i < d[0]:
                nums[i] = 0
            elif d[0] <= i < d[0] + d[1]:
                nums[i] = 1
            else:
                nums[i] = 2


class SolutionUpdateAll(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Keep the end of each color.
        r, w, b = 0, 0, 0

        for i, n in enumerate(nums):
            # Update elements for all colors in the reversed orders.
            if n == 0:
                nums[b] = 2
                nums[w] = 1
                nums[r] = 0
                b += 1
                w += 1
                r += 1
            elif n == 1:
                nums[b] = 2
                nums[w] = 1
                b += 1
                w += 1
            elif n == 2:
                b += 1


def main():
    # Ans: [0,0,1,1,2,2].
    nums = [2,0,2,1,1,0]
    # SolutionCount().sortColors(nums)
    SolutionUpdateAll().sortColors(nums)
    print nums


if __name__ == '__main__':
    main()
