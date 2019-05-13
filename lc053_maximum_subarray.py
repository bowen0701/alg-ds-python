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
        """
        sums = [0] * len(nums)
        sums[0] = nums[0]
        max_sum = sums[0]

        for i in range(1, len(sums)):
        	# Compute current max subarray sum before pos i.  
        	sums[i] = max(sums[i - 1] + nums[i], nums[i])
        	# Track global max sum before pos i.
        	max_sum = max(max_sum, sums[i])

        return max_sum


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # Output: 6.

    print SolutionDp().maxSubArray(nums)


if __name__ == '__main__':
    main()
