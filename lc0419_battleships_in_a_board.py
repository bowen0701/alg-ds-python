"""Leetcode 419. Battleships in a Board
Medium

Given an 2D board, count how many battleships are in it.
The battleships are represented with 'X's, empty slots are represented with '.'s.
You may assume the following rules:
- You receive a valid board, made of only battleships or empty slots.
- Battleships can only be placed horizontally or vertically. In other words,
  they can only be made of the shape 1xN (1 row, N columns) or 
  Nx1 (N rows, 1 column), where N can be of any size.
- At least one horizontal or vertical cell separates between two battleships -
  there are no adjacent battleships.

Example:
X..X
...X
...X
In the above board there are 2 battleships.

Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive -
as battleships will always have a cell separating between them.

Follow up:
Could you do it in one-pass, using only O(1) extra memory and
without modifying the value of the board?
"""

class SolutionDFSRecur(object):
    def _dfsRecur(self, board, r, c):
        if (r < 0 or r >= len(board) or c < 0 or c >= len(board[0])
            or board[r][c] == '.'):
            return None

        # Update board as visited.
        board[r][c] = '.'

        # Recursively visit 4 dirs: up, down, left, and right.
        dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r_, c_ in dirs:
            self._dfsRecur(board, r_, c_)

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int

        Time complexity: O(m*n), where
          - m: number of rows.
          - n: number of columns.
        Space complexity: O(m*n).
        """
        if not board or not board[0]:
            return 0

        num_battleships = 0

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X':
                    num_battleships += 1
                    self._dfsRecur(board, r, c)

        return num_battleships


class SolutionIterCheckFirstEntries(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int

        Time complexity: O(m*n).
        Space complexity: O(1).
        """
        if not board or not board[0]:
            return 0

        num_battleships = 0

        for r in range(len(board)):
            for c in range(len(board[0])):
                # Skip if empty.
                if board[r][c] == '.':
                    continue

                # Skip if it's up is 'X' already.
                if r > 0 and board[r - 1][c] == 'X':
                    continue

                # Skip if it's left is 'X' already.
                if c > 0 and board[r][c - 1] == 'X':
                    continue

                num_battleships += 1

        return num_battleships


def main():
    import time

    print 'By DFS recur:'
    start_time = time.time()
    board = [['X','.','.','X'],
             ['.','.','.','X'],
             ['.','.','.','X']]
    print SolutionDFSRecur().countBattleships(board)
    print 'Time:', time.time() - start_time

    print 'By DFS recur:'
    start_time = time.time()
    board = [['X','.','.','X'],
             ['.','.','.','X'],
             ['.','.','.','X']]
    print SolutionIterCheckFirstEntries().countBattleships(board)
    print 'Time:', time.time() - start_time


if __name__ == '__main__':
    main()
