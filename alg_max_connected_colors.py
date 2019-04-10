from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def _dfs_recur0(r, c, grid, visited_d, cc):
    visited_d[(r, c)] = True
    color = grid[r][c]
    cc[0] += 1

    if (r - 1 >= 0 and not visited_d.get((r - 1, c)) and
        color == grid[r - 1][c]):    # Up.
        _dfs_recur0(r - 1, c, grid, visited_d, cc)
    if (r + 1 <= len(grid) - 1 and not visited_d.get((r + 1, c)) and
        color == grid[r + 1][c]):    # Down.
        _dfs_recur0(r + 1, c, grid, visited_d, cc)
    if (c - 1 >= 0 and not visited_d.get((r, c - 1)) and
        color == grid[r][c - 1]):    # Left.
        _dfs_recur0(r, c - 1, grid, visited_d, cc)
    if (c + 1 <= len(grid[0]) - 1 and not visited_d.get((r, c + 1)) and
        color == grid[r][c + 1]):    # Right.
        _dfs_recur0(r, c + 1, grid, visited_d, cc)


def max_connected_colors0(grid):
    """Maximum number of connected colors (naive).

    Technique: DFS in a double for loops.

    Time complexity: O(m * n).
    Space complexity: O(m * n).
    """
    visited_d = {}
    max_cc = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            cc = [0]
            _dfs_recur0(r, c, grid, visited_d, cc)
            max_cc = max(cc[0], max_cc)

    return max_cc


def _dfs_recur(r, c, grid, color, visited_d):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return 0

    if color != grid[r][c] or visited_d.get((r, c)):
        return 0

    visited_d[(r, c)] = True
    cc = 1

    for r_neighbor in [r - 1, r + 1]:  # Up & down.
        cc += _dfs_recur(r_neighbor, c, grid, color, visited_d)

    for c_neighbor in [c - 1, c + 1]:  # Left & right.
        cc += _dfs_recur(r, c_neighbor, grid, color, visited_d)

    return cc


def max_connected_colors(grid):
    """Maximum number of connected colors.

    Technique: DFS in a double for loops by return.

    Time complexity: O(m * n).
    Space complexity: O(m * n).
    """
    visited_d = {}
    max_cc = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            color = grid[r][c]
            cc = _dfs_recur(r, c, grid, color, visited_d)
            max_cc = max(cc, max_cc)

    return max_cc


def main():
    # A grid of connected colors. Ans: 5 (of 2's).
    grid = [[1, 1, 2, 3],
            [1, 2, 3, 2],
            [3, 2, 2, 2]]

    print(max_connected_colors0(grid))
    print(max_connected_colors(grid))


if __name__ == '__main__':
    main()
