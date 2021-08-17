"""Leetcode 109. Convert Sorted List to Binary Search Tree
Medium

URL: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree
in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted linked list: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5],
which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


class SolutionConvert2ArrayTwoPointers(object):
    def _preorder(self, vals: List[int], left: int, right: int) -> Optional[TreeNode]:
        # Base case.
        if left > right:
            return None

        # Preorder traversal: root->left->right.
        mid = left + (right - left) // 2

        root = TreeNode(vals[mid])
        root.left = self._preorder(vals, left, mid - 1)
        root.right = self._preorder(vals, mid + 1, right)

        return root

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        Time complexity: O(n).
        Space complexity: O(logn).
        """
        if not head:
            return None

        # Convert linked list to arry first.
        vals = []
        current = head
        while current:
            vals.append(current.val)
            current = current.next

        # Apply recursive preorder traversal with two pointer method.
        left, right = 0, len(vals) - 1
        return self._preorder(vals, left, right)


class SolutionPreorderSlowFastRecur(object):
    def _preorderSlowFast(
        self, 
        left: Optional[TreeNode], 
        right: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        # Base case.
        if not left or left == right:
            return None

        # Run to middle node.
        fast, slow = left, left
        while fast.next != right and fast.next.next != right:
            slow = slow.next
            fast = fast.next.next

        # Preorder traversal: root->left->right.
        root = TreeNode(slow.val)
        root.left = self._preorderSlowFast(left, slow)
        root.right = self._preorderSlowFast(slow.next, right)

        return root

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        Time complexity: O(nlogn), as for each node, traverse half nodes.
        Space complexity: O(logn).
        """
        # Apply recursive preorder traversal by slow/fast two pointers.
        # Edge case.
        if not head:
            return None

        left, right = head, None
        return self._preorderSlowFast(left, right)


class SolutionInorderRecur(object):
    def _inorder(self, left: int, right: int) -> Optional[TreeNode]:
        # Base case.
        if left > right:
            return None

        # Inorder traversal: left->root->right.
        mid = left + (right - left) // 2

        root_left = self._inorder(left, mid - 1)
        root = TreeNode(self.current.val)
        root.left = root_left
        self.current = self.current.next
        root.right = self._inorder(mid + 1, right)

        return root

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        Time complexity: O(n).
        Space complexity: O(logn).
        """
        # Apply recursive inorder traversal.
        # Edge case.
        if not head:
            return None

        # Get the size of linked list.
        current = head
        size = 0
        while current:
            size += 1
            current = current.next

        # Attach head to self for memorizing its current node.
        self.current = head

        left, right = 0, size - 1
        return self._inorder(left, right)


def main():
    # Input: [-10,-3,0,5,9].
    # Output:
    #   0
    #  / \
    # -3   9
    # /   /
    # -10  5
    head = ListNode(-10)
    head.next = ListNode(-3)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(9)

    root = SolutionConvert2ArrayTwoPointers().sortedListToBST(head)
    print(root.val,
          root.left.val, root.right.val,
          root.left.right.val, root.right.right.val)

    root = SolutionPreorderSlowFastRecur().sortedListToBST(head)
    print(root.val,
          root.left.val, root.right.val,
          root.left.right.val, root.right.right.val)

    root = SolutionInorderRecur().sortedListToBST(head)
    print(root.val,
          root.left.val, root.right.val,
          root.left.right.val, root.right.right.val)


if __name__ == '__main__':
    main()
