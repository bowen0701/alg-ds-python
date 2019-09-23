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

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionConvert2Array(object):
    def _convert(self, arr, left, right):
        if left > right:
            return None

        mid = left + (right - left) // 2

        root = TreeNode(arr[mid])
        root.left = self._convert(arr, left, mid - 1)
        root.right = self._convert(arr, mid + 1, right)

        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode

        Time complexity: O(n).
        Space complexity: O(logn).
        """
        if not head:
            return None

        # Convert linked list to arry first.
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next

        # Apply recur with two pointer method.
        left, right = 0, len(arr) - 1
        return self._convert(arr, left, right)


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

    root = SolutionConvert2Array().sortedListToBST(head)
    print (root.val,
           root.left.val, root.right.val,
           root.left.right.val, root.right.right.val)


if __name__ == '__main__':
    main()
