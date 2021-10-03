"""Leetcode 300. Longest Increasing Subsequence
Medium

URL: https://leetcode.com/problems/longest-increasing-subsequence/

Given an unsorted array of integers, 
find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], 
therefore the length is 4. 

Note:
There may be more than one LIS combination, 
it is only necessary for you to return the length.
Your algorithm should run in O(n^2) complexity.
Follow up: Could you improve it to O(n*logn) time complexity?
"""

from typing import List


class SolutionRecur(object):
    def _LIS(self, nums: List[int], cur_idx: int, prev_max: int) -> int:
        # Base case: current index out of boundary.
        if cur_idx == len(nums):
            return 0

        # LIS is 1 + LIS including nums[cur_idx], if bigger than prev_max.
        lis_in = 0
        if nums[cur_idx] > prev_max:
            lis_in = 1 + self._LIS(nums, cur_idx + 1, nums[cur_idx])

        # LIS of nums[cur_idx+1:n], excluding nums[cur_idx].
        lis_out = self._LIS(nums, cur_idx + 1, prev_max)

        return max(lis_in, lis_out)

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time limit exceeded.

        Time complexity: O(2^n).
        Space complexity: O(n^2).
        """
        # Apply top-down recursion starting from left index.
        cur_idx = 0
        prev_max = -float('inf')
        return self._LIS(nums, cur_idx, prev_max)


class SolutionMemo(object):
    def _LIS(self, nums: List[int], prev_idx: int, cur_idx: int, T: List[List[int]]) -> int:
        # Base case: current index out of boundary.
        if cur_idx == len(nums):
            return 0

        if T[prev_idx][cur_idx] >= 0:
            return T[prev_idx][cur_idx]

        # LIS is 1 + LIS including nums[cur_idx], if bigger than prev_max.
        lis_in = 0
        if prev_idx < 0 or nums[cur_idx] > nums[prev_idx]:
            lis_in = 1 + self._LIS(nums, cur_idx, cur_idx + 1, T)

        # LIS of nums[cur_idx+1:n], excluding nums[cur_idx].
        lis_out = self._LIS(nums, prev_idx, cur_idx + 1, T)

        T[prev_idx][cur_idx] = max(lis_in, lis_out)
        return T[prev_idx][cur_idx]

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time limit exceeded.

        Time complexity: O(n^2).
        Space complexity: O(n^2).
        """
        # Apply top-down recursion with memoization, starting from left index.
        prev_idx, cur_idx = -1, 0

        # Use memoization table T where T[i][j] is LIS from index j with previous chosen index i.
        n = len(nums)
        T = [[-float('inf')] * n for _ in range(n)]
        return self._LIS(nums, prev_idx, cur_idx, T)


class SolutionDP(object):
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time complexity: O(n^2), where n is the length of the nums.
        Space complexity: O(n).
        """
        # Edge case.
        if not nums:
            return 0

        # Apply bottom-up DP with table T with T[i] denoting LIS up to i.
        n = len(nums)

        T = [1] * n

        # Apply two pointer method: for each r, check if num[l] < num[r], l < r.
        for r in range(n):
            for l in range(r):
                if nums[l] < nums[r] and T[l] + 1 > T[r]:
                    T[r] = T[l] + 1

        # Return max length.
        return max(T)


class SolutionBinarySearchGreedy(object):
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time complexity: O(n*logn), where n is the length of the nums.
        Space complexity: O(n).
        """
        # Edge case.
        if not nums:
            return 0

        # Store the smallest tails T of all increasing subsequences with len i+1 in T[i]:
        # (1) If n is larger than all smallest tails, append it and increase length by 1.
        # (2) if T[i-1] < n <= T[i], update T[i]
        # This will maintain the tails invariant. Then the result is just the size.
        T = [0] * len(nums)
        size = 0
 
        for n in nums:
            # Apply binary search to append to the last or update T[i].
            # [4,5,0,0]
            left, right = 0, size
            while left < right:
                mid = left + (right - left) // 2
                if T[mid] < n:
                    left = mid + 1
                else:
                    right = mid

            T[left] = n

            size = max(left + 1, size)

        return size


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
    print('By binary search: {}'.format(time.time() - start_time))

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
    print('By binary search: {}'.format(time.time() - start_time))

    # Output: 1
    nums = [7,7,7,7,7,7,7]

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
    print('By binary search: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
