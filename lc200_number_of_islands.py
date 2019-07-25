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
    def _dfs(self, r, c, grid, visited_d):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            # If visit outside of the grid boundary.
            return None

        if grid[r][c] == '0' or visited_d.get((r, c)):
            # If visit water or already visisted before.
            return None

        visited_d[(r, c)] = True

        for r_neighbor in [r - 1, r + 1]:  # Up & down.
            self._dfs(r_neighbor, c, grid, visited_d)

        for c_neighbor in [c - 1, c + 1]:  # Left & right.
            self._dfs(r, c_neighbor, grid, visited_d)


    def numIslands(self, grid):
        """Number of islands by recursion.
        :type grid: List[List[str]]
        :rtype: int

        Time complexity: O(m * n).
        Space complexity: O(m * n).
        """
        if not grid:
            return 0

        visited_d = {}
        n_islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and not visited_d.get((r, c)):
                    n_islands += 1
                    self._dfs(r, c, grid, visited_d)

        return n_islands


class SolutionRecur2(object):
    def _dfs(self, r, c, grid, visited_d):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            # If visit outside of the grid boundary.
            return 0

        if grid[r][c] == '0' or visited_d.get((r, c)):
            # If visit water or already visisted before.
            return 0

        visited_d[(r, c)] = True
        n_connects = 1

        for r_neighbor in [r - 1, r + 1]:  # Up & down.
            n_connects += self._dfs(r_neighbor, c, grid, visited_d)

        for c_neighbor in [c - 1, c + 1]:  # Left & right.
            n_connects += self._dfs(r, c_neighbor, grid, visited_d)

        return n_connects

    def numIslands(self, grid):
        """Number of islands by recursion w/ return.
        :type grid: List[List[str]]
        :rtype: int

        Time complexity: O(m * n).
        Space complexity: O(m * n).
        """
        if not grid:
            return 0

        visited_d = {}
        n_islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and not visited_d.get((r, c)):
                    n_connects = self._dfs(r, c, grid, visited_d)
                    if n_connects > 0:
                        n_islands += 1

        return n_islands


class SolutionIter(object):
    def _get_tovisit_ls(self, v_start, grid):
        (r, c) = v_start
        tovisit_ls = []

        if r - 1 >= 0 and grid[r - 1][c] == '1':            # Up.
            tovisit_ls.append((r - 1, c))
        if r + 1 < len(grid) and grid[r + 1][c] == '1':     # Down.
            tovisit_ls.append((r + 1, c))
        if c - 1 >= 0 and grid[r][c - 1] == '1':            # Left.
            tovisit_ls.append((r, c - 1))
        if c + 1 < len(grid[0]) and grid[r][c + 1] == '1':  # Right.
            tovisit_ls.append((r, c + 1))

        return tovisit_ls

    def _get_visited_ls(self, visited_d):
        return [k for (k, v) in visited_d.items() if v is True]

    def _dfs(self, r, c, grid, visited_d):
        visited_d[(r, c)] = True

        # Use stack for iterative DFS.
        stack = []
        stack.append((r, c))

        while stack:
            tovisit_ls = self._get_tovisit_ls(stack[-1], grid)
            visited_ls = self._get_visited_ls(visited_d)

            if set(tovisit_ls) - set(visited_ls):
                for v_neighbor in tovisit_ls:
                    if v_neighbor not in visited_ls:
                        (r_neighbor, c_neighbor) = v_neighbor
                        visited_d[(r_neighbor, c_neighbor)] = True
                        stack.append((r_neighbor, c_neighbor))
                        break  # break for continuing DFS.
            else:
                stack.pop()

    def numIslands(self, grid):
        """Number of islands by iteration using stack.

        Time complexity: O(m * n).
        Space complexity: O(m * n).
        """
        if not grid:
            return 0

        visited_d = {}
        n_islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and not visited_d.get((r, c)):
                    n_islands += 1
                    self._dfs(r, c, grid, visited_d)

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
    print SolutionRecur2().numIslands(grid1)
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
    print SolutionRecur2().numIslands(grid2)
    print 'Time for recursion: {}'.format(time.time() - start_time)

    start_time = time.time()
    print SolutionIter().numIslands(grid2)
    print 'Time for iteration: {}'.format(time.time() - start_time)

if __name__ == '__main__':
    main()
