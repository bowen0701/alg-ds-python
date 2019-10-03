"""Leetcode 144. Binary Tree Preorder Traversal
Medium

URL: https://leetcode.com/problems/binary-tree-preorder-traversal/

Given a binary tree, return the preorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,2,3]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionRecur(object):
    def _preorderRecur(self, root, vals):
        if not root:
            return None

        current = root
        vals.append(current.val)
        self._preorderRecur(current.left, vals)
        self._preorderRecur(current.right, vals)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        # Apply recursive preorder traversal.
        vals = []
        self._preorderRecur(root, vals)
        return vals


def main():
    # Input: [1,null,2,3]
    #    1
    #     \
    #      2
    #     /
    #    3
    # Output: [1,2,3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print SolutionRecur().preorderTraversal(root)


if __name__ == '__main__':
    main()
