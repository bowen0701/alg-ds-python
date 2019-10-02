"""Leetcode 437. Path Sum III
Easy (?)

URL: https://leetcode.com/problems/path-sum-iii/

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf,
but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range
-1,000,000 to 1,000,000.

Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1
Return 3. The paths that sum to 8 are:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionRecur(object):
    def _countPathSum(self, root, sum):
        if not root:
            return 0

        # Single root val is sum.
        if root.val == sum:
            root_path_sum = 1
        else:
            root_path_sum = 0

        # With root val, count path sum leading by left/right node. 
        root_left_path_sum = self._countPathSum(root.left, sum - root.val)
        root_right_path_sum = self._countPathSum(root.right, sum - root.val)

        return root_path_sum + root_left_path_sum + root_right_path_sum


    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int

        Time complexity: O(n*logn), if balanced tree; O(n^2) if single sided.
        Space complexity: O(logn).
        """
        if not root:
            return 0

        # Count path sum leading by root.
        lead_path_sum = self._countPathSum(root, sum)

        # Recursively get path sum starting from left/right node.
        left_path_sum = self.pathSum(root.left, sum)
        right_path_sum = self.pathSum(root.right, sum)
        
        return lead_path_sum + left_path_sum + right_path_sum


def main():
    #       10
    #      /  \
    #     5   -3
    #    / \    \
    #   3   2   11
    #  / \   \
    # 3  -2   1
    # Output: 3
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)
    sum = 8

    print SolutionRecur().pathSum(root, sum)


if __name__ == '__main__':
    main()
