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


class SolutionValMinDiffBST(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        # Traverse through BST to update currrent value & min_diff
        val = 0
        min_diff = float('inf')

        current = root
        while current:
            if abs(current.val - target) < min_diff:
                val = current.val
                min_diff = abs(current.val - target)

            if target < current.val:
                current = current.left
            else:
                current = current.right

        return val


def main():
    # target: 3.714286
    # BST:
    #     4
    #    / \
    #   2   5
    #  / \
    # 1   3
    # Output: 4
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)    
    target = 3.714286
    print SolutionValMinDiffBST().closestValue(root, target)


if __name__ == '__main__':
    main()
