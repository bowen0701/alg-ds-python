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

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionRecur(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Edge case.
        if not root:
            return 0

        # If min depth > 0: 1 + min depth; otherwise: 1 + max depth.
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        min_depth = min(left_depth, right_depth)
        if min_depth > 0:
            return 1 + min_depth
        else:
            return 1 + max(left_depth, right_depth)


class SolutionLevelBFS(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        from collections import deque

        # Apply level-traversal BFS with queue.
        if not root:
            return 0

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

                # When no child nodes, arrived at leaf.
                if not current.left and not current.right:
                    return depth


def main():
    # Tree: [1, 2]
    # Output: 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    print SolutionRecur().minDepth(root)
    print SolutionLevelBFS().minDepth(root)

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
    print SolutionRecur().minDepth(root)
    print SolutionLevelBFS().minDepth(root)


if __name__ == '__main__':
    main()
