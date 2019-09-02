"""Leetcode Treasure Island
Medium

URL: https://leetcode.com/discuss/interview-question/347457

Note: Amazon OA 2019.

You have a map that marks the location of a treasure island.
Some of the map area has jagged rocks and dangerous reefs.
Other areas are safe to sail in.
There are other explorers trying to find the treasure.
So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid,
represented by a matrix of characters.
You must start from the top-left corner of the map and
can move one block up, down, left or right at a time.
The treasure island is marked as 'X' in a block of the matrix.
'X' will not be at the top-left corner.
Any block with dangerous rocks or reefs will be marked as 'D'.
You must not enter dangerous blocks.
You cannot leave the map area. Other areas 'O' are safe to sail in.
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

class SolutionSteps(object):
    def treasureIsland(self, grid):
        """
        :type logs: List[list[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1

        n_rows, n_cols = len(grid), len(grid[0])

        # Apply BFS using queue for shortest route.
        queue = [(0, 0)]

        # Update grid to mark (0, 0) as visited.
        grid[0][0] = 'D'

        steps = 0

        while queue:
            size = len(queue)

            for _ in range(size):
                r, c = queue.pop()

                dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

                for r_neighbor, c_neighbor in dirs:
                    if (r_neighbor < 0 or r_neighbor >= n_rows or 
                        c_neighbor < 0 or c_neighbor >= n_cols or
                        grid[r_neighbor][c_neighbor] == 'D'):
                        continue

                    if grid[r_neighbor][c_neighbor] == 'X':
                        return steps + 1
                    
                    if grid[r_neighbor][c_neighbor] == 'O':
                        # Update grid to mark as visited.
                        grid[r_neighbor][c_neighbor] = 'D'
                        queue.insert(0, (r_neighbor, c_neighbor))

            steps += 1

        return -1


class SolutionDistances(object):
    def treasureIsland(self, grid):
        """
        :type logs: List[list[str]]
        :rtype: int
        """
        from collections import defaultdict

        if not grid or not grid[0]:
            return -1

        n_rows, n_cols = len(grid), len(grid[0])

        # Apply BFS using queue for shortest route.
        queue = [(0, 0)]

        # Update grid to mark (0, 0) as visited.
        grid[0][0] = 'D'

        steps_d = defaultdict(int)
        steps_d[(0, 0)] = 0

        while queue:
            size = len(queue)

            for _ in range(size):
                r, c = queue.pop()

                dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

                for r_neighbor, c_neighbor in dirs:
                    if (r_neighbor < 0 or r_neighbor >= n_rows or 
                        c_neighbor < 0 or c_neighbor >= n_cols or
                        grid[r_neighbor][c_neighbor] == 'D'):
                        continue

                    if grid[r_neighbor][c_neighbor] == 'X':
                        steps_d[(r_neighbor, c_neighbor)] =  steps_d[(r, c)] + 1
                        break
                    
                    if grid[r_neighbor][c_neighbor] == 'O':
                        # Update grid to mark as visited.
                        grid[r_neighbor][c_neighbor] = 'D'

                        steps_d[(r_neighbor, c_neighbor)] =  steps_d[(r, c)] + 1
                        queue.insert(0, (r_neighbor, c_neighbor))

        if steps_d.get((n_rows - 1, 0)):
            return steps_d[(n_rows - 1, 0)]
        else:
            return -1


def main():
    # Ans: 5.
    grid = [['O', 'O', 'O', 'O'],
            ['D', 'O', 'D', 'O'],
            ['O', 'O', 'O', 'O'],
            ['X', 'D', 'D', 'O']]
    print SolutionSteps().treasureIsland(grid)

    grid = [['O', 'O', 'O', 'O'],
            ['D', 'D', 'D', 'O'],
            ['O', 'O', 'O', 'O'],
            ['X', 'D', 'D', 'O']]
    print SolutionDistances().treasureIsland(grid)


if __name__ == '__main__':
    main()
