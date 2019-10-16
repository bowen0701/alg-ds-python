"""Leetcode 113. Path Sum II
Medium

URL: https://leetcode.com/problems/path-sum-ii/

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum
equals the given sum.

Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionPreorderRecur(object):
    def _find_paths(self, root, sum, cur_path, paths):
        # Base case.
        if not root:
            return None

        # Recursive call for preorder traversal.
        cur_path.append(root.val)

        # Traverse root.
        if root.val == sum and not root.left and not root.right:
            paths.append(cur_path)
            return None

        # Traverse root's left & right with "copied" current path.
        self._find_paths(root.left, sum - root.val, cur_path[:], paths)
        self._find_paths(root.right, sum - root.val, cur_path[:], paths)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        # Apply recursive preorder traversal.
        paths = []

        cur_path = []
        self._find_paths(root, sum, cur_path, paths)

        return paths


def main():
    # Binary tree:
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  /  \    / \
    # 7    2  5   1
    # sum = 22
    # Outpur:
    # [
    #    [5,4,11,2],
    #    [5,8,4,5]
    # ]
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    sum = 22
    print SolutionPreorderRecur().pathSum(root, sum)


if __name__ == '__main__':
    main()
