"""Leetcode: Treasure Island
Medium

URL: https://leetcode.com/discuss/interview-question/347457

Note: A.k.a. Min Distance to Remove the Obstacle.

You have a map that marks the location of a treasure island.
Some of the map area has jagged rocks and dangerous reefs.
Other areas are safe to sail in.
There are other explorers trying to find the treasure.
So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters.
You must start from the top-left corner of the map and can move one block 
up, down, left or right at a time.
- The treasure island is marked as 'X' in a block of the matrix.
  'X' will not be at the top-left corner.
- Any block with dangerous rocks or reefs will be marked as 'D'.
  You must not enter dangerous blocks.
- You cannot leave the map area. Other areas 'O' are safe to sail in.
The top-left corner is always safe.
Output the minimum number of steps to get to the treasure.

Example:
Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]
Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) 
The minimum route takes 5 steps.
"""

from typing import List, Dict, Tuple


class SolutionBFS(object):
    def _bfs(self, r: int, c: int, grid: List[List[str]]) -> int:
        from collections import deque

        n_rows, n_cols = len(grid), len(grid[0])

        # Mark (r, c) as visited.
        grid[r][c] = 'D'
        distance = 0

        # Apply BFS with queue.
        queue = deque([(r, c)])

        while queue:
            for _ in range(len(queue)):
                r, c = queue.pop()

                # Visiting neighbors: top/down/left/down.
                dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                for r_next, c_next in dirs:
                    # If is out of boundary or visited.
                    if (r_next < 0 or r_next >= n_rows
                        or c_next < 0 or c_next >= n_cols 
                        or grid[r_next][c_next] == 'D'):
                        continue

                    # If found treasure, return result.
                    if grid[r_next][c_next] == 'X':
                        return distance + 1
                    
                    # If visit safe area, mark it as visited and visit neighbors.
                    if grid[r_next][c_next] == 'O':
                        grid[r_next][c_next] = 'D'
                        queue.appendleft((r_next, c_next))

            distance += 1

        return -1


    def treasureIsland(self, grid: List[list[str]]) -> int:
        """
        Time complexity: O(m*n).
        Space complexity: O(m*n).
        """
        # Edge case.
        if not grid or not grid[0]:
            return -1

        # Apply BFS using queue, given (0, 0) and marked it as visited.
        r, c = 0, 0
        return self._bfs(r, c, grid)


class SolutionBFSAll(object):
    def _bfs(self, 
        r: int,
        c: int,
        grid: List[List[int]],
        pos_distance_d: Dict[Tuple[int, int], int]
    ) -> int:
        from collections import deque

        n_rows, n_cols = len(grid), len(grid[0])

        # Mark as visited.
        pos_distance_d[(r, c)] = 0
        grid[r][c] = 'D'

        # Apply BFS with queue.
        queue = deque([(r, c)])

        while queue:
            for _ in range(len(queue)):
                r, c = queue.pop()

                # Visit neighbors: up/down/left/right.
                dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                for r_next, c_next in dirs:
                    # If is out of boundary or visited, skip visiting.
                    if (r_next < 0 or r_next >= n_rows or 
                        c_next < 0 or c_next >= n_cols or
                        grid[r_next][c_next] == 'D'):
                        continue

                    # If found treasure, update distance.
                    if grid[r_next][c_next] == 'X':
                        pos_distance_d[(r_next, c_next)] = pos_distance_d[(r, c)] + 1
                        break
                    
                    # If safe area, mark visited and visit neighbors.
                    if grid[r_next][c_next] == 'O':
                        grid[r_next][c_next] = 'D'
                        pos_distance_d[(r_next, c_next)] = pos_distance_d[(r, c)] + 1
                        queue.appendleft((r_next, c_next))

    def treasureIsland(self, grid: List[list[str]]) -> int:
        """
        Time complexity: O(m*n).
        Space complexity: O(m*n).
        """
        from collections import defaultdict

        # Edge case.
        if not grid or not grid[0]:
            return -1

        n_rows, n_cols = len(grid), len(grid[0])

        # Collect pos->distance.
        pos_distance_d = defaultdict(int)

        # Apply BFS with queue, given (0, 0) and marked it as visited.
        r, c = 0, 0
        self._bfs(r, c, grid, pos_distance_d)

        if pos_distance_d.get((n_rows - 1, 0)):
            return pos_distance_d[(n_rows - 1, 0)]
        else:
            return -1


class SolutionDFSRecur(object):
    def _dfs(self, r: int, c: int, distance: int, grid: List[list[str]]) -> None:
        # Apply recursive DFS.
        n_rows, n_cols = len(grid), len(grid[0])

        # Base case: is out of boundary or visited or have smaller distance.
        if (r < 0 or r >= n_rows
            or c < 0 or c >= n_cols
            or grid[r][c] == 'D'
            or self.result < distance):
            return None

        # If found treasure, update distance and return result.
        if grid[r][c] == 'X':
            self.result = distance
            return None

        # Mark (r, c) as visited.
        grid[r][c] = 'D'

        # TODO: Visit neighbors: top/down/left/down.
        dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r_next, c_next in dirs:
            self._dfs(r_next, c_next, distance + 1, grid)

    def treasureIsland(self, grid: List[list[str]]) -> int:
        """
        Time complexity: O(m*n).
        Space complexity: O(m*n).
        """
        # Edge case.
        if not grid or not grid[0]:
            return -1

        # Apply recursive DFS given (0, 0).
        self.result = float('inf')
        r, c = 0, 0
        distance = 0
        self._dfs(r, c, distance, grid)
        
        if self.result < float('inf'):
            return self.result
        else:
            return -1


def main():
    import copy
    import time

    # Output: 5.
    grid = [['O', 'O', 'O', 'O'],
            ['D', 'O', 'D', 'O'],
            ['O', 'O', 'O', 'O'],
            ['X', 'D', 'D', 'O']]

    grid1 = copy.deepcopy(grid)
    start_time = time.time()
    print(SolutionBFS().treasureIsland(grid1))
    print("SolutionBFS time:", time.time() - start_time)

    grid1 = copy.deepcopy(grid)
    print(SolutionBFSAll().treasureIsland(grid1))
    print("SolutionBFSAll time:", time.time() - start_time)

    grid1 = copy.deepcopy(grid)
    print(SolutionDFSRecur().treasureIsland(grid1))
    print("SolutionDFSRecur time:", time.time() - start_time)


if __name__ == '__main__':
    main()
