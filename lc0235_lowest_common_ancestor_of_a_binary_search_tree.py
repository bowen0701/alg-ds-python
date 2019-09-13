"""Leetcode 235. Lowest Common Ancestor of a Binary Search Tree
Easy

URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) of
two given nodes in the BST.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is
defined between two nodes p and q as the lowest node in T that has both p and q
as descendants (where we allow a node to be a descendant of itself)."

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
      6
    /   \
   2     8
  / \   / \
 0   4 7   9
    / \
   3   5

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2,
since a node can be a descendant of itself according to the LCA definition.
 
Note:
- All of the nodes' values will be unique.
- p and q are different and both values will exist in the BST.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionRecur(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Check both p & q are in the node's left or right subtree. 
        # If not, the node splits p and q, so returh the node.
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


def main():
    #      6
    #    /   \
    #   2     8
    #  / \   / \
    # 0   4 7   9
    #    / \
    #   3   5
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    # Input: p = 2, q = 8
    # Output: 6
    p = root.left
    q = root.right
    print SolutionRecur().lowestCommonAncestor(root, p, q).val

    # Input: p = 2, q = 4
    # Output: 2
    p = root.left
    q = root.left.right
    print SolutionRecur().lowestCommonAncestor(root, p, q).val


if __name__ == '__main__':
    main()
