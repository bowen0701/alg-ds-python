"""Leetcode 674. Longest Continuous Increasing Subsequence
Easy

URL: https://leetcode.com/problems/longest-continuous-increasing-subsequence/

Given an unsorted array of integers nums, return the length of the longest
continuous increasing subsequence (i.e. subarray). The subsequence must be
strictly increasing.

A continuous increasing subsequence is defined by two indices l and r
(l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]
and for each l <= i < r, nums[i] < nums[i + 1].

Example 1:
Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with
length 3. Even though [1,3,5,7] is an increasing subsequence, it is not
continuous as elements 5 and 7 are separated by element 4.

Example 2:
Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with
length 1. Note that it must be strictly increasing.

Constraints:
- 1 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
"""

from typing import List


class SolutionRecur:
    def _lcis_recur(self, nums: List[int], i: int) -> int:
        # Base case: first element, LCIS length is 1.
        if i == 0:
            return 1

        # Top-down: shrink i toward base case i=0; bottom-up DP iterates i=1,..., n-1.
        # If strictly increasing, extend LCIS ending at i-1.
        if nums[i - 1] < nums[i]:
            return self._lcis_recur(nums, i - 1) + 1
        else:
            return 1

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        Time complexity: O(n^2).
          - max() iterates n elements, each triggering a recur chain up to O(n).
        Space complexity: O(n).
        """
        n = len(nums)
        return max(self._lcis_recur(nums, i) for i in range(n))


class SolutionMemo:
    def _lcis_memo(
        self,
        nums: List[int],
        i: int,
        T: List[int],
    ) -> int:
        # Base case: first element, LCIS length is 1.
        if i == 0:
            return 1

        # Check memo table.
        if T[i] > 0:
            return T[i]

        # Top-down: shrink i toward base case i=0; bottom-up DP iterates i=1,..., n-1.
        # If strictly increasing, extend LCIS ending at i-1.
        if nums[i - 1] < nums[i]:
            T[i] = self._lcis_memo(nums, i - 1, T) + 1
        else:
            T[i] = 1

        return T[i]

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(n).
        """
        n = len(nums)
        T = [0] * n
        return max(self._lcis_memo(nums, i, T) for i in range(n))


class SolutionDP:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(n).
        """
        n = len(nums)

        # T[i] = length of LCIS ending at index i.
        T = [1] * n

        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                T[i] = T[i - 1] + 1

        return max(T)


class SolutionIter:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(1).
        """
        result = 1
        cur_len = 1

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                cur_len += 1
                result = max(result, cur_len)
            else:
                # Reset LCIS starting from i.
                cur_len = 1

        return result


def main():
    # Output: 3
    nums = [1, 3, 5, 4, 7]
    print(SolutionRecur().findLengthOfLCIS(nums))
    print(SolutionMemo().findLengthOfLCIS(nums))
    print(SolutionDP().findLengthOfLCIS(nums))
    print(SolutionIter().findLengthOfLCIS(nums))

    # Output: 1
    nums = [2, 2, 2, 2, 2]
    print(SolutionRecur().findLengthOfLCIS(nums))
    print(SolutionMemo().findLengthOfLCIS(nums))
    print(SolutionDP().findLengthOfLCIS(nums))
    print(SolutionIter().findLengthOfLCIS(nums))

    # Output: 5
    nums = [1, 2, 3, 4, 5]
    print(SolutionRecur().findLengthOfLCIS(nums))
    print(SolutionMemo().findLengthOfLCIS(nums))
    print(SolutionDP().findLengthOfLCIS(nums))
    print(SolutionIter().findLengthOfLCIS(nums))


if __name__ == '__main__':
    main()
