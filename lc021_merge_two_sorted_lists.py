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

def show_linked_list(ll):
    ls = []
    current = ll
    while current:
        ls.append(current.val)
        current = current.next
    print ls


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        elif l1 and not l2:
            return l1
        elif not l1 and l2:
            return l2

        head = None
        current = head

        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    ll = l1
                    l1 = l1.next
                else:
                    ll = l2
                    l2 = l2.next

                if not head:
                    head = ListNode(ll.val)
                    current = head
                else:
                    current.next = ListNode(ll.val)
                    current = current.next                
            elif l1 and not l2:
                current.next = ListNode(l1.val)
                current = current.next
                l1 = l1.next
            elif not l1 and l2:
                current.next = ListNode(l2.val)
                current = current.next
                l2 = l2.next
        return head


def main():
    # # Input: 1->2->4, 1->3->4
    # # Output: 1->1->2->3->4->4
    # l1 = ListNode(1)
    # l1.next = ListNode(2)
    # l1.next.next = ListNode(4)
    # show_linked_list(l1)

    # l2 = ListNode(1)
    # l2.next = ListNode(3)
    # l2.next.next = ListNode(4)
    # show_linked_list(l2)

    # ls = Solution().mergeTwoLists(l1, l2)
    # show_linked_list(ls)

    # # Input: 1->2->4, None
    # # Output: 1->2->4
    # l1 = ListNode(1)
    # l1.next = ListNode(2)
    # l1.next.next = ListNode(4)
    # show_linked_list(l1)

    # l2 = None

    # ls = Solution().mergeTwoLists(l1, l2)
    # show_linked_list(ls)

    # # Input: None, 1->3->4
    # # Output: 1->3->4
    # l1 = None

    # l2 = ListNode(1)
    # l2.next = ListNode(3)
    # l2.next.next = ListNode(4)
    # show_linked_list(l2)

    # ls = Solution().mergeTwoLists(l1, l2)
    # show_linked_list(ls)

    # # Input: None, None
    # # Output: None
    # l1 = None
    # l2 = None

    # ls = Solution().mergeTwoLists(l1, l2)
    # show_linked_list(ls)

    # Input: [-9,3], [5,7]
    # Output: [-9,3, 5,7]
    l1 = ListNode(-9)
    l1.next = ListNode(3)
    show_linked_list(l1)

    l2 = ListNode(5)
    l2.next = ListNode(7)
    show_linked_list(l2)

    ls = Solution().mergeTwoLists(l1, l2)
    show_linked_list(ls)


if __name__ == '__main__':
    main()
