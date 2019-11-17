"""Leetcode 86. Partition List
Medium

URL: https://leetcode.com/problems/partition-list/

Given a linked list and a value x, partition it such that all nodes less than
x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two
partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SolutionTwoLists(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode

        Time complexity: O(n).
        Space complexity: O(1).
        """
        prev_head1 = ListNode(None)
        prev_head2 = ListNode(None)
        current1 = prev_head1
        current2 = prev_head2

        current = head
        while current:
            if current.val < x:
                current1.next = current
                current1 = current1.next
            else:
                current2.next = current
                current2 = current2.next

            current = current.next

        current1.next = prev_head2.next
        current2.next = None
        return prev_head1.next


def main():
    # Input: head = 1->4->3->2->5->2, x = 3
    # Output: 1->2->2->4->3->5
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    x = 3
    new_head = SolutionTwoLists().partition(head, x)
    print new_head.val
    print new_head.next.val
    print new_head.next.next.val
    print new_head.next.next.next.val
    print new_head.next.next.next.next.val
    print new_head.next.next.next.next.next.val


if __name__ == '__main__':
    main()
