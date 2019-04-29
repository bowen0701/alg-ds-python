"""Leetcode 234. Palindrome Linked List
Easy

URL: https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
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


class Solution1(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(n).
        """
        a_list = []
        current = head

        while current:
            a_list.append(current.val)
            current = current.next

        return a_list == a_list[::-1]


def main():
    # 1->2->2->1: Yes.
    a_list = LinkedList()
    a_list.append(1)
    a_list.append(2)
    a_list.append(2)
    a_list.append(1)
    
    print a_list.head.val
    print a_list.head.next.val
    print a_list.head.next.next.val
    print a_list.head.next.next.next.val

    print Solution1().isPalindrome(a_list.head)

    # 1->2->3->1: No.
    a_list = LinkedList()
    a_list.append(1)
    a_list.append(2)
    a_list.append(3)
    a_list.append(1)
    
    print a_list.head.val
    print a_list.head.next.val
    print a_list.head.next.next.val
    print a_list.head.next.next.next.val

    print Solution1().isPalindrome(a_list.head)


if __name__ == '__main__':
    main()
