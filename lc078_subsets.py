"""Leetcode 78. Subsets
Medium

URL: https://leetcode.com/problems/subsets/

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class SolutionBackTrack(object):
    def _backtrack(self, result, temps, nums, start):
        result.append(temps[:])

        for i in range(start, len(nums)):
            temps.append(nums[i])
            self._backtrack(result, temps, nums, i + 1)
            temps.pop()

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Time complexity: O(n * 2^n).
        Space complexity: O(n * 2^n).
        """
        result = []
        self._backtrack(result, [], nums, 0)
        return result


def main():
    nums = [1, 2, 3]
    print Solution().subsets(nums)


if __name__ == '__main__':
    main()
