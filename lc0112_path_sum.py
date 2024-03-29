"""Leetcode 112. Path Sum
Easy

URL: https://leetcode.com/problems/path-sum/

Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionPreorderRecur:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        # Base case.
        if not root:
            return False

        # Preorder traversal: root->left->right, to check root-to-leaf path sum.
        if root.val == targetSum and not root.left and not root.right:
            return True

        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))


class SolutionPreorderIter:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        # Edge case.
        if not root:
            return False

        # Apply iterative preorder traversal with stack.
        stack = [(root, targetSum)]

        while stack:
            cur, cur_sum = stack.pop()

            # Preorder traversal: root->left->right, to check root-to-leaf path sum.
            if cur.val == cur_sum and not cur.left and not cur.right:
                return True

            # Append right->left because stack is LIFO.
            if cur.right:
                stack.append((cur.right, cur_sum - cur.val))
            if cur.left:
                stack.append((cur.left, cur_sum - cur.val))

        return False


class SolutionPostorderRecur:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        # Base case.
        if not root:
            return False
        
        # Postorder traversal: left->right->root, to check root-to-leaf path sum.
        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)
        if left or right:
            return True
        
        if root.val == targetSum and not root.left and not root.right:
            return True
        
        return False


class SolutionInorderRecur:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case.
        if not root:
            return False

        # Inorder traversal: left->root->right, to check root-to-leaf path sum.
        left = self.hasPathSum(root.left, targetSum - root.val)
        if left:
            return True

        if root.val == targetSum and not root.left and not root.right:
            return True

        right = self.hasPathSum(root.right, targetSum - root.val)
        if right:
            return True

        return False


def main():
    # Given the below binary tree and sum = 22,
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  /  \      \
    # 7    2      1
    # return true, 
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)

    targetSum = 22
    print(SolutionPreorderRecur().hasPathSum(root, targetSum))
    print(SolutionPreorderIter().hasPathSum(root, targetSum))
    print(SolutionPostorderRecur().hasPathSum(root, targetSum))
    print(SolutionInorderRecur().hasPathSum(root, targetSum))

    targetSum = 21
    print(SolutionPreorderRecur().hasPathSum(root, targetSum))
    print(SolutionPreorderIter().hasPathSum(root, targetSum))
    print(SolutionPostorderRecur().hasPathSum(root, targetSum))
    print(SolutionInorderRecur().hasPathSum(root, targetSum))


if __name__ == '__main__':
    main()
