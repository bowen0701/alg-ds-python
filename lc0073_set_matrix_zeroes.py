"""Leetcode 73. Set Matrix Zeroes
Medium

URL: https://leetcode.com/problems/set-matrix-zeroes/

Given a m x n matrix, if an element is 0, set its entire row and column to 0. 
Do it in-place.

Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:
- A straight forward solution using O(mn) space is probably a bad idea.
- A simple improvement uses O(m + n) space, but still not the best solution.
- Could you devise a constant space solution?
"""

class SolutionCopy(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.

        Time complexity: O(m * n * max(m, n)).
        Space complexity: O(m * n).
        """
        m, n = len(matrix), len(matrix[0])

        # Copy matrix to a new matrix.
        copy = [[matrix[i][j] for j in range(n)] for i in range(m)]
        
        # Update its row and col by checking matrix[i][j] == 0.
        for i in range(m):
            for j in range(n):
                if copy[i][j] == 0:
                    for r in range(m):
                        matrix[r][j] = 0
                    for c in range(n):
                        matrix[i][c] = 0


def main():
    matrix = [
               [1,1,1],
               [1,0,1],
               [1,1,1]
             ]
    SolutionCopy().setZeroes(matrix)
    print matrix


    matrix = [
               [0,1,2,0],
               [3,4,5,2],
               [1,3,1,5]
             ]
    SolutionCopy().setZeroes(matrix)
    print matrix


if __name__ == '__main__':
    main()
