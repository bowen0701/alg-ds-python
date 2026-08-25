"""Leetcode 213. House Robber II
Medium

URL: https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed. All houses at this place
are arranged in a circle. That means the first house is the neighbor of
the last one. Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police if two adjacent houses were
broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting
the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000
"""


class SolutionRecur:
    def _recur(self, nums, start, end):
        """House Robber I recursion on nums[start:end+1]."""
        if start > end:
            return 0

        # To rob or not to rob house end.
        amount_in = nums[end] + self._recur(nums, start, end - 2)
        amount_ex = self._recur(nums, start, end - 1)
        return max(amount_in, amount_ex)

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(2^n).
        Space complexity: O(n).
        """
        # Apply top-down recursion.
        # Since houses are in a circle, house 0 and house n-1 can't both be robbed.
        # Split into two subproblems: rob [0, n-2] or rob [1, n-1].
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(
            self._recur(nums, 0, len(nums) - 2),
            self._recur(nums, 1, len(nums) - 1),
        )


class SolutionMemo:
    def _recur(self, nums, start, end, T):
        """House Robber I recursion + memo on nums[start:end+1]."""
        if start > end:
            return 0

        if T[end] is not None:
            return T[end]

        # To rob or not to rob house end.
        amount_in = nums[end] + self._recur(nums, start, end - 2, T)
        amount_ex = self._recur(nums, start, end - 1, T)
        T[end] = max(amount_in, amount_ex)
        return T[end]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Apply top-down recursion with memoization.
        # Since houses are in a circle, house 0 and house n-1 can't both be robbed.
        # Split into two subproblems: rob [0, n-2] or rob [1, n-1].
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        T1 = [None] * len(nums)
        T2 = [None] * len(nums)
        return max(
            self._recur(nums, 0, len(nums) - 2, T1),
            self._recur(nums, 1, len(nums) - 1, T2),
        )


class SolutionDP:
    def _rob_range(self, nums, start, end):
        """House Robber I on nums[start:end+1]."""
        if start == end:
            return nums[start]

        T = [0] * len(nums)

        # If only 1 or 2 houses, get the max amount.
        T[start] = nums[start]
        T[start + 1] = max(nums[start], nums[start + 1])

        for i in range(start + 2, end + 1):
            T[i] = max(nums[i] + T[i - 2], T[i - 1])

        return T[end]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Apply bottom-up DP.
        # Since houses are in a circle, house 0 and house n-1 can't both be robbed.
        # Split into two subproblems: rob [0, n-2] or rob [1, n-1].
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(
            self._rob_range(nums, 0, len(nums) - 2),
            self._rob_range(nums, 1, len(nums) - 1),
        )


class SolutionIter:
    def _rob_range(self, nums, start, end):
        """House Robber I on nums[start:end+1] with O(1) space."""
        if start == end:
            return nums[start]

        a = nums[start]
        b = max(nums[start], nums[start + 1])

        for i in range(start + 2, end + 1):
            a, b = b, max(nums[i] + a, b)

        return b

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Apply bottom-up DP w/ iteration.
        # Since houses are in a circle, house 0 and house n-1 can't both be robbed.
        # Split into two subproblems: rob [0, n-2] or rob [1, n-1].
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(
            self._rob_range(nums, 0, len(nums) - 2),
            self._rob_range(nums, 1, len(nums) - 1),
        )


def main():
    # Output: 3.
    nums = [2, 3, 2]
    print(SolutionRecur().rob(nums))
    print(SolutionMemo().rob(nums))
    print(SolutionDP().rob(nums))
    print(SolutionIter().rob(nums))

    # Output: 4.
    nums = [1, 2, 3, 1]
    print(SolutionRecur().rob(nums))
    print(SolutionMemo().rob(nums))
    print(SolutionDP().rob(nums))
    print(SolutionIter().rob(nums))

    # Output: 3.
    nums = [1, 2, 3]
    print(SolutionRecur().rob(nums))
    print(SolutionMemo().rob(nums))
    print(SolutionDP().rob(nums))
    print(SolutionIter().rob(nums))


if __name__ == '__main__':
    main()
