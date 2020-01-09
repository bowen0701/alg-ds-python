"""Leetcode 103. Binary Tree Zigzag Level Order Traversal
Medium

URL: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        Time complexity: O(n), where n is the number of nodes.
        Space complexity: O(m), where m is the biggest number of nodes in levels.
        """
        from collections import deque

        if not root:
            return []

        # Apply queue for BFS travesal in levels.
        queue = deque([root])
        result = []
        level_id = 0

        while queue:
            level = deque([])

            for i in range(len(queue)):
                # Get the oldest node from queue.
                current = queue.pop()

                # Insert its left and right nodes to queue.
                if current.left:
                    queue.appendleft(current.left)
                if current.right:
                    queue.appendleft(current.right)
            
                if level_id % 2 == 0:
                    # If even level, append current value to level's tail.
                    level.append(current.val)
                else:
                    # If odd, insert current value to level's head.
                    level.appendleft(current.val)

            level_id += 1
            result.append(list(level))

        return result


def main():
    # Given binary tree:
    #      3
    #    /    \
    #   9     20
    #  / \   /  \
    # 6   8 15   7
    # Ans: [[3], [20, 9], [6, 8, 15, 7]]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print Solution().zigzagLevelOrder(root)


if __name__ == '__main__':
    main()
