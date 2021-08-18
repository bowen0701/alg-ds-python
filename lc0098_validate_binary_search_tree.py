"""Leetcode 98. Validate Binary Search Tree
Medium

URL: https://leetcode.com/problems/validate-binary-search-tree/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the 
node's key. The right subtree of a node contains only nodes with keys 
greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:
    2
   / \
  1   3
Input: [2,1,3]
Output: true

Example 2:
    5
   / \
  1   4
     / \
    3   6
Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val: Optional[int]):
        self.val = val
        self.left = None
        self.right = None


class SolutionMinMaxPreorderRecur(object):
    def _preorderRecur(self, root, min_val: int, max_val: int) -> bool:
        # Base case.
        if not root:
            return True
        
        # Preorder traveral: root->left->right, with updated left's max & right's min.
        if root.val <= min_val or root.val >= max_val:
            return False

        if not self._preorderRecur(root.left, min_val, root.val):
            return False

        if not self._preorderRecur(root.right, root.val, max_val):
            return False

        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        # Recursive preorder traversal to check if current val is in range (min, max),
        min_val, max_val = -float('inf'), float('inf')
        return self._preorderRecur(root, min_val, max_val)


class SolutionMinMaxPreorderIter(object):
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        # Edge case.
        if not root:
            return True

        # Iterative preorder traversal to check if current val is in range (min, max).
        min_val, max_val = -float('inf'), float('inf')

        stack = [(root, min_val, max_val)]
        while stack:
            current, min_val, max_val = stack.pop()

            # Preorder traveral: root->left->right, with updated left's max & right's min.
            if current.val <= min_val or current.val >= max_val:
                return False

            # Append right and then left because of stack's FILO.
            if current.right:
                stack.append([current.right, current.val, max_val])
            if current.left:
                stack.append([current.left, min_val, current.val])

        return True


class SolutionIncreasingInorderRecur(object):
    def _inorderRecur(self, root: Optional[TreeNode]) -> bool:
        # Base case.
        if not root:
            return True
 
        # Inorder traversal: left->root->right.
        if not self._inorderRecur(root.left):
            return False

        if self.previous and self.previous.val >= root.val:
            return False
        self.previous = root

        if not self._inorderRecur(root.right):
            return False

        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        # Check if inorder traversal visits values in an increasing fashion.
        self.previous = None
        return self._inorderRecur(root)


class SolutionIncreasingInorderIter(object):
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        # Check if inorder traversal visits values in an increasing fashion.
        # Edge case.
        if not root:
            return True

        previous = None
        current = root

        # Use stack for iterative inorder traversal: left->root->right.
        stack = []

        while current or stack:
            # Visit leftmost node.
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            # Visit current node to check if current val < previous val.
            if previous and previous.val >= current.val:
                return False

            # Visit its right.
            previous = current
            current = current.right

        return True


def main():
    import time

    # Input: [2,1,3]
    #    2
    #   / \
    #  1   3
    # Output: true
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    start_time = time.time()
    print('By MinMaxPreorderRecur: {}'
          .format(SolutionMinMaxPreorderRecur().isValidBST(root)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By MinMaxPreorderIter: {}'
          .format(SolutionMinMaxPreorderIter().isValidBST(root)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By IncreasingInorderRecur: {}'
          .format(SolutionIncreasingInorderRecur().isValidBST(root)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By IncreasingInorderIter: {}'
          .format(SolutionIncreasingInorderIter().isValidBST(root)))
    print('Time: {}'.format(time.time() - start_time))
    print('---')

    # Input: [5,1,4,null,null,3,6]
    #    5
    #   / \
    #  1   4
    #     / \
    #    3   6
    # Output: false
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)

    start_time = time.time()
    print('By MinMaxPreorderRecur: {}'
          .format(SolutionMinMaxPreorderRecur().isValidBST(root)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By MinMaxPreorderIter: {}'
          .format(SolutionMinMaxPreorderIter().isValidBST(root)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By IncreasingInorderRecur: {}'
          .format(SolutionIncreasingInorderRecur().isValidBST(root)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By IncreasingInorderIter: {}'
          .format(SolutionIncreasingInorderIter().isValidBST(root)))
    print('Time: {}'.format(time.time() - start_time))
    print('---')

    # Input: [10,5,15,null,null,6,20]
    #      10
    #     /  \
    #    5   15
    #       /  \
    #      6   20
    # Output: false
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(20)

    start_time = time.time()
    print('By MinMaxPreorderRecur: {}'
          .format(SolutionMinMaxPreorderRecur().isValidBST(root)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By MinMaxPreorderIter: {}'
          .format(SolutionMinMaxPreorderIter().isValidBST(root)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By IncreasingInorderRecur: {}'
          .format(SolutionIncreasingInorderRecur().isValidBST(root)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By IncreasingInorderIter: {}'
          .format(SolutionIncreasingInorderIter().isValidBST(root)))
    print('Time: {}'.format(time.time() - start_time))
    print('---')

    # Input:
    #      10
    #     /  \
    #    5   15
    #       /  \
    #      12   20
    #      /\
    #     6 14
    # Output: false
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)
    root.right.left.left = TreeNode(6)
    root.right.left.right = TreeNode(14)

    start_time = time.time()
    print('By MinMaxPreorderRecur: {}'
          .format(SolutionMinMaxPreorderRecur().isValidBST(root)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By MinMaxPreorderIter: {}'
          .format(SolutionMinMaxPreorderIter().isValidBST(root)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By IncreasingInorderRecur: {}'
          .format(SolutionIncreasingInorderRecur().isValidBST(root)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By IncreasingInorderIter: {}'
          .format(SolutionIncreasingInorderIter().isValidBST(root)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
