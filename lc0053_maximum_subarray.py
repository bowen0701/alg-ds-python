"""Leetcode 53. Maximum Subarray
Easy

Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle.
"""

class SolutionDp(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Maximum subarray sum by Kadane's algorithm.

        Time complexity: O(n).
        Space complexity: O(n).
        """
        cur_max_sums = [0] * len(nums)
        cur_max_sums[0] = nums[0]
        max_sum = cur_max_sums[0]

        for i in range(1, len(nums)):
            # Compute max sum at i: to include max sum at i - 1 or not.
            cur_max_sums[i] = max(cur_max_sums[i - 1] + nums[i], nums[i])
            max_sum = max(max_sum, cur_max_sums[i])

        return max_sum


class SolutionIter(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Maximum subarray sum by Kadane's algorithm w/ optimized space.

        Time complexity: O(n).
        Space complexity: O(1).
        """        
        cur_max_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            # Compute max sum at i: to include max sum at i - 1 or not.
            cur_max_sum = max(cur_max_sum + nums[i], nums[i])
            max_sum = max(max_sum, cur_max_sum)

        return max_sum


def main():
    # Output: 6.
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print SolutionDp().maxSubArray(nums)
    print SolutionIter().maxSubArray(nums)


if __name__ == '__main__':
    main()
