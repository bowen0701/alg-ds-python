"""Leetcode 1197. Minimum Knight Moves
Medium

URL: https://leetcode.com/problems/minimum-knight-moves/

In an infinite chess board with coordinates from -infinity to +infinity,
you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below.
Each move is two squares in a cardinal direction, then one square in an
orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y].
It is guaranteed the answer exists.

Example 1:
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] -> [2, 1]

Example 2:
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] -> [2, 1] -> [4, 2] -> [3, 4] -> [5, 5]

Constraints:
|x| + |y| <= 300
"""


class SolutionNaiveBFS(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # Apply naive BFS from source (x, y) to search (0, 0), with seen_set.
        from collections import deque

        # Edge case.
        if (x, y) == (0, 0):
            return 0

        # Apply iterative BFS with queue for traversal and seen set for marking visited.
        queue = deque([(x, y)])
        seen_set = set([(x, y)])
        step = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.pop()

                # Directions for knight moves.
                dirs = [
                    (r + 1, c + 2), (r + 1, c - 2), 
                    (r - 1, c + 2), (r - 1, c - 2),
                    (r + 2, c + 1), (r + 2, c - 1), 
                    (r - 2, c + 1), (r - 2, c - 1)
                ]

                for r_next, c_next in dirs:
                    if (r_next, c_next) not in seen_set:
                        if (r_next, c_next) == (0, 0):
                            return step + 1
                        else:
                            seen_set.add((r_next, c_next))
                            queue.appendleft((r_next, c_next))

            step += 1


class SolutionBFS(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # Apply BFS from source (x, y) to search (0, 0), with seen_set.
        # - Based on symmetry, search (|x|, |y|) from (0, 0).
        # - Search only in 1st quadrant.

        from collections import deque

        # Edge case.
        if (x, y) == (0, 0):
            return 0

        # Apply iterative BFS with queue for traversal and seen set for marking visited.
        # Based on symmetry, search (|x|, |y|) from (0, 0).
        x, y = abs(x), abs(y)
        queue = deque([(0, 0)])
        seen_set = set([(0, 0)])
        step = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.pop()

                # Directions for knight moves.
                dirs = [
                    (r + 1, c + 2), (r + 1, c - 2), 
                    (r - 1, c + 2), (r - 1, c - 2),
                    (r + 2, c + 1), (r + 2, c - 1), 
                    (r - 2, c + 1), (r - 2, c - 1)
                ]

                for r_next, c_next in dirs:
                    # Search if not seen and only in 1st quadrant.
                    if ((r_next, c_next) not in seen_set and
                        r_next > -2 and c_next > -2):
                        if (r_next, c_next) == (x, y):
                            return step + 1
                        else:
                            seen_set.add((r_next, c_next))
                            queue.appendleft((r_next, c_next))

            step += 1


def main():
    # Output: 1
    x = 2
    y = 1
    print SolutionNaiveBFS().minKnightMoves(x, y)
    print SolutionBFS().minKnightMoves(x, y)

    # Output: 4
    x = 5
    y = 5
    print SolutionNaiveBFS().minKnightMoves(x, y)
    print SolutionBFS().minKnightMoves(x, y)


if __name__ == '__main__':
    main()
