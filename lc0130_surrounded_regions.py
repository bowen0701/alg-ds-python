"""Leetcode 130. Surrounded Regions
Medium

URL: https://leetcode.com/problems/surrounded-regions/

Given a 2D board containing 'X' and 'O' (the letter O),
capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:
Surrounded regions shouldn't be on the border,
which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O'
on theborder will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected
horizontally or vertically.
"""

class SolutionDFS(object):
    def _dfs(self, r, c, board):
        # Skip the boards and land 'X'.
        if (r <= 0 or r >= len(board) - 1 or
            c <= 0 or c >= len(board[0]) - 1 or
            board[r][c] == 'X'):
            return None

        # Skip land '*'.
        if board[r][c] == '*':
            return None

        # If land is 'O', modify it to '*' to skip modification to 'X'.
        if board[r][c] == 'O':
            board[r][c] = '*'

        # Visit its up, down, left and right.
        self._dfs(r - 1, c, board)
        self._dfs(r + 1, c, board)
        self._dfs(r, c - 1, board)
        self._dfs(r, c + 1, board)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.

        Time complexity: O((m+n)*m*n), where m and n is the number of rows and columns.
        Space complxity: O(m*n).
        """
        if not board or not board[0]:
            return None

        n_rows, n_cols = len(board), len(board[0])

        # First, check the four borders. If there is a element is 'O', 
        # modify it and all its neighbor 'O' elements to '*'.
        for r in range(n_rows):
            if board[r][0] == 'O':
                self._dfs(r, 1, board)
            if board[r][n_cols - 1] == 'O':
                self._dfs(r, n_cols - 2, board)

        for c in range(n_cols):
            if board[0][c] == 'O':
                self._dfs(1, c, board)
            if board[n_rows - 1][c] == 'O':
                self._dfs(n_rows - 2, c, board)

        # Then, skip boards to modify all the 'O' to 'X' or all '*' back to 'O'.
        for r in range(1, n_rows - 1):
            for c in range(1, n_cols - 1):
                if board[r][c] == '*':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'


def main():
    board = [
      ['X','X','X','X'],
      ['X','O','O','X'],
      ['X','X','O','X'],
      ['X','O','X','X']
    ]
    SolutionDFS().solve(board)
    print board


if __name__ == '__main__':
    main()
