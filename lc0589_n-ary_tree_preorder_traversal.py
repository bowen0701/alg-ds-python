"""Leetcode 589. N-ary Tree Preorder Traversal
Easy

URL: https://leetcode.com/problems/n-ary-tree-preorder-traversal/

Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:
      1
    / | \
   3  2  4
  / \
 5   6
Return its preorder traversal as: [1,3,5,6,2,4].

Note:
Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        pass

  
def main():
    pass


if __name__ == '__main__':
    main()
