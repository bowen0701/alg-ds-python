"""Leetcode 23. Merge k Sorted Lists
Hard

URL: https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in
ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are [1->4->5, 1->3->4, 2->6], and merging them
into one sorted list: 1->1->2->3->4->4->5->6.

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10^4.
"""

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class SolutionAllSort:
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


class SolutionMergeTwoToFirst:
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

        Merge two lists to the first:
        https://github.com/bowen0701/alg-ds-python/blob/master/lc0021_merge_two_sorted_lists.py

        Time complexity: O(k^2 * n)
          - n is the max number of nodes in one list.
          - k is the length of lists.
          - Merge #1: n + n = 2n, merge #2: 2n + n = 3n, ...,
            merge #(k-1): (k-1)n + n = kn.
          - Total: 2n + 3n + ... + kn = n * k*(k+1)/2 = O(k^2 * n).
        Space complexity: O(kn)
          - Recursive _merge2Lists stack depth = total length of both lists.
          - By the last merge, lists[0] has (k-1)*n nodes, so depth = kn.
        """
        n = len(lists)

        # Sequentially merge each list into lists[0].
        # lists[0] grows after each merge, making later merges more expensive.
        for i in range(1, n):
            lists[0] = self._merge2Lists(lists[0], lists[i])

        return lists[0]


class SolutionMergeTwoRecur:
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

        Merge each pair of two lists at a time (divide and conquer).

        Time complexity: O(nk * logk), where
          - n is the max number of nodes in one list.
          - k is the length of lists.
          - Each round merges k/2 pairs, each pair touching 2n nodes,
            so nk nodes per round.
          - logk rounds to reduce k lists down to 1.
        Space complexity: O(nk)
          - Recursive _merge2Lists stack depth = total length of both lists.
          - In the final round, one pair has ~nk nodes, so depth = O(nk).
        """
        if not lists:
            return None

        n = len(lists)

        # Pair up lists from both ends and merge inward; halve k each round.
        while n > 1:
            for i in range(n // 2):
                lists[i] = self._merge2Lists(lists[i], lists[n - 1 - i])

            # Decrement n to half.
            n = (n + 1) // 2

        return lists[0]


class SolutionMergeTwoIter:
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

        Time complexity: O(nk * logk), where
          - n is the max number of nodes in one list.
          - k is the length of lists.
          - Each round merges k/2 pairs, each pair touching 2n nodes,
            so nk nodes per round.
          - logk rounds to reduce k lists down to 1.
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


class SolutionMinHeap:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        Push (val, sid, node) tuples to avoid comparing ListNode directly.
        sid is a unique tiebreaker for equal vals.

        Time complexity: O(nk * logk), where
          - n is the max number of nodes in one list.
          - k is the length of lists.
          - nk nodes to connect, logk for heap push/pop.
        Space complexity: O(k).
        """
        import heapq

        if not lists:
            return None

        # Push (val, sid, node); sid breaks ties for equal vals.
        sid = 0
        minheap = []
        for node in lists:
            if node:
                heapq.heappush(minheap, (node.val, sid, node))
                sid += 1

        pre_head = ListNode(None)
        current = pre_head

        while minheap:
            val, _, node = heapq.heappop(minheap)
            current.next = node
            current = current.next

            if current.next:
                heapq.heappush(minheap, (current.next.val, sid, current.next))
                sid += 1

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
