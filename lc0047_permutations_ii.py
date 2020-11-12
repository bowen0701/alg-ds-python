"""Leetcode 47. Permutations II
Medium

URL: https://leetcode.com/problems/permutations-ii/

Given a collection of numbers that might contain duplicates,
return all possible unique permutations.

Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class SolutionSortBacktrack(object):
    def _backtrack(self, result, temp, is_used, nums):
        if len(temp) == len(nums):
            # Once a permutation is completed, shallow copy it to result.
            result.append(temp[:])
            return None

        for i in range(len(nums)):
            if (is_used[i] or 
                (i > 0 and nums[i] == nums[i - 1] and is_used[i - 1])):
                continue

            is_used[i] = True
            temp.append(nums[i])
            self._backtrack(result, temp, is_used, nums)

            # Backtracking.
            is_used[i] = False
            temp.pop()

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Time complexity: O(n*n!), where
          - n is the length of nums for copying temp,
          - n! is for permutation.
        Space complexity: O(n*n!).
        """
        # Sort to avoid duplicates.
        nums.sort()

        result = []
        temp = []

        # Use used array to memorize usage in backtracking.
        is_used = [False] * len(nums)

        self._backtrack(result, temp, is_used, nums)
        return result


def main():
    # Output: [[1,1,2],[1,2,1],[2,1,1]]
    nums = [1,1,2,4]
    print SolutionSortBacktrack().permuteUnique(nums)


if __name__ == '__main__':
    main()
