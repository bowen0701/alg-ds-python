"""Leetcode 200. Number of Islands

URL: https://leetcode.com/problems/number-of-islands/description/

Given a 2d grid map of '1's (land) and '0's (water), 
count the number of islands. 
An island is surrounded by water and is formed by connecting 
adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
11110
11010
11000
00000
Answer: 1

Example 2:
11000
11000
00100
00011
Answer: 3
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        pass


def main():
    grid1 = [['1', '1', '1', '1', '0'],
             ['1', '1', '0', '1', '0'], 
             ['1', '1', '0', '0', '0'],
             ['0', '0', '0', '0', '0']]

    print Solution().numIslands(grid1)

    grid2 = [['1', '1', '0', '0', '0'],
             ['1', '1', '0', '0', '0'], 
             ['0', '0', '1', '0', '0'],
             ['0', '0', '0', '1', '1']]

    print Solution().numIslands(grid2)


if __name__ == '__main__':
    main()
