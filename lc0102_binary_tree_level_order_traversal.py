"""Leetcode 102. Binary Tree Level Order Traversal
Medium

URL: https://leetcode.com/problems/binary-tree-level-order-traversal/

Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionBFS(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        Time complexity: O(n), where n is the number of nodes.
        Space complexity: O(2^logn)=O(n), as the number of nodes in the bottom.
        """
        from collections import deque

        if not root:
            return []

        # Use queue for BFS.
        queue = deque([root])
        result = []

        while queue:
            level = []
            
            # Iterate through all nodes in this level.
            for i in range(len(queue)):
                # Pop queue's last node and append it to level.
                current = queue.pop()
                level.append(current.val)

                # Insert left/right nodes in next level into queue.
                if current.left:
                    queue.appendleft(current.left)
                if current.right:
                    queue.appendleft(current.right)
            
            # Append level nodes to result.
            result.append(level)

        return result


def main():
    # Given binary tree:
    #     3
    #    / \
    #   9   20
    #  /   /  \
    # 6   15   7
    # Ans: [[3], [9,20], [6, 15,7]]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(6)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print SolutionBFS().levelOrder(root)


if __name__ == '__main__':
    main()
