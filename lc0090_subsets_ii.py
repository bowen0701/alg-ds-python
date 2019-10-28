"""Leetcode 90. Subsets II
Medium

URL: https://leetcode.com/problems/subsets-ii/

Given a collection of integers that might contain duplicates, nums,
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class SolutionBacktrack(object):
    def _backtrack(self, result, temp, start, nums):
        # Use shallow copy.
        result.append(temp[:])

        # Iterate starting from start.
        for i in range(start, len(nums)):
            # Avoid duplicate by checking the previous num.
            if i > start or nums[i] == nums[i - 1]:
                continue

            temp.append(nums[i])
            self._backtrack(result, temp, i + 1, nums)

            # Pop for backtracking.
            temp.pop()

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Time complexity: O(n*2^n).
        Space complexity: O(2^n).
        """
        # Sort nums to avoid duplicates.
        nums.sort()

        result = []
        temp = []
        start = 0
        self._backtrack(result, temp, start, nums)
        return result


def main():
    # Output = [[2],[1],[1,2,2],[2,2],[1,2],[]]
    nums = [1,2,2]
    print SolutionBacktrack().subsetsWithDup(nums)


if __name__ == '__main__':
    main()
