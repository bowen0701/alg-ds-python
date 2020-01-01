"""Leetcode 138. Copy List with Random Pointer
Medium

URL: https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each
node is represented as a pair of [val, random_index] where:
- val: an integer representing Node.val
- random_index: the index of the node (range from 0 to n-1) where random pointer
points to, or null if it does not point to any node.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Example 4:
Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.

Constraints:
--10000 <= Node.val <= 10000
-Node.random is null or pointing to a node in the linked list.
- Number of Nodes will not exceed 1000.
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class SolutionInsertItself(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if not head:
            return None

        # Insert node's copy to its next: current->current_cp->current.next.
        # Why not directly copy? due to linked list's memoryless and random pointer.
        current = head
        while current:
            current_cp = Node(current.val, None, None)

            current_cp.next = current.next
            current.next = current_cp
            current = current_cp.next

        # Point copy's random to old random's copy: random's next.
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            
            # Iterate through original nodes.
            current = current.next.next


        # Break linked list into two: one for old, the other for copy.
        head_cp = head.next

        current = head
        current_cp = head_cp
        while current_cp.next:
            current.next = current_cp.next
            current_cp.next = current_cp.next.next

            current = current.next
            current_cp = current_cp.next

        current.next = None

        return head_cp


def main():
    head = Node(1, None, None)
    head.next = Node(2, None, None)
    head.random = head.next
    head.next.next = None
    head.next.random = head.next

    head_cp = SolutionInsertItself().copyRandomList(head)
    print head_cp.val              # 1
    print head_cp.next.val         # 2
    print head_cp.random.val       # 2
    print head_cp.next.next        # None
    print head_cp.next.random.val  # 2


if __name__ == '__main__':
    main()
