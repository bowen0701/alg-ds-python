"""Leetcode 542. 01 Matrix
Medium

URL: https://leetcode.com/problems/01-matrix/

Given a matrix consists of 0 and 1, 
find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:
Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]
Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]] 

Note:
- The number of elements of the given matrix will not exceed 10,000.
- There are at least one 0 in the given matrix.
- The cells are adjacent in only four directions: up, down, left and right.
"""

class SolutionBFS(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n_rows, n_cols = len(matrix), len(matrix[0])

        # Use queue for BFS.
        queue = []

        for r in range(n_rows):
            for c in range(n_cols):
                if matrix[r][c] == 0:
                    # Just explore from cells with value 0.
                    queue.append((r, c))
                else:
                    # For cell with value != 0, update its distance to inf.
                    matrix[r][c] = float('inf')

        # Visiting directions.
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS explore from cells with value 0.
        while queue:
            r, c = queue.pop()
            for r_dir, c_dir in dirs:
                r_visit, c_visit = r + r_dir, c + c_dir

                # If visiting is out of boundary or does not shorten distance.
                if (r_visit < 0 or r_visit >= n_rows or
                    c_visit < 0 or c_visit >= n_cols or
                    matrix[r_visit][c_visit] < matrix[r][c] + 1):
                    continue

                matrix[r_visit][c_visit] = matrix[r][c] + 1
                queue.insert(0, (r_visit, c_visit))

        return matrix


def main():
    # Output:
    # [[0,0,0],
    #  [0,1,0],
    #  [0,0,0]]
    matrix = [[0,0,0],
              [0,1,0],
              [0,0,0]]
    print SolutionBFS().updateMatrix(matrix)

    # Output:
    # [[0,0,0],
    #  [0,1,0],
    #  [1,2,1]]
    matrix = [[0,0,0],
              [0,1,0],
              [1,1,1]]
    print SolutionBFS().updateMatrix(matrix)    


if __name__ == '__main__':
    main()
