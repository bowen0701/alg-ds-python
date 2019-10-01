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


class SolutionRecur(object):
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
        # Apply recursive sort list with iterative merge sorted lists.
        # Create base condition: no or just one node.
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


def main():
    # Input: 4->2->1->3
    # Output: 1->2->3->4
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    sorted_head = SolutionRecur().sortList(head)
    print (sorted_head.val, sorted_head.next.val,
           sorted_head.next.next.val, 
           sorted_head.next.next.next.val)

    # Input: -1->5->3->4->0
    # Output: -1->0->3->4->5

if __name__ == '__main__':
    main()
