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

class SolutionRecur(object):
    def dfs(self, r, c, grid, visited_d, n_rows, n_cols):
        visited_d[(r, c)] = True

        if (0 <= r - 1 and grid[r - 1][c] == '1' and 
            not visited_d.get((r - 1, c))):  # Up.
            self.dfs(r - 1, c, grid, visited_d, n_rows, n_cols)
        if (r + 1 < n_rows and grid[r + 1][c] == '1' and 
            not visited_d.get((r + 1, c))):  # Down.
            self.dfs(r + 1, c, grid, visited_d, n_rows, n_cols)
        if (0 <= c - 1 and grid[r][c - 1] == '1' and 
            not visited_d.get((r, c - 1))):  # Left.
            self.dfs(r, c - 1, grid, visited_d, n_rows, n_cols)
        if (c + 1 < n_cols and grid[r][c + 1] == '1' and 
            not visited_d.get((r, c + 1))):  # Right.
            self.dfs(r, c + 1, grid, visited_d, n_rows, n_cols)

    def numIslands(self, grid):
        """Number of islands by recursion.
        :type grid: List[List[str]]
        :rtype: int

        Time complexity: O(m * n).
        Space complexity: O(m * n).

        Recursive procedure:
          - Starting from the top-left corner, run DFS with counter n_islands.
          - If the grid was not visited before, mark it as visited and 
            add n_islands by 1; if yes, skip DFS.
        """
        if not grid:
            return 0

        n_rows, n_cols = len(grid), len(grid[0])
        visited_d = {}
        n_islands = 0

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == '1' and not visited_d.get((r, c)):
                    n_islands += 1
                    self.dfs(r, c, grid, visited_d, n_rows, n_cols)

        return n_islands


class SolutionIter(object):
    def get_tovisit_ls(self, v_start, grid, n_rows, n_cols):
        (r, c) = v_start
        tovisit_ls = []

        if r - 1 >= 0 and grid[r - 1][c] == '1':  # Up.
            tovisit_ls.append((r - 1, c))
        if r + 1 < n_rows and grid[r + 1][c] == '1':  # Down.
            tovisit_ls.append((r + 1, c))
        if c - 1 >= 0 and grid[r][c - 1] == '1':  # Left.
            tovisit_ls.append((r, c - 1))
        if c + 1 < n_cols and grid[r][c + 1] == '1':  # Right.
                tovisit_ls.append((r, c + 1))

        return tovisit_ls

    def get_visited_ls(self, visited_d):
        return [k for (k, v) in visited_d.items() if v is True]

    def dfs(self, r, c, grid, visited_d, n_rows, n_cols):
        visited_d[(r, c)] = True
        stack = []
        stack.append((r, c))

        while stack:
            tovisit_ls = self.get_tovisit_ls(stack[-1], grid, n_rows, n_cols)
            visited_ls = self.get_visited_ls(visited_d)

            if set(tovisit_ls) - set(visited_ls):
                for v_neighbor in tovisit_ls:
                    if v_neighbor not in visited_ls:
                        (r_neighbor, c_neighbor) = v_neighbor
                        visited_d[(r_neighbor, c_neighbor)] = True
                        stack.append((r_neighbor, c_neighbor))
                        break
            else:
                stack.pop()

    def numIslands(self, grid):
        """Number of islands by iteration using stack.

        Time complexity: O(m * n).
        Space complexity: O(m * n).
        """
        if not grid:
            return 0

        n_rows, n_cols = len(grid), len(grid[0])
        visited_d = {}
        n_islands = 0

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == '1' and not visited_d.get((r, c)):
                    n_islands += 1
                    self.dfs(r, c, grid, visited_d, n_rows, n_cols)

        return n_islands


def main():
    import time

    # Num of islands = 1.
    grid1 = [['1', '1', '1', '1', '0'],
             ['1', '1', '0', '1', '0'], 
             ['1', '1', '0', '0', '0'],
             ['0', '0', '0', '0', '0']]

    start_time = time.time()
    print SolutionRecur().numIslands(grid1)
    print 'Time for recursion: {}'.format(time.time() - start_time)

    start_time = time.time()
    print SolutionIter().numIslands(grid1)
    print 'Time for iteration: {}'.format(time.time() - start_time)

    # Num of islands = 3.
    grid2 = [['1', '1', '0', '0', '0'],
             ['1', '1', '0', '0', '0'], 
             ['0', '0', '1', '0', '0'],
             ['0', '0', '0', '1', '1']]

    start_time = time.time()
    print SolutionRecur().numIslands(grid2)
    print 'Time for recursion: {}'.format(time.time() - start_time)

    start_time = time.time()
    print SolutionIter().numIslands(grid2)
    print 'Time for iteration: {}'.format(time.time() - start_time)

if __name__ == '__main__':
    main()
