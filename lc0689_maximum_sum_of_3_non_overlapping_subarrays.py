"""Leetcode 689. Maximum Sum of 3 Non-Overlapping Subarrays
Hard

URL: https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

In a given array nums of positive integers, find three non-overlapping subarrays
with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k
entries.

Return the result as a list of indices representing the starting position of each
interval (0-indexed). If there are multiple answers, return the lexicographically
smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices
[0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be
lexicographically larger.

Note:
- nums.length will be between 1 and 20000.
- nums[i] will be between 1 and 65535.
- k will be between 1 and floor(nums.length / 3).
"""

from typing import List


class SolutionLeftRightMaxSumMidIter(object):
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        Time complexity: O(n).
        Space complexity: O(n).
        """
        n = len(nums)
        max_sum = 0
        result = [0, 0, 0]

        # Compute cumsums before pos i: [0, n[0], n[0]+n[1], ...]
        cumsums = [0]

        for num in nums:
            cumsums.append(cumsums[-1] + num)

        # Compute left max sum's starting pos in range [0, r], with initial 0.
        # Interate through left intervals's right pos r.
        left_start_pos = [0] * n
        left_max_sum = cumsums[k] - cumsums[0]

        for r in range(k, n):
            if cumsums[r + 1] - cumsums[r + 1 - k] > left_max_sum:
                left_max_sum = cumsums[r + 1] - cumsums[r + 1 - k]
                left_start_pos[r] = r - k + 1
            else:
                left_start_pos[r] = left_start_pos[r - 1]

        # Compute right max sum's starting pos in range [l, n-1], with initial n - k.
        # Interate through right intervals's left pos l.
        right_start_pos = [n - k] * n
        right_max_sum = cumsums[n] - cumsums[n - k]

        for l in range(n - k - 1, -1, -1):
            if cumsums[l + k] - cumsums[l] >= right_max_sum:
                right_max_sum = cumsums[l + k] - cumsums[l]
                right_start_pos[l] = l
            else:
                right_start_pos[l] = right_start_pos[l + 1]

        # Check every possible middle interval and its left/right ones.
        # Interate through left pos m of middle intervals to update max sum.
        for m in range(k, n - 2 * k + 1):
            l = left_start_pos[m - 1]
            r = right_start_pos[m + k]

            subarrays_sum = ((cumsums[l + k] - cumsums[l]) +
                             (cumsums[m + k] - cumsums[m]) +
                             (cumsums[r + k] - cumsums[r]))
            if subarrays_sum > max_sum:
                max_sum = subarrays_sum
                result = [l, m, r]

        return result


def main():
    # Output: [0, 3, 5]
    nums = [1,2,1,2,6,7,5,1]
    k = 2
    print(SolutionLeftRightMaxSumMidIter().maxSumOfThreeSubarrays(nums, k))

    # Output: [0,2,4]
    nums = [9,8,7,6,2,2,2,2]
    k = 2
    print(SolutionLeftRightMaxSumMidIter().maxSumOfThreeSubarrays(nums, k))


if __name__ == '__main__':
    main()
