"""Leetcode 203. Remove Linked List Elements
Easy

URL: https://leetcode.com/problems/remove-linked-list-elements/

Remove all elements from a linked list of integers that have value val.

Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SolutionIter(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if not head:
            return None

        pre_head = ListNode(None)

        # Check if head's val is val.
        if head.val == val:
            pre_head.next = head.next
        else:
            pre_head.next = head

        # Iterate through remaining list.
        previous = pre_head
        current = pre_head.next

        while current:
            if current.val == val:
                # If node has val, keep previous & update current by skipping it.
                previous.next = current.next
                current = current.next
            else:
                previous = current
                current = current.next

        return pre_head.next


def main():
    # Input:  1->2->6->3->4->5->6, val = 6
    # Output: 1->2->3->4->5
    head = ListNode(6)
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)
    val = 6
    new_head = SolutionIter().removeElements(head, val)
    print(new_head.val,                     # Should be 1 
          new_head.next.val,                # Should be 2
          new_head.next.next.val,           # Should be 3
          new_head.next.next.next.val)      # Should be 4
          # new_head.next.next.next.val,      # Should be 4
          # new_head.next.next.next.next.val) # Should be 5


if __name__ == '__main__':
    main()
