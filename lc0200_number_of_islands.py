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

class SolutionDFSRecurVisit(object):
    def _dfs(self, r, c, grid, visited_d):
        # If visit outside of boundary or water or visited.
        if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or
            grid[r][c] == '0' or visited_d.get((r, c))):
            return None

        # Mark (r, c) as visited.
        visited_d[(r, c)] = True

        # Vist up & down and left & right.
        dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r_next, c_next in dirs:
            self._dfs(r_next, c_next, grid, visited_d)

    def numIslands(self, grid):
        """Number of islands by recursion.
        :type grid: List[List[str]]
        :rtype: int

        Time complexity: O(m * n).
        Space complexity: O(m * n).
        """
        if not grid or not grid[0]:
            return 0

        visited_d = {}
        n_islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # If a "new" land is 1, start DFS visiting.
                if grid[r][c] == '1' and not visited_d.get((r, c)):
                    n_islands += 1
                    self._dfs(r, c, grid, visited_d)

        return n_islands


class SolutionDFSRecurVisitReturn(object):
    def _dfs(self, r, c, grid, visited_d):
        # If visit outside of boundary or water or visited.
        if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or
            grid[r][c] == '0' or visited_d.get((r, c))):
            return 0

        # Mark (r, c) as visited.
        visited_d[(r, c)] = True

        n_connects = 1

        # Count connects by visiting up, down, left & right.
        dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r_next, c_next in dirs:
            n_connects += self._dfs(r_next, c_next, grid, visited_d)

        return n_connects

    def numIslands(self, grid):
        """Number of islands by recursion w/ return num of connects.
        :type grid: List[List[str]]
        :rtype: int

        Time complexity: O(m * n).
        Space complexity: O(m * n).
        """
        if not grid or not grid[0]:
            return 0

        visited_d = {}
        n_islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # If a "new" land is 1, start DFS visiting.
                if grid[r][c] == '1':
                    n_connects = self._dfs(r, c, grid, visited_d)
                    if n_connects > 0:
                        n_islands += 1

        return n_islands


class SolutionDFSRecurUpdate(object):
    def _dfs(self, r, c, grid):
        # If visit outside of boundary or water or visited.
        if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or
            grid[r][c] == '0'):
            return None

        # Update (r, c) as visited.
        grid[r][c] = '0'

        # Visit up & down and left & right.
        dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r_next, c_next in dirs:
            self._dfs(r_next, c_next, grid)

    def numIslands(self, grid):
        """Number of islands by recursion.
        :type grid: List[List[str]]
        :rtype: int

        Time complexity: O(m * n).
        Space complexity: O(m * n).
        """
        if not grid or not grid[0]:
            return 0

        n_islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # If a land is 1, start DFS visiting.
                if grid[r][c] == '1':
                    n_islands += 1
                    self._dfs(r, c, grid)

        return n_islands


class SolutionDFSRecurUpdateReturn(object):
    def _dfs(self, r, c, grid):
        # If visit outside of boundary or water or visited.
        if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or
            grid[r][c] == '0'):
            return None

        # Update (r, c) as visited.
        grid[r][c] = '0'

        n_connects = 1

        # Count connects by visiting up, down, left & right.
        dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r_next, c_next in dirs:
            n_connects += self._dfs(r_next, c_next, grid)

        return n_connects

    def numIslands(self, grid):
        """Number of islands by recursion w/ return num of connects.
        :type grid: List[List[str]]
        :rtype: int

        Time complexity: O(m * n).
        Space complexity: O(m * n).
        """
        if not grid or not grid[0]:
            return 0

        n_islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # If a "new" land is 1, start DFS visiting.
                if grid[r][c] == '1':
                    n_connects = self._dfs(r, c, grid)
                    if n_connects > 0:
                        n_islands += 1

        return n_islands


class SolutionDFSIterVisit(object):
    def _get_tovisit_ls(self, v_start, grid):
        (r, c) = v_start
        tovisit_ls = []

        # Visit up, down, left and right.
        dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r_next, c_next in dirs:
            if (0 <= r_next < len(grid) and 0 <= c_next < len(grid[0]) and
                grid[r_next][c_next] == '1'):
                tovisit_ls.append((r_next, c_next))

        return tovisit_ls

    def _get_visited_ls(self, visited_d):
        return [k for (k, v) in visited_d.items() if v is True]

    def _dfs(self, r, c, grid, visited_d):
        visited_d[(r, c)] = True

        # Use stack for iterative DFS.
        stack = [(r, c)]

        while stack:
            tovisit_ls = self._get_tovisit_ls(stack[-1], grid)
            visited_ls = self._get_visited_ls(visited_d)

            if set(tovisit_ls) - set(visited_ls):
                for v_neighbor in tovisit_ls:
                    if v_neighbor not in visited_ls:
                        # Mark (r_next, c_next) as visited.
                        (r_next, c_next) = v_neighbor
                        visited_d[(r_next, c_next)] = True
                        stack.append((r_next, c_next))
                        # break for continuing DFS.
                        break
            else:
                # Backtrack by popping stack.
                stack.pop()

    def numIslands(self, grid):
        """Number of islands by iteration using stack.

        Time complexity: O(m * n).
        Space complexity: O(m * n).
        """
        if not grid or not grid[0]:
            return 0

        visited_d = {}
        n_islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # If a "new" land is 1, start DFS visiting.
                if grid[r][c] == '1' and not visited_d.get((r, c)):
                    n_islands += 1
                    self._dfs(r, c, grid, visited_d)

        return n_islands


class SolutionDFSIterUpdate(object):
    def _get_tovisit_ls(self, v_start, grid):
        (r, c) = v_start
        tovisit_ls = []

        # Visit up, down, left and right.
        dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r_next, c_next in dirs:
            if (0 <= r_next < len(grid) and 0 <= c_next < len(grid[0]) and
                grid[r_next][c_next] == '1'):
                tovisit_ls.append((r_next, c_next))

        return tovisit_ls

    def _dfs(self, r, c, grid):
        # Update (r, c) as visited.
        grid[r][c] = '0'

        # Use stack for iterative DFS.
        stack = [(r, c)]

        while stack:
            tovisit_ls = self._get_tovisit_ls(stack[-1], grid)

            if tovisit_ls:
                for v_neighbor in tovisit_ls:
                    # Mark (r_next, c_next) as visited.
                    (r_next, c_next) = v_neighbor
                    grid[r_next][c_next] = '0'
                    stack.append((r_next, c_next))
                    # break for continuing DFS.
                    break
            else:
                # Backtrack by popping stack.
                stack.pop()

    def numIslands(self, grid):
        """Number of islands by iteration using stack.

        Time complexity: O(m * n).
        Space complexity: O(m * n).
        """
        if not grid or not grid[0]:
            return 0

        n_islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # If a "new" land is 1, start DFS visiting.
                if grid[r][c] == '1':
                    n_islands += 1
                    self._dfs(r, c, grid)

        return n_islands


def main():
    import time

    # Num of islands = 1.
    grid1 = [['1', '1', '1', '1', '0'],
             ['1', '1', '0', '1', '0'], 
             ['1', '1', '0', '0', '0'],
             ['0', '0', '0', '0', '0']]

    start_time = time.time()
    print 'By recur+visit:', SolutionDFSRecurVisit().numIslands(grid1)
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By recur+update:', SolutionDFSRecurUpdate().numIslands(grid1)
    print 'Time: {}'.format(time.time() - start_time)

    grid1 = [['1', '1', '1', '1', '0'],
             ['1', '1', '0', '1', '0'], 
             ['1', '1', '0', '0', '0'],
             ['0', '0', '0', '0', '0']]

    start_time = time.time()
    print 'By iter+visit:', SolutionDFSIterVisit().numIslands(grid1)
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By iter+visit:', SolutionDFSIterUpdate().numIslands(grid1)
    print 'Time: {}'.format(time.time() - start_time)

    # Num of islands = 3.
    grid2 = [['1', '1', '0', '0', '0'],
             ['1', '1', '0', '0', '0'], 
             ['0', '0', '1', '0', '0'],
             ['0', '0', '0', '1', '1']]

    start_time = time.time()
    print 'By recur+visit:', SolutionDFSRecurVisit().numIslands(grid2)
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By recur+update:', SolutionDFSRecurUpdate().numIslands(grid2)
    print 'Time: {}'.format(time.time() - start_time)

    grid2 = [['1', '1', '0', '0', '0'],
             ['1', '1', '0', '0', '0'], 
             ['0', '0', '1', '0', '0'],
             ['0', '0', '0', '1', '1']]

    start_time = time.time()
    print 'By iter+visit:', SolutionDFSIterVisit().numIslands(grid2)
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By iter+visit:', SolutionDFSIterUpdate().numIslands(grid2)
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
