"""Leetcode 162. Find Peak Element
Medium

URL: https://leetcode.com/problems/find-peak-element/

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] != nums[i+1],
find a peak element and return its index.

The array may contain multiple peaks,
in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -oo.
Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where
             the peak element is 2, or index number 5 where the peak element is 6.

Note:
Your solution should be in logarithmic complexity.
"""

class SolutionBinarySearchIter(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(logn), where n is the length of nums.
        Space complexity: O(1).
        """
        # Apply variant of binary search.
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[mid + 1]:
                # If mid < mid's right, search right part. 
                left = mid + 1
            else:
                # Otherwise, search left part.
                right = mid

        return left


def main():
    # Ans: 2
    nums = [1,2,3,1]
    print SolutionBinarySearchIter().findPeakElement(nums)

    # Ans: 1 or 5.
    nums = [1,2,1,3,5,6,4]
    print SolutionBinarySearchIter().findPeakElement(nums)

    # Ans: 0
    nums = [2,1]
    print SolutionBinarySearchIter().findPeakElement(nums)


if __name__ == '__main__':
    main()
