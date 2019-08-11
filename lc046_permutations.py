"""Leetcode 46. Permutations
Medium

URL: https://leetcode.com/problems/permutations/

Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution(object):
    def _backtrack(self, permutations, temps, nums):
        if len(temps) == len(nums):
            # One of permutations is completed.
            permutations.append(temps[:])
            return None

        for i in range(len(nums)):
            # If num i was used, skip it; otherwise add it to temps.
            if nums[i] in temps:
                continue
            temps.append(nums[i])

            # Apply DFS by recursion with backtracking.
            self._backtrack(permutations, temps, nums)
            temps.pop()

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Time complexity: O(n * n!), where
          - the 1st component, n, is for copying temps,
          - the 2nd component, n!, is for permutation.
        Space complexity: O(n).
        """
        permutations = []
        self._backtrack(permutations, [], nums)
        return permutations


def main():
    nums = [1, 2, 3]
    print Solution().permute(nums)


if __name__ == '__main__':
    main()
