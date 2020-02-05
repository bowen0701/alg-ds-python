"""Leetcode 222. Count Complete Tree Nodes
Medium

URL: https://leetcode.com/problems/count-complete-tree-nodes/

Given a complete binary tree, count the number of nodes.

Note:
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far left as
possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:
Input: 
    1
   / \
  2   3
 / \  /
4  5 6
Output: 6
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionPreorderRecur(object):
    def _preorderRecur(self, root):
        if not root:
            return None
        
        self.n_nodes += 1
        self._preorderRecur(root.left)
        self._preorderRecur(root.right)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        # Apply recursive preorder traversal.
        self.n_nodes = 0
        self._preorderRecur(root)
        return self.n_nodes


class SolutionPreorderIter(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        if not root:
            return 0

        n_nodes = 0

        stack = [root]

        while stack:
            current = stack.pop()
            n_nodes += 1

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return n_nodes


class SolutionLevelorderIter(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        from collections import deque

        queue = deque([root])
        n_nodes = 0

        while queue:
            for i in range(len(queue)):
                current = queue.pop()
                n_nodes += 1

                if current.left:
                    queue.appendleft(current.left)
                if current.right:
                    queue.appendleft(current.right)

        return n_nodes


class SolutionLeftRightDepths(object):
    def _countLeftDepth(self, root):
        if not root:
            return 0
        return 1 + self._countLeftDepth(root.left)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time complexity: O((logn)^2) for balanced tree; O(n^2) for single sided.
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        if not root:
            return 0

        # Compare left & right subtrees's depths.
        left_depth = self._countLeftDepth(root.left)
        right_depth = self._countLeftDepth(root.right)

        if left_depth == right_depth:
            # If left & right depths are equal, left subtree is full.
            return pow(2, left_depth) + self.countNodes(root.right)
        else:
            # If not, right subtree is full, and left depth is bigger.
            return self.countNodes(root.left) + pow(2, right_depth)


def main():
    # Input: 
    #     1
    #    / \
    #   2   3
    #  / \  /
    # 4  5 6
    # Output: 6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    print SolutionPreorderRecur().countNodes(root)
    print SolutionPreorderIter().countNodes(root)
    print SolutionLevelorderIter().countNodes(root)
    print SolutionLeftRightDepths().countNodes(root)


if __name__ == '__main__':
    main()
