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
    def _backtrack(self, result, temps, nums):
        if len(temps) == len(nums):
            # One of permutations is completed.
            result.append(temps[:])
            return None

        for i in range(len(nums)):
            # If num i was used, skip it; otherwise add it to temps.
            if nums[i] in temps:
                continue
            temps.append(nums[i])

            # Apply DFS by recursion with backtracking.
            self._backtrack(result, temps, nums)
            temps.pop()

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Time complexity: O(n * n!), where
          - n is the length of nums and for copying temps,
          - n! is for permutation.
        Space complexity: O(n * n!).
        """
        # Apply backtracking.
        result = []
        temps = []
        self._backtrack(result, temps, nums)
        return result


def main():
    nums = [1, 2, 3]
    print Solution().permute(nums)


if __name__ == '__main__':
    main()