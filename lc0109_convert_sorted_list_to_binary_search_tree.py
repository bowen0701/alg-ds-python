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


class SolutionSlowFast(object):
    def runSlowFast(self, left, right):
        if not left or left == right:
            return None

        # Run to middle node.
        fast, slow = left, left
        while fast.next != right and fast.next.next != right:
            fast = fast.next.next
            slow = slow.next

        root = TreeNode(slow.val)
        root.left = self.runSlowFast(left, slow)
        root.right = self.runSlowFast(slow.next, right)

        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode

        Time complexity: O(nlogn).
        Space complexity: O(logn).
        """
        if not head:
            return None

        left, right = head, None
        return self.runSlowFast(left, right)


class SolutionInorder(object):
    def _inorder(self, left, right):
        if left > right:
            return None

        mid = left + (right - left) // 2

        root_left = self._inorder(left, mid - 1)

        root = TreeNode(self.node.val)
        root.left = root_left
        self.node = self.node.next

        root.right = self._inorder(mid + 1, right)

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

        # Get the size of linked list.
        current = head
        size = 0
        while current:
            size += 1
            current = current.next

        # Attach head to self for memorizing its update.
        self.node = head

        return self._inorder(0, size - 1)


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

    root = SolutionSlowFast().sortedListToBST(head)
    print (root.val,
           root.left.val, root.right.val,
           root.left.right.val, root.right.right.val)

    root = SolutionInorder().sortedListToBST(head)
    print (root.val,
           root.left.val, root.right.val,
           root.left.right.val, root.right.right.val)


if __name__ == '__main__':
    main()
