from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def _dfs(r, c, grid, visited_d):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return 0
   
    if grid[r][c] == 0 or visited_d.get((r, c)):
        return 0

    visited_d[(r, c)] = True
    cc = 1
    for r_neighbor in range(r - 1, r + 2):
        for c_neighbor in range(c - 1, c + 2):
            if (r_neighbor, c_neighbor) != (r, c):
                    cc += _dfs(r_neighbor, c_neighbor, grid, visited_d)
    return cc

def max_connected_cells(grid):
    visited_d = {}
    max_cc = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1 and not visited_d.get((r, c)):
                cc = _dfs(r, c, grid, visited_d)
                max_cc = max(cc, max_cc)
    return max_cc


def main():
    # Ans: 7 at right-upper corner.
    grid = [[0, 0, 0, 1, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0],
            [1, 1, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 0],
            [1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0]]

    print('Max connected cells: {}'.format(max_connected_cells(grid)))


if __name__ == '__main__':
    main()
