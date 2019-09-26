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

class SolutionBacktrack(object):
    def _backtrack(self, result, temps, nums, start):
        result.append(temps[:])

        # For start, add nums[i] and DFS i+1, and then pop for backtrack.
        for i in range(start, len(nums)):
            temps.append(nums[i])
            self._backtrack(result, temps, nums, i + 1)
            temps.pop()

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Time complexity: O(n*2^n).
        Space complexity: O(2^n).
        """
        # Apply backtracking.
        result = []
        temps = []

        start = 0
        self._backtrack(result, temps, nums, start)
        
        return result


class SolutionBFS(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Time complexity: O(n * 2^n).
        Space complexity: O(2^n).
        """
        # Apply DFS.
        result = [[]]
        for n in nums:
            # Accumulate result: [[], [1], [2], [1, 2], [3], [1, 3], [1, 2, 3]].
            result += [res + [n] for res in result]
        return result


def main():
    import time

    nums = [1, 2, 3]
    
    start_time = time.time()
    print 'Backtracking:', SolutionBacktrack().subsets(nums)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'BFS:', SolutionBFS().subsets(nums)
    print 'Time:', time.time() - start_time


if __name__ == '__main__':
    main()
