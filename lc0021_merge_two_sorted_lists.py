"""Leetcode 21. Merge Two Sorted Lists
Easy

URL: https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class SolutionSortAll:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Time complexity: O((n1+n2)*log(n1+n2)), where ni is the length of list i.
        Space complexity: O((n1+n2)).
        """
        # Edge cases: list1 or list2 is empty.
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


class SolutionRecur:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Time complexity: O(n1+n2), where ni is the length of list i.
        Space complexity: O(n1+n2).
        """
        # Edge cases: list1 or list2 is empty.
        if not l1 or not l2:
            return l1 or l2

        # Recusively append next node to the smaller node. 
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


class SolutionIter:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Time complexity: O(n1+n2), where ni is the length of list i.
        Space complexity: O(1).
        """
        # Edge cases: list1 or list2 is empty.
        if not l1 or not l2:
            return l1 or l2

        # Iteratively append smaller node to the tail when both exist.
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

        # Append the remaining node.
        current.next = l1 or l2

        return pre_head.next


def show(ls):
    result = []
    current = ls
    while current:
        result.append(current.val)
        current = current.next
    print(result)


def main():
    # Input: 1->2->4, 1->3->4
    # Output: 1->1->2->3->4->4
    print('By sort:')
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    ls = SolutionSortAll().mergeTwoLists(l1, l2)
    show(ls)

    print('By recur:')
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    ls = SolutionRecur().mergeTwoLists(l1, l2)
    show(ls)

    print('By iter:')
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
