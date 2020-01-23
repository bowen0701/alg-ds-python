"""Leetcode 958. Check Completeness of a Binary Tree
Medium

URL: https://leetcode.com/problems/check-completeness-of-a-binary-tree/

Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely
filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:
Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:
Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 
Note:
The tree will have between 1 and 100 nodes.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionLevelorderOneByOneIter(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(logn) for complete tree, O(n) for singly linked list.
        """
        from collections import deque

        # Apply level-order traversal with queue to collect all nodes one by ones.
        queue = deque([root])

        # Stop collection until met empty node.
        while queue and queue[-1]:
            print queue
            current = queue.pop()
            if not current:
                break

            queue.appendleft(current.left)
            queue.appendleft(current.right)            

        # Pop empty nodes until met node, then check if queue is empty or not.
        while queue and not queue[-1]:
            queue.pop()

        return not queue


def main():
    # Input: [1,2,3,4,5,6]
    # Output: true
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    print SolutionLevelorderOneByOneIter().isCompleteTree(root)

    # Input: [1,2,3,4,5,null,7]
    # Output: false
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(7)
    print SolutionLevelorderOneByOneIter().isCompleteTree(root)


if __name__ == '__main__':
    main()
