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
        stack = []
        current = head

        while current:
            stack.append(current.val)
            current = current.next

        # for i in range(len(stack) // 2):
        #     if stack[i] != stack[len(stack) - 1 - i]:
        #         return False
        # return True

        return stack == stack[::-1]


class Solution2(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(1).
        """        
        # Find the middle node: slow
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the 2nd half of linked list using slow.
        reverse = None
        while slow:
            nxt = slow.next
            slow.next = reverse
            reverse = slow
            slow = nxt
        
        # Traverse the 1st half and reversed 2nd half at the same time
        # and compare their val.
        while reverse:
            if reverse.val != head.val:
                return False

            reverse = reverse.next
            head = head.next

        return True


def main():
    import time

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

    start_time = time.time()
    print 'Naive: {}'.format(Solution1().isPalindrome(a_list.head))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'Optimized: {}'.format(Solution2().isPalindrome(a_list.head))
    print 'Time: {}'.format(time.time() - start_time)

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

    start_time = time.time()
    print 'Naive: {}'.format(Solution1().isPalindrome(a_list.head))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'Optimized: {}'.format(Solution2().isPalindrome(a_list.head))
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
