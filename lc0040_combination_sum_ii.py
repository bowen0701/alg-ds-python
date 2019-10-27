"""Leetcode 40. Combination Sum II
Medium

URL: https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:
- All numbers (including target) will be positive integers.
- The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

class SolutionBacktrack(object):
    def _backtrack(self, result, temp, start, target, candidates):
        if target < 0:
            # No way to further combine numbers.
            return None

        if target == 0:
            # Use shallow copy.
            result.append(temp[:])
            return None

        # From start to the end of candidates.
        for i in range(start, len(candidates)):
            # Avoid duplicate by checking the previous cadidate.
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            temp.append(candidates[i])

            # Use next index i+1 since we cannot use same element.
            self._backtrack(result, temp, i + 1,
                            target - candidates[i], candidates)

            # Pop for backtracking.
            temp.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

        Apply backtracking with sorting to avoid duplicates.

        Time complexity: O(2^n).
        Space complexity: O(k).
        """
        # Sort candidates to avoid duplicates.
        candidates.sort()

        result = []
        temp = []
        start = 0
        self._backtrack(result, temp, start, target, candidates)
        return result


def main():
    # Output: [[1, 7],[1, 2, 5],[2, 6],[1, 1, 6]]
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print SolutionBacktrack().combinationSum2(candidates, target)

    # Output: [[1, 2, 2],[5]]
    candidates = [2,5,2,1,2]
    target = 5
    print SolutionBacktrack().combinationSum2(candidates, target)


if __name__ == '__main__':
    main()
