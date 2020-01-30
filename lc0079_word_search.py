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

class SolutionDfsBacktrackRecur(object):
    def _dfsBracktrackRecur(self, i, j, board, word, pos, visited_d):
        # If there are no letters, complete search.
        if pos == len(word):
            return True

        # If (i, j) is out of boundaries, does not match letter or is visited.
        if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or 
            board[i][j] != word[pos] or
            visited_d.get((i, j))):
            return False

        # Mark (i, j) as visited.
        visited_d[(i, j)] = True

        # Start DFS: if one of DFSs is true, return True.
        is_found = False
        dirs = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for i_next, j_next in dirs:
            is_found |= self._dfsBracktrackRecur(
                i_next, j_next, board, word, pos + 1, visited_d)

        # Backtrack.
        visited_d[(i, j)] = False

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
                # Start from 0th letter pos of word.
                pos = 0
                visited_d = {}
                if self._dfsBracktrackRecur(i, j, board, word, pos, visited_d):
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
    print SolutionDfsBacktrackRecur().exist(board, word)

    # Given word = "SEE", return true.
    word = 'SEE'
    print SolutionDfsBacktrackRecur().exist(board, word)

    # Given word = "ABCB", return false.
    word = 'ABCB'
    print SolutionDfsBacktrackRecur().exist(board, word)


if __name__ == '__main__':
    main()
