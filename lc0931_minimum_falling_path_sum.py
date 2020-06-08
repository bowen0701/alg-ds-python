"""Leetcode 931. Minimum Falling Path Sum
Medium

URL: https://leetcode.com/problems/minimum-falling-path-sum/

Given a square array of integers A, we want the minimum sum of a falling
path through A.

A falling path starts at any element in the first row, and chooses one
element from each row. The next row's choice must be in a column that is
different from the previous row's column by at most one.

Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation: 
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.
"""

class SolutionRecur(object):
    def _fallingPathSumRecur(self, A, r, c):
        n = len(A)

        # If arrives at the 1st row, return its value.
        if r == 0:
            return A[r][c]

        min_sum = float('inf')
        for j in range(n):
            if j - r <= 1:
                min_sum = min(
                    min_sum, 
                    A[r][c] + self._fallingPathSumRecur(A, r - 1, j)
                )
        return min_sum

    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int

        Time complexity: O(n*3^n), where n is the number of rows of A.
        Space complexity: O(n).
        """
        # Edge case.
        if not A or not A[0]:
            return 0

        # Apply top-down recursion with iterating through the last row.
        n = len(A)
        min_sum = float('inf')
        for c in range(n):
            min_sum = min(min_sum, self._fallingPathSumRecur(A, n - 1, c))
        return min_sum


def main():
    # Output: 12
    A = [[1,2,3],
         [4,5,6],
         [7,8,9]]
    print SolutionRecur().minFallingPathSum(A)

    # Output: 6
    A = [[1,2,3,4],
         [5,2,7,8],
         [9,9,3,9]]
    print SolutionRecur().minFallingPathSum(A)


if __name__ == '__main__':
    main()
