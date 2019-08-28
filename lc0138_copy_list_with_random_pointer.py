"""Leetcode 138. Copy List with Random Pointer
Medium

URL: https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list is given such that each node contains an additional 
random pointer which could point to any node in the list or null.

Return a deep copy of the list. 

Example 1:
Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},
 "random":{"$ref":"2"},"val":1}
Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and 
its random pointer points to itself.
 
Note:
You must return the copy of the given head as a reference to the cloned list.
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
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

        # Point copy's random to original's random's next, i.e. a copy node.
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            
            # Iterate through original nodes.
            current = current.next.next


        # Break linked list into two: one for original, the other for copy.
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

    head_cp = Solution().copyRandomList(head)
    print head_cp.val              # 1
    print head_cp.next.val         # 2
    print head_cp.random.val       # 2
    print head_cp.next.next        # None
    print head_cp.next.random.val  # 2


if __name__ == '__main__':
    main()
