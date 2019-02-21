"""Leetcode 2. Add Two Numbers
Medium

URL: https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order and each of their 
nodes contain a single digit. Add the two numbers and return it as a 
linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Time complexity: O(n).
        Space complexity: O(1).
        """
        head = ListNode(0)
        current, carry = head, 0

        while l1 or l2 or carry:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
    
            carry, val = (
                (val1 + val2 + carry) // 10, 
                (val1 + val2 + carry) % 10)

            current.next = ListNode(val)
            current = current.next

        return head.next


def main():
    import time
    # Add two numbers: 342 + 465 = 807.
    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    # Output: 7 -> 0 -> 8

    # 1st number: 342.
    l1 = ListNode(2)
    l1_2 = ListNode(4)
    l1_3 = ListNode(3)
    l1.next = l1_2
    l1_2.next = l1_3
    l1_3.next = None

    # 2nd number: 465.
    l2 = ListNode(5)
    l2_2 = ListNode(6)
    l2_3 = ListNode(4)
    l2.next = l2_2
    l2_2.next = l2_3
    l2_3.next = None

    start_time = time.time()
    l = Solution().addTwoNumbers(l1, l2)
    print(l.next.next.val * 1E2 + l.next.val * 1E1 + l.val)
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
