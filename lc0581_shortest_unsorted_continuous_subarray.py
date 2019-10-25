"""Leetcode 581. Shortest Unsorted Continuous Subarray
Easy

URL: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

Given an integer array, you need to find one continuous subarray that if you only
sort this subarray in ascending order, then the whole array will be sorted in
ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
whole array sorted in ascending order.

Note:
- Then length of the input array is in range [1, 10,000].
- The input array may contain duplicates, so ascending order here means <=.
"""

class SolutionSort(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Sort the nums and check element match from left and from right.

        Time complexity: O(n*logn).
        Space complexity: O(n).
        """
        # Store sorted nums in a new list.
        sorted_nums = sorted(nums)

        # Iterate from left/right to check element match of nums and sorted nums.
        n = len(nums)
        l, r = 0, n - 1

        while l < n and nums[l] == sorted_nums[l]:
            l += 1

        while r > l and nums[r] == sorted_nums[r]:
            r -= 1

        return r - (l - 1)


class SolutionMinRHSMaxLHS(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        For a sorted list: min is the minimum on RHS; similarly with max.
        create min RHS and max LHS lists, and then check their element match.

        Time complexity: O(n*logn).
        Space complexity: O(n).
        """
        n = len(nums)

        # Create min RHS list from right to left.
        min_r = float('inf')
        min_rhs = [None] * n

        for r in range(n - 1, -1, -1):
            min_r = min(min_r, nums[r])
            min_rhs[r] = min_r

        # Create max LHS list from left to right.
        max_l = -float('inf')
        max_lhs = [None] * n

        for l in range(n):
            max_l = max(max_l, nums[l])
            max_lhs[l] = max_l

        # Iterate from left/right to check match of nums and min RHS / max LHS.
        l, r = 0, n - 1

        while l < n and nums[l] == min_rhs[l]:
            l += 1

        while r > l and nums[r] == max_lhs[r]:
            r -= 1

        return r - (l - 1)


def main():
    # Output: 5
    nums = [2, 6, 4, 8, 10, 9, 15]
    print SolutionSort().findUnsortedSubarray(nums)
    print SolutionMinRHSMaxLHS().findUnsortedSubarray(nums)


if __name__ == '__main__':
    main()
