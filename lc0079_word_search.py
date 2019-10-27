"""Leetcode 79. Word Search
Medium

URL: https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

class SolutionDFSRecurBacktrack(object):
    def _dfsRecur(self, i, j, board, word, pos, visited):
        # If there are no letters, return True.
        if pos == len(word):
            return True

        # If (i, j) is out of boundaries, does not match word letter or is visited.
        if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or 
            board[i][j] != word[pos] or
            visited.get((i, j))):
            return False

        # Mark (i, j) as visited.
        visited[(i, j)] = True

        # Start DFS visiting, one of DFSs is true, then return True.
        is_found = False
        dirs = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for r, c in dirs:
            is_found = is_found or self._dfsRecur(r, c, board, word, pos + 1, visited)

        # Backtrack.
        visited[(i, j)] = False

        return is_found

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool

        Time complexity: O(m * n * 4^s), where
          - m is the number of rows,
          - n is the number of cols,
          - s is the length of word.
        Space complexity: O(m * n).
        """
        if not board or not board[0]:
            return False

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                pos = 0
                visited = {}
                if self._dfsRecur(i, j, board, word, pos, visited):
                    return True

        return False


def main():
    board = [
              ['A','B','C','E'],
              ['S','F','C','S'],
              ['A','D','E','E']
            ]

    # Given word = "ABCCED", return true.
    word = 'ABCCED'
    print SolutionDFSRecurBacktrack().exist(board, word)

    # Given word = "SEE", return true.
    word = 'SEE'
    print SolutionDFSRecurBacktrack().exist(board, word)

    # Given word = "ABCB", return false.
    word = 'ABCB'
    print SolutionDFSRecurBacktrack().exist(board, word)


if __name__ == '__main__':
    main()
