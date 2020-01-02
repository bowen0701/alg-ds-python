"""19. Remove Nth Node From End of List
Medium

URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given a linked list, remove the n-th node from the end of list and return 
its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SolutionTwoPassesGetSize(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode

        Time complexity: O(m), where m is the length of list.
        Space complexity: O(1).
        """
        # If no node will be removed.
        if n == 0:
            return head

        # Get the size of the linked list.
        size = 0
        current = head
        while current:
            size += 1
            current = current.next

        # If the head is removed.
        if n == size:
            return head.next

        # Arrive at the (N-1)th node.
        pos = -1
        previous = None
        current = head
        while pos < size - n - 1:
            pos += 1
            previous = current
            current = current.next

        # If the Nth node exists, replace the Nth node by the (N+1)th,
        # and return head.
        if current:
            previous.next = previous.next.next

        return head


class SolutionOnePass(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode

        Time complexity: O(m), where m is the length of list.
        Space complexity: O(1).
        """
        # If no node will be removed.
        if n == 0:
            return head

        # Apply Two Pointers: fast and slow.
        fast = head
        slow = head
        previous = ListNode(None)

        # Move fast n nodes into the list.
        for i in range(n):
            fast = fast.next

        # Move all nodes at the same pace, and stop at the left of nth node.
        while fast.next:
            fast = fast.next
            previous = slow
            slow = slow.next

        # Remove nth node.
        previous.next = previous.next.next

        return head


def main():
    # Solution = SolutionTwoPassesGetSize
    Solution = SolutionOnePass

    # Given linked list: 1->2->3->4->5, and n = 2
    # Remove the 2nd node from the end: 1->2->3->5.
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution().removeNthFromEnd(head, 2).next.next.next.val


if __name__ == '__main__':
    main()
