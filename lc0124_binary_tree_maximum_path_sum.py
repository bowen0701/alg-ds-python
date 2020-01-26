"""Leetcode 124. Binary Tree Maximum Path Sum
Hard

URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting
node to any node in the tree along the parent-child connections. The path must
contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]
       1
      / \
     2   3
Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]
   -10
   / \
  9  20
    /  \
   15   7
Output: 42
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionLeftRightMaxPathDownSumRecur(object):
    def maxPathDownSum(self, root):
        # Edge case.
        if not root:
            return 0

        # Collect max path sum from root value, down paths from left/right nodes.
        # If one branch sum is less than 0, do not connect that branch by max(0, .).
        left_max_sum = max(0, self.maxPathDownSum(root.left))
        right_max_sum = max(0, self.maxPathDownSum(root.right))

        self.max_sum = max(self.max_sum, root.val + left_max_sum + right_max_sum)

        # Return max path down sum from left or right, including root values.
        return max(left_max_sum, right_max_sum) + root.val

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree, O(n) for singly linked list.
        """
        # Use global max path sum for memorization.
        self.max_sum = -float('inf')

        # Collect max path down sum from left or right and update global max sum.
        self.maxPathDownSum(root)
        return self.max_val


def main():
    # Output: 6
    #   1
    #  / \
    # 2   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print SolutionLeftRightMaxPathDownSumRecur().maxPathSum(root)

    # Output: 42
    #  -10
    #  / \
    # 9  20
    #   /  \
    #  15   7
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print SolutionLeftRightMaxPathDownSumRecur().maxPathSum(root)


if __name__ == '__main__':
    main()
