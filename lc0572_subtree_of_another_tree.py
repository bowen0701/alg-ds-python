"""Leetcode 572. Subtree of Another Tree
Easy

URL: https://leetcode.com/problems/subtree-of-another-tree/

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure 
and node values with a subtree of s. 
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionPreorderSubtreeTreeMatchRecur:
    def _isTreeMatch(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case.
        if not root or not subRoot:
            return root is subRoot

        # Preorder traversal: root->left->right, to check root and left/right tree matches.
        if root.val != subRoot.val:
            return False

        return (self._isTreeMatch(root.left, subRoot.left)
                and self._isTreeMatch(root.right, subRoot.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(|s|*|t|), where |s| is the number of nodes in s.
        Space complexity: O(log|s|+log|t|), for balanced tree; 
          O(|s|+|t|) for single sided tree.
        """
        # Base case.
        if not root:
            return False

        # Check tree match first: if yes return True, if not, start checking left/right subtrees.
        # Preorder traversal: root->left->right, check if matches or subtree of left or right.
        if self._isTreeMatch(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot)
                or self.isSubtree(root.right, subRoot))


class SolutionTreeSerializationStringSearchKmp:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Time complexity
        Space complexity
        """
        pass


def main():
    # Given tree s:
    #      3
    #     / \
    #    4   5
    #   / \
    #  1   2
    # Given tree t:
    #    4 
    #   / \
    #  1   2
    # Output: True
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)
    print(SolutionPreorderSubtreeTreeMatchRecur().isSubtree(root, subRoot))

    # Given tree s:
    #      3
    #     / \
    #    4   5
    #   / \
    #  1   2
    #     /
    #    0
    # Given tree t:
    #    4
    #   / \
    #  1   2
    # Output: False
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(0)
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)
    print(SolutionPreorderSubtreeTreeMatchRecur().isSubtree(root, subRoot))


if __name__ == '__main__':
    main()
