"""Leetcode 189. Rotate Array
Easy

URL: https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:
- Try to come up as many solutions as you can, 
  there are at least 3 different ways to solve this problem.
- Could you do it in-place with O(1) extra space?
"""

class SolutionCopy(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # If k >= n, truncate k by n.
        n = len(nums)
        if k >= n:
            k -= n

        # Append right with left.
        nums[:] = nums[-k:] + nums[:-k]


def main():
    # Ans: [5,6,7,1,2,3,4]
    nums = [1,2,3,4,5,6,7]
    k = 3
    SolutionCopy().rotate(nums, k)
    print nums

    # Ans: [3,99,-1,-100]
    nums = [-1,-100,3,99]
    k = 2
    SolutionCopy().rotate(nums, k)
    print nums

    # Ans: [2,1]
    nums = [1,2]
    k = 3
    SolutionCopy().rotate(nums, k)
    print nums


if __name__ == '__main__':
    main()
