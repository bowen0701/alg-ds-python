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
    def _backtrack(self, result, temp, start, nums):
        # Use shallow copy.
        result.append(temp[:])

        # From start to the end of nums.
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self._backtrack(result, temp, i + 1, nums)

            # Pop for backtracking.
            temp.pop()

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Time complexity: O(n*2^n).
        Space complexity: O(2^n).
        """
        # Apply backtracking.
        result = []
        temp = []
        start = 0
        self._backtrack(result, temp, start, nums)
        
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
