"""Leetcode 41. First Missing Positive
Hard

URL: https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1

Note:
Your algorithm should run in O(n) time and uses constant extra space.
"""

class SolutionSwapToCorrectPos(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(1).
        """
        n = len(nums)

        # Iterate through all positions, continue swapping nums[i]'s to
        # their correct position (i + 1)'s.
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Check each updated elements in nums with true positive integer.
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1

        # If all elements in nums are correct, return the last one plus one.
        return n + 1


def main():
    # Output: 3
    nums = [1,2,0]
    print SolutionSwapToCorrectPos().firstMissingPositive(nums)

    # Output: 2
    nums = [3,4,-1,1]
    print SolutionSwapToCorrectPos().firstMissingPositive(nums)

    # Output: 1
    nums = [7,8,9,11,12]
    print SolutionSwapToCorrectPos().firstMissingPositive(nums)

    # Output: 1
    nums = []
    print SolutionSwapToCorrectPos().firstMissingPositive(nums)

    # Output: 2
    nums = [1]
    print SolutionSwapToCorrectPos().firstMissingPositive(nums)

    # Output: 3
    nums = [-1,4,2,1,9,10]
    print SolutionSwapToCorrectPos().firstMissingPositive(nums)


if __name__ == '__main__':
    main()
