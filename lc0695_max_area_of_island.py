"""Leetcode 695. Max Area of Island
Medium

URL: https://leetcode.com/problems/max-area-of-island/

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array.
(If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11,
because the island must be connected 4-directionally.

Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.

Note: The length of each dimension in the given grid does not exceed 50.
"""

from typing import List, Tuple


class SolutionDFSRecurUpdate(object):
    def _dfs(self, r: int, c: int, grid: List[List[int]]) -> int:
        # Check exit conditions: out of boundaries, in water.
        if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or 
            grid[r][c] == 0):
            return 0

        # Mark (r, c) as visited.
        grid[r][c] = 0
        area = 1

        # Visit 4 directions to accumulate area.
        dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r_next, c_next in dirs:
            area += self._dfs(r_next, c_next, grid)

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Time complexity: O(m*n).
        Space complexity: O(m*n).
        """
        if not grid or not grid[0]:
            return 0

        max_area = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = self._dfs(r, c, grid)
                    max_area = max(max_area, area)

        return max_area


class SolutionDFSIterUpdate(object):
    def _get_tovisits(self, v_start: Tuple[int, int], grid: List[List[int]]) -> List[Tuple[int, int]]:
        r, c = v_start

        tovisits = []

        # Visit up, down, left and right.
        dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r_next, c_next in dirs:
            if (0 <= r_next < len(grid) and 
                0 <= c_next < len(grid[0]) and
                grid[r_next][c_next] == 1):
                tovisits.append((r_next, c_next))

        return tovisits

    def _dfs(self, r: int, c: int, grid: List[List[int]]) -> int:
        grid[r][c] = 0

        # Use stack for DFS.
        stack = [(r, c)]
        area = 1

        while stack:
            # Get to-visit nodes from the top of stack.
            tovisits = self._get_tovisits(stack[-1], grid)

            if tovisits:
                for r_next, c_next in tovisits:
                    grid[r_next][c_next] = 0
                    area += 1
                    stack.append((r_next, c_next))
                    # Break to continue DFS.
                    break
            else:
                stack.pop()

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Time complexity: O(m*n).
        Space complexity: O(m*n).
        """
        if not grid or not grid[0]:
            return 0

        max_area = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = self._dfs(r, c, grid)
                    max_area = max(max_area, area)

        return max_area


def main():
    # Output: 6
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(SolutionDFSRecurUpdate().maxAreaOfIsland(grid))

    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(SolutionDFSIterUpdate().maxAreaOfIsland(grid))

    # Output: 0.
    grid = [[0,0,0,0,0,0,0,0]]
    print(SolutionDFSRecurUpdate().maxAreaOfIsland(grid))

    grid = [[0,0,0,0,0,0,0,0]]
    print(SolutionDFSIterUpdate().maxAreaOfIsland(grid))


if __name__ == '__main__':
    main()
