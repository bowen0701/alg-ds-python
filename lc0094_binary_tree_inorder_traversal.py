"""Leetcode 94. Binary Tree Inorder Traversal
Medium

URL: https://leetcode.com/problems/binary-tree-inorder-traversal/

Given a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionRecur(object):
    def _inorderUtil(self, root, nodes):
        if not root:
            return None

        self._inorderUtil(root.left, nodes)
        nodes.append(root.val)
        self._inorderUtil(root.right, nodes)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        nodes = []
        self._inorderUtil(root, nodes)
        return nodes


class SolutionIter(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        nodes = []

        previous = None
        current = root

        # Use stack for inorder traversal.
        stack = []

        while current or stack:
            while current:
                # If current exists, push to stack and visit leftmost node.
                stack.append(current)
                current = current.left

            # Pop stack as current and print its value.
            current = stack.pop()
            nodes.append(current.val)

            # Update previous & current by current & right.
            current = current.right
            previous = current

        return nodes


def main():
    # Input: [1,null,2,3]
    # 1
    #  \
    #   2
    #  /
    # 3
    # Output: [1,3,2]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print 'By recur: {}'.format(SolutionRecur().inorderTraversal(root))
    print 'By iter: {}'.format(SolutionIter().inorderTraversal(root))
    

if __name__ == '__main__':
    main()
