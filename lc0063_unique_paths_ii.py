"""Leetcode 63. Unique Paths II.
Medium

URL: https://leetcode.com/problems/unique-paths-ii/

A robot is located at the top-left corner of a m x n grid 
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid
(marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. 
How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """Unique paths with obstacles.

        Time complexity: O(mn).
        Space complexity: O(mn).
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        path = [[0] * n for _ in range(m)]
        
        # Set the top-left to 1.
        if obstacleGrid[0][0] == 0:
            path[0][0] = 1
    
        # Set the 1st row to 1 util reach obstacles.
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                path[0][j] = path[0][j - 1]
            else:
                break

        # Set the 1st col to 1 util reach obstacles.
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                path[i][0] = path[i - 1][0]
            else:
                break
        
        # Compute path to (i, j) from (i - 1, j) and (i, j - 1).
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    path[i][j] = path[i - 1][j] + path[i][j - 1]
        
        return path[-1][-1]


def main():
    obstacleGrid = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    
    print Solution().uniquePathsWithObstacles(obstacleGrid)


if __name__ == '__main__':
    main()
