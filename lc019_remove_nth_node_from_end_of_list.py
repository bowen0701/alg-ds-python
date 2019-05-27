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


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val)
            return None

        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(val)
        return None

    def show(self):
        ls = []
        current = self.head
        while current:
            ls.append(current.val)
            current = current.next
        print(ls)


class SolutionTwoPasses(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Get the size of the linked list.
        size = 0
        current = head
        while current:
            size += 1
            current = current.next

        # Arrive at the (N-1)th node.
        pos = -1
        previous = None
        current = head
        while pos < size - n - 1:
            pos += 1
            previous = current
            current = current.next

        # If the Nth node is head, return head.next.
        if current == head:
            return head.next

        # If the Nth node exists, replace the Nth node by the (N+1)th,
        # and return head.
        if current:
            previous.next = previous.next.next
        return head


def main():
    # Given linked list: 1->2->3->4->5, and n = 2.
    # After removing the 2nd node from the end: 1->2->3->5.
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.show()

    print SolutionTwoPasses().removeNthFromEnd(ll.head, 2).next.next.next.val

    # After removing the 5th node from the end: 2->3->4->5.
    print SolutionTwoPasses().removeNthFromEnd(ll.head, 5).val

    # After removing the 0th node from the end: 1->2->3->4->5.
    print SolutionTwoPasses().removeNthFromEnd(ll.head, 0).val


if __name__ == '__main__':
    main()
