"""Leetcode 142. Linked List Cycle II
Medium

URL: https://leetcode.com/problems/linked-list-cycle-ii/

Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which
represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the 
second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, 
where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Follow-up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SolutionSet(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Use set to collect visited nodes.
        visited_nodes = set()

        # Visit node and check it exists in set.
        current = head

        while current:
            if current in visited_nodes:
                return current

            visited_nodes.add(current)
            current = current.next

        return None


class SolutionSlowFast(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        If there is a cycle, the node where fast and slow meet will
        have the same distance to cycle starting node as head.
        Specifically, suppose 
        - distance from head to loop start: x1
        - distance from loop start to their meet: x2
        - distance from their meet to loop start: x3
        Then
        - distance of fast moves when meets slow: x1 + x2 + x3 + x2.
        - distance of slow moves when meets fast: x1 + x2.
        - their relationship: x1 + x2 + x3 + x2 = 2 * (x1 + x2) => x1 = x3.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Two pointers: slow move for 1 step; fast for 2 steps.
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If there exists cycle, move head & slow together until they meet.
            if slow == fast:
                current = head
                while current:
                    if current == slow:
                        return current

                    current = current.next
                    slow = slow.next

        return None


def main():
    # Input: head = [3,2,0,-4], pos = 1 (val: 2)
    # Output: 2
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next = ListNode(-4)
    head.next.next.next = head.next

    print SolutionSet().detectCycle(head).val
    print SolutionSlowFast().detectCycle(head).val

    # head = [1,2], pos = 0 (val: 1)
    # Output: 1
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head

    print SolutionSet().detectCycle(head).val
    print SolutionSlowFast().detectCycle(head).val

    # head = [1, 2], pos = -1
    # Output: None
    head = ListNode(1)
    head.next = ListNode(2)

    print SolutionSet().detectCycle(head)
    print SolutionSlowFast().detectCycle(head)

    # head = [-1,-7,7,-4,19,6,-9,-5,-2,-5], pos = 6 (val: -9)
    head = ListNode(-1)
    head.next = ListNode(-7)
    head.next.next = ListNode(7)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = ListNode(19)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(-9)
    head.next.next.next.next.next.next.next = ListNode(-5)
    head.next.next.next.next.next.next.next.next = ListNode(-2)
    head.next.next.next.next.next.next.next.next.next = ListNode(-5)
    head.next.next.next.next.next.next.next.next.next.next = (
        head.next.next.next.next.next.next)

    print SolutionSet().detectCycle(head).val
    print SolutionSlowFast().detectCycle(head).val


if __name__ == '__main__':
    main()
