"""Leetcode 101. Symmetric Tree
Easy

URL: https://leetcode.com/problems/symmetric-tree/

Given a binary tree, check whether it is a mirror of itself 
(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionRecur(object):
    def isMirror(self, left, right):
        # Check left & right nodes's symmetry.
        if not left and not right:
            return True

        if not left or not right:
            return False

        # Check left & right nodes's values.
        if left.val != right.val:
            return False

        # Check outside & inside pairs.
        out_pair = self.isMirror(left.left, right.right)
        in_pair = self.isMirror(left.right, right.left)
        return out_pair and in_pair

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        if not root:
            return True

        return self.isMirror(root.left, root.right)


class SolutionIter(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        if not root:
            return True

        queue = [(root.left, root.right)]

        while queue:
            left, right = queue.pop()

            # Check left & right nodes's symmetry.
            if not left and not right:
                continue

            if not left or not right:
                return False

            # Check left & right nodes's values.
            if left.val != right.val:
                return False

            # Check outside & inside pairs.
            queue.insert(0, (left.left, right.right))
            queue.insert(0, (left.right, right.left))

        return True


def main():
    # Output: True.
    #     1
    #    / \
    #   2   2
    #  / \ / \
    # 3  4 4  3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    print SolutionRecur().isSymmetric(root)
    print SolutionIter().isSymmetric(root)

    # Output: False.
    #     1
    #    / \
    #   2   2
    #    \   \
    #     3   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)
    
    print SolutionRecur().isSymmetric(root)
    print SolutionIter().isSymmetric(root)


if __name__ == '__main__':
    main()
