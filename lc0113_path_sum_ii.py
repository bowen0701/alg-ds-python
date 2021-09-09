"""Leetcode 113. Path Sum II
Medium

URL: https://leetcode.com/problems/path-sum-ii/

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum
equals the given sum.

Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionPreorderBacktrackingRecur:
    def _preorder_backtrack(
        self, 
        root: Optional[TreeNode], 
        targetSum: int, 
        result: List[List[int]], 
        temp: List[int]
    ) -> None:
        # Base case.
        if not root:
            return None

        temp.append(root.val)

        # Preorder traversal: root->left->right, with temp's shallow copy.
        if root.val == targetSum and not root.left and not root.right:
            result.append(temp[:])
            return None

        self._preorder_backtrack(root.left, targetSum - root.val, result, temp[:])
        self._preorder_backtrack(root.right, targetSum - root.val, result, temp[:])

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        # Apply recursive preorder traversal with backtracking.
        result = []
        temp = []
        self._preorder_backtrack(root, targetSum, result, temp)
        return result


class SolutionPreorderBacktrackingIter:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        # Edge case.
        if not root:
            return []

        # Apply iterative preorder traversal with stack and backtracking.
        result = []
        temp = []

        stack = [(root, targetSum, temp)]

        while stack:
            cur, cur_sum, temp = stack.pop()

            temp.append(cur.val)

            # Preorder traversal: root->left->right, with temp's shallow copy.
            if cur.val == cur_sum and not cur.left and not cur.right:
                result.append(temp[:])

            # Append right->left because stack is LIFO.
            if cur.right:
                stack.append((cur.right, cur_sum - cur.val, temp[:]))
            if cur.left:
                stack.append((cur.left, cur_sum - cur.val, temp[:]))

        return result


def main():
    # Binary tree:
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  /  \    / \
    # 7    2  5   1
    # sum = 22
    # Outpur:
    # [
    #    [5,4,11,2],
    #    [5,8,4,5]
    # ]
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    targetSum = 22
    print(SolutionPreorderBacktrackingRecur().pathSum(root, targetSum))
    print(SolutionPreorderBacktrackingIter().pathSum(root, targetSum))


if __name__ == '__main__':
    main()
