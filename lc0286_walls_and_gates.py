"""Leetcode 286. Walls and Gates (Premium)
Medium

URL: https://leetcode.com/problems/walls-and-gates/

You are given a m x n 2D grid initialized with these three possible values.
-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to
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

class SolutionBFS(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.

        Apply BFS starting from all gates.

        Time complexity: O(kmn), where
          - k: number of gates
          - m: number of rows
          - n: number of columns
        Space complexity: O(mn).
        """
        nrows, ncols = len(rooms), len(rooms[0])

        # Collect all gates in queue.
        gates = []
        for i in range(nrows):
            for j in range(ncols):
                if rooms[i][j] == 0:
                    gates.append((i, j))

        # For each gate, start BFS to update neighbors's shorter distances.
        while gates:
            queue = [gates.pop()]

            while queue:
                r, c = queue.pop()

                dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                for r_next, c_next in dirs:
                    if (0 <= r_next < nrows and 0 <= c_next < ncols and
                        rooms[r_next][c_next] > rooms[r][c] + 1):
                        rooms[r_next][c_next] = rooms[r][c] + 1
                        queue.insert(0, (r_next, c_next))


def main():
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
    SolutionBFS().wallsAndGates(rooms)
    print rooms


if __name__ == '__main__':
    main()
