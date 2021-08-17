"""Leetcode 230. Kth Smallest Element in a BST
Medium

URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given a binary search tree, write a function kthSmallest to find the 
kth smallest element in it.

Note: 
You may assume k is always valid, 1 <= k <= BST's total elements.

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and 
you need to find the kth smallest frequently? 
How would you optimize the kthSmallest routine?
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val: Optional[int] = None):
        self.val = val
        self.left = None
        self.right = None


class SolutionInorderRecur(object):
    def _inorderRecur(self, root: Optional[TreeNode]) -> None:
        # Base case.
        if not root:
            return None

        # Inorder traversal: left->root->right.
        self._inorderRecur(root.left)

        self.k -= 1
        if self.k == 0:
            self.result = root.val
            return None

        self._inorderRecur(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Time complexity: O(k).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        # Apply recursive inorder traversal.
        self.result = None
        self.k = k
        self._inorderRecur(root)
        return self.result


class SolutionInorderIter(object):
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Time complexity: O(k).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        # Apply iterative inorder traversal: left->root->right.
        previous = None
        current = root

        stack = []

        while current or stack:
            # Visit the leftmost node.
            while current:
                stack.append(current)
                current = current.left

            # Visit its parent.
            current = stack.pop()
            k -= 1
            if k == 0:
                break

            # Then visit its right.
            previous = current
            current = current.right

        return current.val

        
def main():
    # Input: root = [3,1,4,null,2], k = 1
    #    3
    #   / \
    #  1   4
    #   \
    #    2
    # Output: 1
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    k = 1
    print('By recur: {}'.format(SolutionInorderRecur().kthSmallest(root, k)))
    print('By iter: {}'.format(SolutionInorderIter().kthSmallest(root, k)))

    # Input: root = [5,3,6,2,4,null,null,1], k = 3
    #        5
    #       / \
    #      3   6
    #     / \
    #    2   4
    #   /
    #  1
    # Output: 3
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    k = 3
    print('By recur: {}'.format(SolutionInorderRecur().kthSmallest(root, k)))
    print('By iter: {}'.format(SolutionInorderIter().kthSmallest(root, k)))


if __name__ == '__main__':
    main()
