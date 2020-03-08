"""Leetcode 118. Pascal's Triangle
Easy

URL: https://leetcode.com/problems/pascals-triangle/

Given a non-negative integer numRows, generate the first numRows of 
Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly 
above it.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]

        Time complexity: O(n^2).
        Space complexity: O(n).
        """
        if numRows == 0:
            return []

        # Create base of Pascal triangle.
        T = [[1] * (r + 1) for r in range(numRows)]

        if numRows <= 2:
            return T

        # For each row >= 3, update middle numers by last row.
        for r in range(2, numRows):
            for i in range(1, r):
                T[r][i] = T[r - 1][i - 1] + T[r - 1][i]

        return T


def main():
    numRows = 5
    print('Pascal\'s triangle:\n{}'.format(
        Solution().generate(numRows)))


if __name__ == '__main__':
    main()
