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

from typing import List, Tuple, Dict


class SolutionDFSUpdateRecur(object):
    def _dfs(self, r: int, c: int, grid: List[List[str]]):
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

    def numIslands(self, grid: List[List[str]]) -> int:
        """Number of islands by recursion.

        Time complexity: O(m*n).
        Space complexity: O(m*n).
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


class SolutionDFSVisitRecur(object):
    def _dfs(self, r: int, c: int, 
             grid: List[List[str]],
             visited_d: Dict[Tuple[int, int], bool]):
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

    def numIslands(self, grid: List[List[str]]) -> int:
        """Number of islands by recursion.

        Time complexity: O(m*n).
        Space complexity: O(m*n).
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


class SolutionDFSUpdateIter(object):
    def _get_tovisits(self, v_start: Tuple[int, int], grid: List[List[str]]):
        (r, c) = v_start
        tovisits = []

        # Visit up, down, left and right.
        dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r_next, c_next in dirs:
            if (0 <= r_next < len(grid) and 0 <= c_next < len(grid[0]) and
                grid[r_next][c_next] == '1'):
                tovisits.append((r_next, c_next))

        return tovisits

    def _dfs(self, r: int, c: int, grid: List[List[str]]):
        # Update (r, c) as visited.
        grid[r][c] = '0'

        # Use stack for iterative DFS.
        stack = [(r, c)]

        while stack:
            tovisits = self._get_tovisits(stack[-1], grid)

            if tovisits:
                for v_neighbor in tovisits:
                    # Mark (r_next, c_next) as visited.
                    (r_next, c_next) = v_neighbor
                    grid[r_next][c_next] = '0'
                    stack.append((r_next, c_next))
                    # break for continuing DFS.
                    break
            else:
                # Backtrack by popping stack.
                stack.pop()

    def numIslands(self, grid: List[List[str]]) -> int:
        """Number of islands by iteration using stack.

        Time complexity: O(m*n).
        Space complexity: O(m*n).
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


class SolutionDFSVisitIter(object):
    def _get_tovisits(self, v_start: Tuple[int, int], grid: List[List[str]]):
        (r, c) = v_start
        tovisits = []

        # Visit up, down, left and right.
        dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r_next, c_next in dirs:
            if (0 <= r_next < len(grid) and 0 <= c_next < len(grid[0]) and
                grid[r_next][c_next] == '1'):
                tovisits.append((r_next, c_next))

        return tovisits

    def _get_visited_ls(self, visited_d: Dict[Tuple[int, int], bool]):
        return [k for (k, v) in visited_d.items() if v is True]

    def _dfs(self, r: int, c: int, 
             grid: List[List[str]], 
             visited_d: Dict[Tuple[int, int], bool]):
        visited_d[(r, c)] = True

        # Use stack for iterative DFS.
        stack = [(r, c)]

        while stack:
            tovisits = self._get_tovisits(stack[-1], grid)
            visited_ls = self._get_visited_ls(visited_d)

            if set(tovisits) - set(visited_ls):
                for v_neighbor in tovisits:
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

    def numIslands(self, grid: List[List[str]]) -> int:
        """Number of islands by iteration using stack.

        Time complexity: O(m*n).
        Space complexity: O(m*n).
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


class SolutionDFSUpdateReturnConnectsRecur(object):
    def _dfs(self, r: int, c: int, grid: List[List[str]]):
        # If visit outside of boundary or water or visited.
        if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or
            grid[r][c] == '0'):
            return 0

        # Update (r, c) as visited.
        grid[r][c] = '0'

        # Count connects by visiting up, down, left & right.
        n_connects = 1
        dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r_next, c_next in dirs:
            n_connects += self._dfs(r_next, c_next, grid)

        return n_connects

    def numIslands(self, grid: List[List[str]]) -> int:
        """Number of islands by recursion w/ return num of connects.

        Time complexity: O(m*n).
        Space complexity: O(m*n).
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


class SolutionDFSVisitReturnConnectsRecur(object):
    def _dfs(self, r: int, c: int, 
             grid: List[List[str]], 
             visited_d: Dict[Tuple[int, int], bool]):
        # If visit outside of boundary or water or visited.
        if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or
            grid[r][c] == '0' or visited_d.get((r, c))):
            return 0

        # Mark (r, c) as visited.
        visited_d[(r, c)] = True

        # Count connects by visiting up, down, left & right.
        n_connects = 1
        dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r_next, c_next in dirs:
            n_connects += self._dfs(r_next, c_next, grid, visited_d)

        return n_connects

    def numIslands(self, grid: List[List[str]]) -> int:
        """Number of islands by recursion w/ return num of connects.

        Time complexity: O(m*n).
        Space complexity: O(m*n).
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


def main():
    import copy
    import time

    # Num of islands = 1.
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'], 
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]

    grid1 = copy.deepcopy(grid)
    start_time = time.time()
    print('By recur+update:', SolutionDFSUpdateRecur().numIslands(grid1))
    print('Time: {}'.format(time.time() - start_time))

    grid1 = copy.deepcopy(grid)
    start_time = time.time()
    print('By recur+visit:', SolutionDFSVisitRecur().numIslands(grid1))
    print('Time: {}'.format(time.time() - start_time))

    grid1 = copy.deepcopy(grid)
    start_time = time.time()
    print('By iter+update:', SolutionDFSUpdateIter().numIslands(grid1))
    print('Time: {}'.format(time.time() - start_time))

    grid1 = copy.deepcopy(grid)
    start_time = time.time()
    print('By iter+visit:', SolutionDFSVisitIter().numIslands(grid1))
    print('Time: {}'.format(time.time() - start_time))

    grid1 = copy.deepcopy(grid)
    start_time = time.time()
    print('By recur+update+return connects:', 
          SolutionDFSUpdateReturnConnectsRecur().numIslands(grid1))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By recur+visit+return connects:', 
          SolutionDFSUpdateReturnConnectsRecur().numIslands(grid1))
    print('Time: {}'.format(time.time() - start_time))


    # Num of islands = 3.
    grid = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'], 
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']]

    grid2 = copy.deepcopy(grid)
    start_time = time.time()
    print('By recur+update:', SolutionDFSUpdateRecur().numIslands(grid2))
    print('Time: {}'.format(time.time() - start_time))

    grid2 = copy.deepcopy(grid)
    start_time = time.time()
    print('By recur+visit:', SolutionDFSVisitRecur().numIslands(grid2))
    print('Time: {}'.format(time.time() - start_time))

    grid2 = copy.deepcopy(grid)
    start_time = time.time()
    print('By iter+update:', SolutionDFSUpdateIter().numIslands(grid2))
    print('Time: {}'.format(time.time() - start_time))

    grid2 = copy.deepcopy(grid)
    start_time = time.time()
    print('By iter+visit:', SolutionDFSVisitIter().numIslands(grid2))
    print('Time: {}'.format(time.time() - start_time))

    grid2 = copy.deepcopy(grid)
    start_time = time.time()
    print('By recur+update+return connects:', 
          SolutionDFSUpdateReturnConnectsRecur().numIslands(grid2))
    print('Time: {}'.format(time.time() - start_time))

    grid2 = copy.deepcopy(grid)
    start_time = time.time()
    print('By recur+visit+return connects:', 
          SolutionDFSUpdateReturnConnectsRecur().numIslands(grid2))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
