"""Leetcode 112. Path Sum
Easy

URL: https://leetcode.com/problems/path-sum/

Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionPreorderRecur(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        # Apply recursive preorder traversal.
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        return (self.hasPathSum(root.left, sum - root.val) or
                self.hasPathSum(root.right, sum - root.val))


class SolutionPreorderIter(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        # Apply iterative preorder traversal with queue.
        if not root:
            return False

        # Apply DFS with stack.
        stack = [(root, sum)]

        while stack:
            cur, _sum = stack.pop()

            if not cur.left and not cur.right and cur.val == _sum:
                return True

            if cur.right:
                stack.append((cur.right, _sum - cur.val))

            if cur.left:
                stack.append((cur.left, _sum - cur.val))

        return False


def main():
    # Given the below binary tree and sum = 22,
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  /  \      \
    # 7    2      1
    # return true, 
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)
    sum = 22
    print SolutionPreorderRecur().hasPathSum(root, sum)
    print SolutionPreorderIter().hasPathSum(root, sum)


if __name__ == '__main__':
    main()
