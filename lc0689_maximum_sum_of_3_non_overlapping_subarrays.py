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


class SolutionCusumLeftRightMiddleSlidingWindow(object):
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        Time complexity: O(n).
        Space complexity: O(n).
        """
        n = len(nums)
        result = [0, 0, 0]

        # Compute cumsums before pos i: [0, n[0], n[0]+n[1], ...]
        cumsums = [0]

        for num in nums:
            cumsums.append(cumsums[-1] + num)

        # Memorize max left sum [0, r]'s starting pos, with > condition.
        left_start_pos = [0] * n
        max_left_sum = cumsums[k] - cumsums[0]

        for r in range(k, n):
            if cumsums[r + 1] - cumsums[r + 1 - k] > max_left_sum:
                max_left_sum = cumsums[r + 1] - cumsums[r + 1 - k]
                left_start_pos[r] = r - k + 1
            else:
                left_start_pos[r] = left_start_pos[r - 1]

        # Memorize max right sum [l, n-1]'s starting pos, with >= condition. 
        right_start_pos = [n - k] * n
        max_right_sum = cumsums[n] - cumsums[n - k]

        for l in range(n - k - 1, -1, -1):
            if cumsums[l + k] - cumsums[l] >= max_right_sum:
                max_right_sum = cumsums[l + k] - cumsums[l]
                right_start_pos[l] = l
            else:
                right_start_pos[l] = right_start_pos[l + 1]

        # Slide middle window's starting pos with max left/righgt sums.
        max_three_sum = -float('inf')

        for m in range(k, n - 2 * k + 1):
            l = left_start_pos[m - 1]
            r = right_start_pos[m + k]

            three_sum = (
                cumsums[l + k] - cumsums[l]
                + cumsums[m + k] - cumsums[m]
                + cumsums[r + k] - cumsums[r]
            )
            if three_sum > max_three_sum:
                max_three_sum = three_sum
                result = [l, m, r]

        return result


class SolutionLeftMiddleRightSlidingWindows(object):
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        Time complexity: O(n).
        Space complexity: O(1).
        """
        n = len(nums)

        left_sum, mid_sum, right_sum = (
            sum(nums[:k]), sum(nums[k:2*k]), sum(nums[2*k:3*k])
        )
        
        max_one_sum, max_two_sum, max_three_sum = (
            left_sum, left_sum + mid_sum, left_sum + mid_sum + right_sum
        )

        one_start_poc, two_start_poc, three_start_poc = [0], [0, k], [0, k, 2*k]

        # Slide to keep 3 windows moving and memorize max one & two window sums.
        for l in range(1, n - 3*k + 1):
            left_sum += nums[l + k - 1] - nums[l - 1]
            mid_sum += nums[l + 2*k - 1] - nums[l + k - 1]
            right_sum += nums[l + 3*k - 1] - nums[l + 2*k - 1]

            if left_sum > max_one_sum:
                max_one_sum = left_sum
                one_start_poc = [l]

            if max_one_sum + mid_sum > max_two_sum:
                max_two_sum = max_one_sum + mid_sum
                two_start_poc = one_start_poc + [l + k]

            if max_two_sum + right_sum > max_three_sum:
                max_three_sum = max_two_sum + right_sum
                three_start_poc = two_start_poc + [l + 2*k]

        return three_start_poc


def main():
    # Output: [0, 3, 5]
    nums = [1,2,1,2,6,7,5,1]
    k = 2
    print(SolutionCusumLeftRightMiddleSlidingWindow().maxSumOfThreeSubarrays(nums, k))
    print(SolutionLeftMiddleRightSlidingWindows().maxSumOfThreeSubarrays(nums, k))

    # Output: [0,2,4]
    nums = [9,8,7,6,2,2,2,2]
    k = 2
    print(SolutionCusumLeftRightMiddleSlidingWindow().maxSumOfThreeSubarrays(nums, k))
    print(SolutionLeftMiddleRightSlidingWindows().maxSumOfThreeSubarrays(nums, k))


if __name__ == '__main__':
    main()
