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


class SolutionLeftRightMaxSumMidIter(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        n = len(nums)
        max_sum = 0
        result = [0, 0, 0]

        # Compute cumsum before pos i: [0, n1, n1+n2, ...]
        cumsum = [0]

        for num in nums:
            cumsum.append(cumsum[-1] + num)

        # Compute left max sum's starting pos in range [0, i], with initial 0.
        # Interate through left intervals's right pos r.
        left_pos = [0] * n
        left_sum = cumsum[k] - cumsum[0]

        for r in range(k, n):
            if cumsum[r + 1] - cumsum[r + 1 - k] > left_sum:
                left_pos[r] = r + 1 - k
                left_sum = cumsum[r + 1] - cumsum[r + 1 - k]
            else:
                left_pos[r] = left_pos[r - 1]

        # Compute right max sum's starting pos in range [i, n-1], with initial n - k.
        # Interate through right intervals's left pos l.
        right_pos = [n - k] * n
        right_sum = cumsum[n] - cumsum[n - k]

        for l in range(n - k - 1, -1, -1):
            if cumsum[l + k] - cumsum[l] >= right_sum:
                right_pos[l] = l
                right_sum = cumsum[l + k] - cumsum[l]
            else:
                right_pos[l] = right_pos[l + 1]

        # Check every possible middle interval and its left/right ones.
        # Interate through left pos l of middle intervals to update max sum.
        for m in range(k, n - 2 * k + 1):
            l = left_pos[m - 1]
            r = right_pos[m + k]

            total_sum = ((cumsum[l + k] - cumsum[l]) +
                       (cumsum[m + k] - cumsum[m]) +
                       (cumsum[r + k] - cumsum[r]))
            if total_sum > max_sum:
                max_sum = total_sum
                result = [l, m, r]

        return result


def main():
    # Output: [0, 3, 5]
    nums = [1,2,1,2,6,7,5,1]
    k = 2
    print SolutionLeftRightMaxSumMidIter().maxSumOfThreeSubarrays(nums, k)

    # Output: [0,2,4]
    nums = [9,8,7,6,2,2,2,2]
    k = 2
    print SolutionLeftRightMaxSumMidIter().maxSumOfThreeSubarrays(nums, k)


if __name__ == '__main__':
    main()
