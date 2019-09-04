"""Leetcode 104. Maximum Depth of Binary Tree
Easy

URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the 
root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionBFS(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        if not root:
            return 0

        depth = 0

        # Use queue for BFS.
        queue = [root]

        while queue:
            # Increment depth for each level.
            depth += 1

            # Vist all nodes in the same level.
            for i in range(len(queue)):
                current = queue.pop()
                if current.left:
                    queue.insert(0, current.left)
                if current.right:
                    queue.insert(0, current.right)

        return depth


class SolutionDFS(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
         


def main():
    # Binary tree: [3,9,20,null,null,15,7], ans: 3.
    #     3
    #    / \
    #   9  20
    #  /  /  \
    # 6  15   7
    #      \
    #      10
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(6)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.left.left = TreeNode(15)
    
    print SolutionBFS().maxDepth(root)
    print SolutionDFS().maxDepth(root)


if __name__ == '__main__':
    main()
