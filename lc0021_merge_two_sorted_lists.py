"""Leetcode 21. Merge Two Sorted Lists
Easy

URL: https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SolutionSort(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Time complexity: O((n1+n2)*log(n1+n2)), where ni is the length of list i.
        Space complexity: O((n1+n2)).
        """
        if not l1 or not l2:
            return l1 or l2

        # Collect all nodes.
        nodes = []
        for head in [l1, l2]:
            current = head
            while current:
                nodes.append(current)
                current = current.next

        # Sort nodes by their values.
        sorted_nodes = sorted(nodes, key=lambda x: x.val)

        # Link sorted nodes.
        pre_head = ListNode(None)
        current = pre_head

        for node in sorted_nodes:
            current.next = node
            current = current.next

        return pre_head.next


class SolutionRecur(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Time complexity: O(n1+n2), where ni is the length of list i.
        Space complexity: O(logn1+logn2).
        """
        if not l1 or not l2:
            return l1 or l2

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


class SolutionIter(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Time complexity: O(n1+n2), where ni is the length of list i.
        Space complexity: O(1).
        """
        if not l1 or not l2:
            return l1 or l2

        pre_head = ListNode(None)
        current = pre_head

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        current.next = l1 or l2

        return pre_head.next


def show(head):
    ls = []

    current = head
    while current:
        ls.append(current.val)
        current = current.next
    
    print ls


def main():
    # Input: 1->2->4, 1->3->4
    # Output: 1->1->2->3->4->4
    print 'By sort:'
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    ls = SolutionSort().mergeTwoLists(l1, l2)
    show(ls)

    print 'By recur:'
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    ls = SolutionRecur().mergeTwoLists(l1, l2)
    show(ls)

    print 'By iter:'
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    ls = SolutionIter().mergeTwoLists(l1, l2)
    show(ls)


if __name__ == '__main__':
    main()
