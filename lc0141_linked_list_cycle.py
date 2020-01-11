"""Leetcode 141. Linked List Cycle
Easy

URL: https://leetcode.com/problems/linked-list-cycle/

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos
which represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list,
where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list,
where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SolutionSet(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool

        Time complexity: O(n), where n is the length of linked list.
        Space complexity: O(n).
        """
        if not head:
            return False

        # Create set to collect visited nodes.
        visited_nodes = set()

        current = head

        while current:
            if current in visited_nodes:
                return True

            visited_nodes.add(current)
            current = current.next

        return False


class SolutionSlowFast(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool

        Time complexity: O(n), where n is the lenght of linked list.
        Space complexity: O(1).
        """
        if not head:
            return False

        # Two pointers: slow move for 1 step; fast for 2 steps.
        slow = fast = head

        # while fast.next and fast.next.next:
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If fast cathes up slow, there is a cycle.
            if slow == fast:
                return True

        return False


def main():
    # Input: head = [3,2,0,-4], pos = 1. Output: true
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    print SolutionSet().hasCycle(head)
    print SolutionSlowFast().hasCycle(head)

    # Input: head = [1,2], pos = 0. Output: true
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    print SolutionSet().hasCycle(head)
    print SolutionSlowFast().hasCycle(head)

    # Input: head = [1], pos = -1. Output: false
    head = ListNode(1)
    print SolutionSet().hasCycle(head)    
    print SolutionSlowFast().hasCycle(head)


if __name__ == '__main__':
    main()
