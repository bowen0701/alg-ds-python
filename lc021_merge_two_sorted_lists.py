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


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val)
            return None
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(val)
        return None

    def show(self):
        ls = []
        current = self.head
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
        pass


def main():
    # Input: 1->2->4, 1->3->4
    # Output: 1->1->2->3->4->4
    ls1 = LinkedList()
    ls1.append(1)
    ls1.append(2)
    ls1.append(4)
    ls1.show()

    ls2 = LinkedList()
    ls2.append(1)
    ls2.append(3)
    ls2.append(4)
    ls2.show()


if __name__ == '__main__':
    main()
