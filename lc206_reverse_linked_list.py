"""206. Reverse Linked List
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
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionIter(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Two pointer method: previous & head.
        previous = None
        while head:
            # Create new node as current, and 
            # reverse the list by pointing to previous.
            current = ListNode(head.val)
            current.next = previous

            # Move head and previous to next nodes.
            head = head.next
            previous = current
        return previous


class SolutionRecur(object):
    def reverseList(self, head, previous=None):
        """
        :type head: ListNode
        :rtype: ListNode

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if not head:
            return previous

        current = ListNode(head.val)
        current.next = previous

        head = head.next
        previous = current
        return self.reverseList(head, previous)


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
    print SolutionIter().reverseList(node1).val
    print SolutionRecur().reverseList(node1).val
    # Ans: 4.
    print SolutionIter().reverseList(node1).next.val
    # Ans: 3.
    print SolutionIter().reverseList(node1).next.next.val


if __name__ == '__main__':
    main()
