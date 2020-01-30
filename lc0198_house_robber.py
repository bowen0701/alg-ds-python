"""Leetcode 198. House Robber
Easy

URL: https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security system connected and it will
automatically contact the police if two adjacent houses were broken into
on the same night.

Given a list of non-negative integers representing the amount of money of
each house, determine the maximum amount of money you can rob tonight
without alerting the police.

Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and
             rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""

class SolutionRecur(object):
    def _recur(self, nums, n):
        if n < 0:
            return 0

        # To rob or not to rob house n: T[n] = max(nums[n] + T[n-2], T[n-1]).
        amount_in_n = nums[n] + self._recur(nums, n - 2)
        amount_ex_n = self._recur(nums, n - 1)
        return max(amount_in_n, amount_ex_n)

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(2^n).
        Space complexity: O(n).
        """
        # Apply top-down recursion.
        if not nums:
            return 0

        return self._recur(nums, len(nums) - 1)


class SolutionMemo(object):
    def _recurMemo(self, nums, n, T):
        if n < 0:
            return 0

        if T[n]:
            return T[n]

        # To rob or not to rob house n: T[n] = max(nums[n] + T[n-2], T[n-1]).
        amount_in_n = nums[n] + self._recurMemo(nums, n - 2, T)
        amount_ex_n = self._recurMemo(nums, n - 1, T)
        T[n] = max(amount_in_n, amount_ex_n)
        return T[n]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Apply top-down recursion with memoization.
        if not nums:
            return 0

        T = [None] * len(nums)
        return self._recurMemo(nums, len(nums) - 1, T)


class SolutionDp(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Apply bottom-up dynamic programming.
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        T = [0] * len(nums)

        # If only 1 or 2 houses, get the max amount.
        T[0] = nums[0]
        T[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            T[i] = max(nums[i] + T[i - 2], T[i - 1])

        return T[-1]


class SolutionIter(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Apply bottom-up dynamic programming w/ iteration.
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        # If only 1 or 2 houses, get the max amount.
        a = nums[0]
        b = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            a, b = b, max(nums[i] + a, b)

        return b


def main():
    # Output: 4.
    nums = [1,2,3,1]
    print SolutionRecur().rob(nums)
    print SolutionMemo().rob(nums)
    print SolutionDp().rob(nums)
    print SolutionIter().rob(nums)

    # Outpyt: 12.
    nums = [2,7,9,3,1]
    print SolutionRecur().rob(nums) 
    print SolutionMemo().rob(nums)
    print SolutionDp().rob(nums)
    print SolutionIter().rob(nums)


if __name__ == '__main__':
    main()
