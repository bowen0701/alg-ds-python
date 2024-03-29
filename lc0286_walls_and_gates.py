"""Leetcode 286. Walls and Gates (Premium)
Medium

URL: https://leetcode.com/problems/walls-and-gates/

You are given a m x n 2D grid initialized with these three possible values.
- -1 - A wall or an obstacle.
- 0 - A gate.
- INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to
represent INF as you may assume that the distance to a gate is less than 2147483647.
 
Fill each empty room with the distance to its nearest gate.
If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
0  -1 INF INF

After running your function, the 2D grid should be:
3  -1   0   1
2   2   1  -1
1  -1   2  -1
0  -1   3   4
"""

from typing import List


class SolutionDFSRecur(object):
    def _dfs(self, r: int, c: int, distance: int, rooms: List[List[int]]) -> None:
        # Base case: out of boundary, or have smaller distance or hit a wall.
        if (r < 0 or r >= len(rooms) 
            or c < 0 or c >= len(rooms[0]) 
            or rooms[r][c] < distance):
            return None

        # Update the shortest distance.
        rooms[r][c] = distance

        # Visit gate's neighbors: up/down/left/right with DFS.
        dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r_next, c_next in dirs:
            self._dfs(r_next, c_next, distance + 1, rooms)

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Time complexity: O(kmn), where
          - k: number of gates
          - m: number of rows
          - n: number of columns
        Space complexity: O(mn), for gates list.
        """
        # Edge case.
        if not rooms or not rooms[0]:
            return None
        
        # Apply recursive DFS to visit rooms starting from all gates.
        n_rows, n_cols = len(rooms), len(rooms[0])

        # Collect all gates.
        gates = [(r, c) for r in range(n_rows) for c in range(n_cols)
                 if rooms[r][c] == 0]

        # Iterate through gates to update distance to gate.
        for (r, c) in gates:
            distance = 0
            self._dfs(r, c, distance, rooms)


class SolutionBFS(object):
    def _bfs(self, r: int, c: int, rooms: List[List[int]]) -> None:
        from collections import deque

        n_rows, n_cols = len(rooms), len(rooms[0])

        # Put one of gates in the queue.
        queue = deque([(r, c)])

        while queue:
            for _ in range(len(queue)):
                r, c = queue.pop()

                # Visit gate's neighbors: up/down/left/right.
                dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                for r_next, c_next in dirs:
                    # If out of boundary, skip visiting.
                    if (r_next < 0 or r_next >= n_rows
                        or c_next < 0 or c_next >= n_cols):
                        continue

                    # If found short distance, update distance & visit neigghbors.
                    if rooms[r_next][c_next] > rooms[r][c] + 1:
                        rooms[r_next][c_next] = rooms[r][c] + 1
                        queue.appendleft((r_next, c_next))

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Time complexity: O(kmn), where
          - k: number of gates
          - m: number of rows
          - n: number of columns
        Space complexity: O(mn).
        """
        # Edge case.
        if not rooms or not rooms[0]:
            return None

        # Apply iterative BFS to visit rooms starting from all gates.
        n_rows, n_cols = len(rooms), len(rooms[0])

        # Collect all gates.
        gates = [(r, c) for r in range(n_rows) for c in range(n_cols)
                 if rooms[r][c] == 0]

        # Iterate through gates by BFS to update neighbors's shorter distances.
        for (r, c) in gates:
            self._bfs(r, c, rooms)


def main():
    import copy
    import time

    # After running your function, the 2D grid should be:
    # 3  -1   0   1
    # 2   2   1  -1
    # 1  -1   2  -1
    # 0  -1   3   4
    rooms = [
        [float('inf'), -1, 0, float('inf')],
        [float('inf'), float('inf'), float('inf'), -1],
        [float('inf'), -1, float('inf'), -1],
        [0, -1, float('inf'), float('inf')]
    ]

    rooms1 = copy.deepcopy(rooms)
    start_time = time.time()
    SolutionDFSRecur().wallsAndGates(rooms1)
    print("SolutionDFSRecur:", time.time() - start_time)
    print(rooms1)

    rooms1 = copy.deepcopy(rooms)
    start_time = time.time()
    SolutionBFS().wallsAndGates(rooms1)
    print("SolutionBFS:", time.time() - start_time)
    print(rooms1)


if __name__ == '__main__':
    main()
