"""Leetcode 559. Maximum Depth of N-ary Tree
Easy

URL: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node
down to the farthest leaf node.

For example, given a 3-ary tree:
      1
    / | \
   3  2  4
  / \
 5   6
We should return its max depth, which is 3.

Note:
- The depth of the tree is at most 1000.
- The total number of nodes is at most 5000.
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        """
        :type val: int
        :type children: list
        :rtype: int
        """
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        pass


def main():
    pass
