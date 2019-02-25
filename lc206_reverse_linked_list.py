"""206. Reverse Linked List
Easy

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        new_head = ListNode(head.val)
        current = head
        previous = None
        # TODO: Revise reversion.
        while current.next is not None:
            print current.val
            new_head = current
            current = current.next
            previous = new_head
            new_head.next = previous
        return new_head


def main():
    # 1->2->3->4->5->NULL
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    print node1.val
    node1.next = node2
    print node2.val
    node2.next = node3
    print node3.val
    node3.next = node4
    print node4.val
    node4.next = node5
    print node5.val

    # print Solution().reverseList(node1).val


if __name__ == '__main__':
    main()
