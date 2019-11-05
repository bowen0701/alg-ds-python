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


class Solution(object):
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
                next_ = current.next
                while next_.next and next_.val == next_.next.val:
                    next_ = next_.next
                current.next = next_.next

            # Increment current node.
            current = current.next

        return head


def main():
    # Input: 1->1->2
    # Output: 1->2
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    Solution().deleteDuplicates(head)
    print (head.val, head.next.val, head.next.next)

    # Input: 1->1->2->3->3
    # Output: 1->2->3
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    Solution().deleteDuplicates(head)
    print (head.val, head.next.val, head.next.next.val, head.next.next.next)


if __name__ == '__main__':
    main()
