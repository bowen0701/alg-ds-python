"""Leetcode 543. Diameter of Binary Tree
Easy

URL: https://leetcode.com/problems/diameter-of-binary-tree/

Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any
two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of
edges between them.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionPathDepthRecur(object):
    def _pathDepth(self, root):
        if not root:
            return 0

        left_depth = self._pathDepth(root.left)
        right_depth = self._pathDepth(root.right)
        self.diameter = max(self.diameter, left_depth + right_depth)
        return 1 + max(left_depth, right_depth)

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time complexity: O(logn) for balanced tree; O(n) for single sided.
        Space complexity: O(logn) or O(n).
        """
        # Apply postorder traversal to get sum of left & right subtree depths.
        self.diameter = 0
        self._pathDepth(root)
        return self.diameter


def main():
    # Given a binary tree
    #           1
    #          / \
    #         2   3
    #        / \     
    #       4   5
    # Output: 3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print SolutionPathDepthRecur().diameterOfBinaryTree(root)


if __name__ == '__main__':
    main()
