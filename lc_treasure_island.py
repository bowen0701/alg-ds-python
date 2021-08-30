"""Leetcode: Treasure Island
Medium

URL: https://leetcode.com/discuss/interview-question/347457

Note: A.k.a. Min Distance to Remove the Obstacle.

You have a map that marks the location of a treasure island.
Some of the map area has jagged rocks and dangerous reefs.
Other areas are safe to sail in.
There are other explorers trying to find the treasure.
So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid,
represented by a matrix of characters.
You must start from the top-left corner of the map and
can move one block up, down, left or right at a time.
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

from typing import List


class SolutionBFSSteps(object):
    def treasureIsland(self, grid: List[list[str]]) -> int:
        """
        Time complexity: O(m*n).
        Space complexity: O(m*n).
        """
        from collections import deque

        # Edge case.
        if not grid or not grid[0]:
            return -1

        n_rows, n_cols = len(grid), len(grid[0])

        # Apply BFS using queue, starting from (0, 0), marked as visited.
        queue = deque([(0, 0)])
        grid[0][0] = 'D'
        steps = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.pop()

                # Visiting directions.
                dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                for r_next, c_next in dirs:
                    # If is out of boundary or visited, skip visiting.
                    if (r_next < 0 or r_next >= n_rows or 
                        c_next < 0 or c_next >= n_cols or
                        grid[r_next][c_next] == 'D'):
                        continue

                    # If found treasure, return result.
                    if grid[r_next][c_next] == 'X':
                        return steps + 1
                    
                    # If visit safe area, mark it as visited and visit neighbors.
                    if grid[r_next][c_next] == 'O':
                        grid[r_next][c_next] = 'D'
                        queue.appendleft((r_next, c_next))

            steps += 1

        return -1


class SolutionBFSAllSteps(object):
    def treasureIsland(self, grid: List[list[str]]) -> int:
        """
        Time complexity: O(m*n).
        Space complexity: O(m*n).
        """
        from collections import defaultdict
        from collections import deque

        # Edge case.
        if not grid or not grid[0]:
            return -1

        n_rows, n_cols = len(grid), len(grid[0])

        # Apply BFS with queue, starting from (0, 0), marked as visited.
        queue = deque([(0, 0)])
        grid[0][0] = 'D'

        pos_steps_d = defaultdict(int)
        pos_steps_d[(0, 0)] = 0

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
                        pos_steps_d[(r_next, c_next)] = pos_steps_d[(r, c)] + 1
                        break
                    
                    # If safe area, mark visited and visit neighbors.
                    if grid[r_next][c_next] == 'O':
                        grid[r_next][c_next] = 'D'
                        pos_steps_d[(r_next, c_next)] = pos_steps_d[(r, c)] + 1
                        queue.appendleft((r_next, c_next))

        if pos_steps_d.get((n_rows - 1, 0)):
            return pos_steps_d[(n_rows - 1, 0)]
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
    print(SolutionBFSSteps().treasureIsland(grid1))
    print("SolutionBFSSteps time:", time.time() - start_time)

    grid1 = copy.deepcopy(grid)
    print(SolutionBFSAllSteps().treasureIsland(grid1))
    print("SolutionBFSAllSteps time:", time.time() - start_time)


if __name__ == '__main__':
    main()
