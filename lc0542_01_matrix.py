"""Leetcode 542. 01 Matrix
Medium

URL: https://leetcode.com/problems/01-matrix/

Given a matrix consists of 0 and 1, 
find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:
Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]
Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]] 

Note:
- The number of elements of the given matrix will not exceed 10,000.
- There are at least one 0 in the given matrix.
- The cells are adjacent in only four directions: up, down, left and right.
"""

from typing import List


class SolutionBFS(object):
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Time complexity: O(mn), where
          - m: number of rows
          - n: number of columns
        Space complexity: O(mn).
        """
        if not mat or not mat[0]:
            return mat
    
        n_rows, n_cols = len(mat), len(mat[0])

        # Use queue for BFS.
        queue = []

        for r in range(n_rows):
            for c in range(n_cols):
                if mat[r][c] == 0:
                    # Collect cells with value 0 for exploration.
                    queue.append((r, c))
                else:
                    # For cell with value != 0, update its distance to inf.
                    mat[r][c] = float('inf')

        # BFS explore from cells with value 0.
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.pop()
            for dr, dc in dirs:
                r_next, c_next = r + dr, c + dc

                # If out of boundary or does not shorten distance.
                if (r_next < 0 or r_next >= n_rows or
                    c_next < 0 or c_next >= n_cols or
                    mat[r_next][c_next] < mat[r][c] + 1):
                    continue

                mat[r_next][c_next] = mat[r][c] + 1
                queue.insert(0, (r_next, c_next))

        return mat


class SolutionDP(object):
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Time complexity: O(mn), where
          - m: number of rows
          - n: number of columns
        Space complexity: O(1).
        """
        if not mat or not mat[0]:
            return mat

        n_rows, n_cols = len(mat), len(mat[0])

        # Iterate through all cells from upper left.
        for r in range(n_rows):
            for c in range(n_cols):
                if mat[r][c] == 0:
                    continue

                # Check its up & left.
                if r > 0:
                    up = mat[r - 1][c]
                else:
                    up = float('inf')

                if c > 0:
                    left = mat[r][c - 1]
                else:
                    left = float('inf')

                # Update cell by min(up & left).
                mat[r][c] = min(up, left) + 1

        # Iterate through all cells from bottom right, check its down & right.
        for r in range(n_rows - 1, -1, -1):
            for c in range(n_cols -1, -1, -1):
                if mat[r][c] == 0:
                    continue

                # Check its down & right.
                if r < n_rows - 1:
                    down = mat[r + 1][c]
                else:
                    down = float('inf')

                if c < n_cols - 1:
                    right = mat[r][c + 1]
                else:
                    right = float('inf')

                # Update cell by min(previous result, min(down & right)).
                mat[r][c] = min(mat[r][c], min(down, right) + 1)

        return mat


def main():
    # Output:
    # [[0,0,0],
    #  [0,1,0],
    #  [0,0,0]]
    mat = [[0,0,0],
           [0,1,0],
           [0,0,0]]
    print(SolutionBFS().updateMatrix(mat))

    mat = [[0,0,0],
           [0,1,0],
           [0,0,0]]
    print(SolutionDP().updateMatrix(mat))

    # Output:
    # [[0,0,0],
    #  [0,1,0],
    #  [1,2,1]]
    matrix = [[0,0,0],
              [0,1,0],
              [1,1,1]]
    print(SolutionBFS().updateMatrix(matrix)    )

    matrix = [[0,0,0],
              [0,1,0],
              [1,1,1]]
    print(SolutionDP().updateMatrix(matrix))


if __name__ == '__main__':
    main()
