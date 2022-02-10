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

from typing import Dict, List, Tuple


class SolutionDFSRecurVisitedDict(object):
    def _dfs(self, r: int, c: int, grid: List[List[int]], visited_d: Dict[Tuple[int, int], bool]) -> int:
        # Base case: out of boundary or visited.
        if (r < 0 or r >= len(grid) 
            or c < 0 or c >= len(grid[0])
            or visited_d[(r, c)]
            or grid[r][c] == 0):
            return 0

        # Mark (r, c) as visited.
        visited_d[(r, c)] = True
        area = 1

        # Visit neighbors: top/down/left/right to accumulate area.
        dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r_next, c_next in dirs:
            area += self._dfs(r_next, c_next, grid, visited_d)

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Time complexity: O(m*n).
        Space complexity: O(m*n).
        """
        from collections import defaultdict

        # Edge case.
        if not grid or not grid[0]:
            return 0

        n_rows, n_cols = len(grid), len(grid[0])

        # Apply recursive DFS with a visited grid.
        visited_d = defaultdict(bool)
        result = 0

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1:
                    area = self._dfs(r, c, grid, visited_d)
                    result = max(result, area)

        return result


class SolutionBFSVisitedDict:
    def _bfs(self, r: int, c: int, grid: List[List[int]], visited_d: Dict[Tuple[int, int], bool]) -> int:
        from collections import deque

        n_rows, n_cols = len(grid), len(grid[0])

        # Mark (r, c) as visited.
        visited_d[(r, c)] = True

        # Apply BFS with queue.
        area = 0
        queue = deque([(r, c)])

        while queue:
            r, c = queue.pop()
            area += 1

            # Visit neighboards: top/down/left/down, marked as visited.
            dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for r_next, c_next in dirs:
                if (r_next < 0 or r_next >= n_rows
                    or c_next < 0 or c_next >= n_cols
                    or visited_d[(r_next, c_next)]
                    or grid[r_next][c_next] == 0):
                    continue

                visited_d[(r_next, c_next)] = True
                queue.appendleft((r_next, c_next))

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Time complexity: O(m*n).
        Space complexity: O(m*n).
        """
        from collections import defaultdict

        # Edge cases.
        if not grid or not grid[0]:
            return 0

        n_rows, n_cols = len(grid), len(grid[0])

        # Apply BFS with visited dict to obtain max area.
        visited_d = defaultdict(bool)
        result = 0

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1:
                    result = max(result, self._bfs(r, c, grid, visited_d))

        return result


def main():
    import copy
    import time

    # Output: 6
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    grid1 = copy.deepcopy(grid)
    start_time = time.time()
    print(SolutionDFSRecurVisitedDict().maxAreaOfIsland(grid1))
    print("SolutionDFSRecurVisitedDict:", time.time() - start_time)

    grid1 = copy.deepcopy(grid)
    start_time = time.time()
    print(SolutionBFSVisitedDict().maxAreaOfIsland(grid1))
    print("SolutionBFSVisitedDict:", time.time() - start_time)


if __name__ == '__main__':
    main()
