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
    def _backtrack(self, result, temp, nums):
        if len(temp) == len(nums):
            # Once a permutation is completed, shallow copy it to result.
            result.append(temp[:])
            return None

        for i in range(len(nums)):
            # If num[i] was used, skip it.
            if nums[i] in temp:
                continue
            
            temp.append(nums[i])
            self._backtrack(result, temp, nums)

            # Pop for backtracking.
            temp.pop()

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Time complexity: O(n*n!), where
          - n is the length of nums for copying temp,
          - n! is for permutation.
        Space complexity: O(n*n!).
        """
        # Apply backtracking.
        result = []
        temp = []
        self._backtrack(result, temp, nums)
        return result


def main():
    nums = [1, 2, 3]
    print Solution().permute(nums)


if __name__ == '__main__':
    main()
