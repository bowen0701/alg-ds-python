"""Leetcode 938. Range Sum of BST
Easy

URL: https://leetcode.com/problems/range-sum-of-bst/

Given the root node of a binary search tree, return the sum of values of all
nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

Note:
- The number of nodes in the tree is at most 10000.
- The final answer is guaranteed to be less than 2^31.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionBFS(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(logn) for balanced BST, O(n) for singly-linked list.
        """
        from collections import deque

        # Apply BFS level-traversal to accumulate sum.
        range_sum = 0

        queue = deque([root])

        while queue:
            # Level traversal.
            for i in range(len(queue)):
                current = queue.pop()

                # Check if node's value is in range.
                if L <= current.val <= R:
                    range_sum += current.val

                # Push left and right nodes to queue.
                if current.left and current.val > L:
                    queue.appendleft(current.left)
                if current.right and current.val < R:
                    queue.appendleft(current.right)

        return range_sum


def main():
    # Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
    # Output: 32
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    L = 7
    R = 15

    print SolutionBFS().rangeSumBST(root, L, R)

    # Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
    # Output: 23
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(18)
    root.left.left.left = TreeNode(1)
    root.left.right.left = TreeNode(6)
    L = 6 
    R = 10

    print SolutionBFS().rangeSumBST(root, L, R)


if __name__ == '__main__':
    main()
