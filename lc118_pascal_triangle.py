"""Leetcode 118. Pascal's Triangle
Easy

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

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
    def get_num(self, last_row, i):
        if i < 0 or i >= len(last_row):
            return 0
        return last_row[i]

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]

        Time complexity: O(n^2).
        Space complexity: O(n^2).
        """
        if numRows == 0:
            return []

        triangle = [[1] * (r + 1) for r in range(numRows)]
        if numRows <= 2:
            return triangle
        for r in range(2, numRows):
            last_row = triangle[r - 1]
            current_row = triangle[r]
            for i in range(1, r):
                current_row[i] = last_row[i - 1] + last_row[i]
        return triangle


def main():
    numRows = 5
    print('Pascal\'s triangle:\n{}'.format(
        Solution().generate(numRows)))


if __name__ == '__main__':
    main()
