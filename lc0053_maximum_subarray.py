"""Leetcode 53. Maximum Subarray
Medium

URL: https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the subarray with the largest sum, and return
its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach, which is more subtle.
"""

from typing import List


class SolutionRecur:
    def _max_subarray_sum(self, nums: List[int], i: int) -> int:
        """Max subarray sum ending at index i, considering nums[:i+1]."""
        if i == 0:
            return nums[0]

        # Extend previous subarray or restart at nums[i].
        return max(self._max_subarray_sum(nums, i - 1) + nums[i], nums[i])

    def maxSubArray(self, nums: List[int]) -> int:
        """
        Time complexity: O(2^n).
        Space complexity: O(n).
        """
        return max(self._max_subarray_sum(nums, i) for i in range(len(nums)))


class SolutionMemo:
    def _max_subarray_sum(self, nums: List[int], i: int, memo: List[int]) -> int:
        """Max subarray sum ending at index i, considering nums[:i+1], with memoization."""
        if i == 0:
            return nums[0]

        if memo[i] is not None:
            return memo[i]

        memo[i] = max(self._max_subarray_sum(nums, i - 1, memo) + nums[i], nums[i])
        return memo[i]

    def maxSubArray(self, nums: List[int]) -> int:
        """
        Time complexity: O(n).
        Space complexity: O(n).
        """
        memo = [None] * len(nums)
        return max(self._max_subarray_sum(nums, i, memo) for i in range(len(nums)))


class SolutionDP:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Maximum subarray sum by Kadane's algorithm.

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # T[i]: max subarray sum ending at index i.
        T = [0] * len(nums)
        T[0] = nums[0]
        max_sum = T[0]

        for i in range(1, len(nums)):
            # Compute max sum at i: to include previous subarray or not.
            # When cur_max_sum < 0, it's better to restart the subarray.
            T[i] = max(T[i - 1] + nums[i], nums[i])
            max_sum = max(max_sum, T[i])

        return max_sum


class SolutionIter:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Maximum subarray sum by Kadane's algorithm w/ optimized space.

        Time complexity: O(n).
        Space complexity: O(1).
        """        
        cur_max_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            # Compute max sum at i: to include previous subarray or not?
            # When cur_max_sum < 0, it's better to restart the subarray.
            cur_max_sum = max(cur_max_sum + nums[i], nums[i])
            max_sum = max(max_sum, cur_max_sum)

        return max_sum


def main():
    # Output: 6.
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(SolutionRecur().maxSubArray(nums))
    print(SolutionMemo().maxSubArray(nums))
    print(SolutionDP().maxSubArray(nums))
    print(SolutionIter().maxSubArray(nums))


if __name__ == '__main__':
    main()
