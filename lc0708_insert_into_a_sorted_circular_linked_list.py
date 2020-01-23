"""Leetcode 708. Insert into a Sorted Circular Linked List
Medium

URL: https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

Given a node from a Circular Linked List which is sorted in ascending order,
write a function to insert a value insertVal into the list such that it remains
a sorted circular list. The given node can be a reference to any single node
in the list, and may not be necessarily the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place
to insert the new value. After the insertion, the circular list should remain
sorted.

If the list is empty (i.e., given node is null), you should create a new single
circular list and return the reference to that single node. Otherwise,
you should return the original given node.

Example 1: 
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.

Example 2:
Input: head = [], insertVal = 1
Output: [1]
Explanation: The list is empty (given head is null). We create a new single circular list and return the reference to that single node.

Example 3:
Input: head = [1], insertVal = 0
Output: [1,0]
 
Constraints:
- 0 <= Number of Nodes <= 5 * 10^4
- -10^6 <= Node.val <= 10^6
- -10^6 <= insertVal <= 10^6
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class SolutionTwoPointersIter(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Edge case for empty head with circular link.
        if not head:
            head = Node(val=insertVal)
            head.next = head
            return head

        # Iterate to move two pointers: previous & current, until
        # insert is in the middle of previous & current, or
        # insert is out of range of previous & current.
        previous = head
        current = head.next
        while (not (previous.val <= insertVal and insertVal <= current.val) and
               not (previous.val > current.val and insertVal < current.val) and
               not (previous.val > current.val and insertVal > previous.val)):
            previous = previous.next
            current = current.next

            if current is head:
                break

        # Connect previous to new node to current.
        previous.next = Node(val=insertVal, next=current)

        return head


def main():
    # Input: head = [3,4,1]
    # Output: [3,4,1,2]
    head = Node(val=3)
    head.next = Node(val=4)
    head.next.next = Node(val=1)
    head.next.next.next = head    
    insertVal = 2
    new_head = SolutionTwoPointersIter().insert(head, insertVal)
    print (new_head.val, new_head.next.val, 
           new_head.next.next.val, new_head.next.next.next.val,
           new_head.next.next.next.next.val)

    # Input: head = []
    # Output: [1]
    head = None
    insertVal = 1
    new_head = SolutionTwoPointersIter().insert(head, insertVal)
    print (new_head.val, new_head.next.val)

    # Input: head = [1]
    # Output: [1,0]
    head = Node(1)
    head.next = head
    insertVal = 0
    new_head = SolutionTwoPointersIter().insert(head, insertVal)
    print (new_head.val, new_head.next.val, new_head.next.next.val)

    # Input: head = [3,5,1]
    # Output: [3,5,0,1]
    head = Node(val=3)
    head.next = Node(val=5)
    head.next.next = Node(val=1)
    head.next.next.next = head
    insertVal = 0
    new_head = SolutionTwoPointersIter().insert(head, insertVal)
    print (new_head.val, new_head.next.val, 
           new_head.next.next.val, new_head.next.next.next.val,
           new_head.next.next.next.next.val)


if __name__ == '__main__':
    main()
