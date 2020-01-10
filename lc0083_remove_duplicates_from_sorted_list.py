"""Leetcode 83. Remove Duplicates from Sorted List
Easy

URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given a sorted linked list, delete all duplicates such that each element appear
only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SolutionCurrentNextIter(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Time complexity: O(n), where n is the list length.
        Space complexity: O(1).
        """
        if not head:
            return None

        current = head

        while current and current.next:
            if current.val == current.next.val:
                # Continue updating next until it's not a duplicate, 
                # then link current to non-duplicate.
                cur_next = current.next
                while cur_next.next and cur_next.val == cur_next.next.val:
                    cur_next = cur_next.next
                current.next = cur_next.next

            # Increment current node.
            current = current.next

        return head


def main():
    # Input: 1->1->2
    # Output: 1->2
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    SolutionCurrentNextIter().deleteDuplicates(head)
    print(head.val, head.next.val, head.next.next)

    # Input: 1->1->2->3->3
    # Output: 1->2->3
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    SolutionCurrentNextIter().deleteDuplicates(head)
    print(head.val, head.next.val, head.next.next.val, head.next.next.next)


if __name__ == '__main__':
    main()
