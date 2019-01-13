"""Leetcode 200. Number of Islands
Medium

URL: https://leetcode.com/problems/number-of-islands/description/

Given a 2d grid map of '1's (land) and '0's (water), 
count the number of islands. 
An island is surrounded by water and is formed by connecting 
adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
11110
11010
11000
00000
Answer: 1

Example 2:
11000
11000
00100
00011
Answer: 3
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        Time complexity: O(m * n).
        Space complexity: O(m * n).

        Procedure:
          - Starting from the top-left corner, run DFS with counter n_islands.
          - If the grid was not visited before, mark it as visited and 
            add n_islands by 1; if yes, skip DFS.
        """
        if not grid:
            return 0

        n_rows, n_cols = len(grid), len(grid[0])
        visited_grid = [[False for c in range(n_cols)] for r in range(n_rows)]
        n_islands = 0

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == '1' and not visited_grid[r][c]:
                    n_islands += 1
                    self.dfs(r, c, grid, visited_grid, n_rows, n_cols)

        return n_islands

    def dfs(self, r, c, grid, visited_grid, n_rows, n_cols):
        visited_grid[r][c] = True

        if 0 <= r - 1: # Up.
            if grid[r - 1][c] == '1' and not visited_grid[r - 1][c]:
                self.dfs(r - 1, c, grid, visited_grid, n_rows, n_cols)
        if r + 1 < n_rows: # Down.
            if grid[r + 1][c] == '1' and not visited_grid[r + 1][c]:
                self.dfs(r + 1, c, grid, visited_grid, n_rows, n_cols)
        if 0 <= c - 1: # Left.
            if grid[r][c - 1] == '1' and not visited_grid[r][c - 1]:
                self.dfs(r, c - 1, grid, visited_grid, n_rows, n_cols)
        if c + 1 < n_cols: # Right.
            if grid[r][c + 1] == '1' and not visited_grid[r][c + 1]:
                self.dfs(r, c + 1, grid, visited_grid, n_rows, n_cols)


def main():
    grid1 = [['1', '1', '1', '1', '0'],
             ['1', '1', '0', '1', '0'], 
             ['1', '1', '0', '0', '0'],
             ['0', '0', '0', '0', '0']]

    print Solution().numIslands(grid1)

    grid2 = [['1', '1', '0', '0', '0'],
             ['1', '1', '0', '0', '0'], 
             ['0', '0', '1', '0', '0'],
             ['0', '0', '0', '1', '1']]

    print Solution().numIslands(grid2)


if __name__ == '__main__':
    main()
