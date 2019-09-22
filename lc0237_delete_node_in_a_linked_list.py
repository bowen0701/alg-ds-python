"""Leetcode 237. Delete Node in a Linked List
Easy

URL: https://leetcode.com/problems/delete-node-in-a-linked-list/

Write a function to delete a node (except the tail) in a singly linked list,
given only access to that node.

Given linked list -- head = [4,5,1,9].

Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5,
the linked list should become 4 -> 1 -> 9 after calling your function.

Example 2:
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1,
the linked list should become 4 -> 5 -> 9 after calling your function.

Note:
- The linked list will have at least two elements.
- All of the nodes' values will be unique.
- The given node will not be the tail and it will always be a valid node 
  of the linked list.
- Do not return anything from your function.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SolutionTwoPointers(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        previous = None
        current = node

        while current.next:
            # Update current's value.
            current.val = current.next.val

            # Iterate to next node.
            previous = current
            current = current.next

        previous.next = None


class SolutionChangeValNext(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        Time complexity: O(1).
        Space complexity: O(1).
        """
        # Directly change node's val & next by next's (i.e. skip next).
        node.val = node.next.val
        node.next = node.next.next


def main():
    # Input: head = [4,5,1,9], node = 5
    # Output: [4,1,9]
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)
    node = head.next
    # SolutionTwoPointers().deleteNode(node)
    SolutionChangeValNext().deleteNode(node)
    print head.val, head.next.val, head.next.next.val, head.next.next.next

    # Input: head = [4,5,1,9], node = 1
    # Output: [4,5,9]
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)
    node = head.next.next
    # SolutionTwoPointers().deleteNode(node)
    SolutionChangeValNext().deleteNode(node)
    print head.val, head.next.val, head.next.next.val, head.next.next.next


if __name__ == '__main__':
    main()
