"""Leetcode 1091. Shortest Path in Binary Matrix
Medium

URL: https://leetcode.com/problems/shortest-path-in-binary-matrix/

Given an n x n binary matrix grid, return the length of the shortest
clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell
(i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such
that:
- All the visited cells of the path are 0.
- All the adjacent cells of the path are 8-directionally connected
  (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of the path.

Example 1:
Input: grid = [
  [0,1],
  [1,0]
]
Output: 2

Example 2:
Input: grid = [
  [0,0,0],
  [1,1,0],
  [1,1,0]
]
Output: 4

Example 3:
Input: grid = [
  [1,0,0],
  [1,1,0],
  [1,1,0]
]
Output: -1

Constraints:
- n == grid.length
- n == grid[i].length
- 1 <= n <= 100
- grid[i][j] is 0 or 1
"""

from typing import List
from collections import deque


class SolutionBFS:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Time complexity: O(n^2).
        Space complexity: O(n^2).
        """
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        # BFS with 8-directional movement.
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1

        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)]

        while queue:
            r, c, dist = queue.popleft()

            if r == n - 1 and c == n - 1:
                return dist

            for dr, dc in dirs:
                r_new, c_new = r + dr, c + dc
                if 0 <= r_new < n and 0 <= c_new < n and grid[r_new][c_new] == 0:
                    grid[r_new][c_new] = 1
                    queue.append((r_new, c_new, dist + 1))

        return -1


class SolutionBFSVisited:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Time complexity: O(n^2).
        Space complexity: O(n^2).
        """
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        queue = deque([(0, 0, 1)])
        visited = {(0, 0)}

        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)]

        while queue:
            r, c, dist = queue.popleft()

            if r == n - 1 and c == n - 1:
                return dist

            for dr, dc in dirs:
                r_new, c_new = r + dr, c + dc
                if (0 <= r_new < n and 0 <= c_new < n
                    and grid[r_new][c_new] == 0
                    and (r_new, c_new) not in visited
                ):
                    visited.add((r_new, c_new))
                    queue.append((r_new, c_new, dist + 1))

        return -1


def main():
    # Output: 2.
    grid = [[0, 1], [1, 0]]
    print(SolutionBFS().shortestPathBinaryMatrix([row[:] for row in grid]))
    print(SolutionBFSVisited().shortestPathBinaryMatrix(grid))

    # Output: 4.
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    print(SolutionBFS().shortestPathBinaryMatrix([row[:] for row in grid]))
    print(SolutionBFSVisited().shortestPathBinaryMatrix(grid))

    # Output: -1.
    grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    print(SolutionBFS().shortestPathBinaryMatrix([row[:] for row in grid]))
    print(SolutionBFSVisited().shortestPathBinaryMatrix(grid))


if __name__ == '__main__':
    main()
