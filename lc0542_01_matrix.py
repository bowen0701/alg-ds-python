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


class SolutionBFS:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Time complexity: O(mn), where
          - m: number of rows
          - n: number of columns
        Space complexity: O(mn).
        """
        # Edge cases.
        if not mat or not mat[0]:
            return mat
    
        n_rows, n_cols = len(mat), len(mat[0])

        # Collect 0 cells as BFS start points and update 1 cell values to inf.
        queue = []

        for r in range(n_rows):
            for c in range(n_cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    # For cell with value != 0, update its distance to inf.
                    mat[r][c] = float('inf')

        # BFS: start from value 0 cells, visiting neighbors: up/down/left/right.
        while queue:
            r, c = queue.pop()
            dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

            for r_next, c_next in dirs:
                # Check out of boundary.
                if (r_next < 0 or r_next >= n_rows 
                    or c_next < 0 or c_next >= n_cols):
                    continue

                # Update distance if find shorter.
                if mat[r_next][c_next] > mat[r][c] + 1:
                    mat[r_next][c_next] = mat[r][c] + 1
                    queue.insert(0, (r_next, c_next))

        return mat


class SolutionDFSRecur:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Time complexity: O(?), where
          - m: number of rows
          - n: number of columns
        Space complexity: O(?).
        """
        # Edge cases.
        if not mat or not mat[0]:
            return mat

        n_rows, n_cols = len(mat), len(mat[0])

        # Collect 0 cells as DFS start points and update 1 cell values to inf.
        zero_cells = []

        for r in range(n_rows):
            for c in range(n_cols):
                if mat[r][c] == 0:
                    zero_cells.append((r, c))
                else:
                    mat[r][c] = float('inf')

        # TODO: Iterate through start points and update distance to them.


class SolutionDPTopLeftBottomRight:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Time complexity: O(mn), where
          - m: number of rows
          - n: number of columns
        Space complexity: O(1).
        """
        # Edge cases.
        if not mat or not mat[0]:
            return mat

        n_rows, n_cols = len(mat), len(mat[0])

        # Iterate through from top left, check up & left to update distance.
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

                # Update distance by min(up & left).
                mat[r][c] = min(up, left) + 1

        # Iterate through from bottom right, check down & right to update distance.
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

                # Update distance by min(previous distance, min(down & right)).
                mat[r][c] = min(mat[r][c], min(down, right) + 1)

        return mat


def main():
    import copy
    import time

    # Output:
    # [[0,0,0],
    #  [0,1,0],
    #  [0,0,0]]
    mat = [[0,0,0],
           [0,1,0],
           [0,0,0]]

    start_time = time.time()
    print(SolutionBFS().updateMatrix(copy.deepcopy(mat)))
    print("BFS:", time.time() - start_time)

    start_time = time.time()
    print(SolutionDPTopLeftBottomRight().updateMatrix(copy.deepcopy(mat)))
    print("DP:", time.time() - start_time)

    # Output:
    # [[0,0,0],
    #  [0,1,0],
    #  [1,2,1]]
    mat = [[0,0,0],
           [0,1,0],
           [1,1,1]]

    start_time = time.time()
    print(SolutionBFS().updateMatrix(copy.deepcopy(mat)))
    print("BFS:", time.time() - start_time)

    start_time = time.time()
    print(SolutionDPTopLeftBottomRight().updateMatrix(copy.deepcopy(mat)))
    print("DP:", time.time() - start_time)


if __name__ == '__main__':
    main()
