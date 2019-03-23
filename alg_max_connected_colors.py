def _dfs_recur(grid, visited_d):
    pass


def max_connected_colors(grid):
    """Maximum number of connected colors.

    Technique: DFS in a double for loops.

    Time complexity: O(m * n).
    Space complexity: O(m * n).
    """
    n_rows, n_cols = len(grid), len(grid[0])
    visited_d = {}

    for r in range(n_rows):
        for c in range(n_cols):
            if visited_d.get((r, c), None):
                pass



def main():
    # A grid of connected colors. Ans: 5 (of 2's).
    grid = [[1, 1, 2, 3],
            [1, 2, 3, 2],
            [3, 2, 2, 2]]


if __name__ == '__main__':
    main()
