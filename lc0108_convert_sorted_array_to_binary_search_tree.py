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

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionRecurCopy(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode

        Time complexity: O(n*logn), where n is the length of nums.
        Space complexity: O(n).
        """
        if not nums:
            return None

        left, right = 0, len(nums) - 1
        mid = left + (right - left) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
       
        return root


class SolutionRecurTwoPointers(object):
    def _convert(self, nums, left, right):
        if left > right:
            return None

        mid = left + (right - left) // 2

        root = TreeNode(nums[mid])
        root.left = self._convert(nums, left, mid - 1)
        root.right = self._convert(nums, mid + 1, right)

        return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode

        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(logn).
        """
        if not nums:
            return None

        left, right = 0, len(nums) - 1
        return self._convert(nums, left, right)


class SolutionInorderRecur(object):
    def _inorder(self, nums, left, right):
        if left > right:
            return None

        mid = left + (right - left) // 2

        left = self._inorder(nums, left, mid - 1)
        root = TreeNode(nums[mid])
        root.left = left
        root.right = self._inorder(nums, mid + 1, right)

        return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode

        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(logn).
        """
        if not nums:
            return None

        left, right = 0, len(nums) - 1
        return self._inorder(nums, left, right)


def main():
    nums = [-10, -3, 0, 5, 9]

    root = SolutionRecurCopy().sortedArrayToBST(nums)
    print (root.val,
           root.left.val, root.right.val,
           root.left.right.val, root.right.right.val)

    root = SolutionRecurTwoPointers().sortedArrayToBST(nums)
    print (root.val,
           root.left.val, root.right.val,
           root.left.right.val, root.right.right.val)

    root = SolutionInorderRecur().sortedArrayToBST(nums)
    print (root.val,
           root.left.val, root.right.val,
           root.left.right.val, root.right.right.val)


if __name__ == '__main__':
    main()
