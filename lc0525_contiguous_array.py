"""Leetcode 525. Contiguous Array
Medium

URL: https://leetcode.com/problems/contiguous-array/

Given a binary array, find the maximum length of a contiguous subarray
with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number
of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with
equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""


class SolutionDiffsumIdxDict(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Edge case.
        if len(nums) <= 1:
            return 0

        max_len = 0

        # Create a dict:diffsum->idx.
        diffsum_idx_d = {0: -1}
        diffsum = 0
        for idx, num in enumerate(nums):
            # Get diff by converting 0 to -1 and 1 to 1.
            diffsum += 2 * num - 1

            # Check if diffsum exists, update max_len.
            if diffsum in diffsum_idx_d:
                max_len = max(max_len, idx - diffsum_idx_d[diffsum])
            else:
                diffsum_idx_d[diffsum] = idx

        return max_len


def main():
    # Output: 2
    nums = [0,1]
    print SolutionDiffsumIdxDict().findMaxLength(nums)

    # Output: 2
    nums = [0,1,0]
    print SolutionDiffsumIdxDict().findMaxLength(nums)


if __name__ == '__main__':
    main()
