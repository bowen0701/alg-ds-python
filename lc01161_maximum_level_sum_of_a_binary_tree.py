"""Leetcode 1161. Maximum Level Sum of a Binary Tree
Medium

URL: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

Given the root of a binary tree, the level of its root is 1, 
the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes
at level X is maximal.

Example 1:
Input: [1,7,0,7,-8,null,null]
     1
    / \
   7   0
  / \
 7  -8
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
 
Note:
- The number of nodes in the given tree is between 1 and 10^4.
- -10^5 <= node.val <= 10^5
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        pass


def main():
    pass


if __name__ == '__main__':
    main()
