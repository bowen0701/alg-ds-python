"""Leetcode 23. Merge k Sorted Lists
Hard

URL: https://leetcode.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

from typing import List
import heapq


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SolutionAllSort(object):
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        Time complexity: O(nk*log(nk)), where
          - n is the max number of nodes in one list.
          - k is the length of lists.
        Space complexity: O(nk).
        """
        # Collect all nodes from list.
        nodes = []

        for head in lists:
            current = head
            while current:
                nodes.append(current)
                current = current.next

        # Sort all nodes by their values.
        sorted_nodes = sorted(nodes, key=lambda x: x.val)

        # Link sorted nodes.
        pre_head = ListNode(None)
        current = pre_head

        for node in sorted_nodes:
            current.next = node
            current = current.next

        return pre_head.next


class SolutionMergeTwoToFirst(object):
    def _merge2Lists(self, l1: ListNode, l2: ListNode):
        if not l1 or not l2:
            return l1 or l2

        if l1.val <= l2.val:
            l1.next = self._merge2Lists(l1.next, l2)
            return l1
        else:
            l2.next = self._merge2Lists(l1, l2.next)
            return l2

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        Merge two lists to the first.

        Time complexity: O(k^2n)
          - n is the max number of nodes in one list.
          - k is the length of lists.
        Space complexity: O(n*logk)
        """
        n = len(lists)

        # Merge two lists to the first.
        for i in range(1, n):
            lists[0] = self._merge2Lists(lists[0], lists[i])

        return lists[0]


class SolutionMergeTwoRecur(object):
    def _merge2Lists(self, l1: ListNode, l2: ListNode):
        """Merge two sorted lists recursively."""
        if not l1 or not l2:
            return l1 or l2

        if l1.val <= l2.val:
            l1.next = self._merge2Lists(l1.next, l2)
            return l1
        else:
            l2.next = self._merge2Lists(l1, l2.next)
            return l2

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        Merge each pair of two lists at a time. 

        Time complexity: O(nk*logk), where
          - n is the max number of nodes in one list.
          - k is the length of lists.
          - nk/2 in each run, logk runs.
        Space complexity: O(n*logk).
        """
        if not lists:
            return None

        n = len(lists)

        # For each pair of leftmost & rightmost lists, merge them to the former.
        while n > 1:
            for i in range(n // 2):
                lists[i] = self._merge2Lists(lists[i], lists[n - 1 - i])

            # Decrement n to half.
            n = (n + 1) // 2

        return lists[0]


class SolutionMergeTwoIter(object):
    def _merge2Lists(self, l1: ListNode, l2: ListNode):
        """Merge two sorted lists iteratively."""
        if not l1 or not l2:
            return l1 or l2

        pre_head = ListNode(None)
        current = pre_head

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        current.next = l1 or l2

        return pre_head.next


    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        Time complexity: O(nk*logk), where
          - n is the max number of nodes in one list.
          - k is the length of lists.
          - nk/2 in each run, logk runs.
        Space complexity: O(1).
        """
        if not lists:
            return None

        n = len(lists)

        # For each pair of leftmost & rightmost lists, merge them to the former.
        while n > 1:
            for i in range(n // 2):
                lists[i] = self._merge2Lists(lists[i], lists[n - 1 - i])

            # Decrement n to half.
            n = (n + 1) // 2

        return lists[0]


class SolutionMinHeap(object):
    ListNode.__lt__ = lambda self, other: self.val < other.val

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        Time complexity: O(nk*logk), where
          - n is the max number of nodes in one list.
          - k is the length of lists.
          - nk nodes to connect, logk for heap push.
        Space complexity: O(k).
        """
        # Edge case.
        if not lists:
            return None

        # Use min heap to collect list nodes.
        minheap = [l for l in lists if l]
        heapq.heapify(minheap)

        pre_head = ListNode(None)
        current = pre_head

        # Pop min heap's head and link that min node to list.
        while minheap:
            nxt = heapq.heappop(minheap)
            current.next = nxt
            current = current.next

            # If min heap's head has a next, push to min heap.
            if current.next:
                heapq.heappush(minheap, current.next)

        return pre_head.next


def show(head: ListNode):
    ls = []

    current = head
    while current:
        ls.append(current.val)
        current = current.next

    print(ls)


def main():
    # Input:
    # [
    #   1->4->5,
    #   1->3->4,
    #   2->6
    # ]
    # Output: 1->1->2->3->4->4->5->6
    print('By all sort:')
    head1 = ListNode(1)
    head1.next = ListNode(4)
    head1.next.next = ListNode(5)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    head3 = ListNode(2)
    head3.next = ListNode(6)

    lists = [head1, head2, head3]

    head = SolutionAllSort().mergeKLists(lists)
    show(head)

    print('By merge two to the first:')
    head1 = ListNode(1)
    head1.next = ListNode(4)
    head1.next.next = ListNode(5)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    head3 = ListNode(2)
    head3.next = ListNode(6)

    lists = [head1, head2, head3]

    head = SolutionMergeTwoToFirst().mergeKLists(lists)
    show(head)

    print('By merge two with recursion:')
    head1 = ListNode(1)
    head1.next = ListNode(4)
    head1.next.next = ListNode(5)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    head3 = ListNode(2)
    head3.next = ListNode(6)

    lists = [head1, head2, head3]

    head = SolutionMergeTwoRecur().mergeKLists(lists)
    show(head)

    print('By merge two with iteration:')
    head1 = ListNode(1)
    head1.next = ListNode(4)
    head1.next.next = ListNode(5)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    head3 = ListNode(2)
    head3.next = ListNode(6)

    lists = [head1, head2, head3]

    head = SolutionMergeTwoIter().mergeKLists(lists)
    show(head)

    print('By min heap:')
    head1 = ListNode(1)
    head1.next = ListNode(4)
    head1.next.next = ListNode(5)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    head3 = ListNode(2)
    head3.next = ListNode(6)

    lists = [head1, head2, head3]

    head = SolutionMinHeap().mergeKLists(lists)
    show(head)

    print('For edge case:')
    lists = [None, None]
    head = SolutionAllSort().mergeKLists(lists)
    show(head)
    head = SolutionMergeTwoToFirst().mergeKLists(lists)
    show(head)
    head = SolutionMergeTwoRecur().mergeKLists(lists)
    show(head)
    head = SolutionMergeTwoIter().mergeKLists(lists)
    show(head)
    head = SolutionMinHeap().mergeKLists(lists)
    show(head)


if __name__ == '__main__':
    main()
