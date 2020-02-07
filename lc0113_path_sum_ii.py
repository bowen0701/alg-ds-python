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


class SolutionPreorderBacktrackingRecur(object):
    def _findPathsPreorder(self, root, sum, result, temp):
        # Base case.
        if not root:
            return None

        temp.append(root.val)

        # Visit root and append sum with temp's shallow copy.
        if root.val == sum and not root.left and not root.right:
            result.append(temp[:])
            return None

        # Visit root's left & right if existed, with temp's shallow copy.
        self._findPathsPreorder(root.left, sum - root.val, result, temp[:])
        self._findPathsPreorder(root.right, sum - root.val, result, temp[:])

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        # Apply recursive preorder traversal.
        result = []
        temp = []
        self._findPathsPreorder(root, sum, result, temp)
        return result


class SolutionPreorderBacktrackingIter(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        if not root:
            return []

        # Apply iterative backtracking with result and temp.
        result = []
        temp = []

        # Apply iterative preorder traversal with stack.
        stack = [(root, sum, temp)]

        while stack:
            cur, cur_sum, temp = stack.pop()

            temp.append(cur.val)

            # Visit root to check if root-to-leaf path sum is sum by shallow copy.
            if cur.val == cur_sum and not cur.left and not cur.right:
                result.append(temp[:])

            # Visit root's left & right if existed by shallow copy.
            if cur.right:
                stack.append((cur.right, cur_sum - cur.val, temp[:]))
            if cur.left:
                stack.append((cur.left, cur_sum - cur.val, temp[:]))

        return result


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
    print SolutionPreorderBacktrackingRecur().pathSum(root, sum)
    print SolutionPreorderBacktrackingIter().pathSum(root, sum)


if __name__ == '__main__':
    main()
