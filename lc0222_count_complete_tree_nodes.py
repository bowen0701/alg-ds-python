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
    def _preorder(self, root):
        if not root:
            return None
        
        self.n_nodes += 1
        self._preorder(root.left)
        self._preorder(root.right)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        self.n_nodes = 0
        self._preorder(root)
        return self.n_nodes


class SolutionPreorderIter(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        if not root:
            return 0

        n_nodes = 0

        stack = [root]

        while stack:
            current = stack.pop()
            n_nodes += 1

            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        return n_nodes


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


if __name__ == '__main__':
    main()
