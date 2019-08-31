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

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SolutionSort(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        Time complexity: O(nk*log(nk)), where
          - n is the number of nodes,
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

        # Link nodes in sorted_nodes.
        pre_head = ListNode(None)
        current = pre_head

        for node in sorted_nodes:
            current.next = node
            current = current.next

        return pre_head.next


class SolutionMergeTwoRecur(object):
    def _merge2Lists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2

        if l1.val <= l2.val:
            l1.next = self._merge2Lists(l1.next, l2)
            return l1
        else:
            l2.next = self._merge2Lists(l1, l2.next)
            return l2

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        Time complexity: O(kn*logk), where
          - n is the number of nodes,
          - k is the length of lists.
        Space complexity: O(1).
        """
        if not lists:
            return None

        length = len(lists)

        # When there are at least two lists, merge them.
        while length > 1:
            # Merge each pair of leftmost and rightmost lists.
            for i in range(length // 2):
                lists[i] = self._merge2Lists(lists[i], lists[length - 1 - i])

            # Decrement length.
            length = (length + 1) // 2

        return lists[0]


class SolutionMergeTwoIter(object):
    def _merge2Lists(self, l1, l2):
        if l1 and not l2:
            return l1
        elif not l1 and l2:
            return l2

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


    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        Time complexity: O(kn*logk), where
          - n is the number of nodes,
          - k is the length of lists.
        Space complexity: O(1).
        """
        if not lists:
            return None

        length = len(lists)

        # When there are at least two lists, merge them.
        while length > 1:
            # Merge each pair of leftmost and rightmost lists.
            for i in range(length // 2):
                lists[i] = self._merge2Lists(lists[i], lists[length - 1 - i])

            # Decrement length.
            length = (length + 1) // 2

        return lists[0]


class SolutionMinHeap(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        Time complexity: O(kn*logk), where
          - n is the number of nodes,
          - k is the length of lists.
        Space complexity: O(1).
        """
        # Use min heap to collect sorted nodes.
        import heapq

        if not lists:
            return None

        minheap = [(head.val, head) for head in lists if head]
        heapq.heapify(minheap)

        pre_head = ListNode(None)
        current = pre_head

        # Pop head of min heap and link it to the linked list.
        while minheap:
            _, node = heapq.heappop(minheap)
            current.next = node
            current = current.next

            # If head of min heap has a next node, push to min heap.
            if current.next:
                heapq.heappush(minheap, (current.next.val, current.next))

        return pre_head.next


def show(head):
    ls = []

    current = head
    while current:
        ls.append(current.val)
        current = current.next

    print ls



def main():
    # Input:
    # [
    #   1->4->5,
    #   1->3->4,
    #   2->6
    # ]
    # Output: 1->1->2->3->4->4->5->6
    head1 = ListNode(1)
    head1.next = ListNode(4)
    head1.next.next = ListNode(5)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    head3 = ListNode(2)
    head3.next = ListNode(6)

    lists = [head1, head2, head3]

    print 'By sort:'
    head = SolutionSort().mergeKLists(lists)
    show(head)

    print 'By merge two with recursion:'
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

    print 'By merge two with iteration:'
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

    print 'By min heap:'
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


if __name__ == '__main__':
    main()
