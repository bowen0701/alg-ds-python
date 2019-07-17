"""Leetcode 51. N-Queens.
Hard.

URL: https://leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an nxn chessboard 
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle 
as shown above.
"""

class Solution(object):
    def _is_valid(self, queens):
        """Check current queen position is valid among previous queens."""
        current_row, current_col = len(queens) - 1, queens[-1]

        # Check any queens can attack the current queen.
        for row, col in enumerate(queens[:-1]):
            col_diff = abs(current_col - col)
            row_diff = abs(current_row - row)
            if col_diff == 0 or col_diff == row_diff:
                return False

        return True

    def _dfs(self, n, res=[], queens=[]):
        """DFS for putting queens in suitable position."""
        if n == len(queens):
            res.append(queens[:])
            return None

        for col in range(n):
            # Append current queen's column id. 
            queens.append(col)

            if self._is_valid(queens):
                # If current queen's position is valid, search the next level.
                self._dfs(n, res, queens)

            # Backtrack by poping out current queen.
            queens.pop()

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]

        Time complexity: O(n!).
        Space complexity: O(n).
        """
        # res to collect multiple solutions for n_queens.
        res = []
        # queens is an 1-d array to store the column ids of queens.
        queens = []

        self._dfs(n, res, queens)

        # Make solution configs.
        sol = [['.'*j + 'Q' + '.'*(n - j - 1) for j in queens] 
               for queens in res]
        return sol


def main():
    n = 4
    print Solution().solveNQueens(n)


if __name__ == '__main__':
    main()
