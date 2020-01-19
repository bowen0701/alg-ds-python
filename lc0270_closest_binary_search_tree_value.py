"""Leetcode 270. Closest Binary Search Tree Value
Easy

URL: https://leetcode.com/problems/closest-binary-search-tree-value/

Given a non-empty binary search tree and a target value, find the value in the
BST that is closest to the target.

Note:
- Given target value is a floating point.
- You are guaranteed to have only one unique value in the BST that is closest to
  the target.

Example:
Input: root = [4,2,5,1,3], target = 3.714286
    4
   / \
  2   5
 / \
1   3
Output: 4
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        pass


if __name__ == '__main__':
    main()
