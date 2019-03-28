from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def _dfs_recur(r, c, grid, visited_d, max_num):
    visited_d[(r, c)] = True
    color = grid[r][c]
    max_num[0] += 1

    if (r - 1 >= 0 and not visited_d.get((r - 1, c)) and
        color == grid[r - 1][c]):    # Up.
        _dfs_recur(r - 1, c, grid, visited_d, max_num)
    if (r + 1 <= len(grid) - 1 and not visited_d.get((r + 1, c)) and
        color == grid[r + 1][c]):    # Down.    
        _dfs_recur(r + 1, c, grid, visited_d, max_num)
    if (c - 1 >= 0 and not visited_d.get((r, c - 1)) and
        color == grid[r][c - 1]):    # Left.
        _dfs_recur(r, c - 1, grid, visited_d, max_num)    
    if (c + 1 <= len(grid[0]) - 1 and not visited_d.get((r, c + 1)) and
        color == grid[r][c + 1]):    # Right.
        _dfs_recur(r, c + 1, grid, visited_d, max_num)


def max_connected_colors(grid):
    """Maximum number of connected colors.

    Technique: DFS in a double for loops.

    Time complexity: O(m * n).
    Space complexity: O(m * n).
    """
    visited_d = {}
    max_num = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            max_num_rc = [0]
            _dfs_recur(r, c, grid, visited_d, max_num_rc)

            if max_num_rc[0] > max_num:
                max_num = max_num_rc[0]

    return max_num


def main():
    # A grid of connected colors. Ans: 5 (of 2's).
    grid = [[1, 1, 2, 3],
            [1, 2, 3, 2],
            [3, 2, 2, 2]]
    print(max_connected_colors(grid))


if __name__ == '__main__':
    main()
