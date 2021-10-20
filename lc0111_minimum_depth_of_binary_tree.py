"""Leetcode 111. Minimum Depth of Binary Tree
Easy

URL: https://leetcode.com/problems/minimum-depth-of-binary-tree/

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the
root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class SolutionDFSRecur(object):
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Edge case.
        if not root:
            return 0

        # Edge case: no child node.
        if not root.left and not root.right:
            return 1 

        # If no left node, start from root to check min depth of right node.
        if not root.left:
            return 1 + self.minDepth(root.right)

        # If no right node, start from root to check min depth of left node.
        if not root.right:
            return 1 + self.minDepth(root.left)

        # If both left & right nodes exist, start from root to check min depth of both.
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


class SolutionLevelBFS(object):
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Time complexity: O(n).
        Space complexity: O(n).
        """
        from collections import deque

        # Edge case.
        if not root:
            return 0

        # Apply level-traversal BFS with queue.
        queue = deque([root])
        depth = 0

        while queue:
            depth += 1

            for i in range(len(queue)):
                current = queue.pop()

                if current.left:
                    queue.appendleft(current.left)
                if current.right:
                    queue.appendleft(current.right)

                # When no child nodes, arrived at shortest leaf.
                if not current.left and not current.right:
                    return depth


def main():
    # Tree: [1, 2]
    # Output: 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(SolutionDFSRecur().minDepth(root))
    print(SolutionLevelBFS().minDepth(root))

    # Tree: [3,9,20,null,null,15,7],
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    # Output: 2.
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(SolutionDFSRecur().minDepth(root))
    print(SolutionLevelBFS().minDepth(root))


if __name__ == '__main__':
    main()
