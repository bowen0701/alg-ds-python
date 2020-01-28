"""Leetcode 145. Binary Tree Postorder Traversal
Hard

URL: https://leetcode.com/problems/binary-tree-postorder-traversal/

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionRecur(object):
    def _postorderRecur(self, root, vals):
        if not root:
            return None

        self._postorderRecur(root.left, vals)
        self._postorderRecur(root.right, vals)
        vals.append(root.val)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        vals = []
        self._postorderRecur(root, vals)
        return vals


class SolutionIter(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        if not root:
            return []

        # Collect revsersed values.
        rev_vals = []
        stack = [root]

        while stack:
            current = stack.pop()
            rev_vals.append(current.val)

            # Push left before right since we use stack with FILO.
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        return rev_vals[::-1]


def main():
    # Input: [1,null,2,3]
    #    1
    #     \
    #      2
    #     /
    #    3
    # Output: [3,2,1]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print SolutionRecur().postorderTraversal(root)
    print SolutionIter().postorderTraversal(root)


if __name__ == '__main__':
    main()
