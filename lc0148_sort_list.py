"""Leetcode 148. Sort List
Medium

URL: https://leetcode.com/problems/sort-list/

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SolutionMergeSortRecur(object):
    def _merge_sorted_lists(self, l1, l2):
        if not l1 and not l2:
            return None

        if not l1 or not l2:
            return l1 or l2

        prev = ListNode(None)
        current = prev

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        # Link the remaining non-empty list.
        current.next = l1 or l2

        return prev.next


    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Time complexity: O(n*logn).
        Space complexity: O(logn), for stake call.
        """
        # Apply recursive merge sort with iterative merging sorted lists.

        if not head or not head.next:
            return head

        # Use prev, slow & fast pointers to get middle node prev.
        prev, slow, fast = None, head, head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Split list into two by cutting the link of the 1st to the 2nd.
        prev.next = None

        # Recursively sort 1st and 2nd lists.
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        # Merge two sorted lists into the one.
        return self._merge_sorted_lists(l1, l2)


class SolutionMergeSortIterBottomUp(object):
    def _get_length(self, head):
        """Get list length."""
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        return length

    def _split(self, head, step):
        """Split list with length equal to step, and return next head."""
        counter = 1
        current = head
        while current and counter < step:
            current = current.next
            counter += 1

        if not current:
            return None

        next_head = current.next
        current.next = None
        return next_head

    def _merge(self, l1, l2, head):
        """Merge two lists and return next head."""
        current = head

        # Merge two soreted lists.
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # Connect the remaining list node.
        current.next = l1 or l2

        # Arrive at the end of merged list.
        while current.next:
            current = current.next

        next_head = current
        return next_head

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Time complexity: O(n*logn).
        Space complexity: O(1).
        """
        # Apply iterative bottom-up merge sort with merging sorted lists.

        if not head or not head.next:
            return head

        # Get the list length.
        length = self._get_length(head)

        # Iterate over list with step = 1 (and then double step size):
        # - split into 2 lists, with tracking next head, and 
        # - merge sorted lists.
        prev = ListNode(None)
        prev.next = head     
        step = 1

        while step < length:
            current = prev.next
            next_head = prev

            while current:
                l1 = current
                l2 = self._split(l1, step)
                current = self._split(l2, step)
                next_head = self._merge(l1, l2, next_head)

            # Double step size.
            step *= 2

        return prev.next


def main():
    # Input: 4->2->1->3
    # Output: 1->2->3->4
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    sorted_head = SolutionMergeSortRecur().sortList(head)
    print (sorted_head.val, sorted_head.next.val,
           sorted_head.next.next.val, 
           sorted_head.next.next.next.val)

    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    sorted_head = SolutionMergeSortIterBottomUp().sortList(head)
    print (sorted_head.val, sorted_head.next.val,
           sorted_head.next.next.val, 
           sorted_head.next.next.next.val)

    # Input: -1->5->3->4->0
    # Output: -1->0->3->4->5

if __name__ == '__main__':
    main()
