"""Leetcode 300. Longest Increasing Subsequence
Medium

URL: https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly
increasing subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101],
therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4

Follow up: Can you come up with an algorithm that runs in O(n log(n))
time complexity?
"""

from typing import List


class SolutionRecur:
    def _lis_recur(self, nums: List[int], prev_idx: int, cur_idx: int) -> int:
        # Base case: current index out of boundary.
        if cur_idx == len(nums):
            return 0

        # Include nums[cur_idx], then solve LIS of nums[cur_idx+1:n].
        # Valid if bigger than last included (or none included yet).
        lis_in = 0
        if prev_idx < 0 or nums[cur_idx] > nums[prev_idx]:
            lis_in = 1 + self._lis_recur(nums, cur_idx, cur_idx + 1)

        # Exclude nums[cur_idx], solve LIS of nums[cur_idx+1:n] with same prev.
        lis_out = self._lis_recur(nums, prev_idx, cur_idx + 1)

        return max(lis_in, lis_out)

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time limit exceeded.

        Time complexity: O(2^n).
        Space complexity: O(n).
        """
        # Suffix subproblem: LIS in nums[cur_idx:n] with last chosen at prev_idx.
        # At each step, include or exclude nums[cur_idx], shrink toward base cur_idx=n.
        #   prev_idx: index of last included element (-1 = none yet).
        #   cur_idx: index we're deciding to include or exclude.
        prev_idx, cur_idx = -1, 0
        return self._lis_recur(nums, prev_idx, cur_idx)


class SolutionMemo:
    def _lis_memo(
        self,
        nums: List[int],
        prev_idx: int,
        cur_idx: int,
        T: List[List[int]],
    ) -> int:
        # Base case: current index out of boundary.
        if cur_idx == len(nums):
            return 0

        if T[prev_idx][cur_idx] >= 0:
            return T[prev_idx][cur_idx]

        # Include nums[cur_idx], then solve LIS of nums[cur_idx+1:n].
        # Valid if bigger than last included (or none included yet).
        lis_in = 0
        if prev_idx < 0 or nums[cur_idx] > nums[prev_idx]:
            lis_in = 1 + self._lis_memo(nums, cur_idx, cur_idx + 1, T)

        # Exclude nums[cur_idx], solve LIS of nums[cur_idx+1:n] with same prev.
        lis_out = self._lis_memo(nums, prev_idx, cur_idx + 1, T)

        T[prev_idx][cur_idx] = max(lis_in, lis_out)
        return T[prev_idx][cur_idx]

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time limit exceeded.

        Time complexity: O(n^2).
        Space complexity: O(n^2).
        """
        # Suffix subproblem: LIS in nums[cur_idx:n] with last chosen at prev_idx.
        # Same as SolutionRecur + memo table T[prev_idx][cur_idx].
        #   prev_idx: index of last included element (-1 = none yet).
        #   cur_idx: index we're deciding to include or exclude.
        prev_idx, cur_idx = -1, 0

        # T[i][j]: LIS from index j with previous chosen index i.
        n = len(nums)
        T = [[-float('inf')] * n for _ in range(n)]
        return self._lis_memo(nums, prev_idx, cur_idx, T)


class SolutionDP:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time complexity: O(n^2), where n is the length of the nums.
        Space complexity: O(n).
        """
        # Edge case.
        if not nums:
            return 0

        # Prefix subproblem: T[r] = LIS of nums[0:r+1], ending at index r.
        # For each r, scan all l < r: if nums[l] < nums[r], extend LIS ending at l.
        n = len(nums)

        T = [1] * n

        for r in range(1, n):
            for l in range(r):
                if nums[l] < nums[r]:
                    T[r] = max(T[r], T[l] + 1)

        return max(T)


class SolutionBinarySearchGreedy:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time complexity: O(n*logn), where n is the length of the nums.
        Space complexity: O(n).
        """
        # Edge case.
        if not nums:
            return 0

        # Prefix subproblem: process nums[0:i+1] left to right, maintain tails invariant.
        # T[i]: smallest tail for that length i+1
        #   (1) If n is larger than all tails, append it (new longest subsequence).
        #   (2) If T[i-1] < n <= T[i], update T[i] (smaller tail for same length).
        T = [0] * len(nums)
        n_piles = 0

        for n in nums:
            # Binary search for insertion position in sorted T[0:n_piles].
            # Finds leftmost pile whose top >= n (the card).
            l, r = 0, n_piles
            while l < r:
                mid = l + (r - l) // 2
                if T[mid] < n:
                    # Pile top too small, search right half.
                    l = mid + 1
                else:
                    # Pile top >= n, could place here; search left for earlier pile.
                    r = mid

            # pos = pile index to place the card.
            pos = l
            T[pos] = n

            # If pos == n_piles, we opened a new pile; otherwise no change.
            n_piles = max(pos + 1, n_piles)

        return n_piles


class SolutionBinarySearchBisectLeftGreedy:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time complexity: O(n*logn), where n is the length of the nums.
        Space complexity: O(n).
        """
        from bisect import bisect_left

        # Edge case.
        if not nums:
            return 0

        # Prefix subproblem: same as SolutionBinarySearchGreedy + bisect_left.
        # T[i]: smallest tail for that length i+1.
        T = [0] * len(nums)
        n_piles = 0

        for n in nums:
            # bisect_left finds insertion position in sorted T[0:n_piles].
            # Finds leftmost pile whose top >= n (the card).
            pos = bisect_left(T, n, lo=0, hi=n_piles)
            T[pos] = n

            # If pos == n_piles, we opened a new pile; otherwise no change.
            n_piles = max(pos + 1, n_piles)

        return n_piles


def main():
    import time

    # Output: 4.
    nums = [10, 9, 2, 5, 3, 7, 101, 6]

    start_time = time.time()
    print(SolutionRecur().lengthOfLIS(nums))
    print('By recur: {}'.format(time.time() - start_time))

    start_time = time.time()
    print(SolutionMemo().lengthOfLIS(nums))
    print('By memo: {}'.format(time.time() - start_time))

    start_time = time.time()   
    print(SolutionDP().lengthOfLIS(nums))
    print('By DP: {}'.format(time.time() - start_time))

    start_time = time.time()   
    print(SolutionBinarySearchGreedy().lengthOfLIS(nums))
    print('By binary search greedy: {}'.format(time.time() - start_time))

    start_time = time.time()   
    print(SolutionBinarySearchBisectLeftGreedy().lengthOfLIS(nums))
    print('By binary search bisect greedy: {}'.format(time.time() - start_time))

    # Output: 4
    nums = [0, 1, 0, 3, 2, 3]

    start_time = time.time()
    print(SolutionRecur().lengthOfLIS(nums))
    print('By recur: {}'.format(time.time() - start_time))

    start_time = time.time()
    print(SolutionMemo().lengthOfLIS(nums))
    print('By memo: {}'.format(time.time() - start_time))

    start_time = time.time()
    print(SolutionDP().lengthOfLIS(nums))
    print('By DP: {}'.format(time.time() - start_time))

    start_time = time.time()
    print(SolutionBinarySearchGreedy().lengthOfLIS(nums))
    print('By binary search greedy: {}'.format(time.time() - start_time))

    start_time = time.time()   
    print(SolutionBinarySearchBisectLeftGreedy().lengthOfLIS(nums))
    print('By binary search bisect greedy: {}'.format(time.time() - start_time))

    # Output: 1
    nums = [7, 7, 7, 7, 7, 7, 7]

    start_time = time.time()
    print(SolutionRecur().lengthOfLIS(nums))
    print('By recur: {}'.format(time.time() - start_time))

    start_time = time.time()
    print(SolutionMemo().lengthOfLIS(nums))
    print('By memo: {}'.format(time.time() - start_time))

    start_time = time.time()   
    print(SolutionDP().lengthOfLIS(nums))
    print('By DP: {}'.format(time.time() - start_time))

    start_time = time.time()   
    print(SolutionBinarySearchGreedy().lengthOfLIS(nums))
    print('By binary search greedy: {}'.format(time.time() - start_time))

    start_time = time.time()   
    print(SolutionBinarySearchBisectLeftGreedy().lengthOfLIS(nums))
    print('By binary search bisect greedy: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
