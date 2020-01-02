"""Leetcode 427. Construct Quad Tree
Medium

URL: https://leetcode.com/problems/construct-quad-tree/

We want to use quad trees to store an N x N boolean grid. Each cell in the grid can
only be true or false. The root node represents the whole grid. For each node,
it will be subdivided into four children nodes until the values in the region it
represents are all the same.

Each node has another two boolean attributes : isLeaf and val. isLeaf is true if
and only if the node is a leaf node. The val attribute for a leaf node contains
the value of the region it represents.

Your task is to use a quad tree to represent a given grid. The following example
may help you understand the problem better:
[Image skipped]

Given the 8 x 8 grid below, we want to construct the corresponding quad tree:
[Image skipped]

It can be divided according to the definition above:
[Image skipped]

The corresponding quad tree should be as following, where each node is represented
as a (isLeaf, val) pair.

For the non-leaf nodes, val can be arbitrary, so it is represented as '*'.

Note:
- N is less than 1000 and guaranteened to be a power of 2.
- If you want to know more about the quad tree, you can refer to its wiki.
"""

# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class SolutionAllEqualTopLeftIsLeafRecur(object):
    def _isLeaf(self, grid):
        return all([val == grid[0][0]
                   for row in grid for val in row])

    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node

        Time complexity: O(n^2).
        Space complexity: O(n^2).
        """
        # Recursively check grid's vals equal top left. 
        # If yes: leaf node. Otherwise: not.
        if not grid:
            return None

        # If the node grid is leaf: all vals equal to top left val.
        if self._isLeaf(grid):
            return Node(grid[0][0], True, None, None, None, None)

        # If not, recursively construct quad tree with non-leaf node grid and 
        # its topLeft, topRight, bottomLeft, and bottomRight grid.
        n = len(grid)
        topLeft = self.construct([row[:n//2] for row in grid[:n//2]])
        topRight = self.construct([row[n//2:] for row in grid[:n//2]])
        bottomLeft = self.construct([row[:n//2] for row in grid[n//2:]])
        bottomRight = self.construct([row[n//2:] for row in grid[n//2:]])
        node = Node('*', False, topLeft, topRight, bottomLeft, bottomRight)
        return node


def main():
    grid = [[1, 0],
            [0, 1]]
    head = SolutionAllEqualTopLeftIsLeafRecur().construct(grid)

    # Output: (False, '*')
    print (head.isLeaf, head.val)

    # Output: (True, 1)
    print (head.topLeft.isLeaf, head.topLeft.val)

    # Output: (True, 0)
    print (head.topRight.isLeaf, head.topRight.val)
    
    # Output: (True, 0)
    print (head.bottomLeft.isLeaf, head.bottomLeft.val)

    # Output: (True, 1)
    print (head.bottomRight.isLeaf, head.bottomRight.val)


if __name__ == '__main__':
    main()
