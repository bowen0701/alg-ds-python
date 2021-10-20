"""Leetcode 938. Range Sum of BST
Easy

URL: https://leetcode.com/problems/range-sum-of-bst/

Given the root node of a binary search tree, return the sum of values of all
nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

Note:
- The number of nodes in the tree is at most 10000.
- The final answer is guaranteed to be less than 2^31.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionPreorderBT:
    def _preorder(self, root: Optional[TreeNode], low: int, high: int) -> None:
        # Base cases: no node or out of boundary.
        if not root:
            return None

        # Preorder traversal: root->left->right.
        if low <= root.val <= high:
            self.result += root.val
        self._preorder(root.left, low, high)
        self._preorder(root.right, low, high)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Time complexity: O(n).
        Space complexity: O(logn) for balanced BST, O(n) for singly-linked list.
        """
        # Apply recursive preorder traversal.
        self.result = 0
        self._preorder(root, low, high)
        return self.result


class SolutionBFSLevelBT:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Time complexity: O(n).
        Space complexity: O(logn) for balanced BST, O(n) for singly-linked list.
        """
        from collections import deque

        # Apply BFS level-traversal with queue.
        result = 0

        queue = deque([root])

        while queue:
            # Level traversal.
            for _ in range(len(queue)):
                current = queue.pop()

                # Check if node's value is in range.
                if low <= current.val <= high:
                    result += current.val

                # Push left and right nodes to queue.
                if current.left and current.val > low:
                    queue.appendleft(current.left)
                if current.right and current.val < high:
                    queue.appendleft(current.right)

        return result


class SolutionBST:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Time complexity: O(n).
        Space complexity: O(logn) for balanced BST, O(n) for singly-linked list.
        """
        pass


def main():
    import time

    # Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
    # Output: 32
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    low = 7
    high = 15

    start_time = time.time()
    print(SolutionPreorderBT().rangeSumBST(root, low, high))
    print("Preorder:", time.time() - start_time)

    start_time = time.time()
    print(SolutionBFSLevelBT().rangeSumBST(root, low, high))
    print("BFS Level:", time.time() - start_time)

    # Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
    # Output: 23
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(18)
    root.left.left.left = TreeNode(1)
    root.left.right.left = TreeNode(6)
    low = 6 
    high = 10

    start_time = time.time()
    print(SolutionPreorderBT().rangeSumBST(root, low, high))
    print("Preorder:", time.time() - start_time)

    start_time = time.time()
    print(SolutionBFSLevelBT().rangeSumBST(root, low, high))
    print("BFS Level:", time.time() - start_time)


if __name__ == '__main__':
    main()
