"""206. Reverse Linked List

URL: https://leetcode.com/problems/reverse-linked-list/

Easy

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. 
Could you implement both?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SolutionStack(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Time complexity: O(n).
        Space complexity: O(n).
        """
        stack = []

        current = head
        while current:
            stack.append(current)
            current = current.next

        pre_head = ListNode(None)
        new_current = pre_head
        while stack:
            current = stack.pop()
            new_current.next = ListNode(current.val)
            new_current = new_current.next

        return pre_head.next


class SolutionRecur(object):
    def _reverse(self, head, previous):
        if not head:
            return previous

        # Two pointers method: head + previous.
        # Create new current->current.next by reversing previous->head.
        current = ListNode(head.val)
        current.next = previous

        # Increment previous & head and apply recursion.
        previous = current
        head = head.next
        return self._reverse(head, previous)

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Time complexity: O(n).
        Space complexity: O(n).
        """
        previous = None
        return self._reverse(head, previous)


class SolutionIter(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Two pointer method: head + previous.
        previous = None

        while head:
            # Create new current->current.next by reversing previous->head.
            current = ListNode(head.val)
            current.next = previous

            # Increment previous & head.
            previous = current
            head = head.next
   
        # New head is previous, with head = None.
        return previous


def main():
    # 1->2->3->4->5->NULL
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # 5->4->3->2->1->NULL
    # Should be 5.
    print SolutionStack().reverseList(node1).val
    print SolutionRecur().reverseList(node1).val
    print SolutionIter().reverseList(node1).val
    # Should be 4.
    print SolutionStack().reverseList(node1).next.val
    print SolutionRecur().reverseList(node1).next.val
    print SolutionIter().reverseList(node1).next.val
    # Should be 3.
    print SolutionStack().reverseList(node1).next.next.val
    print SolutionRecur().reverseList(node1).next.next.val
    print SolutionIter().reverseList(node1).next.next.val


if __name__ == '__main__':
    main()
