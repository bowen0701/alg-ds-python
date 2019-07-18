from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def _is_valid(queens):
    """Check current queen position is valid."""
    current_row, current_col = len(queens) - 1, queens[-1]

    # Check any queens can attack the current queen.
    for row, col in enumerate(queens[:-1]):
        col_diff = abs(current_col - col)
        row_diff = abs(current_row - row)
        if col_diff == 0 or col_diff == row_diff:
            return False

    return True


def n_queens(n, queens=[]):
    """The number of N Queens.

    On an N by N board, get the number of possible arrangements of the board 
    where N queens can be placed on the board without attacking each other, 
    i.e. no two queens share the same row, column, or diagonal.

    Time complexity: O(n!).
    Space complexity: O(n).
    """
    # queens is an 1-D array to store the column ids of queens.
    if n == len(queens):
        return 1

    count = 0

    for col in range(n):
        # Append current queen's column id. 
        queens.append(col)

        if _is_valid(queens):
            # If current queen's position is valid, increment count by 1.
            count += n_queens(n, queens)

        # Backtrack by poping out current queen.
        queens.pop()
    
    return count


def main():
    # Should be 1, 1, 0, 0, 2, 10, 4, 40, 92, 352.
    for i in range(10):
        print(n_queens(i))


if __name__ == '__main__':
    main()
