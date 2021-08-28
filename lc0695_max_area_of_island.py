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
        # Base case: out of boundary or visited.
        if (r < 0 or r >= len(grid) 
            or c < 0 or c >= len(grid[0]) 
            or grid[r][c] == 0):
            return 0

        # Mark (r, c) as visited.
        grid[r][c] = 0
        area = 1

        # Visit neighbors: top/down/left/right to accumulate area.
        dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r_next, c_next in dirs:
            area += self._dfs(r_next, c_next, grid)

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Time complexity: O(m*n).
        Space complexity: O(m*n).
        """
        # Edge case.
        if not grid or not grid[0]:
            return 0

        n_rows, n_cols = len(grid), len(grid[0])

        # Apply recursive DFS with updating visited grid.
        result = 0

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1:
                    area = self._dfs(r, c, grid)
                    result = max(result, area)

        return result


class SolutionDFSIterUpdate(object):
    def _get_to_visits(
        self, 
        v_start: Tuple[int, int], 
        grid: List[List[int]]
    ) -> List[Tuple[int, int]]:
        r, c = v_start

        to_visits = []

        # Visit neigghbors: top/down/left/right.
        dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r_next, c_next in dirs:
            if (0 <= r_next < len(grid) and 
                0 <= c_next < len(grid[0]) and
                grid[r_next][c_next] == 1):
                to_visits.append((r_next, c_next))

        return to_visits

    def _dfs(self, r: int, c: int, grid: List[List[int]]) -> int:
        grid[r][c] = 0

        # Apply iterative DFS with stack.
        stack = [(r, c)]
        area = 1

        while stack:
            # Get to-visit nodes from the top of stack.
            to_visits = self._get_to_visits(stack[-1], grid)

            if to_visits:
                for r_next, c_next in to_visits:
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
        # Edgge case.
        if not grid or not grid[0]:
            return 0

        # Apply iterative DFS with stack.
        result = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = self._dfs(r, c, grid)
                    result = max(result, area)

        return result


class SolutionBFS:
    def bfs(self, r: int, c: int, grid: List[List[int]]) -> int:
        from collections import deque

        n_rows, n_cols = len(grid), len(grid[0])

        # Mark as visited.
        grid[r][c] = 0

        # Apply BFS with queue.
        area = 0
        queue = deque([(r, c)])

        while queue:
            r, c = queue.pop()
            area += 1

            # Visit neighboards: top/down/left/down, marked as visited.
            dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for r_next, c_next in dirs:
                # Check out of boundary or visited.
                if (r_next < 0 or r_next >= n_rows
                    or c_next < 0 or c_next >= n_cols
                    or grid[r_next][c_next] == 0):
                    continue

                # Mark as visited and visit neighbors.
                grid[r_next][c_next] = 0
                queue.appendleft((r_next, c_next))

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Time complexity: O(m*n).
        Space complexity: O(m*n).
        """
        # Edge cases.
        if not grid or not grid[0]:
            return 0

        n_rows, n_cols = len(grid), len(grid[0])

        # Apply BFS to obtain max area.
        result = 0

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1:
                    area = self.bfs(r, c, grid)
                    result = max(result, area)

        return result


def main():
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
    start_time = time.time()
    print(SolutionDFSRecurUpdate().maxAreaOfIsland(grid))
    print("SolutionDFSRecurUpdate:", time.time() - start_time)

    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    start_time = time.time()
    print(SolutionDFSIterUpdate().maxAreaOfIsland(grid))
    print("SolutionDFSIterUpdate:", time.time() - start_time)

    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    start_time = time.time()
    print(SolutionBFS().maxAreaOfIsland(grid))
    print("SolutionBFS:", time.time() - start_time)


if __name__ == '__main__':
    main()
