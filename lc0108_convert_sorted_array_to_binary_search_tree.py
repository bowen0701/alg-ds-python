"""Leetcode 108. Convert Sorted Array to Binary Search Tree
Easy

URL: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree
in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following
height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
"""

from typing import List


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionPreorderRecur(object):
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        Time complexity: O(n).
        Space complexity: O(n).
        """
        if not nums:
            return None

        # Apply recursive preorder traversal: root->left->right.
        left, right = 0, len(nums) - 1
        mid = left + (right - left) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
       
        return root


class SolutionPreorderRecurTwoPointers(object):
    def _preorderRecur(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None

        # Apply recursive preorder traversal: root->left->right.
        mid = left + (right - left) // 2

        root = TreeNode(nums[mid])
        root.left = self._preorderRecur(nums, left, mid - 1)
        root.right = self._preorderRecur(nums, mid + 1, right)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        Time complexity: O(n).
        Space complexity: O(logn).
        """
        # Apply recursive preorder traversal with two pointers.
        if not nums:
            return None

        left, right = 0, len(nums) - 1
        return self._preorderRecur(nums, left, right)


class SolutionInorderRecurTwoPointers(object):
    def _inorderRecur(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None

        mid = left + (right - left) // 2

        # Apply recursive inorder traversal: left->root->right.
        left = self._inorderRecur(nums, left, mid - 1)
        root = TreeNode(nums[mid])
        root.left = left
        root.right = self._inorderRecur(nums, mid + 1, right)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        Time complexity: O(n).
        Space complexity: O(logn).
        """
        # Apply recursive inorder traversal w/ two pointers.
        if not nums:
            return None

        left, right = 0, len(nums) - 1
        return self._inorderRecur(nums, left, right)


def main():
    nums = [-10, -3, 0, 5, 9]

    root = SolutionPreorderRecur().sortedArrayToBST(nums)
    print(root.val,
          root.left.val, root.right.val,
          None, root.left.right.val, None, root.right.right.val)

    root = SolutionPreorderRecurTwoPointers().sortedArrayToBST(nums)
    print(root.val,
          root.left.val, root.right.val,
          None, root.left.right.val, None, root.right.right.val)

    root = SolutionInorderRecurTwoPointers().sortedArrayToBST(nums)
    print(root.val,
          root.left.val, root.right.val,
          None, root.left.right.val, None, root.right.right.val)


if __name__ == '__main__':
    main()
